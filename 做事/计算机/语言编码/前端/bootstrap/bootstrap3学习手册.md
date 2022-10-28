---
title: bootstrap3学习手册
permalink: bootstrap3.html
theme: jekyll-theme-cayman
---

Bootstrap 是一个用于快速开发 Web 应用程序和网站的前端框架

bootstrap3 手册 https://v3.bootcss.com/css/

#### 移动设备优先
为了保持对移动设备的友好，需要加上以下代码:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
设置视口[窗口](viewport)对象的 user-scalable=no 属性,禁用缩放。用户只能滚动屏幕，不能双指缩放。 
```html
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
```
#### 排版与链接
bootstrap 内置了基本的全局样式，可以在 scaffolding.less 找到相应的源码。

1. 为body 元素设置 background-color:#fff;
2. 为所有链接设置基本颜色 @link-color,并且 :hover 时有下划线。

### 布局容器
bootstrap 需要为页面内容和栅格系统包裹一个 .container 容器

1. .container 类： 用于固定宽度并支持响应式布局
2. .container-fluid 占据全部视口,100%宽度

### 栅格系统 (用于创建版面布局)

bootstrap 提供了一套响应式、移动设优先的流式栅格系统，随着屏幕或视口尺寸的增加，系统会自动分为最多12列。

栅格系统使用一系列行(row)与列(column)来创建页面布局，下面是一些原理:
- 行 必须包含在 容器中(.contianer 或 .container-fluid) 中
- 内容需放在 列中
- 通过为列设置 padding 属性，从而创建列与列之间的间隔。
- 跨列通过 .col-xs-4 这种形式指定 (有4个列长)
- 如果一行 大于12列，会换行
- col-sm-1 的跨度是 col-xs-12 (即占用手机整列)

#### 媒体查询 (有条件的CSS规则)
``` css
/* 超小设备（手机，小于 768px） */
/* 在Bootstrap中默认情况下没有媒体查询 */

/* 小型设备（平板电脑，768px 起） */
@media (min-width: @screen-sm-min) { ... }

/* 中型设备（台式电脑，992px 起） */
@media (min-width: @screen-md-min) { ... }

/* 大型设备（大台式电脑，1200px 起） */
@media (min-width: @screen-lg-min) { ... }

```
#### 网格结构
> .col-xs- (手机)	.col-sm- (平板)	.col-md-(台式)	.col-lg- (电视)

##### 基本的网格结构
``` html
<div class="container">
   <div class="row">
      <div class="col-*-*"></div>
      <div class="col-*-*"></div>      
   </div>
   <div class="row">...</div>
</div>
<div class="container">....
```
##### 统一列高 clearfix 
列高度不统一时使用

``` html
<div class="container">
    <div class="row" >
        <div class="col-xs-6 col-sm-3"> 
           <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
            eiusmod tempor incididunt ut. 
            </p>
        </div>
 
        <div class="clearfix visible-xs"></div>
 
        <div class="col-xs-6 col-sm-3" >
            <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco 
            laboris nisi ut aliquip ex ea commodo consequat. 
            </p>
        </div>
   </div>
</div>
```

##### 偏移列 (跨过列)
语法格式： col-md-offset-3
##### 嵌套列
##### 列排序 (不会影响其它元素)
语法： col-md-push-8(往后排)  col-md-pull-3(往前排)

### 排版

#### 默认的页面主体
默认样式为 font-size:14px ,line-height:1.428 ，<p>的边框为10px

#### 标题
h1-h6 或者 .h1-.h6 都可以作为标题 
#### 段落
- 段落 <p>
- 着重 .lead 
#### 内联文本元素

- 高亮 <mark> 
- 删除 <del><s>
- 插入 <ins> 有下划线
- 下划线 <u>
- 小号 <small >或 .small
- 着重 <strong>
- 斜体 <em>

#### 文本 对齐+变色
``` html
<p class="text-left">向左对齐文本</p>
<p class="text-center">居中对齐文本</p>
<p class="text-right">向右对齐文本</p>
<p class="text-muted">本行内容是减弱的</p>
<p class="text-primary">本行内容带有一个 primary class</p>
<p class="text-success">本行内容带有一个 success class</p>
<p class="text-info">本行内容带有一个 info class</p>
<p class="text-warning">本行内容带有一个 warning class</p>
<p class="text-danger">本行内容带有一个 danger class</p>
```
#### 改变大小写
```html
<p class="text-lowercase">Lowercased text.</p>
<p class="text-uppercase">Uppercased text.</p>
<p class="text-capitalize">Capitalized text.</p>
```
#### <br/> 用于地址信息等不规则排版
#### 引用（blockquote）
footer 用于表明引用来源，cite用于倾斜footer 中的内容

