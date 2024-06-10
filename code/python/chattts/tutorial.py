# 环境配置
!git clone https://github.com/2noise/ChatTTS.git tts
%cd tts
!pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
!pip install nemo_text_processing WeTextProcessing pynini==2.1.5 -i https://pypi.tuna.tsinghua.edu.cn/simple

# modelscope下载权重
from modelscope import snapshot_download
model_dir = snapshot_download('pzc163/chatTTS',cache_dir='/mnt/workspace/chat_tts')

# 导入
from IPython.display import Audio, display
import torch
torch._dynamo.config.cache_size_limit = 64
torch._dynamo.config.suppress_errors = True
torch.set_float32_matmul_precision('high')

# comilse=False可以提高推理速度
import ChatTTS
chat.load_models(source='local', local_path=model_dir,compile=False)
# chat.load_models() 不指定source为local则会自动从huggingface下载权重文件

# 单个文本推理
text = "飞书我觉得是一个很好用的知识分享桥梁, 不过我不是给字节打广告啊, 确实觉得飞书好用"
wavs = chat.infer(text) # wavs是一个list of array(s), 将array传入Audio即可播放
Audio(wavs[0],rate=24000)

# 批量文本推理
texts = """
在一个遥远的星球上，有一个名叫艾瑞斯的小镇，那里的居民都是由各种颜色的水晶构成的生物。这些水晶生物拥有独特的能力：他们能够通过改变自己的颜色来与他人交流情感和思想。

小镇上住着一位名叫蓝朵的紫色水晶女孩，她拥有一种罕见的能力——能够感知他人内心深处的愿望。蓝朵总是乐于助人，她用她的感知能力帮助小镇上的居民解决各种问题。

有一天，小镇上来了一位名叫灰影的黑色水晶男孩。他总是独自一人，从不与任何人交流。小镇上的居民们都很害怕他，因为他的颜色让他们联想到了不详的事情。

蓝朵注意到了灰影的孤独，她决定用自己的能力去了解他。当她接触到灰影时，她感受到了他内心深处的悲伤和渴望。原来，灰影曾经是一个快乐的水晶生物，但一场意外让他失去了颜色，从此变得孤僻和沉默。

蓝朵决定帮助灰影找回他的颜色。她开始与小镇上的居民们沟通，告诉他们灰影的故事，并请求他们一起帮助灰影。起初，居民们都很犹豫，但蓝朵的善良和坚持最终打动了他们。

小镇上的居民们开始与灰影交流，他们用各自的颜色表达对他的支持和鼓励。慢慢地，灰影感受到了温暖和接纳，他的内心开始发生变化。终于有一天，当小镇上的所有居民一起为他祈祷时，灰影的身体开始发出微弱的光芒，他的颜色逐渐恢复了。

从那以后，灰影不再是一个孤独的黑色水晶，他变成了一个充满活力的彩虹水晶。他学会了与他人交流，也学会了分享自己的情感。艾瑞斯小镇变得更加和谐，所有的居民都因为蓝朵的善良和灰影的转变而感到幸福。

这个故事告诉我们，每个人都有可能经历困难和孤独，但只要我们愿意伸出援手，用理解和爱心去帮助他人，就能够创造奇迹，让世界变得更加美好。
""".split("\n")
texts_list = list(filter(lambda x:x,texts))
print(len(texts_list))
wavs = chat.infer(texts_list) # 通过list批量传入的文本比单条传入速度快很多, 但音色可能不稳定

# 固定音色
rand_spk = chat.sample_random_speaker()
spk_dic = {'spk_emb': rand_spk, "temperature": 0.1**10}

all_wavs = chat.infer(texts_list,params_infer_code=spk_dic) # 传入音色dic用于固定音色
conc_wavs = np.concatenate(all_wavs, axis=1) # 将声音array合并
Audio(conc_wavs1,rate=24000) # 展示所有合并后的声音


# todo 多角色连续对话

# todo .infer其他参数解析