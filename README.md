# ycm_extra_conf.jsondb
VIM's YCM plugin's ycm_extra_conf distribution for json compilation databases.

The goal of this repository is to provide a ycm python plugin, which automates the handling of compilation flags for your projects.
Once you've setup your build system in your project to generate the compilation database, then you will never have to manually manage and maintain your compiler flags in your ycm_extra_conf file.
This is extremely useful, if you are working with a huge number of compilcated C/C++ projects and you don't want to or can't maintain the compiler flags for each projects in your ycm_extra_conf files.

This is not a regular vim plugin. This project provides an alternative ycm_extra_conf file for the famous [YCM](https://github.com/Valloric/YouCompleteMe) vim plugin.

CMAKE can generate conveniently the [compilation database] (http://clang.llvm.org/docs/JSONCompilationDatabase.html).
Of course it is possible to generate it with other build systems as well, since it can be just a plain text output of the build.
Also you can use [BEAR](https://github.com/rizsotto/Bear) to generate the compilation database with any kind of build systems you have.

You might want to open files which are on the include paths of the compilation database. For that you need to setup vim's path. This can be automated too, see [CompileDbPath](https://github.com/martong/vim-compiledb-path) vim plugin.

##Setup
### Set up the environment
These settings are common to all of your vim projects.
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
