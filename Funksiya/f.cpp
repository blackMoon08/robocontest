
using namespace std;
int main()
{
  long long n,count=0;
  cin>>n;
  while(n>1){
    if(n%3==0)
    {
     n=n/3;count++;
    }
    else if(n%3==1)
    {
    n=2*n+1;count++;
    }
    else if(n%3==2)
    {
      n=2*n-1;count++;
  }
  }
  cout<<count;
}