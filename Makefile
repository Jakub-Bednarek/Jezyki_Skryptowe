SHELL  =/bin/bash
CC 	   = g++
CFLAGS = -std=c++17

L1Path = list1/src
L2Path = list2/src
L3Path = list3/src

TARGETS   = make_dirs list1 list2 list3
BUILD_DIR = build
SUBDIRS   = list1 list2 list3

COLOR_RED   := $(shell tput -Txterm setaf 1)
COLOR_GREEN := $(shell tput -Txterm setaf 2)
NO_COLOR 	:= $(shell tput -Txterm sgr0)


# Main targets
all: $(TARGETS)
	@echo "${COLOR_GREEN}Finished building target all${NO_COLOR}"

make_dirs: make_dirs.sh
	@echo Running make_dirs.sh script
	@./make_dirs.sh $(BUILD_DIR) $(SUBDIRS)

list1: kodPowrotu paths pokazPodobne pokazWszystkie skrypt
	@echo "${COLOR_GREEN}Finished building target list1${NO_COLOR}"

list2: head tail
	@echo "${COLOR_GREEN}Finished building target list2${NO_COLOR}"

list3: list2 avg sum
	@echo Running copy_list3_dependencies.sh
	@./copy_list3_dependencies.sh $(L3Path) $(BUILD_DIR)/list3 $(BUILD_DIR)/list2
	@echo "${COLOR_GREEN}Finished building target list3${NO_COLOR}"



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
