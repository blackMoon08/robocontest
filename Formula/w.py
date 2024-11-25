from math import *
x,y=map(float,input().split())
f=(1/(x+2/pow(x,2)+3/pow(x,3))+exp(x*x+3*x))/(atan(x+y)+(x+5)*(x+5))-cos(y*y+x*x/2)*cos(y*y+x*x/2);
print('%.2f'%(f))