# 标准输入

import os
# res= os.read(0,30)

# print(res)


# 标准输出
# os.write(1,b"hello\n")
# os.write(1,b"hello")

f=open("j:/test.txt","r",encoding="utf-8")

# content=f.read()
# count=content.count("hello")
# print("在文件中出现了",count)
count=0

for line  in f:
    words= line.split(" ")
    for word in words:
        if word=="hello":
         # print(words)
         count+=1

print(count)
f.close()
