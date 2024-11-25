z=int(input())
a=list(map(int,input().split()))
k=set(a)
c=0
for i in k:  
  c+=a.count(i)//2
print(c)