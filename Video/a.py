from math import *
a,b,c=map(int,input().split())
m=((c*a)-(b*c))
n=m/b
print(ceil(n))