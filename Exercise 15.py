# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
x=100
y=[]
z=[]
j=int(input("落地次数:"))
for i in range(1,j+1):
    if i ==1:
        y.append(x)
    else:
        y.append(x*2)
    x=x/2
    z.append(x)
print("%d次后经过的总高度为:"%(j),sum(y))
print("第%d次反弹高度:"%(j),z[-1])