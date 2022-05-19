#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
void print(vector <int> polje)
{
    for(int i=0; i < polje.size(); i++)
    {
        std::cout << polje[i] << ' ';
    }
    std::cout<<std::endl;
}

void interval(vector <int> polje, int a, int b)
{
    for (int i=0; i < polje.size(); i++)
    {
        if (a <= polje[i] and polje[i] <= b)
    {
            std::cout << polje[i] << ' ';
    }
    }
    std::cout<<std::endl;
}

vector<int> reverse(vector<int> polje)
{
    vector<int> rpolje={};
    for (int i=1; i <= polje.size(); i++)
    {
        rpolje.push_back(polje[polje.size()-i]);
    }
    return rpolje;
}

vector<int> swap(vector<int> polje,int a, int b)
{
    vector<int> spolje=polje;
    spolje[b]=polje[a];
    spolje[a]=polje[b];
    return spolje;
}

int max(vector <int> polje)
{   int m=polje[0];
    for (int i=0; i < polje.size(); i++)
    {
        if (m < polje[i])
        {
            m=polje[i];
        }
    }
    return m;
}

int main()
{
    vector<int> polje={1,2,3,4,5,6,7};
    interval(polje,2,6);
    print(reverse(polje));
    print(swap(polje,2,5));
    std::cout<<max(polje)<<std::endl;
    return 0;
}