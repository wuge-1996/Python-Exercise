# 计算n的阶乘！
def product(n):
    if ( n== 1):
        return 1
    return n * product(n-1)

# 计算阶乘结果有几个零
def countZero(m):
    if (m % 10 != 0):
        return 0
    return 1+ countZero(m/10)
n=int(input("计算阶乘:\n"))
p = product(n)
print("阶乘为:%d"%p)
print("有几个零:%d"%countZero(p))