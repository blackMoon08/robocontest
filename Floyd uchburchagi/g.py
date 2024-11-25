n=int(input())
a=0
b=0
d=[]
while a!=n:
  a=a+1
  for i in range(a):
    b+=1
    d.append(b)
  print(*d,sep=' ')
  d=[]