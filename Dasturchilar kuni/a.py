x=int(input())
a=""
if x<10:
    a="000"
elif x<100:
    a="00"
elif x<1000:
    a="0"
if x%400==0 or x%4==0 and x%100!=0:
    a=f"12/09/{a+str(x)}"
else:
    a=f"13/09/{a+str(x)}"
print(a)