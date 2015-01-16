# ycm_extra_conf.jsondb
VIM's YCM plugin's ycm_extra_conf distribution for json compilation databases.

##Setup
### Set up the environment
These settings are common to all of you vim projects.
```
% export PYTHONPATH=$PYTHONPATH:/path/to/this/repo
```
Set up the additional compiler flags which are specific to your system:
```
% vi /path/to/this/repo/ycm_jsondb_config.py
```
### Set up your project:
These settings are project specific settings. One project is identified by it's containing directory.
```
% cp /path/to/this/repo/ycm_extra_conf.jsondb.py /path/to/yourproject/.ycm_extra_conf.py
```
Set up the location of the compile_commands.json file's directory:
```
% vi /path/to/yourproject/.ycm_extra_conf.py
```
Now, start vim from /path/to/yourproject/
