# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
a=str(input("输入一个字符串:"))
zimu=0
shuzi=0
kongge=0
qita=0
for i in a:
    if i.isalpha():
        zimu+=1
    elif i.isdigit():
        shuzi+=1
    elif i.isspace():
        kongge+=1
    else:
        qita+=1
print("字母有:%d个,数字有%d个,空格有%d个,其他%d个"%(zimu,shuzi,kongge,qita))