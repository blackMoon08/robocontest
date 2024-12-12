a=[]
for z in range(4):
  n=input()
  l=[]
  l.extend(n)
  a.append(l)
for v in range(int(input())):
    c,x,y=input().split()
    if c=='U':
        for i in range(4):
          for j in range(4):
            if a[i][j].isdigit():
                k=i
                while k!=0:
                    m=a[k][j]
                    if not a[k-1][j].isdigit():
                        a[k][j]='*'
                        a[k-1][j]=m
                    else:
                            if a[k-1][j]==a[k][j]:
                                a[k-1][j]=str(int(a[k-1][j])*2)
                                a[k][j]='*'
                                break
                            else:
                                break
                    k-=1
    elif c=='D':
      for i in range(3,-1,-1):
          for j in range(4):
            if a[i][j].isdigit():
                k=i
                while k!=3:
                    m=a[k][j]
                    if not a[k+1][j].isdigit():
                        a[k][j]='*'
                        a[k+1][j]=m
                    else:
                            if a[k+1][j]==a[k][j]:
                                a[k+1][j]=str(int(a[k+1][j])*2)
                                a[k][j]='*'
                                break
                            else:
                                break
                    k+=1
    elif c=='L':
      for i in range(4):
        for j in range(4):
          if a[i][j].isdigit():
            k=j
            while k!=0:
              if a[i][k-1].isdigit():
                if a[i][k]==a[i][k-1]:
                  a[i][k]='*'
                  a[i][k-1]=str(int(a[i][k-1])*2)
                  break
                else:
                  break
              else:
                a[i][k-1]=a[i][k]
                a[i][k]='*'
              k-=1
    elif c=='R':
      for i in range(4):
        for j in range(3,-1,-1):
          if a[i][j].isdigit():
            k=j
            while k!=3:
              if a[i][k+1].isdigit():
                if a[i][k]==a[i][k+1]:
                  a[i][k]='*'
                  a[i][k+1]=str(int(a[i][k+1])*2)
                  break
                else:
                  break
              else:
                a[i][k+1]=a[i][k]
                a[i][k]='*'
              k+=1
    if not a[abs(4-int(x))][int(y)-1].isdigit():
     a[abs(4-int(y))][int(x)-1]='2'
p=[]
for i in range(4):
    for j in range(4):
        if a[i][j].isdigit():
          p.append(int(a[i][j]))
print(max(p))


#!Diyorbek Qurbonov coder 
#! @dimadev_coder telegramim