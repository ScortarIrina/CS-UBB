cmake_minimum_required(VERSION 3.22)
project(Project1)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Project1
        CSVRepository.cpp
        CSVRepository.h
        HTMLRepository.cpp
        HTMLRepository.h
        main.cpp
        Repository.cpp
        Repository.h
        Service.cpp
        Service.h
        Tutorial.cpp
        Tutorial.h
        Tutorials.csv
        Tutorials.html
        Tutorials.txt
        UI.cpp
        UI.h
        UserRepository.cpp
        UserRepository.h
        UserService.cpp
        UserService.h
        Validator.cpp
        Validator.h
        Watchlist.cpp
        Watchlist.h)
