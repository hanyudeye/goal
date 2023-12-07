
print("Hello","World!")

# 异常判断
try:
    # print(3/0)
    print("good")
except ZeroDivisionError:
    print("3不能除以0")

else:
    print("good")


# name=input("请输入你的名字")

# if name:
#     print('你的名字叫',name,"欢迎您!")


def func(name):
    print("欢迎您",name)

func("aming")

# import module_example

print(2<2)

s="hello, world"

print(s.capitalize())
print(s.title())
print(s.center(20," "))
print(s.rjust(20," "))
print(s.count('l'))
print(s.islower())
print(s.upper())

s=["abc","def","ghi"]
b=reversed(s)
# print(" ".join(reversed(s)))
# print(b)
# print(" ".join(b))
# print(" ".join(b))

riqi="2023-10-11"
print(riqi.split('-'))

artist="Tag你好"

# artist.encode("Latin1")

# print(artist)

artist.encode("utf16")
print(artist)