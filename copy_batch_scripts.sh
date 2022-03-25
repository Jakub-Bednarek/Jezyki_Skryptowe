#!/bin/bash
INPUT_DIR=$1
OUTPUT_DIR=$2
START_DIR=$(pwd)

COLOR_RED='\033[0;31m'
COLOR_GREEN='\033[0;32m'
NO_COLOR='\033[0m'

cd "$INPUT_DIR"
mapfile -d $'\0' FILES < <(find *.bat)
cd "$START_DIR"

if [ ! -z "$FILES" ] 
then
    for VAR in ${FILES[@]}
    do
        echo Copying "$VAR" from "$INPUT_DIR" to "$OUTPUT_DIR"
        cp "$INPUT_DIR"/"$VAR" "$OUTPUT_DIR"/"$VAR"
    done

    printf "${COLOR_GREEN}Finished copying .bat files.${NO_COLOR}\n"
else
    printf "${COLOR_RED}No .bat files found!${NO_COLOR}\n"
fi