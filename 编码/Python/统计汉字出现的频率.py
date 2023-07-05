from collections import Counter
# J:\me\Shijian\Python\统计汉字出现的频率.py
# 识别文件的时候要使用编码
fd=open(r'J:/me/Shijian/Python/测试文档.txt',"r",encoding="utf-8")
s=fd.readline()
result=Counter(s)
print(result)

