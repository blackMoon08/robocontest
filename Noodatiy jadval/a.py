for _ in range(int(input())):
        n,m=map(int,input().split())
        if n%2==0:
                x=(n-1)//2*10+2*m-1
        else:
                x=n//2*10+2*(m-1)
        print(x,end=' ')