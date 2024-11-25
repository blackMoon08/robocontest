y,z=map(int,input().split())
if abs(y-z)%10==0:
  print(abs(y-z)//10)
else:
  print(abs(y-z)//10+1)