```html
<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer>Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>
```

.blockquote-reverse :右对齐引用
#### 列表
``` html
<h4>有序列表</h4>
<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ol>
<h4>无序列表</h4>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ul>
<h4>未定义样式列表</h4>
<ul class="list-unstyled">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ul>
<h4>内联列表： 就是水平显示</h4>
<ul class="list-inline">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ul>
<h4>定义列表</h4>
<dl>
  <dt>Description 1</dt>
  <dd>Item 1</dd>
  <dt>Description 2</dt>
  <dd>Item 2</dd>
</dl>
<h4>水平的定义列表</h4>
<dl class="dl-horizontal">
  <dt>Description 1</dt>
  <dd>Item 1</dd>
  <dt>Description 2</dt>
  <dd>Item 2</dd>
</dl>
```
#### 更多排版类

| 类                  | 描述                                        |
|---------------------+---------------------------------------------|
| .text-justify       | 设定文本对齐,段落中超出屏幕部分文字自动换行 |
| .text-nowrap        | 段落中超出屏幕部分不换行                    |
| .text-lowercase     | 设定文本小写                                |
| .text-uppercase     | 设定文本大写                                |
| .text-capitalize    | 设定单词首字母大写                          |

### 代码
``` html
<p><code>&lt;header&gt;</code> 作为内联元素被包围。</p>
<p>如果需要把代码显示为一个独立的块元素，请使用 &lt;pre&gt; 标签：</p>
<pre>
    &lt;article&gt;
        &lt;h1&gt;Article Heading&lt;/h1&gt;
    &lt;/article&gt;
</pre>

```
### 表格
#### 表格类
| 类                | 描述                                  |
|-------------------+---------------------------------------|
| .table            | 基本样式                              |
| .table-striped    | 在 <tbody> 内添加斑马线形式的条纹     |
| .table-bordered   | 为所有表格的单元格添加边框            |
| .table-hover      | 在 <tbody> 内的任一行启用鼠标悬停状态 |
| .table-condensed  | 让表格更加紧凑                        |
| .table-responsive | 响应式，小型设备有滚动条              |

垂直方向的内容截断: overflow-y: hidden
#### tr,th 和 td 类 (单元格类)

| 类       | 描述                             |
|----------+----------------------------------|
| .active  | 将悬停的颜色应用在行或者单元格上 |
| .success | 表示成功的操作                   |
| .info    | 表示信息变化的操作               |
| .warning | 表示一个警告的操作               |
| .danger  | 表示一个危险的操作               |

### 表单
所有设置了 .form-control 的表单元素都被设置宽度为100%, 将 label 和表单元素放在 .form-group 能获得更好的表现
#### 表单 
``` html
<form role="form">
  <div class="form-group">
    <label for="name">名称</label>
    <input type="text" class="form-control" id="name" placeholder="请输入名称">
  </div>
  <div class="form-group">
    <label for="inputfile">文件输入</label>
    <input type="file" id="inputfile">
    <p class="help-block">这里是块级帮助文本的实例。</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox">请打勾
    </label>
  </div>
  <button type="submit" class="btn btn-default">提交</button>
</form>
```
#### 内联表单 
平板及以上才能展示效果

``` html
<form class="form-inline" role="form">
  <div class="form-group">
    <label class="sr-only" for="name">名称</label>
    <input type="text" class="form-control" id="name" placeholder="请输入名称">
  </div>
  <div class="form-group">
    <label class="sr-only" for="inputfile">文件输入</label>
    <input type="file" id="inputfile">
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox">请打勾
    </label>
  </div>
  <button type="submit" class="btn btn-default">提交</button>
</form>

```
#### 水平表单 .form-horizontal

通过与 栅格类 .col-sm-10 结合，可以控制表单的长度
```html
<form class="form-horizontal">
  <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
    </div>
  </div>
</form>
```


