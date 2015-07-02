#!/bin/bash

print_usage() {
    cat >&2 <<_END_
Copy or symlink .ycm_extra_conf.py and related files to a target directory.

Usage: $0 -h
       $0 [-l] target

Options:
    -h        This help message.
    -l        Symlink instead of copy.
_END_
}

usage_error() {
    print_usage
    exit 2
}

# -------- Main body --------

symlink=
while getopts "hl" Option; do
    case $Option in
    h)
        print_usage
        exit
        ;;
    l)
        symlink=yes
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

if [ -n "$symlink" ]; then
    ln -s "$script_dir/ycm_jsondb_core.py" "$target_directory/ycm_jsondb_core.py"
    ln -s "$script_dir/ycm_extra_conf.jsondb.py" "$target_directory/.ycm_extra_conf.py"
else
    cp "$script_dir/ycm_jsondb_core.py" "$target_directory/ycm_jsondb_core.py"
    cp "$script_dir/ycm_extra_conf.jsondb.py" "$target_directory/.ycm_extra_conf.py"
fi

cp "$script_dir/ycm_jsondb_config.py" "$target_directory/ycm_jsondb_config.py"

