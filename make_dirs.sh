#!/bin/bash
BUILD_DIR=$1

COLOR_YELLOW='\033[0;33m'
COLOR_GREEN='\033[0;32m'
NO_COLOR='\033[0m'

function create_subdirs {
    echo Im in create_subdirs
}

if [ -d "$BUILD_DIR" ] 
then
    printf "${COLOR_YELLOW}Directory ${BUILD_DIR} already exists. (skipping)${NO_COLOR}"
    echo
else
    echo Creating build dir: ${BUILD_DIR}
    mkdir "$BUILD_DIR"
    cd "$BUILD_DIR"

    shift
    
    for var
    do
        echo Creating dir: "$var"
        mkdir "$var"
    done
    printf "${COLOR_GREEN}Finished make_dirs.sh${NO_COLOR}\n"
fi