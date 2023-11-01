[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/linz/lds-metadata-updater/LICENSE) 
[![GitHub Actions Status](https://github.com/linz/lds-metadata-updater/workflows/CI/badge.svg)](https://github.com/linz/lds-metadata-updater/actions)
[![Coverage: 100% branches](https://img.shields.io/badge/Coverage-100%25%20branches-brightgreen.svg)](https://pytest.org/)
[![Kodiak](https://badgen.net/badge/Kodiak/enabled?labelColor=2e3a44&color=F39938)](https://kodiakhq.com/)
[![Dependabot Status](https://badgen.net/badge/Dependabot/enabled?labelColor=2e3a44&color=blue)](https://github.com/linz/lds-bulk-updater/network/updates)
[![License](https://badgen.net/github/license/linz/template-python-hello-world?labelColor=2e3a44&label=License)](https://github.com/linz/lds-bulk-updater/blob/master/LICENSE)
[![Conventional Commits](https://badgen.net/badge/Commits/conventional?labelColor=2e3a44&color=EC5772)](https://conventionalcommits.org)
[![Code Style](https://badgen.net/badge/Code%20Style/black?labelColor=2e3a44&color=000000)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code Style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)

# Note: Highly recommended not to run in production, Please use sandbox to test the script

# lds-bulkdata-updater


This utility updates multiple datasets/layer available in LINZ (as well as others') Data Service.


## Simple Overview

1. Takes the layer ids from the user
2. Creates a draft id for the each layer id in the list. 
3. Use the genertaed draft id to trigger the import
4. Use the layer id and draft id to update the existing layer and publish the new dataset. 


## Execute Bulkdata Update

### Configuration
A config.yaml file must be provided. This can be created by editing the provided
[config_tempate.yaml](https://github.com/linz/lds-bulk-updater/blob/master/bulkdata_updater/config_template.yaml) file. 


#### Configuration Values:

```
Connection:
  Api_key: key <ADMIN API KEY>           # Not Recommended. Should be stored as envi var
  Domain:  <Data Service Domain>         # e.g. data.linz.govt.nz

lds_page_type:  <layers>                 # add either layers/tables

Datasets:
  Layers: <Layers to Process>           # A list of Layers or Table ids
                                        # e.g. [93639,93648, 93649]


Groups:
    group: <group name>                         #add the group name to which the layer belongs

```

**API Key**

The (LINZ) Data Service API key must be generated with the required permissions 
to update data in bulk. It is recommend that a API key is created specifically for 
this task.

The API KEY must have the following permission enabled against it. You will 
need admin rights to be able to enable all of the below 
* Query layer data
* Search and view tables and layers
* Create, edit and delete tables and layers
* View the data catalog and access catalog services (CS-W)

For LDS users, your API key can be managed [here](https://data.linz.govt.nz/my/api/)

There are two options for storing your API Key where the script can utilise the key 
for authentication. The API key can be entered in the config.yml or stored as
an environmental variable. Storing the API Key as an environmental variable is 
the safest and therefore recommended way to do this. The environment variable 
the key is to be assigned to must be `LDS_APIKEY=<lds_apikey>` 



### Execute bulkdata_update.py
Once the config.yaml file has been updated simply run

```cd bulkdata_updater``` (if installed via the recommended setup.py method)

```python bulkdata_updater.py```


### Future Enhancements:
This is so far an initial minimum viable product release.

## Feedback
Please supply any feedback and bug reports to the projects
[GitHub Issues page](https://github.com/linz/lds-bulk-updater/issues)
