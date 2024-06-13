import json
import torch

# 从 JSON 文件中读取数据
with open('slct_voice.json', 'r', encoding='utf-8') as json_file:
    slct_idx_loaded = json.load(json_file)

# 将包含 Tensor 数据的部分转换回 Tensor 对象
for key in slct_idx_loaded:
    tensor_list = slct_idx_loaded[key]["tensor"]
    slct_idx_loaded[key]["tensor"] = torch.tensor(tensor_list)

# 将音色 tensor 打包进params_infer_code，固定使用此音色发音，调低temperature
speak_tensor = slct_idx_loaded["5"]["tensor"] # female
spk_dic = {"spk_emb": speak_tensor, "temperature": 0.0001}
wav = chat.infer(text,params_infer_code=spk_dic)