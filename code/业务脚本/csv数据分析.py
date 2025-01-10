import pandas as pd

# 加载客户数据
data = pd.read_csv("code/customer_data.csv")

data['last']
print(data.head())