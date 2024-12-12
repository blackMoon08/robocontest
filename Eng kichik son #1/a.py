#!Diyorbek Qurbonov 
#!Telegramim @dimadev_coder
import itertools
def main(n):
    return [''.join(x) for x in itertools.product('+-*/', repeat=n)]
n=int(input())
son = str(n)
length = len(son)-1
ifoda = ""
l = []
for LIST in main(length):
    for sign in range(length):
        ifoda += son[sign]+LIST[sign]
    ifoda += son[-1]
    if not "/0" in ifoda:
        temp = eval(ifoda)
        if temp == int(temp):
          l += [int(temp)]
    ifoda = ""
print(min(l))