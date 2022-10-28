---
title: layui使用手册
permalink: layui
theme: jekyll-theme-cayman
---

文档: https://layui.me/doc/index.htm

## 引入
``` html
<link rel="stylesheet" href="./static/css/layui.css" media="all">
<script src="./static/layui.js" charset="utf-8"></script>
```

CDN
``` js
//layui 模块的定义（新 js 文件）
layui.define([mods], function(exports){
  
  //……
  
  exports('mod', api);
});  
 
//layui 模块的使用
layui.use(['mod1', 'mod2'], function(args){
  var mod = layui.mod1;
  
  //……
  
});    
```

   
使用
``` js
    //一般直接写在一个js文件中
    layui.use(['layer', 'form'], function(){
    var layer = layui.layer
    ,form = layui.form;

    layer.msg('Hello World');
    });
```

您可以遵循layui 的模块规范建立一个入口文件，并通过 layui.use() 方式来加载该入口文件
``` html
<script>
layui.config({
  base: '/res/js/modules/' //你存放新模块的目录，注意，不是 layui 的模块目录
}).use('index'); //加载入口
</script>    
```
上述的 index 即为你 /res/js/modules/ 目录下的 index.js,它的内容应该如下：

``` js
index.js 是项目的主入口
以依赖 layui 的 layer 和 form 模块为例

layui.define(['layer','form'],function(exports){
var layer = layui.layer
,form = layui.form;

exports('index',{}); //注意，这里是模块的输出核心，模块必须和 use 是的模块名一致

});

```

从 layui2.6开始，如果你引入的是构建后的 layui.js ，里面包含了所有的内置模块，无需另外指定

``` js
index.js 项目主入口
layui.define(function(){
var layer=layui.layer
,form =layui.form
,table=layui.table;

//..... 代码

exports('index',{}); //注意，这里是模块的输出核心，模块必须和 use 是的模块名一致
})

```

管理扩展模块

除了使用 layui 的内置模块， 必不可少也需要加载扩展模块（符合 layui 模块规范的 js 代码文件)
``` js
//mod1.js
layui.define('layer',function(exports){
//...
exports(mod1,{});
})

//mod2.js, 假设依赖 mod1 和 form
layui.define('mod1','form',function(exports){
//...
exports(mod2,{});
})
```

## 底层方法
> 本篇主要介绍即出库所发挥的作用，其中过滤了大部分在外部不常用的方法，侧重罗列了基础框架支撑。

### 全局配置

方法： layui.config(options)

你可以在使用模块之前，全局化配置一些参数，尽管大部分时候它不是必须的。所以我们目前提供的全局配置项非常少，这也是为了减少一些不必要的工作，尽可能让使用变得更简单。目前支持的全局配置项如下：
``` js
  layui.config({
    dir:'/res/layui/'    // layui.js 所在目录,如果是 script 引入，无需设定
    ,version: false   // 一般用于更新模块缓存，默认不开其。设为 true 则让浏览器缓存，也可设置一个固定值，如 201610
    ,debug: false   //开启调试，如果设置为 true, 则JS 模块的节点会保留在页面
    ,base:'' //设定扩展的 layui 模块的所在目录，一般用于外部模块扩展
  });
```
### 定义模块
方法： layui.define([mods],callback)

通过该方法可在新的 JS文件中定义一个 layui 模块。参数 mods 是可选的，用于声明该模块所依赖的模块。callback即为模块加载完毕的回调函数，它返回一个 exports 参数，用于输出该模块的接口。

```js
/** demo.js **/
layui.define(function(exports){
  //do something
  
  exports('demo', {
    msg: 'Hello Demo'
  });
});
```
跟RequireJS 最大不同的地方在于接口输出， exports 是一个函数，它接受两个参数，第1个参数为模块名，第2个参数为模块接口。

当你声明了上述的一个模块后，你就可以在外部使用了，demo就会注册到 layui对象下，即可通过 var demo = layui.demo 去得到该模块接口。

### 加载模块
方法：layui.use([mods], callback)
``` js
//引用指定模块
layui.use(['layer', 'laydate','demo'], function(){
  var layer = layui.layer
  ,laydate = layui.laydate
  //自定义的模块都在 layui对象下面
  ,demo=layui.demo;
  
  console.log(demo.msg);
  //do something

});
```
注意： 自定义的模块都在 layui 命名空间下面
##  页面元素
### CSS内置公共基础类

