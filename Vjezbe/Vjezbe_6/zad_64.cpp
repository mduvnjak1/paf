#include <iostream>

void sustav(float a1,float b1,float c1,float a2, float b2, float c2)
{
    float x;
    x=(b1*c2-b2*c1)/(a2*b1-a1*b2);
    float y;
    y=(a1*b2*c1+a2*b1*c1-a1*b1*c2-a1*b2*c1)/(a2*b1*b1-a1*b1*b2);
    std::cout << "x = " << x << ", y = " << y << std::endl;
}

int main()
{
    sustav(2,4,3,5,6,1);
    return 0;
}