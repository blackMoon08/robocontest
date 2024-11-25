a=int(input())
b=input().split()
t=''
for i in range(0,a):
    s=int(b[i])
    x1=((-1+(1+8*int(s))**0.5)/2)
    x2=((-1+(1+8*int(s))**0.5)/2)
    if s==0:
        t+='1'
    elif x1>0 and x2<0 and x1%1==0:
        t+='1'
    elif x1<0 and x2>0 and x2%1==0:
        t+='1'
    elif x1>0 and x2>0 and (x1%1==0 or x2%1==0):
        t+='1'
    else:
        t+='0'
print(t)