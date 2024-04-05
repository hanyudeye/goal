# 一个程序，弄出多个人来，分布做各自的事情。

import time
import threading

def worker(name):
    for i  in range(5):
        print(name,i)
        time.sleep(0.5)

# worker('计数A')

t1=threading.Thread(target=worker,args=('计数A',))
t1.start()

t2=threading.Thread(target=worker,args=('计数B',))
t2.start()

print("完成")