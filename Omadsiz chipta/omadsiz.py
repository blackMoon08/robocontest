a=input()
s=0
for i in range(len(a)-1):
    if a[i]== "1" and a[i+1]=="3":
        s=s+1
if s==0:
    print("omadli chipta")      
else:
    print("omadsiz chipta")