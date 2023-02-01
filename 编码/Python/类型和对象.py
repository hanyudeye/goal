
# 对象之间的比较

def compare(a,b):
    if a is b:
        print("a is b")
    if a==b:
        print("a和b有相同的值")
    if type(a)==type(b):
        print("a和b有相同的类型")


# a={3.32,2}
# b={3.32,2}

# compare(a,b)


import re;

result=re.match("helo","heloo",0).group()
print(result)
