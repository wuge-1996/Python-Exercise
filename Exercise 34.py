# 使用lambda来创建匿名函数。
MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x
a = 50
b = 30
print('The largar one is %d' % MAXIMUM(a, b))
print('The lower one is %d' % MINIMUM(a, b))