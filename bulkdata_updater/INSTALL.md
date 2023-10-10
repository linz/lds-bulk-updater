# Installation instructions

## Requirements
* **Linux** - Operating System. In theory works with others OSs but not tested
* **Git**   - Source code storage and versioning
* **Python 3** - Programming language. Version > 3.2 required
* **setuptools** - download, build, install, upgrade, and uninstall Python packages


### Get source code

make a git dir if you do not have one

*  `mkdir git`

change to git dir

*  `cd git`

Clone lds-bulk-updater project
*  `git clone https://github.com/linz/lds-bulk-updater.git`


### Setup.py

ensure you are in the lds-bulk-updater project directory 
*  `cd C:/Users/git/lds-bulk-updater` 

install bulkdata_updater and its dependencies see (requirements.txt)[requirements.txt])
* `python3 setup.py install`