#### 其它
- 多选 
``` html
 <select multiple class="form-control">
```
- 静态控件 
``` html
<p class="form-control-static">email@example.com</p>
``` 
#### 控件状态
``` html
<form class="form-horizontal" role="form">
  <div class="form-group">
    <label class="col-sm-2 control-label">聚焦</label>
    <div class="col-sm-10">
      <input class="form-control" id="focusedInput" type="text" value="该输入框获得焦点...">
    </div>
  </div>
  <div class="form-group">
    <label for="inputPassword" class="col-sm-2 control-label">禁用</label>
    <div class="col-sm-10">
      <input class="form-control" id="disabledInput" type="text" placeholder="该输入框禁止输入..." disabled>
    </div>
  </div>
  <fieldset disabled>
    <div class="form-group">
      <label for="disabledTextInput" class="col-sm-2 control-label">禁用输入（Fieldset disabled）</label>
      <div class="col-sm-10">
        <input type="text" id="disabledTextInput" class="form-control" placeholder="禁止输入">
      </div>
    </div>
    <div class="form-group">
      <label for="disabledSelect" class="col-sm-2 control-label">禁用选择菜单（Fieldset disabled）</label>
      <div class="col-sm-10">
        <select id="disabledSelect" class="form-control">
          <option>禁止选择</option>
        </select>
      </div>
    </div>
  </fieldset>
  <div class="form-group has-success">
    <label class="col-sm-2 control-label" for="inputSuccess">输入成功</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="inputSuccess">
    </div>
  </div>
  <div class="form-group has-warning">
    <label class="col-sm-2 control-label" for="inputWarning">输入警告</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="inputWarning">
    </div>
  </div>
  <div class="form-group has-error">
    <label class="col-sm-2 control-label" for="inputError">输入错误</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="inputError">
    </div>
  </div>
</form>

```
#### 表单帮助文本
``` html
<form role="form">
  <span>帮助文本实例</span>
  <input class="form-control" type="text" placeholder="">
  <span class="help-block">一个较长的帮助文本块，超过一行，
  需要扩展到下一行。本实例中的帮助文本总共有两行。</span>
</form>
```

#### 校验状态
添加校验样式 .has-warning、.has-error 或 .has-success

```html
<div class="form-group has-success">
  <label class="control-label" for="inputSuccess1">Input with success</label>
  <input type="text" class="form-control" id="inputSuccess1" aria-describedby="helpBlock2">
  <span id="helpBlock2" class="help-block">A block of help text that breaks onto a new line and may extend beyond one line.</span>
</div>
```
##### 添加额外的图标
.has-feedback 类并添加正确的图标即可
```html
<div class="form-group has-success has-feedback">
  <label class="control-label" for="inputSuccess2">Input with success</label>
  <input type="text" class="form-control" id="inputSuccess2" aria-describedby="inputSuccess2Status">
  <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>
  <span id="inputSuccess2Status" class="sr-only">(success)</span>
</div>
```

#### 控件尺寸
通过 .input-lg 类似的类可以为控件设置高度，通过 .col-lg-* 类似的类可以为控件设置宽度。
```html
<input class="form-control input-lg" type="text" placeholder=".input-lg">
<input class="form-control" type="text" placeholder="Default input">
<input class="form-control input-sm" type="text" placeholder=".input-sm">

```
### 按钮 
| 类           | 描述                                    |
|--------------+-----------------------------------------|
| .btn         | 为按钮添加基本样式                      |
| .btn-default | 默认/标准按钮                           |
| .btn-primary | 原始按钮样式（未被操作）                |
| .btn-success | 表示成功的动作                          |
| .btn-info    | 该样式可用于要弹出信息的按钮            |
| .btn-warning | 表示需要谨慎操作的按钮                  |
| .btn-danger  | 表示一个危险动作的按钮操作              |
| .btn-link    | 让按钮看起来像个链接 (仍然保留按钮行为) |
| .btn-lg      | 制作一个大按钮                          |
| .btn-sm      | 制作一个小按钮                          |
| .btn-xs      | 制作一个超小按钮                        |
| .btn-block   | 块级按钮(拉伸至父元素100%的宽度)        |
| .active      | 按钮被点击                              |
| .disabled    | 禁用按钮                                |

#### 按钮大小 

| 类         | 描述                     |
| ---------- | ------------------------ |
| .btn-lg    | 这会让按钮看起来比较大。 |
| .btn-sm    | 这会让按钮看起来比较小。 |
| .btn-xs    | 这会让按钮看起来特别小。 |
| .btn-block | 占用整行                 |

