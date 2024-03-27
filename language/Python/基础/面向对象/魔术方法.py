class student:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age


    # __str__ 魔术方法可以用 print 打印
    def __str__(self) -> str:
        return "这是一个学生类"
    
    # 小于，大小逻辑判断 ,等于 __eq__ ，大于 __gt__
    def __lt__(self,other):
        return self.age<other.age


        
s=student("张",34)
print(s)

other=student("李",21)
print(s<other)