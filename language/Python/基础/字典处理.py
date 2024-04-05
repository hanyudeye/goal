# 字典，对象，相当于一个 命名的数组，不同于数字，文字型 数据
# 比如: 商场里的各种东西的价格，进行说明的化就方便

# 备注：单位是 圆
prices={
    "egg":5,
    "fish":10,
    "pork":15
}

print(prices)
# 命名数组重新命名
print(list(zip(prices.values(),prices.keys())))
print(max(zip(prices.values(),prices.keys())))
print(min(zip(prices.values(),prices.keys())))
