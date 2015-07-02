# ycm_extra_conf.jsondb
VIM's YCM plugin's ycm_extra_conf distribution for json compilation databases.

The goal of this repository is to provide a ycm python plugin, which automates
the handling of compilation flags for your projects.  Once you've setup your
build system in your project to generate the compilation database, then you
will never have to manually manage and maintain your compiler flags in your
ycm_extra_conf file.  This is extremely useful, if you are working with a huge
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

Edit the `ycm_jsondb_config.py` file in your project to set up additional
compilation flags. Note that this file is always copied and not symlinked.

```bash
vi /path/to/your/project/ycm_jsondb_config.py
```

