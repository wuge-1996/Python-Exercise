# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半多一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
x=1
y=[]
for i in range(1,11):
    y.append(x)
    x=(x+1)*2
print(y[-1])