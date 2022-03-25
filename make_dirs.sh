#!/bin/bash
BUILD_DIR=$1

function create_subdirs {
    echo Im in create_subdirs
}

if [ -d "$BUILD_DIR" ] 
then
    echo Directory ${BUILD_DIR} already exists. "(skipping)"
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
    echo
fi