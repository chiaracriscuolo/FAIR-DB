# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

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
CMAKE_SOURCE_DIR = /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master

# Include any dependencies generated for this target.
include CMakeFiles/CFDD.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/CFDD.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/CFDD.dir/flags.make

CMakeFiles/CFDD.dir/main.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/main.cpp.o: main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/CFDD.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/main.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/main.cpp

CMakeFiles/CFDD.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/main.cpp > CMakeFiles/CFDD.dir/main.cpp.i

CMakeFiles/CFDD.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/main.cpp -o CMakeFiles/CFDD.dir/main.cpp.s

CMakeFiles/CFDD.dir/data/cfd.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/data/cfd.cpp.o: data/cfd.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/CFDD.dir/data/cfd.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/data/cfd.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/cfd.cpp

CMakeFiles/CFDD.dir/data/cfd.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/data/cfd.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/cfd.cpp > CMakeFiles/CFDD.dir/data/cfd.cpp.i

CMakeFiles/CFDD.dir/data/cfd.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/data/cfd.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/cfd.cpp -o CMakeFiles/CFDD.dir/data/cfd.cpp.s

CMakeFiles/CFDD.dir/data/database.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/data/database.cpp.o: data/database.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/CFDD.dir/data/database.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/data/database.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/database.cpp

CMakeFiles/CFDD.dir/data/database.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/data/database.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/database.cpp > CMakeFiles/CFDD.dir/data/database.cpp.i

CMakeFiles/CFDD.dir/data/database.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/data/database.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/database.cpp -o CMakeFiles/CFDD.dir/data/database.cpp.s

CMakeFiles/CFDD.dir/data/databasereader.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/data/databasereader.cpp.o: data/databasereader.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/CFDD.dir/data/databasereader.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/data/databasereader.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/databasereader.cpp

CMakeFiles/CFDD.dir/data/databasereader.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/data/databasereader.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/databasereader.cpp > CMakeFiles/CFDD.dir/data/databasereader.cpp.i

CMakeFiles/CFDD.dir/data/databasereader.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/data/databasereader.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/databasereader.cpp -o CMakeFiles/CFDD.dir/data/databasereader.cpp.s

CMakeFiles/CFDD.dir/data/types.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/data/types.cpp.o: data/types.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/CFDD.dir/data/types.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/data/types.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/types.cpp

CMakeFiles/CFDD.dir/data/types.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/data/types.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/types.cpp > CMakeFiles/CFDD.dir/data/types.cpp.i

CMakeFiles/CFDD.dir/data/types.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/data/types.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/data/types.cpp -o CMakeFiles/CFDD.dir/data/types.cpp.s

CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.o: algorithms/cfddiscovery.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/cfddiscovery.cpp

CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/cfddiscovery.cpp > CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.i

CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/cfddiscovery.cpp -o CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.s

CMakeFiles/CFDD.dir/algorithms/minernode.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/algorithms/minernode.cpp.o: algorithms/minernode.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object CMakeFiles/CFDD.dir/algorithms/minernode.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/algorithms/minernode.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/minernode.cpp

CMakeFiles/CFDD.dir/algorithms/minernode.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/algorithms/minernode.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/minernode.cpp > CMakeFiles/CFDD.dir/algorithms/minernode.cpp.i

CMakeFiles/CFDD.dir/algorithms/minernode.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/algorithms/minernode.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/minernode.cpp -o CMakeFiles/CFDD.dir/algorithms/minernode.cpp.s

CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.o: algorithms/partitiontable.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building CXX object CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/partitiontable.cpp

CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/partitiontable.cpp > CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.i

CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/algorithms/partitiontable.cpp -o CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.s

CMakeFiles/CFDD.dir/util/setutil.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/util/setutil.cpp.o: util/setutil.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building CXX object CMakeFiles/CFDD.dir/util/setutil.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/util/setutil.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/util/setutil.cpp

CMakeFiles/CFDD.dir/util/setutil.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/util/setutil.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/util/setutil.cpp > CMakeFiles/CFDD.dir/util/setutil.cpp.i

CMakeFiles/CFDD.dir/util/setutil.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/util/setutil.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/util/setutil.cpp -o CMakeFiles/CFDD.dir/util/setutil.cpp.s

CMakeFiles/CFDD.dir/util/stringutil.cpp.o: CMakeFiles/CFDD.dir/flags.make
CMakeFiles/CFDD.dir/util/stringutil.cpp.o: util/stringutil.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building CXX object CMakeFiles/CFDD.dir/util/stringutil.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CFDD.dir/util/stringutil.cpp.o -c /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/util/stringutil.cpp

CMakeFiles/CFDD.dir/util/stringutil.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CFDD.dir/util/stringutil.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/util/stringutil.cpp > CMakeFiles/CFDD.dir/util/stringutil.cpp.i

CMakeFiles/CFDD.dir/util/stringutil.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CFDD.dir/util/stringutil.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/util/stringutil.cpp -o CMakeFiles/CFDD.dir/util/stringutil.cpp.s

# Object files for target CFDD
CFDD_OBJECTS = \
"CMakeFiles/CFDD.dir/main.cpp.o" \
"CMakeFiles/CFDD.dir/data/cfd.cpp.o" \
"CMakeFiles/CFDD.dir/data/database.cpp.o" \
"CMakeFiles/CFDD.dir/data/databasereader.cpp.o" \
"CMakeFiles/CFDD.dir/data/types.cpp.o" \
"CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.o" \
"CMakeFiles/CFDD.dir/algorithms/minernode.cpp.o" \
"CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.o" \
"CMakeFiles/CFDD.dir/util/setutil.cpp.o" \
"CMakeFiles/CFDD.dir/util/stringutil.cpp.o"

# External object files for target CFDD
CFDD_EXTERNAL_OBJECTS =

CFDD: CMakeFiles/CFDD.dir/main.cpp.o
CFDD: CMakeFiles/CFDD.dir/data/cfd.cpp.o
CFDD: CMakeFiles/CFDD.dir/data/database.cpp.o
CFDD: CMakeFiles/CFDD.dir/data/databasereader.cpp.o
CFDD: CMakeFiles/CFDD.dir/data/types.cpp.o
CFDD: CMakeFiles/CFDD.dir/algorithms/cfddiscovery.cpp.o
CFDD: CMakeFiles/CFDD.dir/algorithms/minernode.cpp.o
CFDD: CMakeFiles/CFDD.dir/algorithms/partitiontable.cpp.o
CFDD: CMakeFiles/CFDD.dir/util/setutil.cpp.o
CFDD: CMakeFiles/CFDD.dir/util/stringutil.cpp.o
CFDD: CMakeFiles/CFDD.dir/build.make
CFDD: CMakeFiles/CFDD.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Linking CXX executable CFDD"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/CFDD.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/CFDD.dir/build: CFDD

.PHONY : CMakeFiles/CFDD.dir/build

CMakeFiles/CFDD.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/CFDD.dir/cmake_clean.cmake
.PHONY : CMakeFiles/CFDD.dir/clean

CMakeFiles/CFDD.dir/depend:
	cd /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master /home/chiara/Dropbox/Tesi/cdfAlgorithm/cfddiscovery-master/CMakeFiles/CFDD.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/CFDD.dir/depend
