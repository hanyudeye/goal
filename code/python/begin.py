# def  calculator(x,y,operator):
#        if operator == '+':
#            return x + y
#        elif operator == '-':
#            return x - y
#        elif operator == '*':
#            return x * y
#        elif operator == '/':
#            return x / y
#        else:
#            return "Wrong"
# print(calculator(1,3,'+') )
# print(calculator(1,3,'-') )
# print(calculator(2,3,'*') )
# print(calculator(2,3,'/') )

# 1. **斐波那契数列生成器：** 编写一个生成器函数，能够无限生成斐波那契数列的元素。

# def fbnq(n):
#     if n<=0:
#         return 0
#     else: 
#         return 1*

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# # 使用生成器函数生成斐波那契数列的前10个元素
# fibonacci_gen = fibonacci_generator()
# for _ in range(10):
#     print(next(fibonacci_gen))

# num=3
# print(f'{num}')

# print("hello",end="你好")

# print(f"{type(None)}")

nums=[3,4,6]
nums.remove(3)
print(nums)
