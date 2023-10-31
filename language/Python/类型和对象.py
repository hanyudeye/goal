
# is : 判断对象是不是同一类型

import re
import sys
import os


class O:
    pass

# 继承


class P(O):
    pass


a = b = O()
c = P()

print(a is b)
print(a is c)
print(c is a)
print(isinstance(c, O))



def compare(a, b):
    if a is b:
        print("a is b")
    if a == b:
        print("a和b有相同的值")
    if type(a) == type(b):
        print("a和b有相同的类型")



# result=re.match("helo","heloo",0).group()
# print(result)

# sys.exit()
# 二进制
# print(0b101)
# 八进制
# print("hello,",0o12)
# 十六进制
# print(0x12)
# 浮点数 (精度差)
pi = 3.1415925
# print(2.2+1.1)
# print(type(pi))
# 更精确
# from decimal import Decimal
# print(Decimal(1.1)+Decimal(2.2))

# 空调降温(15)


def low_wendu(num):
    print("降温到 ", num, "°")


low_wendu(22)

# print('我教'+'语文'+str(12))
# print("语文","数学","123")

# 类型转换
元组 = (1, 3, 4, 4, 5, 6, 6)
print(元组)

集合 = set(元组)
print(集合)

队列 = [1, 3, 4, 4, 5, 5]
集合1 = set(队列)
print(队列[2])
print(队列.__getitem__(3))
print("hello")

字典 = {"名字": "3毛", "身高": 150, "职业": "活宝"}
集合2 = set(字典)
print(集合2)

# 类是为了对象复用,因为函数也包含在对象里面,所以函数也能复用


class Person:
    def __init__(self, name, age, sex: str):
        self.name = name
        self.age = age
        self.sex = sex

    def name(self):
        return self.name

    def age(self):
        return self.age


小李 = Person("小李", 33, "女")
print(小李.age)

# 类的继承


class 黑人(Person):
    def __init__(self, name, age, sex: str):
        super().__init__(name, age, sex)
        self.color = "黑色"


小黑 = 黑人("小黑", 23, "女")
print(小黑.color)
