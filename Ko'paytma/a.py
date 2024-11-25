x=int(input())
s=0
n=0
if x==0:
    s=-1
else:
    if x<0:
        n=-x
    else:
        n=x
    i=1
    while i*i<=n:
        if n%i==0:
            s+=1
            if i*i!=n:
                s+=1
        i+=1
    if s%2 and x>0:
        s+=1
print(s)