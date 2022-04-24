#include <iostream>

void pravac(float x1,float y1,float x2,float y2)
{
    float k;
    k=(y2-y1)/(x2-x1);
    float l;
    l=y1-k*x1;
    std::cout << "y = " << k << "x + " << l << std::endl;
}
int main()
{
    pravac(2,4,3,5);
    return 0;
}