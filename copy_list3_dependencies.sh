#!/bin/bash
INPUT_DIR=$1
OUTPUT_DIR=$2
CPP_DIR=$3

COLOR_RED='\033[0;31m'
COLOR_GREEN='\033[0;32m'
NO_COLOR='\033[0m'

# Copy batch scripts
./copy_batch_scripts.sh "$INPUT_DIR" "$OUTPUT_DIR"

# Copy cpp scripts
echo Copying cpp scripts to destination dir
echo Copying head
cp "$CPP_DIR"/head "$OUTPUT_DIR"/head
echo Copying tail
cp "$CPP_DIR"/tail "$OUTPUT_DIR"/tail
printf "${COLOR_GREEN}Success copying list3 dependencies${NO_COLOR}\n"