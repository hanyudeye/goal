import math

'a test module'
__author__ = 'aming'


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs(-13))


def nop():
    pass

# nop()

# 通过弧度和步长移动
def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx, ny

# print(move(1,1,5,math.pi/2))

