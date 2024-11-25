a=int(input())
b=list(map(int,input().split()))
b=sum(b)
if b>0:
  print(b)
else:
  print(b*-1)