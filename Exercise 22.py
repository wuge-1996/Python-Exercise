# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
x=int(input("输入一个数:"))
a=int(x/10000)
b=(int(x/1000))%10
c=(int(x/100))%10
d=(int(x/10))%10
e=x%10
if a!=0:
    print("五位数",a,b,c,d,e)
if a==0 and b!=0:
    print("四位数",b,c,d,e)
if a==0 and b==0 and c!=0:
    print("三位数",c,d,e)
if a==0 and b==0 and c==0 and d!=0:
    print("二位数",d,e)
if a==0 and b==0 and c==0 and d==0 and e!=0:
    print("一位数",e)
