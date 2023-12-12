import re

res=re.match("^hello","hello,world,hello")
# 检索匹配的值
group=res.group()
# 区间
print(res.span())
print(group)


s = '''
<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>
'''
# r = re.sub('</?\w+>', '', s)  # </?\w+> 表示/可有可无，\w表示单词字符，+表示最少出现一次，完美的去掉了<>以及里面的内容
# 返回配对的字符串



r=re.sub('</?\w+>','',s)
print(r)

s = 'itcast:python,php,java-cpp'

r=re.split(':|,|-',s)
print(r)

s = 'aa2343ddd'
print(re.match(r'aa(\d+)', s).group(1))
print(re.match(r'aa(\d+?)', s).group(1))
print(re.match(r'aa(\d+)ddd', s).group(1))
print(re.match(r'aa(\d+?)ddd', s).group(1))

s = '''<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'''
print(re.search(r'https.+?\.jpg', s).group())

# ?表示关闭第一部分的贪婪，你理解一下，到第一个/就截止了，不正是关闭了第一部分的贪婪了嘛
s = 'http://www.interoem.com/messageinfo.asp?id=35'
print(re.match(r'(http://(.+?)/)', s))
print(re.sub(r'(http://.+?/).*', lambda x: x.group(1), s))
