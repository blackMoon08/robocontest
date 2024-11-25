n,x,y = map(int,input().split())
print(min(abs(y - x), abs(n - x - y + 1)))