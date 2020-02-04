# 利用递归方法求5!
def fact(j):
    if j == 0:
        return 1
    else:
        return j * fact(j - 1)
print(fact(5))