| 类名                | 说明                                                                                    |
| ------------------- | --------------------------------------------------------------------------------------- |
|                     | 布局/容器                                                                               |
| layui-main          | 用于设置一个宽度为1140px的水平居中块(无响应式)                                          |
| layui-inline        | 用于将标签设为内联块状元素                                                              |
| layui-box           | 用于排除一些UI框架(如Bootstrap)强制将全部元素设为box-sizing:border-box 所引发的尺寸偏差 |
| layui-clear         | 用于消除浮动（不常用，因为layui 几乎没用到浮动)                                         |
| layui-btn-container | 用于定义按钮的父容器                                                                    |
| layui-btn-fluid     | 用于定义流体按钮，即宽度最大化适应                                                      |
|                     | 辅助                                                                                    |
| layui-icon          | 用于图标                                                                                |
| layui-elip          | 用于单行文本溢出省略                                                                    |
| layui-unselect      | 屏蔽选中                                                                                |
| layui-disabled      | 设置元素不可点击状态                                                                    |
| layui-cicle         | 设置元素为圆形                                                                          |
| layui-show          | 显示块状元素                                                                            |
| layui-hide          | 隐藏元素                                                                                |
|                     | 文本                                                                                    |
| layui-text          | 定义一段文本区域，该区域内的特殊标签(如a、li、em等)将会进行相应处理                     |
| layui-word-aux      | 灰色标注性文字，左右会有间隔                                                            |
|                     | 背景色                                                                                  |
| layui-bg-red        | 用于设置元素赤色背景                                                                    |
| layui-bg-orange     | 用于设置元素橙色背景                                                                    |
| layui-bg-green      | 用于设置元素墨绿色背景（主色调）                                                        |
| layui-bg-cyan       | 用于设置元素藏青色背景                                                                  |
| layui-bg-blue       | 用于设置元素蓝色背景                                                                    |
| layui-bg-black      | 用于设置元素经典黑色背景                                                                |
| layui-bg-gray       | 用于设置元素经典灰色背景                                                                |
|                     | 字体大小及颜色                                                                          |
| layui-font-12       | （12px 的字体）                                                                         |
| layui-font-14       | （14px 的字体）                                                                         |
| layui-font-16       | （16px 的字体）                                                                         |
| layui-font-18       | （18px 的字体）                                                                         |
| layui-font-20       | （20px 的字体）                                                                         |
| layui-font-red      | （红色字体）                                                                            |
| layui-font-orange   | （橙色字体）                                                                            |
| layui-font-green    | （绿色字体）                                                                            |
| layui-font-cyan     | （青色字体）                                                                            |
| layui-font-blue     | （蓝色字体）                                                                            |
| layui-font-black    | （黑色字体）                                                                            |
| layui-font-gray     | （灰色字体）                                                                            |

### HTML规范：常用公共属性
很多时候，元素的基本交互行为，都是由模块自动开启。但不同的区域可能需要触发不同的动作，这就需要你设定我们所支持的自定义属性来作为分区。如下面的 lay-submit、 lay-filter 既为公共属性:

``` html
<button class="layui-btn" lay-submit lay-filter="login">登入</button>
```

目前我们的公共属性如下(既普遍运用于所有元素上的属性):
| 属性          | 描述                                                             |
| ------------- | ---------------------------------------------------------------- |
| lay-skin=""   | 定义相同元素的不同风格，如 checkbox 的开关风格                   |
| lay-filter="" | 事件过滤器，用于监听特定的自定义事件，你可以把它看作一个ID选择器 |
| lay-submit    | 定义一个触发表单提交的button，不用填写值                         |

## 模块规范
### 预先加载模块
layui.use 加载模块

``` js
layui.use(['form', 'upload'], function(){  //如果只加载一个模块，可以不填数组。如：layui.use('form')
  var form = layui.form //获取form模块
  ,upload = layui.upload; //获取upload模块
  
  //监听提交按钮
  form.on('submit(test)', function(data){
    console.log(data);
  });
  
  //实例化一个上传控件
  upload({
    url: '上传接口url'
    ,success: function(data){
      console.log(data);
    }
  })
});
```

### 扩展模块

1. 确认模块名,假设为：mymod，然后新建一个 mymod.js 文件放在项目任意目录下
2. 编写 mymod.js如下：
   ``` js
//  扩展一个 mymod 模块
 
layui.define(function(exports){ //提示：模块也可以依赖其它模块，如：layui.define('mod1', callback);
  var obj = {
    hello: function(str){
      alert('Hello '+ (str||'mymod'));
    }
  };
  
  //输出 mymod 接口
  exports('mymod', obj);
});    
   
   ```
3. 设定扩展模块所在的目录，然后就可以在别的JS文件中使用了

```js
//config的设置是全局的
layui.config({
  base: '/res/js/' //假设这是你存放拓展模块的根目录
}).extend({ //设定模块别名
  mymod: 'mymod' //如果 mymod.js 是在根目录，也可以不用设定别名
  ,mod1: 'admin/mod1' //相对于上述 base 目录的子目录
});
 
//你也可以忽略 base 设定的根目录，直接在 extend 指定路径（主要：该功能为 layui 2.2.0 新增）
layui.extend({
  mod2: '{/}http://cdn.xxx.com/lib/mod2' // {/}的意思即代表采用自有路径，即不跟随 base 路径
})
 
//使用拓展模块
layui.use(['mymod', 'mod1'], function(){
  var mymod = layui.mymod
  ,mod1 = layui.mod1
  ,mod2 = layui.mod2;
  
  mymod.hello('World!'); //弹出 Hello World!
});
```      

大体上说，layui 的模块定义很类似 Require.js 和 Sea.js，但跟他们又有着明显不同，譬如在接口输出等地方。

## 布局
### 栅格系统
为了丰富网页布局，简化 html/css 代码的耦合，并提升多终端的适配能力，layui 在2.0的版本中引进了自己的一套具备响应式能力的栅格系统.我们将容器进行了12等分,预设了4*12中CSS排列类,他们在移动设备,平板,桌面中/大尺寸四种不同的屏幕下发挥着各自的作用.

