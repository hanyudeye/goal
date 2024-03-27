class student:
    def __init__(self) -> None:
        pass

# 构造方法
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("创建了类")


s=student("小李",23,"131233123")

print(s.age)

     