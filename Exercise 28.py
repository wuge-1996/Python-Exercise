# 对10个数进行排序。
# 可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
N=10
l=[]
for i in range(N):
    l.append(int(input("输入一个数\n")))
    l.sort()
print(l)
x=int(input("插入一个数:\n"))
l.append(x)
l.sort()
print(l)