一. 栅格布局规则:
1. 采用 layui-row定义行,如: <div class="layui-row"></div>
2. 采用 layui-col-md* 定义一组列
3. 类可以同时出现最多四种不同的组合,分别是 xs（超小屏幕，如手机<768px）、sm（小屏幕，如平板>=768px）、md（桌面中等屏幕 992px）、lg（桌面大型屏幕>=1200px）
4. 可对列追加类似 layui-col-space5 (列间距，单位 px)、 layui-col-md-offset3 ( 列偏移 )
      
 移动设备、平板、桌面端的不同表现：
   ```  html
         <div class="layui-row">
           <div class="layui-col-xs6 layui-col-sm6 layui-col-md4">
             移动：6/12 | 平板：6/12 | 桌面：4/12
           </div>
           <div class="layui-col-xs6 layui-col-sm6 layui-col-md4">
             移动：6/12 | 平板：6/12 | 桌面：4/12
           </div>
           <div class="layui-col-xs4 layui-col-sm12 layui-col-md4">
             移动：4/12 | 平板：12/12 | 桌面：4/12
           </div>
           <div class="layui-col-xs4 layui-col-sm7 layui-col-md8">
             移动：4/12 | 平板：7/12 | 桌面：8/12
           </div>
           <div class="layui-col-xs4 layui-col-sm5 layui-col-md4">
             移动：4/12 | 平板：5/12 | 桌面：4/12
           </div>
         </div>
       </div>
```
二. 响应式规则:          
栅格的响应式能力,得益于CSS3媒体查询的强力支持,从而针对四类不同的尺寸屏幕,进行相应的适配处理

三. 响应式公共类：
    | 类名（class）             | 说明                                                        |
    | layui-show-*-block        | 定义不同设备下的 display: block; * 可选值有：xs、sm、md、lg |
    | layui-show-*-inline       | 定义不同设备下的 display: inline; * 可选值同上              |
    | layui-show-*-inline-block | 定义不同设备下的 display: inline-block; * 可选值同上        |
    | layui-hide-*              | 定义不同设备下的隐藏类，即： display: none; * 可选值同上    |

四. 布局容器:
将栅格放入一个带有 class="layui-contianer"的特定容器中,以便在小屏幕以上的设备中固定宽度,让列可控.
当然,你也可以不固定容器宽度,只要将栅格和其它元素放入 class="layui-fluid"的容器中,它会100%适应.

五. 列间距 (用来微调列) layui-col-space1 ~ layui-col-space30
六. 列偏移 (用来定位列) layui-col-md-offset*
### 颜色
#### 主色调 (墨绿色)
1. #009688 主色调之一
2. #5FB878 一般用于选中状态
3. #393D49 通常用于导航
4. #1E9FFF 经典蓝

#### 次色调 (场景色)
1.  #FFB800 暖色系
2.  #FF5722 比较引人注意的颜色
3.  #01AAED 文本链接着色
4.  #2F4056 侧边色

#### 中性色 (用于背景、边框等,灰色系)
1. #FAFAFA #F6F6F6 #eeeeee #e2e2e2
2. #dddddd #d2d2d2 #cccccc #c2c2c2

#### 背景色
- 赤色：class="layui-bg-red"
- 橙色：class="layui-bg-orange"
- 墨绿：class="layui-bg-green"
- 藏青：class="layui-bg-cyan"
- 蓝色：class="layui-bg-blue"
- 雅黑：class="layui-bg-black"
- 银灰：class="layui-bg-gray"
    
### 字体图标 (取材于阿里巴巴 iconfont) 
字体图标也是一种字符,可以用 css 属性直接控制.也可以通过 font-class 或 unicode 定义不同图标


``` html
<i class="layui-icon layui-icon-face-smile"></i>   
<i class="layui-icon layui-icon-face-smile" style="font-size: 30px; color: #1E9FFF;"></i>
      ```
内置图标 (168个)


跨域问题的解决

由于浏览器存在同源策略，所以如果 layui（里面含图标字体文件）所在的地址与你当
前的页面地址不在同一个域下，即会出现图标跨域问题。所以要么你就把layui 与网站
放在同一服务器，要么就对 layui 所在的资源服务器的 Response Headers 加上属性：
Access-Control-Allow-Origin: *

### CSS3 动画类 

  动画的使用非常简单,直接对元素赋值动画特定的 class 类名即可

``` html
      <!-- 其中 layui-anim 是必须的，后面跟着的即是不同的动画类 -->
      <div class="layui-anim layui-anim-up"></div>
     
      <!-- 循环动画，追加：layui-anim-loop -->
      <div class="layui-anim layui-anim-up layui-anim-loop"></div>
 
```
         
| 属性             | 值                    |
| ---------------- | --------------------- |
| 从最底部往上滑入 | layui-anim-up         |
| 微微往上滑入     | layui-anim-upbit      |
| 平滑放大         | layui-anim-scale      |
| 平滑放小         | layui-anim-scalesmall |
| 渐现             | layui-anim-fadein     |
| 360度旋转        | layui-anim-rotate     |

### 按钮 (button) 
``` html
     <button type="button" class="layui-btn">一个标准的按钮</button>
     <a href="http://www.layui.com" class="layui-btn">一个可跳转的按钮</a>
```
### 表单 (form 元素集合)
引入 form

