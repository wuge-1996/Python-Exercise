# 输出 9*9 乘法口诀表。
# i控制行，j控制列
for i in range(1,10):
    for j in range(1,i+1):
        if i>j:
            print("%d*%d=%d"%(i,j,i*j),end=" ")
        if i<=j:
            print("%d*%d=%d" % (i, j, i * j))
