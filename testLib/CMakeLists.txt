cmake_minimum_required(VERSION 2.8)
project(MyHello CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(test src/test.cpp)
target_include_directories(test PUBLIC src)
target_link_libraries(test PUBLIC CONAN_PKG::hello)


enable_testing()
add_executable(utest test/first.cpp)
target_link_libraries(utest PRIVATE test CONAN_PKG::gtest)
add_test(NAME utest COMMAND utest)



