height=float(input("身高:\n"))
weight=float(input("体重:\n"))
bmi = weight/(height**2)
if bmi<18.5:
    print("体重过轻")
elif 18.5<=bmi<25:
    print("正常")
elif 25<=bmi<28:
    print("过重")
elif 28<=bmi<32:
    print("肥胖")
else:
    print("严重肥胖")
