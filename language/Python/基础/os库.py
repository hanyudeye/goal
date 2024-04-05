import os

on_rtd=os.environ.get('PATH',None) 
# print(on_rtd)

filename=os.environ.get('PYTHONSTARTUP')
print(filename)


# 删除文件
# os.remove()

# 重命名
# os.rename()