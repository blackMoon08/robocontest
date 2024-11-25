n=int(input())
arr=input().split()
while len(arr) !=n :
  arr.pop()
for x in arr:
  if arr.count(x)==1:
    print(x)