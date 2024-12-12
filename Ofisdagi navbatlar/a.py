l=[]
for i in range(int(input())):
    l.append(tuple(map(int,input().split())))
e=1
t=0
for i in range(0,len(l)):
    if(i!=0 and l[i][0]==l[i-1][0]):
        f=l[i][1]-e
        if f<0:
            f =f*-1
        if(l[i][1]!=l[i-1][1]):
            t=t+1
        t=t+(f)
        if(l[i][1]<l[i-1][1]):
            t=t-(l[i-1][1]-l[i][1])
        e=l[i-1][1]
    else:
        k=l[i][0]-e
        if k<0:
            k=k*-1
        t=t+(k)
        e=l[i][0]
        f=l[i][1]-e
        if f<0:
            f=f*-1
        t=t+(f)
        t=t+2
        e=l[i][1]
print(t)