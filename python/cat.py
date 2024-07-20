# 1. 调用 系统内部cat 命令

import subprocess

def cat(filename):
    try:
        output=subprocess.check_output(['cat',filename])
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# cat('test')


# 2. 方法2
def cat2(filename):
    try:
        with open(filename,'r') as file:
            for line in file:
                print(line,end='') #避免重复换行

    except FileNotFoundError:
        print(f"Error:{filename} not found")

    except PermissionError:
        print(f"Error: {filename} Permission denied")

    except Exception as e:
        print(f"Error: An unexpected error occured:{e}")

cat2('test')
 
