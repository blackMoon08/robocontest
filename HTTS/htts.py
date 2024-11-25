n = int(input())
s = 0
while n > 0:
    y = n % 10
    s += 1
    if y % 2 == 0:
        print("NO")
        exit()
    n //= 10
if s % 2 == 1:
    print("YES")
else:
    print("NO")