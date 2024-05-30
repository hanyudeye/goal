import re

# 定义Token类型
class TokenType:
    NUMBER='NUMBER'
    PLUS='PLUS'
    MINUS='MINUS'
    EOF='EOF'

# Token 类
class Token:
    def __init__(self,type,value) -> None:
       self.type=type
       self.value=value 

    def __repr__(self) -> str:
        return f'Token({self.type},{repr(self.value)})'



def main():


if __name__=='__main__':
    main()