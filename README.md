# ycm_extra_conf.jsondb
VIM's YCM plugin's ycm_extra_conf distribution for json compilation databases.

The goal of this repository is to provide a ycm python plugin, which automates
the handling of compilation flags for your projects.  
* Once you've setup your
build system in your project to generate the compilation database, then you
will never have to manually manage and maintain your compiler flags in your
ycm_extra_conf file.  
* Usually compile_commands.json does not have entries for headers and newly added files.
We try to cleverly guess the flags based on the matching cpp file or the nearest siblings.

This is extremely useful, if you are working with a huge
number of compilcated C/C++ projects and you don't want to or can't maintain
the compiler flags for each projects in your ycm_extra_conf files.

This is not a regular vim plugin. This project provides an alternative
ycm_extra_conf file for the famous
[YCM](https://github.com/Valloric/YouCompleteMe) vim plugin.

CMAKE can generate conveniently the [compilation database]
(http://clang.llvm.org/docs/JSONCompilationDatabase.html).  Of course it is
possible to generate it with other build systems as well, since it can be just
a plain text output of the build.  Also you can use
[BEAR](https://github.com/rizsotto/Bear) to generate the compilation database
with any kind of build systems you have.

You might want to open files which are on the include paths of the compilation
database. For that you need to setup vim's path. This can be automated too, see
[CompileDbPath](https://github.com/martong/vim-compiledb-path) vim plugin.

##Setup

To install the scripts to your project, run `install.sh`.

```bash
./install.sh /path/to/your/project
```

With the `-l` switch, symlinks are created instead of copying the files. It is
the recommended setting if your filesystem supports symlinks.

```bash
./install.sh -l /path/to/your/project
```

To customize your project settings with a config file, copy
`ycm_jsondb_config.py` instead of symlinking, then edit the config file.

```bash
./install.sh -Lyc /path/to/your/project
```

To use a centralized config file stored somewhere else, use the `-s` switch to
get some files from a different directory. Files that exist in the source
directory are used from there, other files are used from the directory of the
script (typically this git repo). In the following example,
`ycm_jsondb_config.py` is used from the config directory, all others from the
script directory.

```bash
cp ycm_jsondb_config.py /path/to/config/directory
./install.sh -l -s /path/to/config/directory /path/to/your/project
```

By default, the compilation database is searched for in the directory where the
`.ycm_extra_conf.py` resides (typically the project root directory). It can be
changed from the config file if per-project config file is used. If a
centralized config file is used, then it can also be changed from
`.ycm_extra_conf.py`. In this case, copy that file instead of symlinking.

```bash
./install.sh -LcC -s /path/to/config/directory /path/to/your/project
```

## Alternatives
https://github.com/rdnetto/YCM-Generator<br/>
Note, this tool will do a full fledged compile, while our tool just needs a compile_commands.json.
This might matter if you are working with huge projects.


