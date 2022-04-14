#include <iostream>
void interval(int polje[],int size, int a, int b)
{
for i in range (size)
{
if (a < polje[i] and polje[i] < b)
{
std::cout << polje[i] << std::endl;
}
}
}
int main()
{
int polje[7]={1,2,3,4,5,6,7}; 
interval(polje,7,2,5);
return 0;
}