#### 按钮状态  active(激活) disabled
#### 按钮组 btn-group  btn-group-lg  .btn-group-vertical (垂直) btn-group-justified (自适应大小)

内嵌下拉菜单的按钮组
``` html
<div class="btn-group">
  <button type="button" class="btn btn-primary">Apple</button>
  <button type="button" class="btn btn-primary">Samsung</button>
  <div class="btn-group">
    <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
    Sony <span class="caret"></span></button>
    <ul class="dropdown-menu" role="menu">
      <li><a href="#">Tablet</a></li>
      <li><a href="#">Smartphone</a></li>
    </ul>
  </div>
</div>

```

分割按钮
``` html
<div class="btn-group">
  <button type="button" class="btn btn-primary">Sony</button>
  <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu" role="menu">
    <li><a href="#">Tablet</a></li>
    <li><a href="#">Smartphone</a></li>
  </ul>
</div>
```
### 图片
| 类              | 描述                                                  |
|-----------------+-------------------------------------------------------|
| .img-rounded    | 添加 border-radius:6px 来获得图片圆角。               |
| .img-circle     | 添加 border-radius:50% 来让整个图片变成圆形。         |
| .img-thumbnail  | 添加一些内边距（padding）和一个灰色的边框。           |
| .img-responsive | 将 max-width: 100%; 和 height: auto; 样式应用在图片上 |

### 辅助类
#### 情境文本 (文本颜色)
通过颜色来展示意图，与下面一样一般用于增加鼠标的行为
```html
<p class="text-muted">...</p>
<p class="text-primary">...</p>
<p class="text-success">...</p>
<p class="text-info">...</p>
<p class="text-warning">...</p>
<p class="text-danger">...</p>
```
#### 背景
| 类          | 描述                             |
|-------------+----------------------------------|
| .bg-primary | 表格单元格使用了 "bg-primary" 类 |
| .bg-success | 表格单元格使用了 "bg-success" 类 |
| .bg-info    | 表格单元格使用了 "bg-info" 类    |
| .bg-warning | 表格单元格使用了 "bg-warning" 类 |
| .bg-danger  | 表格单元格使用了 "bg-danger" 类  |

#### 其它

| 类                    | 描述                                                             |
|-----------------------+------------------------------------------------------------------|
| .pull-left            | 元素浮动到左边                                                   |
| .pull-right           | 元素浮动到右边                                                   |
| .center-block         | 设置元素为 display:block 并居中显示                              |
| .clearfix	清除浮动 |                                                                  |
| .show                 | 强制元素显示                                                     |
| .hidden               | 强制元素隐藏                                                     |
| .sr-only              | 除了屏幕阅读器外，其他设备上隐藏元素                             |
| .sr-only-focusable    | 与 .sr-only 类结合使用，在元素获取焦点时显示(如：键盘操作的用户) |
| .text-hide            | 将页面元素所包含的文本内容替换为背景图                           |
| .close                | 显示关闭按钮                                                     |
| .caret                | 显示下拉式功能                                                   |

#### 关闭图标
``` html
  <button type="button" class="close" aria-hidden="true">
    &times;
  </button>
```

#### 三角符号
``` html
<p>插入符实例
  <span class="caret"></span>
</p>

```
#### 快速浮动
```html
 <div class="pull-left" style="background:#58D3F7;">
    向左快速浮动
  </div>
  <div class="pull-right" style="background: #DA81F5;">
    向右快速浮动
  </div>
  ```
#### 居中 .center-block
1、 文本：class ="text-center"
2、 图片居中：class = "center-block"
#### 垂直居中

bootstrap3 如何让div内部垂直居中：

Bootstrap的栅格系统使用的是float：left的浮动方式，vertical-align属性不起作用，故把内部div的float属性清除，添加display属性，如下：
``` css
.middle {
float: none;
display: inline-block;
vertical-align: middle;
}
 ```

Bootstrap3登录框自适应水平居中+垂直居中

方法2 

``` css
.middle {
 display: flex; 
 flex-direction: column;
 justify-content: center;
 border: 1px solid #ccc;
 height:100px;
 width: 100px;
 text-align: center;
}
 ```
#### 清除浮动
``` html
<div class="clearfix"> </div>
```

#### 显示或隐藏内容
.show .hidden
### 响应式工具
通过使用这些工具类，可以在不同的设备上提供不同的展现形式

