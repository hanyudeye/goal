# 1. 求几个数的平均数 和 和

nums=[1,3,5,7]
sum=0
average=0
count=0


for i in nums:
    try:
        sum+=i
        count+=1

    except ValueError as err:
        print(err)
        continue

average=sum/count
print("和是 ",sum," 平均数是",average)
