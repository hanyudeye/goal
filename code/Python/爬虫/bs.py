# 分析xml

# beautifulsoup 的用法

from urllib.request import urlopen
from urllib.error import HTTPError
from  bs4 import BeautifulSoup

# urlopen 对于不存在的网页会报错中断，所以要异常处理


# html=urlopen("https://pythonscraping.com/pages/page1.html")
# 读取本地文件 J:\me\Shijian\code\Html\404.html
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs=BeautifulSoup(html.read(),"html.parser")
        title=bs.body.h1
    except AttributeError as e:
        return None
    return title

title=getTitle("https://pythonscraping.com/pages/page1.html")
if title==None:
    print("Title could not be found")
else:
    print(title)
