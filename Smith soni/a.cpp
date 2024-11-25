#include<iostream>
using namespace std;
int sum(int n){
    return n<10? n :n%10+sum(n/10);
}
bool smith(int n){
    int S=sum(n);
    int s=0;
    for(int i=2;1LL*i*i<=n;i++){
        while(n%i==0){
            n/=i;
            s+=sum(i);
        }}if(n>1){
            if(s==0)return false;
            s+=sum(n);
        }
        return S==s;
}
int main(){
    int n;
    cin>>n;
    cout<<smith(n);
    return 0;
}