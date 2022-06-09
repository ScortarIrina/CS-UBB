cmake_minimum_required(VERSION 3.22)
project(test3_practice_GUI)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(Headers Dog.h Repository.h Service.h GUI.h)
set(CMAKE_PREFIX_PATH "/home/irina/cmake")

find_package(Qt5Widgets REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5Gui REQUIRED)

add_executable(test3_practice_GUI main.cpp
        Dog.cpp Repository.cpp Service.cpp GUI.cpp gui.cpp gui.h gui.ui)

target_link_libraries(test3_practice_GUI Qt5::Core Qt5::Gui Qt5::Widgets)
