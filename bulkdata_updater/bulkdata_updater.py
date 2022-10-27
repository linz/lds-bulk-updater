# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:09:56 2022

@author: PKhosla
"""

import requests
import json
import sys
import yaml
import os
import re
import argparse
import logging


try: 
    import log
except:
    from . import log
    
logger = logging.getLogger(__name__)
ERRORS = 0

SECRET = "key de10938baf5d476ea6383c212e38e296"
host_name = "sandbox-2gxknc.koordinates.com"

class ConfigReader():
    """
    Create a config object that can
    be passed to the scripts methods
    """

    def __init__(self, cwd = None):
        # READ CONFIG

        # get config path
        if not cwd:
            cwd = os.getcwd()
            regex = re.compile(r'(\\|\/)(bulk_upload_lds)$')
            cwd = regex.sub('', cwd)
            cwd = os.path.join(os.sep, cwd, 'config.yaml')


        #check config exists
        if not os.path.exists(cwd):
            raise FileNotFoundError('Can not find config file')

        with open(cwd, 'r') as f:
            config = yaml.load(f, Loader=yaml.Loader)

        # CONNECTION
        if 'Connection' in config:
            if os.getenv('LDS_APIKEY', None):
                self.api_key = os.environ['LDS_APIKEY']
            else:
                self.api_key = config['Connection']['Api_key']
            if not self.api_key:
                raise SystemExit('No LDS API Key Provided')
            self.domain = config['Connection']['Domain']
        else:
            raise SystemExit('CONFIG ERROR: No "Connection" section')
        

        # DATA TO PROCESS
        if 'Datasets' in config:
            self.layers = config['Datasets']['Layers']
        else:
            raise SystemExit('CONFIG ERROR: No "Datasets" section')
            

def iterate_selective(layers): 
    """
    Iterate through user supplied (via config.yaml)
    dataset IDs. Returns a generator of layer ids to process
    """

    for layer_id in layers:
        yield layer_id

            
def parse_args(args):
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('--config_file', 
                            default=None,
                            nargs='?',
                            help="Path to config file")
    return cli_parser.parse_args()

def get_draft_id(layer_id, api_key, domain):
    draft_id_url = f"https://{domain}/services/api/v1.x/layers/{layer_id}/versions/"
    
    payload = ""
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'{api_key}'
    }
    
    response = requests.request("POST", draft_id_url, headers=headers, data=payload)
    response = requests.request("GET", draft_id_url, headers=headers, data=payload)
    if response.status_code != 200:
        sys.exit(f"{response} Bad request: Check Key or URL")
    else:
        response = response.text
        result = response[response.find("[")+1 : response.find("]")]
        result = u"[%s]" % result
        convertedDict = json.loads(result)
        draft_id = convertedDict[0].get('id')
        return draft_id
 
    
def trigger_import(layer_id, draft_id, api_key, domain):
    import_url = f"https://{domain}/services/api/v1.x/layers/{layer_id}/versions/{draft_id}/import/"
    payload = ""
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'{api_key}'
    }
    
    response = requests.request("POST", import_url, headers=headers, data=payload)
    if response.status_code != 202:
        sys.exit(f"{response} Bad request: Check the draft_id")


def publish_layer(layer_id, draft_id, api_key, domain):
    publish_url = f"https://{domain}/services/api/v1.x/layers/{layer_id}/versions/{draft_id}/publish/"
    
    payload={}
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'{api_key}'
    }
    
    response = requests.request("POST", publish_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Failed to make an Update")
    else:
        print("data updated successfully")
    
    
def main():
    """
    Script for updating LDS layers. Written for the purpose
    of applying the updates to the multiple layersin one go.     
    """

    global ERRORS

    cli_parser = parse_args(sys.argv[1:])
    config_file = cli_parser.config_file

    # CONFIG LOGGING
    log.conf_logging('root')

    #CHECK PYTHON VERSION
    if sys.version_info<(3,3):
        raise SystemExit('Error, Python interpreter must be 3.3 or higher')

    # READ CONFIG IN
    config = ConfigReader(config_file)
    
    layer_ids = iterate_selective(config.layers)
    for layer_id in layer_ids:
        print(layer_id)
        draft_id = get_draft_id(layer_id, config.api_key, config.domain) 
        if draft_id: 
                break
        if not draft_id:
            logger.critical('Failed to get layer {0}. THIS LAYER HAS NOT BEEN PROCESSED'. format(layer_id))
            continue

        trigger_import(layer_id, draft_id, config.api_key, config.domain)
        publish_layer(layer_id, draft_id, config.api_key, config.domain)
          

if __name__ == "__main__":
    main() 
