from torchvision import transforms  
from PIL import Image

# transforms 是一个用来对图片处理的库

# 相对路径 pytorch\dataset\lina.png

img_path="pytorch\dataset\lina.png"
img=Image.open(img_path)
# 显示图片信息
print(img)

tensor_trans = transforms.ToTensor()
tensor_img=tensor_trans(img)
print(tensor_img)
