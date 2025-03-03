from sklearn.datasets import load_boston
# linear regression 是指线性回归
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# 数据集划分
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

# 创建模型
model=LinearRegression()
# 模型训练
model.fit(X_train,y_train)

# 模型预测
y_pred=model.predict(X_test)

# 模型评估
print("Mean squared error: %.2f",mean_squared_error(y_test,y_pred))