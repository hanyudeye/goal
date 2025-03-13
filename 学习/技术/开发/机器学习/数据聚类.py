import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. 生成一些模拟数据
np.random.seed(42)
# 生成两组不同分布的数据点
data1 = np.random.normal(loc=[2, 2], scale=0.8, size=(100, 2))
data2 = np.random.normal(loc=[7, 7], scale=0.8, size=(100, 2))
data = np.vstack((data1, data2))

# 2. 使用K-Means算法进行聚类
kmeans = KMeans(n_clusters=2, random_state=42)  # 指定分为2个聚类
kmeans.fit(data)  # 训练模型
labels = kmeans.labels_  # 获取每个点的聚类标签
centers = kmeans.cluster_centers_  # 获取聚类中心

# 3. 可视化结果
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.6, edgecolor='k')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centers')
plt.title("K-Means Clustering Example")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()