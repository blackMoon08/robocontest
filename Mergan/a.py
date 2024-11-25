def diyorbek(a, n):
    probability = (n * 1) * (1 - a) * (a ** (n - 1))
    return probability

a, n = map(float, input().split())
tmp = diyorbek(a, n)
asd =format(tmp,'.4f')
print(asd)