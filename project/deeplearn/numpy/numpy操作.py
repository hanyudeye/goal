import numpy

x= numpy.array([1.0,2.0,3.0])
y=numpy.array([2.0,3.0,4.0])
print(x+y)
print(x/y)
print(type(x))
print([1,2,3])

A=numpy.array([[1,2],[3,4]])
B=numpy.array([[1,2],[3,4]])
print(A)
print(A+B)
print(A*B)


# 广播： 标量扩展4个，1维数组也扩展4个(上下复制)
print(A*10)

# 访问元素
print(A[0])
print(A[0][0])

# 数组变平，转一维
print(A.flatten())
# 布尔运算
print(A > 3)

