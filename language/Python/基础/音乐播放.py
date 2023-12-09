import pyaudio  
import playsound

# 创建 PyAudio 对象  
pa = pyaudio.PyAudio()

# r=pyaudio.PyAudio.get_default_input_device_info()

# 获取默认通道数量  
channels = pa.get_default_channel_count()

# 创建缓冲区  
buffer_size_seconds = 0.5  # 缓冲区大小为 0.5 秒  
buffer = pyaudio.format_from_socket_time_func(  
    pa.open(  
        format=pyaudio.paInt16,  
        channels=channels,  
        rate=44100,  
        input=True,  
        frames_per_buffer=buffer_size_seconds * buffer_size,  
        input_buffer_time_func=buffer_size_seconds,  
    )  
)

# 播放音频文件  
# playsound.playsound(file="path/to/your/file.mp3")
playsound.playsound(file="J:\me\Shijian\a.mp3")
# 等待音频播放完毕  
pa.wait_for_output(block=False)

# 关闭 PyAudio 对象  
pa.close()  
