# 判断101-200之间有多少个素数，并输出所有素数。
from math import sqrt
a = []
for i in range(101,201):
    for j in range(2,101):
        if i%j==0:
            break;
    else:
        a.append(i)
print(a)