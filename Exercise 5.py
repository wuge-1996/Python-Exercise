# 输入三个整数x,y,z，请把这三个数由小到大输出。
x=[]
for i in range(0,3):
    i=int(input("数字:"))
    x.append(i)
x.sort()
print(x)