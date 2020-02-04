# 输入某年某月某日，判断这一天是这一年的第几天？
# 特殊情况，闰年2月份以上要多加1天
year=int(input("年份:"))
month=int(input("月份:"))
day=int(input("日数:"))

months=(0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month<=12:
    sum=months[month-1]
else:
    print("错误")
sum=sum+day
days=0
if year%400==0 or year%4==0 and year%100!=0:
    days=1
    sum=sum+days
print("这一天是这一年的第%d天"%sum)