![](images/visible.png)

## 组件

### 导航

#### 标签页式导航
```html
<ul class="nav nav-tabs">
  <li role="presentation" class="active"><a href="#">Home</a></li>
  <li role="presentation"><a href="#">Profile</a></li>
  <li role="presentation"><a href="#">Messages</a></li>
</ul>
```

#### 导航条

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Brand</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">One more separated link</a></li>
          </ul>
        </li>
      </ul>
      <form class="navbar-form navbar-left">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
```
### 字体图标(Glyphicons)
用法
```html
<span class="glyphicon glyphicon-search"></span>
```

> 定制尺寸 ,颜色   style="color: rgb(212, 106, 64);" 阴影  style="text-shadow: black 5px 3px 3px;"
``` html
<button type="button" class="btn btn-primary btn-lg" style="font-size: 60px">
  <span class="glyphicon glyphicon-user"></span> User
</button>
```

### 下拉菜单（Dropdowns）
``` html
<div class="dropdown">
    <button type="button" class="btn dropdown-toggle" id="dropdownMenu1" data-toggle="dropdown">主题
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">Java</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据挖掘</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据通信/网络</a>
        </li>
        <li role="presentation" class="divider"></li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">分离的链接</a>
        </li>
    </ul>
</div>

```

标题
``` html
<li role="presentation" class="dropdown-header">下拉菜单标题</li>
```

| 类                   | 描述                                        |
|----------------------+---------------------------------------------|
| .dropdown            | 指定下拉菜单，下拉菜单都包裹在 .dropdown 里 |
| .dropdown-menu       | 创建下拉菜单                                |
| .dropdown-menu-right | 下拉菜单右对齐                              |
| .dropdown-header     | 下拉菜单中添加标题                          |
| .dropup              | 指定向上弹出的下拉菜单                      |
| .disabled            | 下拉菜单中的禁用项                          |
| .divider             | 下拉菜单中的分割线                          |

### 标签
| 类                   | 描述                     |
|----------------------+--------------------------|
| .label label-default | 默认的灰色标签           |
| .label label-primary | "primary" 类型的蓝色标签 |
| .label label-success | "success" 类型的绿色标签 |
| .label label-info    | "info" 类型的浅蓝色标签  |
| .label label-warning | "warning" 类型的黄色标签 |
| .label label-danger  | "danger" 类型的红色标签  |

### 警告（Alerts）

``` html
<div class="alert alert-success">成功！很好地完成了提交。</div>
<div class="alert alert-info">信息！请注意这个信息。</div>
<div class="alert alert-warning">警告！请不要提交。</div>
<div class="alert alert-danger">错误！请进行一些更改。</div>
```

可取消的警告（Dismissal Alerts）

``` html
<div class="alert alert-success alert-dismissable">
            <button type="button" class="close" data-dismiss="alert"
                    aria-hidden="true">
                &times;
            </button>
            成功！很好地完成了提交。
        </div>
        <div class="alert alert-info alert-dismissable">
            <button type="button" class="close" data-dismiss="alert"
                    aria-hidden="true">
                &times;
            </button>
            信息！请注意这个信息。
        </div>
        <div class="alert alert-warning alert-dismissable">
            <button type="button" class="close" data-dismiss="alert"
                    aria-hidden="true">
                &times;
            </button>
            警告！请不要提交。
        </div>
        <div class="alert alert-danger alert-dismissable">
            <button type="button" class="close" data-dismiss="alert"
                    aria-hidden="true">
                &times;
            </button>
            错误！请进行一些更改。
        </div>
```

警告链接
``` html
<div class="alert alert-success">
    <a href="#" class="alert-link">成功！很好地完成了提交。</a>
</div>
```

### 面板（Panels）

``` html
<div class="panel panel-primary">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
<div class="panel panel-success">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
<div class="panel panel-info">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
<div class="panel panel-warning">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
<div class="panel panel-danger">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
```

## 插件 (依赖jQuery)

### 插件概览

关闭插件
``` js
$(document).off('.data-api')
$(document).off('.alert.data-api')
```

使用 
``` js
// 初始化为默认行为
$("#myModal").modal()    
 // 初始化为不支持键盘               
