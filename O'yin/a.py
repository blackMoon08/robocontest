n=int(input())
prime=[True for i in range(n+1)]
p=2
l=[]
while (p*p<=n):
  if(prime[p]==True):
    for i in range(p*2,n+1,p):
      prime[i]=False
  p+=1
prime[0]=False
prime[1]=False
for p in range(n+1):
  if prime[p]:
    l.append(p)
if len(l)%2==0:
  print('Bobur')
else:
  print('Ali')