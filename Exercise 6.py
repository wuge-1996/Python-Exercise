# 斐波那契数列。在数学上，费波那契数列是以递归的方法来定义：
# Fn(0) = 0
# Fn(1) = 1
# Fn(n) = Fn[n-1]+ Fn[n-2](n=>2)
n=int(input(("输入:")))
def Fn(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fn(n-1)+Fn(n-2)
print("Fn(n)=",Fn(n))
