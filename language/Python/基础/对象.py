class Pig:
    def __init__(self) -> None:
        self.name="我是一只猪"

# 只允许一个构造函数
    def __init__(self,name) ->None:
        self.name="我是",name

    def showname(self):
        print(self.name)



pig=Pig("狗")
pig.showname()

# 显示对象id ，内存地址
print(id(pig))

