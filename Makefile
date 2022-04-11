SHELL  =/bin/bash
CC 	   = g++
CFLAGS = -std=c++17

L1Path = list1/src
L2Path = list2/src
L3Path = list3/src
L4Path = list4/src
L5Path = list5/src
L6Path = list6/src

TARGETS   		= makeDirs list1 list2 list3 list5 list6
BUILD_DIR 		= build
SUBDIRS   		= list1 list2 list3 list4 list5 list6
SCRIPTS_DIR 	= scripts

COLOR_RED    := $(shell tput -Txterm setaf 1)
COLOR_GREEN  := $(shell tput -Txterm setaf 2)
COLOR_YELLOW := $(shell tput -Txterm setaf 3)
NO_COLOR 	 := $(shell tput -Txterm sgr0)


# Main targets
all: $(TARGETS)
	@echo "${COLOR_GREEN}Finished building target all${NO_COLOR}"

makeDirs: ${SCRIPTS_DIR}/make_dirs.sh
	@echo "${COLOR_YELLOW}Running make_dirs.sh script${NO_COLOR}"
	@./${SCRIPTS_DIR}/make_dirs.sh $(BUILD_DIR) $(SUBDIRS)

list1: makeDirs kodPowrotu paths pokazPodobne pokazWszystkie skrypt
	@echo "${COLOR_GREEN}Finished building target list1${NO_COLOR}"

list2: makeDirs head tail
	@echo "${COLOR_YELLOW}Copying available list4 python, batch scripts and txt files${NO_COLOR}"
	@./${SCRIPTS_DIR}/copy_py_bat_txt_scripts.sh ${L3Path} ${BUILD_DIR}/list3
	@echo "${COLOR_GREEN}Finished building target list2${NO_COLOR}"

list3: makeDirs list2 avg sum
	@echo "${COLOR_YELLOW}Running copy_list3_dependencies.sh${NO_COLOR}"
	@./${SCRIPTS_DIR}/copy_list3_dependencies.sh $(BUILD_DIR)/list3 $(BUILD_DIR)/list2
	@echo "${COLOR_YELLOW}Copying available list4 python, batch scripts and txt files${NO_COLOR}"
	@./${SCRIPTS_DIR}/copy_py_bat_txt_scripts.sh ${L4Path} ${BUILD_DIR}/list4
	@echo "${COLOR_GREEN}Finished building target list3${NO_COLOR}"

list5: makeDirs cppCovid javaCovid
	@echo "${COLOR_YELLOW}Copying available list5 python scripts${NO_COLOR}"
	@./${SCRIPTS_DIR}/copy_py_bat_txt_scripts.sh ${L5Path} ${BUILD_DIR}/list5

list6: makeDirs
	@echo "${COLOR_YELLOW}Copying available list6 python scripts${NO_COLOR}"
	@./${SCRIPTS_DIR}/copy_py_bat_txt_scripts.sh ${L6Path} ${BUILD_DIR}/list6

# List1 targets
kodPowrotu: $(L1Path)/KodPowrotu.cpp
	@echo Building target KodPowrotu
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list1/kodPowrotu $(L1Path)/KodPowrotu.cpp

paths: $(L1Path)/Paths.cpp
	@echo Building target Paths
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list1/paths $(L1Path)/Paths.cpp

pokazPodobne: $(L1Path)/PokazPodobne.cpp
	@echo Building target PokazPodobne
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list1/pokazPodobne $(L1Path)/PokazPodobne.cpp

pokazWszystkie: $(L1Path)/PokazWszystkie.cpp
	@echo Building target PokazWszystkie
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list1/pokazWszystkie $(L1Path)/PokazWszystkie.cpp

skrypt: $(L1Path)/Skrypt.cpp
	@echo Building target Skrypt
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list1/Skrypt $(L1Path)/Skrypt.cpp
	


# List2 targets	
head: $(L2Path)/Head.cpp
	@echo Building target head
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list2/head $(L2Path)/Head.cpp

tail:
	@echo Building target tail
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list2/tail $(L2Path)/Tail.cpp

clean:
	@echo "$(COLOR_GREEN)Cleaning directory $(BUILD_DIR) $(NO_COLOR)"
	@$(RM) -rf $(BUILD_DIR)
	@echo "$(COLOR_GREEN)Finished$(NO_COLOR)"



# List3 targets
avg: $(L3Path)/Utils.hpp $(L3Path)/Avg.cpp
	@echo Building target avg
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list3/avg $(L3Path)/Avg.cpp

sum: $(L3Path)/Utils.hpp $(L3Path)/Sum.cpp
	@echo Building target sum
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list3/sum $(L3Path)/Sum.cpp

# List5 targets
cppCovid: $(L5Path)/CppCovid.cpp
	@echo Building target cppCovid
	@$(CC) $(CFLAGS) -o $(BUILD_DIR)/list5/CppCovid $(L5Path)/CppCovid.cpp

javaCovid: $(L5Path)/JavaCovid.java
	@echo Building target javaCovid
	@javac $(L5Path)/JavaCovid.java -d $(BUILD_DIR)/list5

measure_times: list5
	@echo
	@echo "${COLOR_YELLOW}Running measure_list5_task2_times.sh${NO_COLOR}"
	@./${SCRIPTS_DIR}/measure_list5_task2_times.sh $(BUILD_DIR)/list5 Germany 3

list6_raport: list6
	@echo
	@echo "${COLOR_YELLOW}Starting list6 raport procedure${NO_COLOR}"