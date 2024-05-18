from transformers import AutoModel, AutoTokenizer

path = "f:/models/bart-large-mnli"
# path = "../../bert-base-uncased"
# F:\me\goforward\code\transformers\导入本地模块.py

def load_plm(model_name='bart-large-mnli'):
    # tokenizer = AutoTokenizer.from pretrained(model name)
    # # model = AutoModel.from pretrained(model name)
    tokenizer = AutoTokenizer.from_pretrained(path)
    model = AutoModel.from_pretrained(path)
    return tokenizer, model


