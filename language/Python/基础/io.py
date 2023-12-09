# 1. 打印命令行参数
# import sys
# print("参数是:",sys.argv)

# 输出
#  python .\code\Python\manual\io.py 1 2 3
# 参数是: ['.\\code\\Python\\manual\\io.py', '1', '2', '3']


# 2. 读取命令行选项
import optparse
# 引入选项分析器包

p=optparse.OptionParser()
# 使用分享器创建一个分析对象

# 分析对象，使用 选项-o ，说明这是 outfile，程序的输出指定一个文件
# action 指定参数类型
p.add_option("-o",action="store",dest="outfile")
p.add_option("-d",action="store_true",dest="debug")

p.set_defaults(d=False)

# 解析命令行，前面是解析出来的对象，后面是剩余参数列表，注意 剩余参数里不能有 -  选项
options,args=p.parse_args()
# 查询具体选项
outfile=options.outfile
debug=options.debug

# print("选项-o是：",outfile)
# print("选项-d是：",debug)
# print("其他参数是：",args)

# 输出:
# python .\code\Python\manual\io.py -o a.txt 1  2 3     
# 选项-o是： a.txt
# 选项-d是： None
# 其他参数是： ['1', '2', '3']

# 3. 环境变量

import os
# print(os.environ['PATH'])
# print(os.environ['USER'])
# print(os.environ['PWD'])
# print(os.environ['TMP'])

