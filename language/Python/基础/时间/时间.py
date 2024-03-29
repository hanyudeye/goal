# 时间格式: 
# 1. 时间戳 ： 1970 到现在的秒数

import time
print(time.time())


# 2. 字符串格式 2023-10-11 11:11:12
print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
print(time.strftime('%Y-%m-%d %X'))

# 3. 结构化的时间
res=time.localtime()
print(res)
print(res.tm_hour)

# datetime，时间运算
import datetime
# 直接格式化
print(datetime.datetime.now())


