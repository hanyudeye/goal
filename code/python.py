
# 最大质数,largest prime factor
def max_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# print(max_prime_factor(13195))

# 最大公约数,greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# print(gcd(12, 17))

# 获取文本内容
def get_text_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# print(get_text_content('code/python.py'))

# 通过三角形的三条边长，计算三角形面积
# 海伦公式（Heron's formula）
def triangle_area(a, b, c):
    # 三角形的半周长
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# print(triangle_area(3, 4, 5))

# 余弦定理
def cos_theorem(a, b, c):
    return (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
# print(cos_theorem(3, 4, 5))
# print(cos_theorem(5, 12, 13))
# print(cos_theorem(8, 15, 21))

# 播放音乐文件 a.mp3  
def play_music(file_path):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# play_music('code/a.mp3')

# 前n个自然数平方和的公式
def sumOfSeries(n):
    x = n * (n + 1) / 2     # 计算前n个自然数的和
    return (int)(x * x)      # 将结果平方并转为整数
# print(sumOfSeries(10))    # 3025

# 求 前 n 个自然数的和
def sum_of_series(n):
    return n * (n + 1) // 2  # 计算 1 + 2 + 3 + ... + n

# print(sum_of_series(3))

# armstrong number
# Armstrong number(阿姆斯特朗数)是一个数字，它等于其每个数字的n次方之和，其中n是该数字的位数
def is_armstrong_number(n):
    return n == sum([int(i) ** len(str(n)) for i in str(n)])

# print(is_armstrong_number(153))  # True
# print(is_armstrong_number(41))  # False


## 字符串操作
print("hello".upper())  # HELLO ，转为大写
print("HELLO".lower())  # hello ，转为小写



