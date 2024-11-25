a,b=map(int,input().split())
s=''
l=0
c=list(map(int,input().split()))
for i in range(a):
    d=c[i]
    if d==b:
        l+=1
        i+=1
        i=str(i)
        i=i+' '
        s=s+i
print(l*b)
print(s,end=' ')