import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# 播放音乐文件，这里假设音乐文件名为 "music.mp3"，请替换为你实际的音乐文件路径
# play_music("music.mp3")
play_music("I:\\music\\纯音乐\\骑蜗牛.wav")
# 
# 让音乐播放一段时间
# pygame.time.wait(5000)  # 播放5秒钟
pygame.time.wait(305000)  # 播放6分钟

# 停止音乐
pygame.mixer.music.stop()

# 退出pygame
pygame.quit()