``` html
      <form class="layui-form" action="">
         <div class="layui-form-item">
           <label class="layui-form-label">输入框</label>
           <div class="layui-input-block">
             <input type="text" name="title" required  lay-verify="required" placeholder="请输入标题" autocomplete="off" class="layui-input">
           </div>
         </div>
         <div class="layui-form-item">
           <label class="layui-form-label">密码框</label>
           <div class="layui-input-inline">
             <input type="password" name="password" required lay-verify="required" placeholder="请输入密码" autocomplete="off" class="layui-input">
           </div>
           <div class="layui-form-mid layui-word-aux">辅助文字</div>
         </div>
         <div class="layui-form-item">
           <label class="layui-form-label">选择框</label>
           <div class="layui-input-block">
             <select name="city" lay-verify="required">
               <option value=""></option>
               <option value="0">北京</option>
               <option value="1">上海</option>
               <option value="2">广州</option>
               <option value="3">深圳</option>
               <option value="4">杭州</option>
             </select>
           </div>
         </div>
         <div class="layui-form-item">
           <label class="layui-form-label">复选框</label>
           <div class="layui-input-block">
             <input type="checkbox" name="like[write]" title="写作">
             <input type="checkbox" name="like[read]" title="阅读" checked>
             <input type="checkbox" name="like[dai]" title="发呆">
           </div>
         </div>
         <div class="layui-form-item">
           <label class="layui-form-label">开关</label>
           <div class="layui-input-block">
             <input type="checkbox" name="switch" lay-skin="switch">
           </div>
         </div>
         <div class="layui-form-item">
           <label class="layui-form-label">单选框</label>
           <div class="layui-input-block">
             <input type="radio" name="sex" value="男" title="男">
             <input type="radio" name="sex" value="女" title="女" checked>
           </div>
         </div>
         <div class="layui-form-item layui-form-text">
           <label class="layui-form-label">文本域</label>
           <div class="layui-input-block">
             <textarea name="desc" placeholder="请输入内容" class="layui-textarea"></textarea>
           </div>
         </div>
         <div class="layui-form-item">
           <div class="layui-input-block">
             <button class="layui-btn" lay-submit lay-filter="formDemo">立即提交</button>
             <button type="reset" class="layui-btn layui-btn-primary">重置</button>
           </div>
         </div>
       </form>
     
       <script>
       //Demo
       layui.use('form', function(){
         var form = layui.form;
      
         //监听提交
         form.on('submit(formDemo)', function(data){
           layer.msg(JSON.stringify(data.field));
           return false;
         });
       });
       </script>
    ```
          
   给 select 分组：
``` html
       <select name="quiz">
         <option value="">请选择</option>
         <optgroup label="城市记忆">
           <option value="你工作的第一个城市">你工作的第一个城市？</option>
         </optgroup>
         <optgroup label="学生时代">
           <option value="你的工号">你的工号？</option>
           <option value="你最喜欢的老师">你最喜欢的老师？</option>
         </optgroup>
       </select>
```
          
         
### 导航 (nav 面包屑)
``` html
<ul class="layui-nav">
  <li class="layui-nav-item">
    <a href="">控制台<span class="layui-badge">9</span></a>
  </li>
  <li class="layui-nav-item">
    <a href="">个人中心<span class="layui-badge-dot"></span></a>
  </li>
  <li class="layui-nav-item">
    <a href=""><img src="//t.cn/RCzsdCq" class="layui-nav-img">我</a>
    <dl class="layui-nav-child">
      <dd><a href="javascript:;">修改信息</a></dd>
      <dd><a href="javascript:;">安全管理</a></dd>
      <dd><a href="javascript:;">退了</a></dd>
    </dl>
  </li>
</ul>
      

```
### 菜单 (基础菜单,水平菜单称为导航，垂直菜单称为菜单)

``` html
<div class="layui-panel">
  <ul class="layui-menu" id="docDemoMenu1">
    <li lay-options="{id: 100}">
      <div class="layui-menu-body-title">menu item 1</div>
    </li>
    <li lay-options="{id: 101}">
      <div class="layui-menu-body-title">
        <a href="#">menu item 2 <span class="layui-badge-dot"></span></a>
      </div>
    </li>
    <li class="layui-menu-item-divider"></li>
    <li class="layui-menu-item-group layui-menu-item-down" lay-options="{type: 'group'}">
      <div class="layui-menu-body-title">
        menu item 3 group <i class="layui-icon layui-icon-up"></i>
      </div>
      <ul>
        <li lay-options="{id: 1031}">menu item 3-1</li>
        <li lay-options="{id: 1032}">
          <div class="layui-menu-body-title">menu item 3-2</div>
        </li>
      </ul>
    </li>
    <li class="layui-menu-item-divider"></li>
    <li lay-options="{id: 104}">
      <div class="layui-menu-body-title">menu item 4</div>
    </li>
    <li class="layui-menu-item-parent" lay-options="{type: 'parent'}">
      <div class="layui-menu-body-title">
        menu item 5 
        <i class="layui-icon layui-icon-right"></i>
      </div>
      <div class="layui-panel layui-menu-body-panel">
        <ul>
          <li lay-options="{id: 1051}">
            <div class="layui-menu-body-title">menu item 5-1</div>
          </li>
          <li lay-options="{id: 1051}">
            <div class="layui-menu-body-title">menu item 5-2</div>
          </li>
        </ul>
      </div>
    </li>
    <li lay-options="{id: 106}">
      <div class="layui-menu-body-title">menu item 6</div>
    </li>
  </ul>
</div>

```

``` js
layui.use(['layer', 'dropdown'], function () {

			var dropdown = layui.dropdown
				, $ = layui.jquery;

			//菜单点击事件，其中 docDemoMenu1 对应的是菜单结构上的 id 指
			dropdown.on('click(docDemoMenu1)', function (options) {
				var othis = $(this); //当前菜单列表的 DOM 对象
				console.log(options); //菜单列表的 lay-options 中的参数
			});
		})

```
### 选项卡 (tabs 切换)
### 进度条 (progress)
### 面板 (panel 卡片 折叠)
### 表格 (静态 table)
### 徽章 (小圆点，小边框)

