# 求100之内的素数
from math import sqrt
a=[]
for i in range(2,101):
    for j in range(2,int(sqrt(i)+1)):
        if i%j==0:
            break
    else:
        a.append(i)
print(a)
