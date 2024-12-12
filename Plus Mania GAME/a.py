#!Diyorbek Qurbonov 
#!Telegramim @dimadev_coder
from pathlib import *
p=Path('nega')
if not(p.is_file()):
  f=open('nega','w')
  f.write('0')
  f.close()
f=open('nega')
s=f.readline()
f.close()
if s=='':
    s=1
else:
    s=int(s)+1
if s==4 or s==6 or s==10 or s==14 or s==20 or s==22 or s==24 or s==26 or s==28:
    print('yes')
elif s==34 or s==38:
    print('yes')
elif s%2==0 or s==9 or s==15 or s==17 or s==19 or s==33 or s==35:
    print('no')
else:
    print('yes')
f=open('nega','w')
f.write(str(s))
f.close()