s=input()
i=0
while i<len(s):
    k=1
    while i+1<len(s) and s[i]==s[(i+1)%len(s)]:
        i+=1
        k+=1
    if k>3:
        print(s[i]+'{'+str(k)+'}',end='')
    else:
        print(s[i]*k,end='')
    i+=1