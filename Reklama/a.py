n=int(input())
a,s=2,2
for i in range(2,n+1):
  a=a*3//2
  s+=a
print(s)