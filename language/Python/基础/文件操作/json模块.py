import json

# 序列化与反序列化
res=json.dumps([1,'aaa',True,False])
print(res,type(res))


# 反序列化
res=json.loads(res)
print(res,type(res))
