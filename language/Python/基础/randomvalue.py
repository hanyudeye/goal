# 随机
import random

# 文章
#冠词 
articles = ["the", "a", "another", "her", "his"]
# 名词主语
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
# 动词
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw","play"]
# 副词
adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]

# 输出5条语句
for _ in [1,2,3,4,5]:
    article=random.choice(articles)
    subject=random.choice(subjects)
    verb=random.choice(verbs)
    adverb=random.choice(adverbs)
    print(article,subject,verb,adverb)



print(random.randint(1,2))

