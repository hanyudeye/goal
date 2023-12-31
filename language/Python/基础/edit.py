# 文件编辑器
# useage: edit filename

import os
import sys

if len(sys.argv) !=2:
    print("use age python edit.py {filename}")
    sys.exit(-1)

filename=sys.argv[1]

fd=open(filename,"r+",encoding="utf-8")
content=fd.read()
# ,encoding="utf-8"
print(content)
fd.close()