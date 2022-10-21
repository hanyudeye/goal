# 正则对象

# 英文
import re
str="hello,world,Ni HAO hao"
pat="hello"

result=re.search(pat,str)
# print(result.group())

if result is not None:
    print(result.group())
