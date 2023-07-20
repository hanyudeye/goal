# -*- coding: utf-8 -*-

def 可变参数(arg1,*argv):
    print("first arg is",arg1)
    for arg in argv:
        print("其它参数是",arg)



if __name__=='__main__':
    可变参数("参数1","参数2","参数3","参数4")