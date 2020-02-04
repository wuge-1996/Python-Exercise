from random import randint
y=int(randint(1,10))
for i in range(3):
    x = int(input("猜数字:\n"))
    if x >y:
        print("大了")
    elif x<y:
        print("小了")
    else:
        print("猜对了")
        break
print("Game over!")