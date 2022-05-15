#!/bin/bash
PWD=$(pwd)
COLOR_GREEN='\033[0;32m'
NO_COLOR='\033[0m'
FILES=( "helpers/data_record.py" "helpers/logger.py" "helpers/file_parser.py" )

for FILE in "${FILES[@]}"
do
    printf "${COLOR_GREEN}list8/src/${FILE} -> list9/src/${FILE}${NO_COLOR}\n"
    cp "list8/src/${FILE}" "list9/src/${FILE}"
done