$("#myModal").modal({ keyboard: false })  
// 初始化并立即调用 show
$("#myModal").modal('show')        
```

### 过渡效果（Transition）插件
### 模态框（Modal）插件
> 表单提交事件 可以用绑定 form  事件 ，这方法很笨!!
> ! 用 form.submit 事件好 ,这个方法好

``` html
<button type="submit" class="btn btn-primary tijiao" form="form1">提交更改</button>
```
#### 创建模态框
``` html
<h2>创建模态框（Modal）</h2>
<!-- 按钮触发模态框 -->
<button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">静态打开 </button>
<!-- 模态框（Modal） -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title" id="myModalLabel">模态框（Modal）标题</h4>
            </div>
            <div class="modal-body">在这里添加一些文本</div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button type="button" class="btn btn-primary">提交更改</button>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal -->
</div>

```

代码讲解：

- 使用模态窗口，您需要有某种触发器。您可以使用按钮或链接。这里我们使用的是按钮。
- 如果您仔细查看上面的代码，您会发现在 <button> 标签中，data-target="#myModal" 是您想要在页面上加载的模态框的目标。您可以在页面上创建多个模态框，然后为每个模态框创建不同的触发器。现在，很明显，您不能在同一时间加载多个模块，但您可以在页面上创建多个在不同时间进行加载。
- 在模态框中需要注意两点：
   1. 第一是 .modal，用来把 <div> 的内容识别为模态框。
   2. 第二是 .fade class。当模态框被切换时，它会引起内容淡入淡出。
- aria-labelledby="myModalLabel"，该属性引用模态框的标题。
- 属性 aria-hidden="true" 用于保持模态窗口不可见，直到触发器被触发为止（比如点击在相关的按钮上）。
- <div class="modal-header">，modal-header 是为模态窗口的头部定义样式的类。
- class="close"，close 是一个 CSS class，用于为模态窗口的关闭按钮设置样式。
- data-dismiss="modal"，是一个自定义的 HTML5 data 属性。在这里它被用于关闭模态窗口。
- class="modal-body"，是 Bootstrap CSS 的一个 CSS class，用于为模态窗口的主体设置样式。
- class="modal-footer"，是 Bootstrap CSS 的一个 CSS class，用于为模态窗口的底部设置样式。
- data-toggle="modal"，HTML5 自定义的 data 属性 data-toggle 用于打开模态窗口。


#### 打开modal
##### 静态打开：通过data属性打开隐藏模态框

> 设置按钮button的data-toggle:"modal"（以模态框的形式打开），data-target:"#myModal"（设置为modal的id）

##### 动态打开：以jquery代码为例
``` js
$("#myModal").modal({
remote:"test/test.jsp";//可以填写一个url，会调用jquery load方法加载数据
backdrop:"static";//指定一个静态背景，当用户点击背景处，modal界面不会消失
keyboard:true;//当按下esc键时，modal框消失
})
 ```
remote处可以填写jsp路径或者html路径，用来给modal框注入内容

其它参数
``` js
//屏蔽键盘
$('#identifier').modal({
keyboard: false
})


//手动切换模态框。	
$('#identifier').modal('toggle')
//手动打开模态框。	
$('#identifier').modal('show')
//手动隐藏模态框。	
$('#identifier').modal('hide')
```

#### 动态打开事件
下表列出了模态框中要用到事件。这些事件可在函数中当钩子使用。

``` js

$("#myModal").on("loaded.bs.modal",function{
//在模态框加载的同时做一些动作
 
});
 
$("#myModal").on("show.bs.modal",function{
 
//在show方法后调用
 
});
 
 
$("#myModal").on("shown.bs.modal",function{
 
//在模态框完全展示出来做一些动作
 
});
 
$("#myModal").on("hide.bs.modal",function{
 
//hide方法后调用
 
});
 
$("#myModal").on("hiden.bs.modal",function{
 
//监听模态框隐藏事件做一些动作
 
});
```


### 弹出框（Popover）插件

``` html
<div class="container" style="padding: 100px 50px 10px;" >
    <button type="button" class="btn btn-default" title="Popover title"
            data-container="body" data-toggle="popover" data-placement="left"
            data-content="左侧的 Popover 中的一些内容">
        左侧的 Popover
    </button>
    <button type="button" class="btn btn-primary" title="Popover title"
            data-container="body" data-toggle="popover" data-placement="top"
            data-content="顶部的 Popover 中的一些内容">
        顶部的 Popover
    </button>
    <button type="button" class="btn btn-success" title="Popover title"
            data-container="body" data-toggle="popover" data-placement="bottom"
            data-content="底部的 Popover 中的一些内容">
        底部的 Popover
    </button>
    <button type="button" class="btn btn-warning" title="Popover title"
            data-container="body" data-toggle="popover" data-placement="right"
            data-content="右侧的 Popover 中的一些内容">
        右侧的 Popover
    </button>
