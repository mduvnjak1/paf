#include <iostream>
#include <math.h>
#include "particle.h"
using namespace std;
int main()
{
Particle p1(10,0.5,0,0);
Particle p2(30,0.5,10,20);
std::cout << p1.range(0.01) << std::endl;
std::cout << p1.time(0.01) << std::endl;
std::cout << p2.range(0.01) << std::endl;
std::cout << p2.time(0.01) << std::endl;
return(0);
}