### 时间线 (timeline)
### 辅助 (引用,字段集，横线等)

## 内置模块

### 弹出层 (layer)
layer 至今仍然作为 layui的代表作，在于不断的坚持。layer 现在非常常用。

#### 使用场景

1. 独立使用(需要引入jquery1.8以上版本)

引入好layer.js后，直接用即可
``` html
<script src="jquery1.9.js"></script>
<script src="layer.js"></script>
<script>
layer.msg('hello'); 
</script>
```

2. 在layui模块化中使用
``` js
layui.use('layer', function(){
  var layer = layui.layer;
  
  layer.msg('hello');
});              
```

#### 基础参数
我们提到的基础参数主要指调用方法时用到的配置项，如: layer.open({content:''}) layer.msg('',{time:3})等等，其中 content和 time 即是基础参数，以键值形式存在。

##### type- 基本层类型
类型：Number,默认：0
layer 提供了5中层类型，可传入的值有：0（信息框),1(页面层)，2(iframe层) 3(加载层) 4(tips层)。若您采用layer.open({type:1})方式调用，则type必填，除默认的信息框

##### title- 标题
类型: String/Array/Boolean,默认："信息"

如果想自定义标题区域样式，可以用 Array 类型 , 如 title:['文本','font-size:18px;']，数组第二项可以写任意css 样式; 如果不想显示标题栏，可以使用 Boolean ， title:false

##### content- 内容
类型: String/DOM/Array，默认为空 
content 可传入的值是灵活多变的，不仅可以传入普通的html内容，还可以指定DOM，更可以随着type的不同而不同
譬如：
``` js
/!*
 如果是页面层
 */
layer.open({
  type: 1, 
  content: '传入任意的文本或html' //这里content是一个普通的String
});
layer.open({
  type: 1,
  content: $('#id') //这里content是一个DOM，注意：最好该元素要存放在body最外层，否则可能被其它的相对元素所影响
});
//Ajax获取
$.post('url', {}, function(str){
  layer.open({
    type: 1,
    content: str //注意，如果str是object，那么需要字符拼接。
  });
});
/!*
 如果是iframe层
 */
layer.open({
  type: 2, 
  content: 'http://sentsin.com' //这里content是一个URL，如果你不想让iframe出现滚动条，你还可以content: ['http://sentsin.com', 'no']
}); 
/!*
 如果是用layer.open执行tips层
 */
layer.open({
  type: 4,
  content: ['内容', '#id'] //数组第二项即吸附元素选择器或者DOM
});        
```        

##### skin - 样式类名

skin 不仅允许你传入 layer内置的样式class 名，还可以传入您自定义的 class 名。这意味着你可以借助 skin 轻松完成不同的风格定制。内置的 skin 有: layui-layer-lan layui-layer-molv,下面是一个自定义风格的简单例子

``` 
//单个使用
layer.open({
  skin: 'demo-class'
});
//全局使用。即所有弹出层都默认采用，但是单个配置skin的优先级更高
layer.config({
  skin: 'demo-class'
})
//CSS 
body .demo-class .layui-layer-title{background:#c00; color:#fff; border: none;}
body .demo-class .layui-layer-btn{border-top:1px solid #E9E7E7}
body .demo-class .layui-layer-btn a{background:#333;}
body .demo-class .layui-layer-btn .layui-layer-btn1{background:#999;}
…
加上body是为了保证优先级。你可以借助Chrome调试工具，定义更多样式控制层更多的区域。    
```

##### area - 宽高
类型: Sting/Array,默认 : 'auto'
默认是自适应的，如果你想定义宽度时，你可以: area:'500px',高度仍然是自适应的。如果你想全部定义，可以:area:['500px','300px']

##### offset - 坐标
类型:String/Array,默认：垂直水平居中

| 值                        | 备注                        |
| ------------------------- | --------------------------- |
| offset: 'auto'            | 默认坐标，即垂直水平居中    |
| offset: '100px'           | 只定义top坐标，水平保持居中 |
| offset: ['100px', '50px'] | 同时定义top、left坐标       |
| offset: 't'               | 快捷设置顶部坐标            |
| offset: 'r'               | 快捷设置右边缘坐标          |
| offset: 'b'               | 快捷设置底部坐标            |
| offset: 'l'               | 快捷设置左边缘坐标          |
| offset: 'lt'              | 快捷设置左上角              |
| offset: 'lb'              | 快捷设置左下角              |
| offset: 'rt'              | 快捷设置右上角              |
| offset: 'rb'              | 快捷设置右下角              |

##### icon - 图标。信息框和加载层的私有参数
类型:Number,默认：-1（信息框)/0 (加载层)
信息框默认不显示图标，当你想显示图标时，默认皮肤可以可以传入 0-6，如果是加载层，可以传入 0-2。如

```js
//eg1
layer.alert('酷毙了', {icon: 1});
//eg2
layer.msg('不开心。。', {icon: 5});
//eg3
layer.load(1); //风格1的加载
```

##### TODO btn - 按钮
TODO: 未完，待续

