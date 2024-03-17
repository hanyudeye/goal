from data_define import Record

# 创建抽象类
class FileReader:
    def read_data(self) ->list[Record]:
        pass


class TextFileReader(FileReader):
    def __init__(self) -> None:
        super().__init__()

    def __init__(self,path):
        self.path=path  #初始化路径

    def read_data(self) -> list[Record]:
        f=open(self.path,"r",encoding="utf-8")
        for line in f.readlines():
            print(line)

# J:\me\Shijian\language\Python\基础\面向对象\file_define.py
# J:\me\Shijian\language\Python\基础\面向对象\2024-2月销售额.txt
if __name__=='__main__':
    print("goo")
    text_file_reader=TextFileReader("J:/me/Shijian/language/Python/基础/面向对象/2024-2月销售额.txt")
    text_file_reader.read_data()
