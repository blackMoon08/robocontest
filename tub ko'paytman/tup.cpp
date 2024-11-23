#include <iostream>
using namespace std;
int main()
{
   long long a;
   cin >>a;
   if (a>=1 && a<=3*(10e18)){
    if(a>=5){
        cout << 1;
    }
    else if (a>=1 && a<5)
    {
        cout << 0;
    }
   }
    return 0;
}