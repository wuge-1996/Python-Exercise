# 两个变量值互换
def fn(x,y):
    x,y=y,x
    return(x,y)
print(fn(10,20))