
# 对象之间的比较

def compare(a,b):
    if a is b:
        print("a is b")
    if a==b:
        print("a和b有相同的值")
    if type(a)==type(b):
        print("a和b有相同的类型")

import re;

# result=re.match("helo","heloo",0).group()
# print(result)

# 二进制
# print(0b101)
# 八进制
# print("hello,",0o12)
# 十六进制
# print(0x12)

# 浮点数 (精度差)
pi=3.1415925
# print(2.2+1.1)
# print(type(pi))
# 更精确 
# from decimal import Decimal
# print(Decimal(1.1)+Decimal(2.2))

# 空调降温(15)

def low_wendu(num):
    print("降温到 ",num,"°")

low_wendu(22)

# print('我教'+'语文'+str(12))
# print("语文","数学","123")