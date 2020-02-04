# 1+2!+3!+...+20!的和。
x=1
y=0
for i in range(1,21):
    x=x*i
    y=y+x
print(y)