</div>
 
<script>
$(function (){
    $("[data-toggle='popover']").popover();
});
</script>
</div>

```
### 标签页(选项卡) tab.js
通过选项卡，或者下拉菜单来切换内容

#### 用法

激活标签(选项卡)每个选项卡需要单独激活

```js
$('#myTabs a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})
```
其它激活方式
```js
$('#myTabs a[href="#profile"]').tab('show') // Select tab by name
$('#myTabs a:first').tab('show') // Select first tab
$('#myTabs a:last').tab('show') // Select last tab
$('#myTabs li:eq(2) a').tab('show') // Select third tab (0-indexed)
```

#### 标记
如果不写 js 脚本，可以 通过 指定元素的 data-toggle="tab" 或者 data-toggle="pill" 属性。
给 ul 添加 nav 和 nav-tabs 类，可以应用 bootstrap的 tab 样式。而 nav 与 nav-pills 会应用 pill 样式。 

```html
<div>

  <!-- Nav tabs -->
  <ul class="nav nav-tabs" role="tablist">
    <li role="presentation" class="active"><a href="#home" aria-controls="home" role="tab" data-toggle="tab">Home</a></li>
    <li role="presentation"><a href="#profile" aria-controls="profile" role="tab" data-toggle="tab">Profile</a></li>
    <li role="presentation"><a href="#messages" aria-controls="messages" role="tab" data-toggle="tab">Messages</a></li>
    <li role="presentation"><a href="#settings" aria-controls="settings" role="tab" data-toggle="tab">Settings</a></li>
  </ul>

  <!-- Tab panes -->
  <div class="tab-content">
    <div role="tabpanel" class="tab-pane active" id="home">...</div>
    <div role="tabpanel" class="tab-pane" id="profile">...</div>
    <div role="tabpanel" class="tab-pane" id="messages">...</div>
    <div role="tabpanel" class="tab-pane" id="settings">...</div>
  </div>

</div>
```
#### 淡入淡出
给每个 .tab-pane (窗格) 添加 .fade ，第一个tab pane 另外要加 .in 类

```html
<div class="tab-content">
  <div role="tabpanel" class="tab-pane fade in active" id="home">...</div>
  <div role="tabpanel" class="tab-pane fade" id="profile">...</div>
  <div role="tabpanel" class="tab-pane fade" id="messages">...</div>
  <div role="tabpanel" class="tab-pane fade" id="settings">...</div>
</div>
```

#### 事件
```js
$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
  e.target // newly activated tab
  e.relatedTarget // previous active tab
})
```
### 折叠（Collapse）插件
``` html
<div class="panel-group" id="accordion">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a data-toggle="collapse" data-parent="#accordion" 
                href="#collapseOne">
                点击我进行展开，再次点击我进行折叠。第 1 部分--hide 方法
                </a>
            </h4>
        </div>
        <div id="collapseOne" class="panel-collapse collapse in">
            <div class="panel-body">
                Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred 
                nesciunt sapiente ea proident. Ad vegan excepteur butcher vice 
                lomo.
            </div>
        </div>
    </div>
    <div class="panel panel-success">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a data-toggle="collapse" data-parent="#accordion" 
                href="#collapseTwo">
                点击我进行展开，再次点击我进行折叠。第 2 部分--show 方法
                </a>
            </h4>
        </div>
        <div id="collapseTwo" class="panel-collapse collapse">
            <div class="panel-body">
                Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred 
                nesciunt sapiente ea proident. Ad vegan excepteur butcher vice 
                lomo.
            </div>
        </div>
    </div>
    <div class="panel panel-info">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a data-toggle="collapse" data-parent="#accordion" 
                href="#collapseThree">
                点击我进行展开，再次点击我进行折叠。第 3 部分--toggle 方法
                </a>
            </h4>
        </div>
        <div id="collapseThree" class="panel-collapse collapse">
            <div class="panel-body">
                Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred 
                nesciunt sapiente ea proident. Ad vegan excepteur butcher vice 
                lomo.
            </div>
        </div>
    </div>
    <div class="panel panel-warning">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a data-toggle="collapse" data-parent="#accordion" 
                href="#collapseFour">
                点击我进行展开，再次点击我进行折叠。第 4 部分--options 方法
                </a>
            </h4>
        </div>
        <div id="collapseFour" class="panel-collapse collapse">
            <div class="panel-body">
                Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred 
                nesciunt sapiente ea proident. Ad vegan excepteur butcher vice 
                lomo.
            </div>
        </div>
    </div>
