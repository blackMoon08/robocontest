x=int(input())
a=x-(x%100//2)
b=x-((x%100)+100)//2

if a>b:
  print(b,a)
else:
  print(a,b)