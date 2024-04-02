import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.fc1 = nn.Linear(in_features=64 * 5 * 5, out_features=128)
        self.fc2 = nn.Linear(in_features=128, out_features=10)

    def forward(self, x):
        x = nn.functional.relu(self.conv1(x))
        x = nn.functional.max_pool2d(x, kernel_size=2)
        x = nn.functional.relu(self.conv2(x))
        x = nn.functional.max_pool2d(x, kernel_size=2)
        x = x.view(-1, 64 * 5 * 5)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

        
        
# 这段代码是一个简单的神经网络模型，用于图像分类任务，具体含义如下：

# import torch.nn as nn: 导入PyTorch深度学习框架中的nn模块，用于定义神经网络。

# class NeuralNetwork(nn.Module):: 定义了一个名为NeuralNetwork的类，继承自nn.Module类，这是PyTorch中定义神经网络模型的一种常见方式。

# def __init__(self):: 定义了类的初始化方法。在初始化方法中，进行了神经网络模型的初始化操作。

# self.conv1 = nn.Conv2d(1, 32, 3, 1): 创建了一个二维卷积层，conv1，输入通道数为1，输出通道数为32，卷积核大小为3x3，步幅为1。

# self.conv2 = nn.Conv2d(32, 64, 3, 1): 创建了另一个二维卷积层，conv2，输入通道数为32，输出通道数为64，卷积核大小为3x3，步幅为1。

# self.fc1 = nn.Linear(in_features=64 * 5 * 5, out_features=128): 创建了一个全连接层，fc1，输入特征数为6455（由于经过两次池化层，图像尺寸减半两次），输出特征数为128。

# self.fc2 = nn.Linear(in_features=128, out_features=10): 创建了另一个全连接层，fc2，输入特征数为128，输出特征数为10，这里的10代表着图像分类的类别数。

# def forward(self, x):: 定义了前向传播方法，用于定义数据在神经网络中的流动过程。

# x = nn.functional.relu(self.conv1(x)): 执行第一个卷积操作，并将结果通过ReLU激活函数处理。

# x = nn.functional.max_pool2d(x, kernel_size=2): 执行最大池化操作，将特征图尺寸缩小一半。

# x = nn.functional.relu(self.conv2(x)): 执行第二个卷积操作，并将结果通过ReLU激活函数处理。

# x = nn.functional.max_pool2d(x, kernel_size=2): 再次执行最大池化操作，将特征图尺寸缩小一半。

# x = x.view(-1, 64 * 5 * 5): 将特征图展平成一维向量，以便送入全连接层。

# x = nn.functional.relu(self.fc1(x)): 执行第一个全连接层操作，并将结果通过ReLU激活函数处理。

# x = self.fc2(x): 执行第二个全连接层操作，这一层不需要激活函数，因为后续将使用交叉熵损失函数计算损失，它内部会进行softmax操作。

# return x: 返回最终的输出。





