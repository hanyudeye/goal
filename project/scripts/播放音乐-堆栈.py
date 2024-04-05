class MusicStack:
    def __init__(self):
        self.stack = []

    def add_song(self, song):
        if len(self.stack) == 0:
            self.stack.append(song)
            print(f"Added song: {song}")
        else:
            print("Cannot add song. Stack is full.")

    def play_song(self):
        if len(self.stack) > 0:
            print(f"Now playing: {self.stack[-1]}")
        else:
            print("No song to play.")

    def remove_song(self):
        if len(self.stack) > 0:
            song = self.stack.pop()
            print(f"Removed song: {song}")
        else:
            print("No song to remove.")

# 创建一个音乐播放歌单
music_stack = MusicStack()

# 添加歌曲
music_stack.add_song("Song 1")
music_stack.add_song("Song 2")

# 播放歌曲
music_stack.play_song()

# 删除歌曲
music_stack.remove_song()

# 再次播放歌曲
music_stack.play_song()