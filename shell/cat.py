import sys
import os
# 文件名参数 
argv1=sys.argv[1]

fs=open(argv1,"r")
str=fs.read()
print(str)