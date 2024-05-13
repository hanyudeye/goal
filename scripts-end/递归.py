
# 创建递归功能，调用自己，需要有一个 逻辑器让递归终止
def digui(count):
   if(count<0): 
    print("end")
   else:
       print(count)
       count-=1
       digui(count)


# digui(6)
digui(3)