# 打印斜着的爱心

# 返回与 count等量的空格
def space(count):
   return " "*count 

# 返回与 2倍 count等量的空格
def space2(count):
   return " "*count*2

count=0
while(count<10):
    print(space2(count)+"❤")
    count=count+1


