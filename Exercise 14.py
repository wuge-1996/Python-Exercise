# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
s=[]
t=0
a=int(input("a= "))
b=int(input("b= "))
for x in range(a):
    t=t+b
    b=b*10
    s.append(t)
    print(t)
print(sum(s))