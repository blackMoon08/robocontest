#include<iostream>
using namespace std;
int main()
{
  long long a,n,m,s,k;
  cin>>a;
  s=0;
  n=18;
  while (s!=a)
  {
    m=0;
    n=n+1;
    k=n;
    while (k!=0)
    {
      m=m+k%10;
      k=k/10;
    }
    if(m==10) s=s+1;
  }
  cout<<n;
}