def subset(a, n, i, product, k, full):
    global cnt

    if i == n:
        if 0 < full < n:
            cnt += 1
        return

    if product <= k / a[i]:
        subset(a, n, i + 1, product * a[i], k, full + 1)
    
    subset(a, n, i + 1, product, k, full)


def solve():
    global cnt
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    cnt = 0
    subset(a, n, 0, 1, k, 0)
    
    print(cnt)


t = 1
# t = int(input())
for _ in range(t):
    solve()