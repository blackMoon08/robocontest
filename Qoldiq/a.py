a,k,l,r = map(int,input().split())
cnt = (r-k)//a-(l-k-1)//a
if a == 1 and k==0:
  print(r-l-1)
elif a == 1 or k >= a:
  print(0)
else:
  print(cnt)