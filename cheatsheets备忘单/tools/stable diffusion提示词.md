1、提升画面质量的提示词：
HDR, HD，UHD, 64K (HDR、UHD、4K、8K和64K)

表示图片效果，带来的改变可以试试，不过也会影响渲染出图的时间，会根据你要求的画面质量延长时间。

Highly detailed 增加很多的细节，有时候描述没有那么多，随手丢进去，它会补细节。

Studio lighting 添加和谐的靠谱一些的灯光效果，小概率加一些纹理

Professional 会帮助自动调节对比度，色彩的和谐程度

Vivid Colors 会帮忙增加一些鲜艳的颜色，比如用画中国画高级的配色，希望用到景泰蓝，经常会出现有点雾蒙蒙的，加入后会增强颜色的纯度和饱和度。

Bokeh 画人像可以多尝试用这个词语，会比较突出人像

high quality 高品质

masterpiece 杰出

best quality 最好品质

photography 摄影作品

ultra highres 超高分辨率

RAW photo 原始照片

ultra-detailed

finely detail

highres

8k wallpaper

示例：

正向提示词:

(8k, best quality, masterpiece, ultra highres:1.2) Photo of Pretty Japanese woman in the (style of paul rubens and rebecca guay:1.1) (melancholy winter snow:1.4)

反向提示词

(worst quality:2.0)







正向提示词：

( (8k:1.27), best quality, masterpiece, ultra highres:1.2) Photo of Pretty Japanese woman (beautiful:1.1) (sci-fi warrior woman:1.1) space soldier, (beanie:1.61) (leather jacket:1.21) intricate elegant, fantasy, detailed, ometric by greg rutkowski and alphonse mucha, gradient lighting

反向提示词：

(worst quality:2.0)






2、常用的反向提示词：
worst quality

bad quality

low quality

normal quality

lowres

normal quality

示例可以见1上的反向提示词。

3、小括号用法：
小括号代表的是1.1倍，比如Exquisite Crown（精美的皇冠），加上（Exquisite Crown）就代表皇冠这个词语的权重变成1.1倍，(((Exquisite Crown)))，代表1.1x1.1x1.1，1.331倍。

中括号用法：

中括号代表的是降权，因为初始化的权重是1，用[Exquisite Crown]代表的是0.952倍。

大括号用法：

大括号代表的是1.05倍，展示方式{Exquisite Crown}。

注意：一般小括号用的比较多，可以用数字表示权重，这样就不需要中括号和大括号，比如Exquisite Crown：1.331）=(((Exquisite Crown)))

示例：

正向提示词

masterpiece, illustration,best_quality, rosaria_\(genshin_impact\), <lora:rosaria_anything_v4:0.95>, nun, fishnet, shoulder_gloves, bare_shoulder, bangs, (pray:1.2), hands together, sitting on floor, church, looking up, crying with eyes open, looking up,<lora:Moxin_10:0.2>, <lora:LORAChineseDoll_chinesedolllikeness1:0.2>, <lora:tifaMeenow_tifaV2:0.5>, red hair, red eyes, headdress, short hair, skinny, crown, [after]{zoom_enhance mask="fingers" replacement="closeup hand" max_denoising_strength=0.2 precision=80}[/after], white gloves,
反向提示词

wrinkles Deformed eyes, ((disfigured)), ((bad art)), ((deformed)), ((extra limbs)), (((duplicated))), ((morbid)), ((mutilated)), out of frame, extra fingers, mutated hands, poorly drawn eyes, ((poorly drawn hands)), ((poorly drawn face)), (((extra legs))), (fused fingers), (too many fingers), (((long neck))), tiling, poorly drawn, mutated, cross-eye, canvas frame, frame, cartoon, 3d, weird colors, blurry, ((old)), ((ugly)), ((child)),, NG_DeepNegative_V1_75T, (extra hand:1.4),



生成图：


4、元素的融合：
方法一：中括号表示法

[pink|blond]long hair，beautiful girl, gothic dress, clear details, Gothic architecture interior

在这个里面的[pink|blond]long hair，用中括号将颜色隔开，渲染的时候，是一步粉红一步金色，最后出来的是调节过后的粉金色。中括号起到了混合的作用，同理，我们还可以用在服装材质、款式、背景玄幻...除了用中括号，另外还可以用and来连接，这是更细致的写法，可以用来规定某一个你想要混合的色彩的权重。

方法二：AND

pink long hair AND blond long hair，beautiful girl, gothic dress, clear details, Gothic architecture interior

方法三：

此方法被称作为元素渐变。可以通过混合两个关键词来实现更有趣效果，使用语法为“[keyword1 : keyword2: factor]”，其中factor值控制了把keyword1切换到keyword2的步骤值，是一个介于0到1之间的数字。

举个例子，输入提示词“Oil painting portrait of [Joe Biden: Donald Trump: 0.5]”，采样步数设置为30。这里指的是，第1~15步，提示词为“Oil painting portrait of Joe Biden”；第16~30步，提示词为“Oil painting portrait of Donald Trump”。解释一下，factor值决定了关键词的切换节点，设置为0.5时指的是在30*0.5 = 15步时切换。

示例：

正向提示词：

((extreme detail)),(ultra-detailed), extremely detailed CG unity 8k wallpaper, <lora:MarinKitagawa:0.7>(anime screencap:1.2), marin kitagawa, school uniform, plaid skirt, black choker, smile, teeth, looking at viewer, sitting, crossed legs, night sky, stars, outdoors,
反向提示词：

sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy,(fat:1.2), lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, username,blurry,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,

5、元素的精细控制：
使用[keyword:number]方式表示

[flower:5],long blond hair, beautiful girl, gothic dress, clear details, Gothic architecture interior

[flower:5]的意思是从第5步开始画花花，直到结束，以降低画的步数来达到弱化的效果。

但是这也有个局限，在我们画画步数本来就不高的情况下，很容易画不出来，它没办法只用10步或15步给画出来的时候，往往不理你。

此外，还有一些采样会不太搭理这种写法，可以探索看看。

小黑板：

[flower:5] 代表从第5步开始直到结束

[flower::10] 代表从开始就一起画，但是画到第10步就不画了

[[flower::30]:5] 代表从第5步开始画，到30步结束

长呼一口浊气，试想一下，如果我们在画画的时候，写tag能够这样精细控制，熟练掌握各个元素出现的轻重，出来的画面能多细致。

6、画面的比重控制：
上面是控制某一个东西的比重，下面来扒画面的比重。

但是这是需要很长的步数来表现的，我今天用的不画那么多步，就写一下怎么表示。

比如说我们将步数设定在100，前面50步用来画人，后面50步用来画花花。

[girl：flower：0.5]，这样就表示前面的50%步数是画人的，后面的用来画花，人就会画到50步就结束了；

另外一种就是直接写步数，据说可以这样用，但是我觉得并不好用，写法：[girl:flower:50]，在总步数100的时候，前面50用来画人，后面的画花。

只是两种写法不一样，亲测下面的不如上面的写法好用。

7、元素随机选择：
这个在批量生成的时候会好用一些，一张两张的体现不出。

这里用到的是大括号。

之前的tag：

Long blond hair, beautiful girl, gothic dress, clear details, Gothic architecture interior

之后的tag：

CrownCorolla|Hairpin|Bowknot，long blond hair, beautiful girl, gothic dress, clear details, Gothic architecture interior

8、词汇顺序/数量/位置影响
早期的标记具有更一致的位置，因此神经网络更容易预测它们的相关性。而且由于attention机制的特殊性，每次训练时，开始的标记和结束的标记总会被注意到（attention）。而且由于标记越多，单个标记被被注意到的概率越低。

基于以上特性，有以下几点需要注意：

开头与结尾的词往往作用性更强。

提示词数量越多，单个提示词的作用性越低。

开头的数个提示词的作用较强，有更强的相关。

关于数量，你可能已经注意到了，当你写prompt时会有数量限制。

但是在 webui中，你是可以写 75 个词汇以上的提示的。webui会自动通过对提示词进行分组。当提示超过 75 个 token（可以理解token代表你的提示词），提交多组 75 个 token。单个token只具有同一组中其他内容的上下文。

每一组都会被补充至(1,77,768)的张量，然后进行合并，比如俩组就会合并为(1,154,768)的张量，然后被送入U-Net。

值得注意的是，

为了避免将你的短语分成俩组，webui在分组时会查看附近是否有,来尽量还原你想要的输入。

然后你还能通过输入BREAK来快速分组，BREAK必须为大写。



描述人物
(1girl:2.0), solo, nilou ((genshin impact\), solo, long hair, jewelry, blue gemstone, earrings,horns, crown, cyan satin strapless dress, white veil, neck ring, red hair, [green eyes],

描述场景
indoor, room, house, sofa, wooden floor, plant, flowers, trees, windows，outdoor,forest,wild,travel,woods in the background(背景虚化，增加景深)

描述环境(时间光)
day, morning, sunlight, dappled sunlight, backlight, light rays, cloudy sky

描述画幅视角
full body, wide angle shot, depth of field

其他画面要素
light particles,fantasy, wind blow, maple leaf, dusty, ...(其他往后增加)

高品质标准化
[Imasterpiece]], [best quality],highres), original, reflection, unreal engine, body shadowartstationextremely detailed CG unity 8k wallpaper

画风标准化
(illustration), (painting), (sketch), anime coloring, fantasy,

其他特殊要求
exaggerated body proportions, greasy skin, realistic and delicate facial features, SFW.

## 增加权重，可以关键词 外面加括号，括号越多，权重越高 ，或者详细说明权重  (white flower:1.5)


- 圆括号: (white flower)  每套一层,额外x1.1倍。
- 大括号: {white flower}  每套一层,额外x1.05倍
- 方括号: [white flower]  每套一层,额外x0.9倍


## 模型
模型总结，朋友们可对应在C站搜索下载

二次元：
1.最受欢迎的二次元模型：Anything
2精致度满满，室内外场景优秀：counterfeit
3.魔幻感十足：dreamlike diffusion

真实：
1.真实朴素：Realistic vision
2.照片级：Lofi
3.精细的写实风格：deliberate

2.5D
1.动漫角色的二次创作，即真实又二次元：never ending  dream
2.超现实的画面：Protogen x3.4 (Photorealism)
3.国风、小人书、水墨风：guofeng3

拓展：
富有现代感的建筑（dvArch - Multi-Prompt Archittecture Tuned Model)
富有魔幻感的场景(Cheese Daddy's Landscapes mix)
富有高级感的平面设计(Graphic design_2.0)