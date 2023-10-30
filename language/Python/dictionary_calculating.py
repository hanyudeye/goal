# example of calculating dictionaries 

prices={
    'alibaba':232,
    'tencent':231,
    'baidu':211,
    'FB':123
}

print(min(zip(prices.values(),prices.keys())))

# print(min([2,4,6,1]))
# print(prices.values())