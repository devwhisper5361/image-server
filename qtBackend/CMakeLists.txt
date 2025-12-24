cmake_minimum_required(VERSION 3.16)
project(qtprocessor)

set(CMAKE_CXX_STANDARD 17)

find_package(Qt6 REQUIRED COMPONENTS Core)

add_executable(qtprocessor main.cpp)
target_link_libraries(qtprocessor Qt6::Core)
