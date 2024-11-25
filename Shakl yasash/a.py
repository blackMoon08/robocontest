a=int(input())
if(a%2==0):
  print(-1)
else:
  g=a-2
  s=a//2
  for x in range(1,a+1,2):
    print(' '*(s),'*'*x,sep='')
    s=s-1
  s=1
  for i in range(1,a,2):
    print(' '*s,'*'*g,sep='')
    g=g-2
    s=s+1