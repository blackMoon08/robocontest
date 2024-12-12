#!Diyorbek Qurbonov 
#!Telegramim @dimadev_coder
a,b=map(int,input().split())
for i in range(a,b-1,-1):
  i=str(i)
  if  i.count(str(b))>=1:
    a1=(a-int(i))
    break
if a1==0:
  print('Yes')
else:
  print(a1)