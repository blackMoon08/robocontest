#include<iostream>
using namespace std;
using ll=long long ;
const ll mod=1e9+7;
ll a(ll n){
if(n<2) return 0;
  else if(n%2==0){
  n/=2;
    return 3*a(n) + (n*(n-1))/2;
  } else {
  n=(n-1)/2;
    return 2*a(n)+a(n+1)+((n+1)*n)/2;
  }
}
signed main(){
ll n;
  cin>>n;
  cout<<a(n+1);
  return 0;
}