a,b = map(int,input().split())
s = a*b
p = 2*(a+b)
if s > p:
  print(s)
else:
  print(p)