import time

def worker(name):
    for i  in range(5):
        print(name,i)
        time.sleep(0.5)

worker('计数A')

print("完成")