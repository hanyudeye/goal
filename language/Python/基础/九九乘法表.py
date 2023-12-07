'''
1*1=1

1*2=2 2*2=4
...

1*9=9  2*9=18  .. 9*9=81

'''

# 方法1:

for i in range(1,10):
    print('')
    for j in range(1,i+1):
        print('%d*%d=%d' %(j,i,i*j),end='   ')


