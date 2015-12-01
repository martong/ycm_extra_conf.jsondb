#!/bin/bash

print_usage() {
    cat >&2 <<_END_
Copy or symlink .ycm_extra_conf.py and related files to a target directory.

Usage: $0 -h
       $0 [-l] target

Options:
    -h        This help message.

    -l        Symlink all files.

    -L flags  Symlink selected files:
                  y = .ycm_extra_conf.py
                  c = ycm_jsondb_core.py
                  C = ycm_jsondb_config.py

    -s dir    The source directory to get files from. If not given or a
              particular file does not exist in the source directory, the file
              in the directory of the script is copied.
_END_
}

usage_error() {
    print_usage
    exit 2
}

get_source_file() {
    local filename="$1"

    if [ -n "$source_dir" -a -e "${source_dir}/${filename}" ]; then
        echo "${source_dir}/${filename}"
    else
        echo "${script_dir}/${filename}"
    fi
}

# -------- Main body --------

symlink=
source_dir=
while getopts "hlL:s:" Option; do
    case $Option in
    h)
        print_usage
        exit
        ;;
    l)
        symlink=ycC
        ;;
    L)
        symlink="$OPTARG"
        ;;
    s)
        source_dir="$OPTARG"
        ;;
    *)
        usage_error
        ;;
    esac
done

shift $(($OPTIND - 1))

target_directory="$1"

if [ -z "$target_directory" ]; then
    usage_error
fi

set -e
readlink=greadlink
# No greadlink, so we are probably on Linux
hash greadlink 2>/dev/null || { readlink=readlink; }
script_dir=$($readlink -ev "$(dirname "$(which "$0")")")
target_directory=$($readlink -ev "$target_directory")

if [ -n "$source_dir" ]; then
    source_dir=$($readlink -ev "$source_dir")
fi

ln_command="ln -s"
cp_command=cp

if [[ "$symlink" == *y* ]]; then
    ycm_command="$ln_command"
else
    ycm_command="$cp_command"
fi

if [[ "$symlink" == *c* ]]; then
    core_command="$ln_command"
else
    core_command="$cp_command"
fi

if [[ "$symlink" == *C* ]]; then
    config_command="$ln_command"
else
    config_command="$cp_command"
fi

$ycm_command "$(get_source_file ycm_extra_conf.jsondb.py)" "$target_directory/.ycm_extra_conf.py"
$core_command "$(get_source_file ycm_jsondb_core.py)" "$target_directory/ycm_jsondb_core.py"
$config_command "$(get_source_file ycm_jsondb_config.py)" "$target_directory/ycm_jsondb_config.py"
