#include <iostream>
using namespace std;

int main(void)
{
    int T;
    cin>>T;
    for (int i = 0; i < T; i ++)
    {
        int p;
        cin>>p;
        int total = 0, remaining = 0;
        if(p > 100)
        {
            total += (p / 100);
            remaining = p - (total * 100);
        }
        else if(p > 50)
        {
            total += (p / 50);
            remaining = p - (total * 50);
        }
        else if(p > 10)
        {
            total += (p / 10);
            remaining = p - (total * 10);
        }
        else if (p > 5)
        {
            total += (p / 5);
            remaining = p - (total * 5);
        }
        else if (p > 2)
        {
            total += (p / 2);
            remaining = p - (total * 2);
        }
        else
        {
            total += remaining;
        }
        cout<<"Total : "<<total<<'\n';
        
    }
}