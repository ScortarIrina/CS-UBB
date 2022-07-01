cmake_minimum_required(VERSION 3.22)
project(task-manager-2)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "/opt/homebrew/bin/cmake" "/opt/homebrew/Cellar/qt@5/5.15.3")


find_package(Qt5Widgets REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5Gui REQUIRED)

add_executable(task-manager-2 main.cpp domain/Subject.h domain/Observer.h domain/AppException.h domain/Programmer.cpp domain/Programmer.h domain/Task.cpp domain/Task.h repository/ProgrammersRepository.cpp repository/ProgrammersRepository.h repository/TasksRepository.cpp repository/TasksRepository.h controller/Controller.cpp controller/Controller.h ui/GUIManager.cpp ui/GUIManager.h ui/gui.cpp ui/gui.h ui/gui.ui)
target_link_libraries(task-manager-2
        Qt5::Core
        Qt5::Gui
        Qt5::Widgets
        )
