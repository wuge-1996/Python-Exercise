# 输入四位数整数，每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
y = int(input("输入一个数:"))
x = []
x.append(int(y / 1000))
x.append(int(y / 100) % 10)
x.append(int(y / 10) % 10)
x.append(int(y % 10))


for i in range(len(x)):
    x[i] = (x[i] + 5) % 10
x.reverse()
for j in x:
    print(j, end="")