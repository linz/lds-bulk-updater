[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/linz/lds-metadata-updater/LICENSE) 
[![GitHub Actions Status](https://github.com/linz/lds-metadata-updater/workflows/CI/badge.svg)](https://github.com/linz/lds-metadata-updater/actions)


# lds-bulkdata-updater


This utility updates multiple datasets/layer available in LINZ (as well as others') Data Service.

For installation instructions see [INSTALL.md](bulkdata_updater/INSTALL.md)

## Simple Overview

1.Takes the layer ids from the user
2. creates a draft id for the each layer id in the list.
3. Use the genertaed draft id to trigger the import
4. Use the layer id and draft id to update the existing layer and publish the new dataset. 


## Execute Metadata Update

### Configuration
A config.yaml file must be provided. This can be created by editing the provided
[config_tempate.yaml](config_tempate.yaml) file. 


#### Configuration Values:

```
Connection:
  Api_key = <ADMIN API KEY>             # See notes below on API Keys
  Domain =  <Data Service Domain>       # e.g. data.linz.govt.nz


Datasets:
  Layers: <Layers to Process>           # A list of Layers/Table ids or "All"
                                        # All will process All Tables and Layers 
                                        # e.g. [93639,93648, 93649] or "All"

```

**API Key**

The (LINZ) Data Service API key must be generated with the required permissions 
to update metadata. It is recommend that a API key is created specifically for 
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

```bulkdata_updater``` (if installed via the recommended setup.py method)


### Future Enhancements:
This is so far an initial minimum viable product release.

## Feedback
Please supply any feedback and bug reports to the projects
[GitHub Issues page](https://github.com/linz/lds-bulk-updater/issues)
