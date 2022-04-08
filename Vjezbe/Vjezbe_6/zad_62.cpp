#include <iostream>

void kruznica(float x1,float y1,float p,float q,float r)
{
if ((x1-p)*(x1-p)+(y1-q)*(y1-q)<r*r)
{
    std::cout << "Tocka se nalazi unutar kruznice" << std::endl;
}
else if ((x1-p)*(x1-p)+(y1-q)*(y1-q)==r*r)
{
    std::cout << "Tocka se nalazi na kruznici" << std::endl;
}
else if ((x1-p)*(x1-p)+(y1-q)*(y1-q)>r*r)
{    
    std::cout << "Tocka se nalazi izvan kruznice" << std::endl;
}
}
int main()
{
kruznica(5,5,0,0,3);
return 0;
}
