#!/bin/bash

LIST5_DIR=$1
TEST_COUNTRY=$2
TEST_MONTH=$3

COLOR_YELLOW='\033[0;33m'
COLOR_GREEN='\033[0;32m'
NO_COLOR='\033[0m'

printf "${COLOR_YELLOW}Changing dir to: ${LIST5_DIR}${NO_COLOR}\n"
cd ${LIST5_DIR}

test_scenario_for_language() {
printf "\nTest scenario: ${COLOR_YELLOW}Language $2 ${NO_COLOR}\n"
    printf "${COLOR_GREE}Result: "
    START=$(date +%s%N)

    $1 ${TEST_COUNTRY} ${TEST_MONTH}

    END=$(date +%s%N)
    printf "${COLOR_GREEN}Time passed: $(($(($END-$START))/1000000)) ms${NO_COLOR}\n"
}

printf "\nStarting tests for 4 Covid programms.\n${COLOR_GREEN}Test data:\n\t${COLOR_YELLOW}Country: ${TEST_COUNTRY}\n\tMonth: ${TEST_MONTH}${NO_COLOR}\n"

test_scenario_for_language "java JavaCovid" Java
test_scenario_for_language "python3 PyCovid.py" Python
test_scenario_for_language ./CppCovid C++
test_scenario_for_language "wine cmd /c BatchCovid.bat" Batch

printf "\n${COLOR_YELLOW}Finished tests for 4 Covid programms.${NO_COLOR}"