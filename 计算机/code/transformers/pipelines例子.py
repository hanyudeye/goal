from transformers import pipeline,AutoTokenizer,AutoModelForSequenceClassification,AutoModel


# path = "f:/models/bart-large-mnli"
path = "f:/models/distilbertdistilbert-base-cased-distilled-squad"

tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModel.from_pretrained(path)

# 这个模块不支持
# classifier=pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)  #情感分析
# classifier("I've been waiting for you a whole morning")

# 定义一个分类任务的 pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# 输入文本
text = "This is a test sentence."

# 进行推理
result = classifier(text)

# 打印结果
print(result)