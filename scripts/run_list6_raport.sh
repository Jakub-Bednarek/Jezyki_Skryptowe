#!/bin/bash

COLOR_YELLOW='\033[0;33m'
COLOR_GREEN='\033[0;32m'
NO_COLOR='\033[0m'

TOTAL_TEST_CASES=$1
LIST6_PATH=$2

printf "${COLOR_YELLOW}Starting list6_raport script${NO_COLOR}\n\n"
printf "${COLOR_GREEN}--------------PC SPECS--------------\n${NO_COLOR}"
hwinfo --short

printf "${COLOR_GREEN}\nStarting script_tester\n${NO_COLOR}"
START=$(date +%s)

cd ${LIST6_PATH}
python3 script_tester.py ${TOTAL_TEST_CASES}

END=$(date +%s)
printf "Finished, total took: ${COLOR_GREEN}$(($(($END-$START)))) s\n"