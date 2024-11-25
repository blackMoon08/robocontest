#include<iostream>

using namespace std;
int main(){
    int n,k,s=0,x,p;
    cin >> n >> k;
    int a[n];
    for(int i = 0; i < n; ++ i){
        cin >> a[i];
        s += a[i];
    }
    p = s - a[k];
    cin >> x;
    cout << x - p/2;
    return 0;
}