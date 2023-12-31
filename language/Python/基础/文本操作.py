# 文本内容 是  "hello, baby"

# 文本截取，截取第3 个到第5个，截取了两个文字，本身要注意不能过长

a="hello, baby"
print(a[3:5])

# 文本中，替换某一段文本
res=a.replace("hello","how are you")
print(res)

# 拼接文本，把文本串 ，用 某个符号串起来
res=a.join("||||")
print(res)

res='.'.join(["nice","to","meet","you"])
print(res)

