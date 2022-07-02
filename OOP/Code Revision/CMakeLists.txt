cmake_minimum_required(VERSION 3.22)
project(code-revision)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "/opt/homebrew/bin/cmake" "/opt/homebrew/Cellar/qt@5/5.15.3")


find_package(Qt5Widgets REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5Gui REQUIRED)

add_executable(code-revision main.cpp domain/Member.cpp domain/Member.h domain/AppException.h domain/Observer.h domain/Subject.h domain/SourceFile.cpp domain/SourceFile.h repository/MemberRepository.cpp repository/MemberRepository.h repository/SourceFileRepository.cpp repository/SourceFileRepository.h controller/Controller.cpp controller/Controller.h ui/GUIManager.cpp ui/GUIManager.h ui/GUI.cpp ui/GUI.h ui/GUI.ui)
target_link_libraries(code-revision
        Qt5::Core
        Qt5::Gui
        Qt5::Widgets
        )
