cmake_minimum_required(VERSION 3.22)
project(bachelor-theses-2)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "/opt/homebrew/bin/cmake" "/opt/homebrew/Cellar/qt@5/5.15.3")


find_package(Qt5Widgets REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5Gui REQUIRED)

add_executable(bachelor-theses-2 main.cpp domain/Teacher.cpp domain/Teacher.h domain/AppException.h domain/Student.cpp domain/Student.h domain/Subject.h domain/Observer.h repository/TeacherRepository.cpp repository/TeacherRepository.h repository/StudentRepository.cpp repository/StudentRepository.h controller/Controller.cpp controller/Controller.h ui/GUIManager.cpp ui/GUIManager.h ui/GUI.cpp ui/GUI.h ui/GUI.ui ui/EditStudentWindow.cpp ui/EditStudentWindow.h ui/EditStudentWindow.ui)
target_link_libraries(bachelor-theses-2
        Qt5::Core
        Qt5::Gui
        Qt5::Widgets
        )
