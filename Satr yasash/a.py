n=list(map(int,input().split()))
sums=sum(n)
abc="abcdefghijklmnopqrstuvwxyz"
mn="0"
edt=False
while True:
    if sum(n)==0:
        break
    k1=max(n)
    mx=n.index(k1)
    n[mx]=0
    nwstr=abc[mx]

    k2=max(n)
    mx1=n.index(k2)
    nwstr1=abc[mx1]
    n[mx]=k1
    if mn[-1]!=nwstr:
        mn+=nwstr
        n[mx]-=1

    elif mn[-1]!=nwstr1:
        mn+=nwstr1
        n[mx1]-=1


print(mn[1:])