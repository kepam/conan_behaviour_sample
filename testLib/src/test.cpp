#include "test.h"

#include <hello.h>

#include <iostream>


extern void hello();
void test(){
    std::cout << "[testLib]" << std::endl;
    std::cout << "VER is " << VER << std::endl;
    hello();
}
