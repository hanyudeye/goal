import json
bicycles = ['trek', 'cannondale', 'redline', 'specialized',"鸡蛋"]
goup={"msg":"这里是嘎斯打法收到"}

# goup.popitem()
# goup.update({"msg":"嘎斯打法收到"})
# goup['aaa'] = "bicycles"

sorted(bicycles)
bicycles.sort(reverse=False)

print(bicycles)

for bicycle in bicycles:
    print(bicycle.capitalize())