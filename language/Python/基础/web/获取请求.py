import requests
import json

# 接口地址
api_url="https://baidu.com"

# 发送请求
response=requests.get(api_url)

# 解析响应
# data=json.loads(response.content)

# 处理响应
# print(data)

# 上面的json会解析错误，直接打印响应内容了
print(response.content)

