import os  
import pygame

# 初始化 Pygame  
pygame.init()

# 设置窗口大小  
screen_width = 640  
screen_height = 480  
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题  
pygame.display.set_caption("MP3 Player")

# 查找文件  
# file_path = os.path.join(os.path.expanduser("~"), "Desktop", "example.mp3")
file_path = "J:/me/Shijian/a.mp3"
# print(file_path)
# exit()

# 播放文件  
pygame.mixer.music.load(file_path)  
pygame.mixer.music.play()

# 保持窗口打开  
while pygame.mixer.music.get_busy():  
    pygame.display.update()  
    pygame.time.Clock().tick(30)

# 关闭窗口  
pygame.quit()  
