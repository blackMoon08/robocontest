#include <iostream>
using namespace std;
int main()
{
   long n,k;
   cin >> n >>k;
   if ((n>=1 && n<=10e9) && (k>=1 && k<=10e9) ){
    if(n%k==0){
        cout << n/k;
    }
    else if (n%k!=0){
        cout << (n/k)+1;
    }
   }
    return 0;
}