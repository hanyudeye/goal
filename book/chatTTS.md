加入口语化 ：[oral]笑声：[laugh]停顿：[uv_break] 停顿

配置端口: 再项目根目录  .env 文件进行修改

对话式 TTS: ChatTTS针对对话式任务进行了优化，实现了自然流畅的语音合成，同时支持多说话人。
细粒度控制: 该模型能够预测和控制细粒度的韵律特征，包括笑声、停顿和插入词等。
更好的韵律: ChatTTS在韵律方面超越了大部分开源TTS模型。同时提供预训练模型，支持进一步的研究

``` python
inputs_cn = """
chat T T S 是一款强大的对话式文本转语音模型。它有中英混读和多说话人的能力。
chat T T S 不仅能够生成自然流畅的语音，还能控制[laugh]笑声啊[laugh]，
停顿啊[uv_break]语气词啊等副语言现象[uv_break]。这个韵律超越了许多开源模型[uv_break]。
请注意，chat T T S 的使用应遵守法律和伦理准则，避免滥用的安全风险。[uv_break]'
""".replace('\n', '')

params_refine_text = {
  'prompt': '[oral_2][laugh_0][break_4]'
} 
audio_array_cn = chat.infer(inputs_cn, params_refine_text=params_refine_text)
# audio_array_en = chat.infer(inputs_en, params_refine_text=params_refine_text)

torchaudio.save("output3.wav", torch.from_numpy(audio_array_cn[0]), 24000)

```
