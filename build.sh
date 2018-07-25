#!/bin/bash
cd hello 
conan create . test/test
cd ..

cd hellov2 
conan create . test/test
cd ..

cd testLib 
conan create . test/test
cd ..

cd rootLib 
mkdir -p build
cd build
conan install ..
conan build ..
./bin/root