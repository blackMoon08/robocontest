def daraja2(x):
  count = 0
  while x>0:
    x/=2
    count+=1
  return pow(2,count)
n,s,k,t=0,0,0,0
t=int(input())
for i in range(t):
  n=int(input())
  k=daraja2(n)
  while k>0:
    s+=n//k
    n=n%k
    k//=2
  print(s)
  s=0