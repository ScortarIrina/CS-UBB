cmake_minimum_required(VERSION 3.22)
project(DSA_SoretedBag_lab5)

set(CMAKE_CXX_STANDARD 14)

add_executable(DSA_SortedBag_lab5 main.cpp SortedBag.cpp SortedBag.h SortedBagIterator.cpp SortedBagIterator.h
        ShortTest.h ShortTest.cpp ExtendedTest.h ExtendedTest.cpp)
