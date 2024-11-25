n=int(input())
if n<38: print(n)
else:
    if n%5==0: print(n)
    else:
        if (n//5+1)*5-n>=3: print(n)
        else:
            print((n//5+1)*5)