### confirm
    ``` js
     var index = layer.confirm('您确定要删除该产品信息？', {
                                title: '友情提示',
                                icon: 3,
                                btn: ['确定', '取消']
                            }, function() {

                                $.getJSON('{:url("weixinshop/del")}', {id: e.data.id}, function (res) {

                                    if(0 == res.code) {

                                        layer.msg(res.msg);
                                        setTimeout(function () {
                                            renderTable();
                                        }, 300);
                                    } else {
                                        layer.alert(res.msg);
                                    }
                                });
                            }, function(){

                            });
    ```

### 日期与时间选择 (laydate)

### 分页 (laypage)

### 模板引擎(laytpl)

### 数据表格 (table)

### 表单 (form)
### 文件上传 (upload)
上传模块子 layui 2.0 版本开始，进行加强。 任何元素都可以作为上传组件来调用，譬如按钮、图片、普通的DIV等等，而不再是一个单调的 file 文件域

#### 快速使用
通常情况下，我们上传文件是借助 type="file" 的input标签来完成的，但非常遗憾的是，它不能很好地与其它表单元素共存，所以我们常常要单独为它做一个业务层面的“异步上传”，即先让图片上传，再和其它表单一起提交保存。如下：

``` html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>upload模块快速使用</title>
  <link rel="stylesheet" href="/static/build/layui.css" media="all">
</head>
<body>
 
<button type="button" class="layui-btn" id="test1">
  <i class="layui-icon">&#xe67c;</i>上传图片
</button>
 
<script src="/static/build/layui.js"></script>
<script>
layui.use('upload', function(){
  var upload = layui.upload;
   
  //执行实例
  var uploadInst = upload.render({
    elem: '#test1' //绑定元素
    ,url: '/upload/' //上传接口
    ,done: function(res){
      //上传完毕回调
    }
    ,error: function(){
      //请求异常回调
    }
  });
});
</script>
</body>
</html>
```

这原本是一个普通的 button，正是upload模块赋予了它"文件选择"的特殊技能。

#### 核心方法与基础参数选项
使用 upload模块必须与 upload.render(options) 方法打交道，其中的 options 即为基础参数，它是一个对象。

``` js
var upload = layui.upload; // 得到 upload 对象

/创建一个上传组件
upload.render({
elem:'#id',
url:'',
done:function(res,index,upload){
//上传后的回调
},
accept:'file', //允许上传的文件类型
size:50 //最大允许上传文件的大小
});
```
从 layui2.1 开始，允许你直接在元素上设定基础参数，如：

```
[HTML]
<button class="layui-btn test" lay-data="{url:'/a/'}"}>上传图片</button> 
<button class="layui-btn test" lay-data="{url: '/b/', accept: 'file'}">上传文件</button>

[JS]
upload.render({
  elem: '.test'
  ,done: function(res, index, upload){
    //获取当前触发上传的元素，一般用于 elem 绑定 class 的情况，注意：此乃 layui 2.1.0 新增
    var item = this.item;
  }
})

```
更多支持的参数详见下表，合理的配置，应对各式各样的业务要求。

| 参数选项   | 说明                                                                                                                                                    | 类型          | 默认值                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------- |
| elem       | 指向容器选择器，如：emem:'#id'。也可以是 DOM对象                                                                                                        | string/object | -                                         |
| url        | 服务端上传接口，返回的数据规范请详见下文                                                                                                                | string        | -                                         |
| data       | 请求上传接口的额外参数。如：data:{id:'xxx'}，从layui2.2开始，支持动态值 <br> data: { <br> id: function(){ <br> return $('#id').val(); <br> }<br> } <br> | object        | -                                         |
| headers    | 接口的请求头。如:headers:{token:'sasas'}。layui2.2 新增                                                                                                 | object        | -                                         |
| accept     | 指定允许上传时校验的文件类型，可选的值有：images、file,video,audio                                                                                      | string        | images                                    |
| acceptMime | 规定打开文件选择框时，筛选的文件类型，如: acceptMime:'image/*'(只显示图片)，acceptMime:'image/jpg,image/png'                                            | string        | images                                    |
| exts       | 允许上传的文件后缀，一般结合accept参数设定 如 exts:'zip &#124;rar&#124;7z'                                                                              | string        | jpg &#124;png&#124;gif&#124;bmp&#124;jpeg |
| auto       | 是否选完文件后自动上传。如设定为 false，那么需要设置 bindAction参数来指向一个其它按钮提交上传                                                           | bllolean      | true                                      |
| bindAction | 指向一个按钮出发上传,值为选择器或DOM对象,如:bindAction:'#btn'                                                                                           | string/object | -                                         |
| field      | 设定文件域的字段名                                                                                                                                      | string        | file                                      |
| size       | 设置文件最大可允许上传的大小，单位 KB                                                                                                                   | number        | 0(即不限制)                               |
| multiple   | 是否支持多文件上传                                                                                                                                      | boolean       | false                                     |
| number     | 设置同时上传的文件数量,一般配合 multiple参数出现                                                                                                        | number        | 0(不限制)                                 |
| drag       | 是否支持拖拽                                                                                                                                            | boolean       | true                                      |
| ---        | 回调                                                                                                                                                    | 回调          | ---                                       |
| choose     | 选择文件后的回调函数                                                                                                                                    | function      | -                                         |
| before     | 文件提交上传前的回调                                                                                                                                    | function      | -                                         |
| done       | 执行上传请求后的回调。返回： res(服务端响应)，index(当前文件索引),upload(重新上传方法)                                                                  | funciton      | -                                         |
| error      | 执行上传请求出现异常的回调(一般为网络异常，URL404等)，返回：index(当前文件索引),upload(重新上传方法)                                                    | function      | -                                         |

