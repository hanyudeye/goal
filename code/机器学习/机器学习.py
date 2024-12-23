# 数学基础

# 向量

import numpy as np

# 标量，没有方向
s=5
# print(s)

# 向量，有大小和方向，2个量表示
v=np.array([1,2])
# print(v)

# 矩阵
m=np.array([[1,2],[3,4]])
# print(m)

# 张量 tensor ，超过二维的数组
t=np.array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[11,12,13],[14,15,16],[17,18,19]],
    [[21,22,23],[24,25,26],[27,28,29]]
])
# print(t)

print( np.__version__)
