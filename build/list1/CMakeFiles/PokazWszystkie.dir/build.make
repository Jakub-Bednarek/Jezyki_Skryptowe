# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/black_flage/Desktop/studia/jskryptowe

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/black_flage/Desktop/studia/jskryptowe/build

# Include any dependencies generated for this target.
include list1/CMakeFiles/PokazWszystkie.dir/depend.make

# Include the progress variables for this target.
include list1/CMakeFiles/PokazWszystkie.dir/progress.make

# Include the compile flags for this target's objects.
include list1/CMakeFiles/PokazWszystkie.dir/flags.make

list1/CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.o: list1/CMakeFiles/PokazWszystkie.dir/flags.make
list1/CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.o: ../list1/src/PokazWszystkie.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/black_flage/Desktop/studia/jskryptowe/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object list1/CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.o"
	cd /home/black_flage/Desktop/studia/jskryptowe/build/list1 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.o -c /home/black_flage/Desktop/studia/jskryptowe/list1/src/PokazWszystkie.cpp

list1/CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.i"
	cd /home/black_flage/Desktop/studia/jskryptowe/build/list1 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/black_flage/Desktop/studia/jskryptowe/list1/src/PokazWszystkie.cpp > CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.i

list1/CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.s"
	cd /home/black_flage/Desktop/studia/jskryptowe/build/list1 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/black_flage/Desktop/studia/jskryptowe/list1/src/PokazWszystkie.cpp -o CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.s

# Object files for target PokazWszystkie
PokazWszystkie_OBJECTS = \
"CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.o"

# External object files for target PokazWszystkie
PokazWszystkie_EXTERNAL_OBJECTS =

list1/PokazWszystkie: list1/CMakeFiles/PokazWszystkie.dir/src/PokazWszystkie.cpp.o
list1/PokazWszystkie: list1/CMakeFiles/PokazWszystkie.dir/build.make
list1/PokazWszystkie: list1/CMakeFiles/PokazWszystkie.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/black_flage/Desktop/studia/jskryptowe/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable PokazWszystkie"
	cd /home/black_flage/Desktop/studia/jskryptowe/build/list1 && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/PokazWszystkie.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
list1/CMakeFiles/PokazWszystkie.dir/build: list1/PokazWszystkie

.PHONY : list1/CMakeFiles/PokazWszystkie.dir/build

list1/CMakeFiles/PokazWszystkie.dir/clean:
	cd /home/black_flage/Desktop/studia/jskryptowe/build/list1 && $(CMAKE_COMMAND) -P CMakeFiles/PokazWszystkie.dir/cmake_clean.cmake
.PHONY : list1/CMakeFiles/PokazWszystkie.dir/clean

list1/CMakeFiles/PokazWszystkie.dir/depend:
	cd /home/black_flage/Desktop/studia/jskryptowe/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/black_flage/Desktop/studia/jskryptowe /home/black_flage/Desktop/studia/jskryptowe/list1 /home/black_flage/Desktop/studia/jskryptowe/build /home/black_flage/Desktop/studia/jskryptowe/build/list1 /home/black_flage/Desktop/studia/jskryptowe/build/list1/CMakeFiles/PokazWszystkie.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : list1/CMakeFiles/PokazWszystkie.dir/depend

