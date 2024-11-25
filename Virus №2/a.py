mod = 1000000007
n, k = map(int,input().split())
print(pow(k+1,n,mod) if n!=0 else 1 )