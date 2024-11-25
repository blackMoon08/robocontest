n=int(input())
if n%4==3:
    print(int(((n+4)**(1/2)-1)/4))
else:
    print(-1)