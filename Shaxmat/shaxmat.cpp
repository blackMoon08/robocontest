#include <iostream>
using namespace std;
int main(){
    int a;
    cin >>a;
    if (a>=1 && a<=100){
        if (a%2==0){
            cout << ((a/2+1)*(a/2+1));
        }
        else if (a%2==1){
            cout << (((a+1)/2)+1)*((a+1)/2);
        }
    }

    return 0;
}