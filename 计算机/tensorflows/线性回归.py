import tensorflow as tf
import numpy as np

# 构造数据
X_train = np.array([1, 2, 3, 4])
y_train = np.array([0, -1, -2, -3])

# 定义模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# 编译模型
model.compile(optimizer='sgd', loss='mean_squared_error')

# 训练模型
model.fit(X_train, y_train, epochs=1000, verbose=0)

# 打印结果
print("W: %s, b: %s" % (model.layers[0].get_weights()[0], model.layers[0].get_weights()[1]))