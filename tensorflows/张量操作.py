import tensorflow as tf

# 创建两个张量
tensor1 = tf.constant([[1, 2], [3, 4]])
tensor2 = tf.constant([[5, 6], [7, 8]])

# 加法操作
result = tf.add(tensor1, tensor2)
print(result)
print(result.numpy())
