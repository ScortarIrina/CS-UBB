cmake_minimum_required(VERSION 3.22)
project(ga_lab5)

set(CMAKE_CXX_STANDARD 14)

add_executable(ga_lab5 main.cpp customHash.cpp customHash.h edge.cpp edge.h mainProgram.cpp weightedGraph.cpp weightedGraph.h)
