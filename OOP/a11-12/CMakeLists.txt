cmake_minimum_required(VERSION 3.22)
project(a11-12-ScortarIrina)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(Headers Watchlist.h Validator.h UserService.h UserRepository.h GUI.h Tutorial.h Service.h Repository.h
        HTMLRepository.h CSVRepository.h)
set(CMAKE_PREFIX_PATH "/home/irina/cmake")

find_package(Qt5Widgets REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5Gui REQUIRED)

#add_executable(a11-12-ScortarIrina main.cpp)

add_executable(a11-12-ScortarIrina main.cpp
        Watchlist.cpp Validator.cpp UserService.cpp UserRepository.cpp GUI.cpp Tutorial.cpp Service.cpp Repository.cpp
        HTMLRepository.cpp CSVRepository.cpp)

target_link_libraries(a11-12-ScortarIrina Qt5::Core Qt5::Gui Qt5::Widgets)
