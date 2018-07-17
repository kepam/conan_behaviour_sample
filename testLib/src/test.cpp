#include "test.h"

#include <hello.h>

#include <iostream>


extern void hello();
void test(){
    std::cout << "test" << std::endl;
    hello();
}
