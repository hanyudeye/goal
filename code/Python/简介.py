

class 数学:
    def 求和(self,x,y):
        return x+y

    def 求差(self,x,y):
        return x-y


数学实例= 数学()
he=数学实例.求和(10,3)

print(he)
# 类型转换
print(int('45'))

偶数=[2,4,6]
偶数.append(8)
print(偶数)

# 成员操作
家庭=("父亲","母亲","子女")
是否成员="母亲" in 家庭
print(是否成员)


# 不是一般的逻辑操作
five=5
two=2
print(two and five)
print(five and two)

try:
    print("hello")
    a=int("hfsd")
except ValueError as e:
    print("错误",e)
