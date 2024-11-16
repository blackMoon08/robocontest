a,b,c,d,e=map(int,input().split())
q=a+b+c+d+e
q1=q-max(a,b,c,d,e)
q2=q-min(a,b,c,d,e)
print(q1,q2)