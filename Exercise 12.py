# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
x=float(input("分数:"))
if x>=90:
    jibie="A"
if 60<=x<90:
    jibie="B"
if x<60:
    jibie="C"
print("级别:%s"%jibie)
