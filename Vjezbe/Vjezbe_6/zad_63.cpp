#include <iostream>

void interval(int polje[],int size, int a, int b)
{
for (int i=0; i < size; i++)
{
    if (a <= polje[i] and polje[i] <= b)
{
        std::cout << polje[i] << std::endl;
}
}
}
void reverse(int polje[],int size)
{
int rpolje[]={};
for (int i=1; i <= size; i++)
{
    rpolje.push_back(polje[size-i]);
}
for (int i=0; i < size; i++)
{
    polje[i]=rpolje[i];
}
}
int main()
{
int polje[7]={1,2,3,4,5,6,7}; 
interval(polje,7,2,5);
reverse(polje,7);
return 0;
}