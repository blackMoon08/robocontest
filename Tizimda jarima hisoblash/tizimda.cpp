#include <iostream>
using namespace std;
int main(){
    int m,x,s;
    cin >> x >>m;
    if ((x>=0 && x<=100) && (m>=1 && m<=180)){
        s=m-1+5*x;
        cout << s;
    }

    return 0;
}