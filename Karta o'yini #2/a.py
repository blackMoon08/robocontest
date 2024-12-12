k,n = map(int, input().split())
a = []
for i in range(k):
  a.append(input().split())
l = int(input())
p = []
for i in range(n):
  for j in range(k):
    p.append(a[j][i])
print(p[-l])