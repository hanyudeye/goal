ls=[1,2,3,4,7,5,6]

# 对象自我修改
ls.sort()
print(ls)

# list 类的方法
nums=[2,3,1,2,4,1,5,2]
list.sort(nums)

print(nums)

names=["aa","bbb","c","dddd","ee"]
# 排序形式，根据长度进行排序
list.sort(names,key=len)
print(names)


# sorted 可以对任意类型的序列进行排序，返回新对象
nums=[2,3,1,2,4,1,5,2]
out=sorted(nums)
print(out)