</div>
<script>
$(function () { $('#collapseFour').collapse({
        toggle: false
    })});
    $(function () { $('#collapseTwo').collapse('show')});
    $(function () { $('#collapseThree').collapse('toggle')});
    $(function () { $('#collapseOne').collapse('hide')});
</script>
```

### 轮播（Carousel）插件
#### 可选的标题
您可以通过 .item 内的 .carousel-caption 元素向幻灯片添加标题。只需要在该处放置任何可选的 HTML 即可，它会自动对齐并格式化

``` html
<div id="myCarousel" class="carousel slide">
    <!-- 轮播（Carousel）指标 -->
    <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>   
    <!-- 轮播（Carousel）项目 -->
    <div class="carousel-inner">
        <div class="item active">
            <img src="/wp-content/uploads/2014/07/slide1.png" alt="First slide">
            <div class="carousel-caption">标题 1</div>
        </div>
        <div class="item">
            <img src="/wp-content/uploads/2014/07/slide2.png" alt="Second slide">
            <div class="carousel-caption">标题 2</div>
        </div>
        <div class="item">
            <img src="/wp-content/uploads/2014/07/slide3.png" alt="Third slide">
            <div class="carousel-caption">标题 3</div>
        </div>
    </div>
    <!-- 轮播（Carousel）导航 -->
    <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>

```
#### 方法
``` js
$(function(){
        // 初始化轮播
        $(".start-slide").click(function(){
            $("#myCarousel").carousel('cycle');
        });
        // 停止轮播
        $(".pause-slide").click(function(){
            $("#myCarousel").carousel('pause');
        });
        // 循环轮播到上一个项目
        $(".prev-slide").click(function(){
            $("#myCarousel").carousel('prev');
        });
        // 循环轮播到下一个项目
        $(".next-slide").click(function(){
            $("#myCarousel").carousel('next');
        });
        // 循环轮播到某个特定的帧 
        $(".slide-one").click(function(){
            $("#myCarousel").carousel(0);
        });
        $(".slide-two").click(function(){
            $("#myCarousel").carousel(1);
        });
        $(".slide-three").click(function(){
            $("#myCarousel").carousel(2);
        });
    });

```

#### 事件
``` js

$('#identifier').on('slide.bs.carousel', function () {
//当调用 slide 实例方法时立即触发该事件。
})


$('#identifier').on('slid.bs.carousel', function () {
//当轮播完成幻灯片过渡效果时触发该事件。	
})
```


## 其它内容
### 修改 input里file的样式
``` html
<div class="form-group">
    <label class="col-sm-2 control-label"><img src="index.png"alt=""></label>
    <div class="col-sm-2 ">
        <label for="file"class=" btn btn-default">更换头像</label>
        <input id="file"type="file"style="display:none">
    </div>
</div>
```

> 使用 label for 作指向，隐藏 input file
> label 中的样式可以对应 button 的样式


## 遮罩

<div class="modal fade" id="loadingModal">
    <div style="width: 200px;height:20px; z-index: 20000; position: absolute; text-align: center; left: 50%; top: 50%;margin-left:-100px;margin-top:-10px">
        <div class="progress progress-striped active" style="margin-bottom: 0;">
            <div class="progress-bar" style="width: 100%;"></div>
        </div>
        <h5>正在加载...</h5>
    </div>
</div>

2、用jquery进行显示和隐藏

//显示
$("#loadingModal").modal('show');
//隐藏
$("#loadingModal").modal('hide');
3、其他设置

//使点击空白处遮罩层不会消失
$("#loadingModal").modal({backdrop:'static'});
//按Tab键遮罩层不会消失 ，默认值为true
$("#loadingModal").modal({keyboard:false});
  
//也可以一起运用
//backdrop 为 static 时，点击模态对话框的外部区域不会将其关闭。
//keyboard 为 false 时，按下 Esc 键不会关闭 Modal。
$('#loadingModal').modal({backdrop: 'static', keyboard: false});
