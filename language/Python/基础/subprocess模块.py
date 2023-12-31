# 执行shell 命令

import subprocess

obj=subprocess.Popen('ls /',shell=True,stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)

print(obj)
# err_res=