#### 上传接口
设定一个URL给 url参数
``` js
upload.render({
  elem: '#id'
  ,url: '/api/upload/' //必填项
  ,method: ''  //可选项。HTTP类型，默认post
  ,data: {} //可选项。额外的参数，如：{id: 123, abc: 'xxx'}
});      
      
```
改接口返回的响应信息必须是一个标准的JSON格式
注意：如果上传后，出现文件下载框（一般为ie下），那么你需要在服务端对response的header设置 Content-Type: text/html

#### 选择文件的回调
在文件被选择后触发，该回调会在 before 回调之前。一般用于非自动上传（即 auto: false ）的场景，比如预览图片等。

``` js
upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,auto: false //选择文件后不自动上传
  ,bindAction: '#testListAction' //指向一个按钮触发上传
  ,choose: function(obj){
    //将每次选择的文件追加到文件队列
    var files = obj.pushFile();
    
    //预读本地文件，如果是多文件，则会遍历。(不支持ie8/9)
    obj.preview(function(index, file, result){
      console.log(index); //得到文件索引
      console.log(file); //得到文件对象
      console.log(result); //得到文件base64编码，比如图片
      
      //obj.resetFile(index, file, '123.jpg'); //重命名文件名，layui 2.3.0 开始新增
      
      //这里还可以做一些 append 文件列表 DOM 的操作
      
      //obj.upload(index, file); //对上传失败的单个文件重新上传，一般在某个事件中使用
      //delete files[index]; //删除列表中对应的文件，一般在某个事件中使用
    });
  }
});      
```
#### 多文件上传完毕后的状态回调
只有当开启多文件时（即 multiple: true），该回调才会被触发。回调返回一个 object 类型的参数，包含一些状态数据：
```js
upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,multiple: true
  ,allDone: function(obj){ //当文件全部被提交后，才触发
    console.log(obj.total); //得到总文件数
    console.log(obj.successful); //请求成功的文件数
    console.log(obj.aborted); //请求失败的文件数
  }
  ,done: function(res, index, upload){ //每个文件提交一次触发一次。详见“请求成功的回调”
  
  }
});      
      
```
#### 文件上传进度的回调
在网速一般的情况下，大文件的上传通常需要一定时间的等待，而浏览器并不会醒目地告知你它正在努力地上传中，此时为了提升用户体验，我们可以通过该回调制作一个进度条。注：该回调为 layui 2.5.5 新增

```js
upload.render({
  elem: '#id'
  ,url: '/api/upload/'
  ,progress: function(n, elem, res, index){
    var percent = n + '%' //获取进度百分比
    element.progress('demo', percent); //可配合 layui 进度条元素使用
    
    console.log(elem); //得到当前触发的元素 DOM 对象。可通过该元素定义的属性值匹配到对应的进度条。
    console.log(res); //得到 progress 响应信息
    console.log(index); //得到当前上传文件的索引，多文件上传时的进度条控制，如：
    element.progress('demo-'+ index, n + '%'); //进度条
  }
});       
```

### 下拉菜单 (dropdown)

### 穿梭框 (transfer)

### 树形组件 (tree)

### 颜色选择器(colorpicker)

### 常用元素操作 (element)

### 滑块 (slider)

### 评分 (rate)

### 轮播 (carousel)

### 流加载 (flow)
该模块包含 信息流加载 和 图片懒加载 两大核心支持，无论是对服务端、还是前端体验，都有非常大的性能帮助。

#### 使用 
flow 模块包含两个核心方法，如下：

```js
layui.use('flow',function(){

var flow = layui.flow;
//信息流
flow.load(options);

//图片懒加载
flow.lazyimg(options);
});
```
#### 信息流
信息流即异步逐页渲染列表元素，假设你的页面初始时只有6个列。

```html
<ul id="demo">
  <li>1</li>
  <li>2</li>
  ...
  <li>6</li>
</ul>
```
你想通过加载更多来显示余下列表，那么你只需执行方法： flow.load(options)即可。
```js
layui.use('flow',function(){
  var $ = layui.jquery;  //不用额外加载jQuery,flow 模块本身依赖jQuery
  var flow = layui.flow;

  flow.load({
    elem:'#demo', //指定列表容器
    done:function(page,next){ //到达临界点（默认滚动出发），触发下一页
      var lis=[];
      //以jquery 的 ajax 请求为例，请求下一页数据(注意：page是从2开始返回)
      $.get('/api/list?page='+page,function(res){
        //假设你的列表返回在 data集合中
        layui.each(res.data, function(index,item){
          lis.push('<li>'+item.title+'</li>');
        });
        
        //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
        //pages 为 ajax返回的总页数，只有当前页小于总页数的情况下，才会继续出现加载更多
        next(lis.join(''),page <res.pages);
      });
    }
  });
});
```

上述是一个比较简单的例子，以下是信息流完整的参数支撑

