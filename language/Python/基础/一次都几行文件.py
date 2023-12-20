
i=[]
def get_lines():
    # with open('todo.md',"rb") as f:
    with open("test.md","rb") as f:
        data=f.readlines(15)
        print(data)
        i.append(data)
        yield i


# f=open(r"J:/me/Shijian/Python/test.md","+a",encoding="utf-8")
res=get_lines()
print(res)

print(i)