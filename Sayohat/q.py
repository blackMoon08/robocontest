import math as m
a, b = map(int, input().split())
cnt = 0
cnt = sum(1 for i in range(1, 7) if i >= a and i >= b)
gcd = m.gcd(cnt, 6)
surat = cnt // gcd
mahraj = 6 // gcd
print(f"{surat}/{mahraj}")