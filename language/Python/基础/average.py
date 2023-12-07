# average1_ans.py

# 求平均值
numbers=[]
total=0
while True:
    try:
        line=input("enter a number or Enter to finish: ")

        if not line:
            break
        number=int(line)
        numbers.append(number)
        total+=number

    except ValueError as err:
        print(err)


print("numbers:",numbers)
print("total:",total)