| 参数       | 类型     | 描述                                                                                                                                                                                                                      |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| elem       | string   | 指定列表容器的选择器                                                                                                                                                                                                      |
| scrollElem | string   | 滚动条所在元素选择器，默认 document。如果你不是通过窗口滚动来触发流加载，<br>而是页面中的某一个容器的滚动条，需指定此参数                                                                                                 |
| isAuto     | boolean  | 是否自动加载。默认true. 如手动，会在列表底部生成一个 "加载更多"的button                                                                                                                                                   |
| end        | string   | 用于显示页末内容，可传入任意Html。默认为：没有更多了                                                                                                                                                                      |
| isLazying  | boolean  | 是否开启图片懒加载，默认 false.如果设为true，<br>则只会对可视区域的图片按需加载。同时，在拼接列表字符时，<br>不能给 img 元素赋值src，必须用 lay-src取代,如<br>``` lis.push('<li><img lay-src="'+ item.src +'"></li>');``` |
| mb         | number   | 与底部的临界距离，默认50.即滚动条与底部距离。mb=margin-bottom                                                                                                                                                             |
| done       | function | 到达临界点触发加载的回调，例子如下                                                                                                                                                                                        |

``` js
done: function(page, next){
  //请注意：layui 1.0.5 之前的版本是从第2页开始返回，也就是说你的第一页数据并非done来触发加载
  （为之前这个愚蠢的设计表示抱歉）
  //从 layui 1.0.5 的版本开始，page是从1开始返回，初始时即会执行一次done回调。
  //console.log(page) //获得当前页
  
  //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
  //只有当前页小于总页数的情况下，才会继续出现加载更多
  next('列表HTML片段', page < res.pages); 
}
```

实现案例：
```js
var pageSize = 5;//每次请求新闻的条数
flow.load({
    elem: '#newsList' //指定列表容器
    ,scrollElem: '#newsList'//滚动条所在元素
    ,done: function(page, next){ //到达临界点（默认滚动触发），触发下一页的回调
        $.ajax({
            type: "POST",
            dataType: "json",
            data: {'pageIndex': page,'pageSize':pageSize},//请求的页码和每页显示条数
            async: true,
            url: '/news/list.do',
            success: function (result) {
                var lis = [];
                if (result.req && result.rows.length > 0) {//数据插入
                    //result.rows为Ajax返回的新闻数据
                    layui.each(result.rows, function(index, item){
                        var newsHtml = '<span news-id="'+item.id+'">'+ item.title +'</span>';
                        lis.push(newsHtml);
                    });

                    //执行下一页渲染，第二参数为：满足“加载更多”的条件，即后面仍有分页
                    //result.total为Ajax返回的总页数，只有当前页小于总页数的情况下，才会继续出现加载更多
                    next(lis.join(''), page < Math.ceil(result.total/pageSize));
                }

            }
        });
    }
});
```

#### 图片懒加载
语法： flow.lazyimg(options)

``` js
layui.use('flow', function(){
  var flow = layui.flow;
  //当你执行这样一个方法时，即对页面中的全部带有 lay-src 的 img 元素开启了懒加载（当然你也可以指定相关 img）
  flow.lazyimg(); 
});
```

它只会针对以下 img 元素有效：
```html
<img src="占位图地址" lay-src="预加载图地址"> 
<img src="" src="bbb.jpg">
<img src="" lay-src="ccc.jpg">       
```      
options参数可支持的 key 如下:

| 参数       | 类型   | 描述                                                                    |
| ---------- | ------ | ----------------------------------------------------------------------- |
| elem       | string | 指定开启懒加载的img元素选择器，如 elem: '.demo img' 或 elem: 'img.load' |
| scrollElem | string | 滚动条所在元素选择器，默认document。                                    |

### 工具组件 (util)
我们将一些工具性元素放入 util 模块中，以供选择性使用。

#### 固定块
语法： util.fixbar(options)

```js
layui.use('util', function(){
  var util = layui.util;
  
  //执行
  util.fixbar({
    bar1: true
    ,click: function(type){
      console.log(type);
      if(type === 'bar1'){
        alert('点击了bar1')
      }
    }
  });
});
```      

#### 倒计时(返回倒计时数值)
语法：util.countdown(endTime, serverTime, callback)

例子：
```js
<div id="test"></div>
 
<script>
layui.use('util', function(){
  var util = layui.util;
  
  //示例
  var endTime = new Date(2099,1,1).getTime() //假设为结束日期
  ,serverTime = new Date().getTime(); //假设为当前服务器时间，这里采用的是本地时间，实际使用一般是取服务端的
   
  util.countdown(endTime, serverTime, function(date, serverTime, timer){
    var str = date[0] + '天' + date[1] + '时' +  date[2] + '分' + date[3] + '秒';
    layui.$('#test').html('距离2099年1月1日还有：'+ str);
  });
});
</script>
```

### 代码高亮显示 (code)
# 其它
### layui上传视频

https://blog.csdn.net/weixin_41692437/article/details/107086260
https://www.cnblogs.com/wangpeihua/p/9525521.html
https://blog.csdn.net/qq_41654694/article/details/107162738


#### 上传视频

``` html
  <div class="layui-form-item" style="width:200%;">
                  <label class="layui-form-label">商品视频</label>
                  <div>
                    <video controls='controls' style="margin-top: 10px;max-width: 400px;width: 100%;">
                      <source src="" type='video/mp4' id="video">
                    </video>
                    <p>
                      <input type="text" name="goods_video" id="goods_video" style="display: none"><button
                        style="margin-left:110px;" type="button" class="layui-btn" id="video_upload_btn">上传视频</button>
                      <span style="color:brown">（支持AVI、mp4、wma、rm、rmvb、flash、mid、3GP格式）</span>
                    </p>
                  </div>
                </div>
```
