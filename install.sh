#!/bin/bash

print_usage() {
    cat >&2 <<_END_
Copy or symlink .ycm_extra_conf.py and related files to a target directory.

Usage: $0 -h
       $0 [-l] target

Options:
    -h        This help message.

    -l        Symlink all files.

    -L        Symlink selected files:
                  y = .ycm_extra_conf.py
                  c = ycm_jsondb_core.py
                  C = ycm_jsondb_config.py

_END_
}

usage_error() {
    print_usage
    exit 2
}

# -------- Main body --------

symlink=
while getopts "hlL:" Option; do
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
script_dir=$(readlink -e "$(dirname "$(which "$0")")")
target_directory=$(readlink -e "$target_directory")

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

$ycm_command "$script_dir/ycm_extra_conf.jsondb.py" "$target_directory/.ycm_extra_conf.py"
$core_command "$script_dir/ycm_jsondb_core.py" "$target_directory/ycm_jsondb_core.py"
$config_command "$script_dir/ycm_jsondb_config.py" "$target_directory/ycm_jsondb_config.py"
