# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# print(8*7*6*5*4*3*2)

def fac(num):
    if num==0:
        return 1
    return num*fac(num-1)

l=[4,2,1,8]

result=[]

for i in l:
    result.append(str(fac(i)))

# print(result)
print(','.join(result))
