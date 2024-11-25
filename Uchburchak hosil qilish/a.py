n, m = map(int, input().split())
if m*n < 2:
    print(-1)
else:
    res = int((m*n*(m+n-2)/2))%1000000007
    print(res)