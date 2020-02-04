# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
x=input("第一个字母:")
if x=="S":
    x=input("第二个字母:")
    if x=="a":
        print("Saturday")
    elif x=="u":
        print("Sunday")
    else:
        print("错误")
if x=="M":
    print("Monday")
if x=="W":
    print("Wednesday")
if x=="F":
    print("Friday")
if x=="T":
    x=input("第二个字母:")
    if x=="u":
        print("Tuesday")
    elif x=="h":
        print("Thursday")
    else:
        print("错误")