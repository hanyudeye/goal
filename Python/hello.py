# -*- coding: utf-8 -*-

count=10

while count>0:
    print("{0:0.1f}".format(count))
    count-=1

# if 3>2:
    # print("good")

# if "hello.exe" in ["hello.exe","hello.jpg"]:
    # print("nice")

f=open("计算.py")
line=f.readline()
while line:
    print(line)
    line=f.readline()

