#### getTableInfo 获取表的信息
``` php 
// 获取`think_user`表所有信息
Db::getTableInfo('think_user');
// 获取`think_user`表所有字段
Db::getTableInfo('think_user', 'fields');
// 获取`think_user`表所有字段的类型
Db::getTableInfo('think_user', 'type');
// 获取`think_user`表的主键
Db::getTableInfo('think_user', 'pk');
```
### 查询语法
#### 查询表达式
``` php
where('id','between','1,8');
$map['id'] = array('not between','1,8');
where('id','not in','1,5,8');
where('name','not null');
where('id','exp',' IN (1,3,8) ');
// 正确 推荐写法
$model->whereExp('id', '>score')->find();
```
### 链式操作(连贯操作)

| 连贯操作      | 作用                                 |
| ------------- | ------------------------------------ |
| where*        | 用于AND查询                          |
| whereOr*      | 用于OR查询                           |
| wheretime*    | 用于时间日期的快捷查询               |
| table         | 用于定义要操作的数据表名称           |
| alias         | 用于给当前数据表定义别名             |
| field*        | 用于定义要查询的字段（支持字段排除） |
| order*        | 用于对结果排序                       |
| limit         | 用于限制查询结果数量                 |
| page          | 用于查询分页（内部会转换成limit）    |
| group         | 用于对查询的group支持                |
| having        | 用于对查询的having支持               |
| join*         | 用于对查询的join支持                 |
| union*        | 用于对查询的union支持                |
| view*         | 用于视图查询                         |
| distinct      | 用于查询的distinct支持               |
| lock          | 用于数据库的锁机制                   |
| cache         | 用于查询缓存                         |
| relation*     | 用于关联查询                         |
| with*         | 用于关联预载入                       |
| bind*         | 用于数据绑定操作                     |
| comment       | 用于SQL注释                          |
| force         | 用于数据集的强制索引                 |
| master        | 用于设置主服务器读取数据             |
| strict        | 用于设置是否严格检测字段名是否存在   |
| sequence      | 用于设置Pgsql的自增序列名            |
| failException | 用于设置没有查询到数据是否抛出异常   |
| partition     | 用于设置分表信息                     |


所有的连贯操作都返回当前的模型实例对象（this），其中带*标识的表示支持多次调用。
#### field 

``` php
//可以用于合法性写入
Db::table('think_user')->field('title,email,content')->insert($data);

//在 field中还可以使用函数
Db::table('think_user')->field('id,nickname as name,SUM(score)')->select();

field(['id','concat("abc",path)'=>'path'])
```

#### limit
limit 方法主要用于指定查询和操作的数量，特别是在分页查询的时候。

##### 限制结果数量
```php
->limit(10)
```

##### 分页查询
```php
Db::table('think_article')->limit('10,25')->select();
//或者 ->limit(10,25)
```
表示查找从第10行开始的25条数据

#### page
page 方法是为分页查询而创建的一个人性化操作的方法。

``` php
// 查询第一页数据，page的第一个参数指定页号，比limit更人性
Db::table('think_article')->page('1,10')->select();

```

获取总页数 totalPages

### group

``` php
Db::table('think_user')
->field('user_id,username,max(score)')
->group('user_id')
->select();
```

### having
``` php
Db::table('think_user')
->field('username,max(score)')
->group('user_id')
->having('count(test_time)>3')
->select();
```

### cache
``` php
Db::table('think_user')->cache(true,60)->find();
// 或者使用下面的方式 是等效的
Db::table('think_user')->cache(60)->find();
```

### 时间
``` php
// 获取今天的博客
Db::table('think_blog') ->whereTime('create_time', 'today')->select();
// 获取昨天的博客
Db::table('think_blog')->whereTime('create_time', 'yesterday')->select();
// 获取本周的博客
Db::table('think_blog')->whereTime('create_time', 'week')->select();
// 获取上周的博客

```
### 子查询
1.构造
``` php
$subQuery = Db::table('think_user')
->field('id,name')
->where('id','>',10)
->buildSql();
```

2. 执行
``` php
Db::table($subQuery.' a')
->where('a.name','like','thinkphp')
->order('id','desc')
->select();
```
闭包构造
``` php
Db::table('think_user')
->where('id','IN',function($query){
$query->table('think_profile')->where('status',1)->field('id');
})
->select();

```
### with 连接两个表

``` php
   $list = $this->model
                ->with('taocan,account')
                ->where($where)
                ->order($sort, $order)
                ->paginate($limit);
                
                //model
  public function account()
    {
        return $this->belongsTo("app\admin\model\ShopAccount"[关联表], "shop_account_id"[主表字段], 'id'[关联字段], [], 'LEFT')->setEagerlyType(0);
    }
                
 $data = [
            'total'     => $r->total(),         // 总记录数
            'cur'       => $r->currentPage(),   // 当前页码
            'size'      => $r->listRows(),      // 每页记录数
            'list'      => $r->items()          // 分页数据
        ];
```

## 模型

### 模型定义
``` php
<?php
namespace app\index\model;

use think\Model;
class User extends Model{ }
```

### 模型使用

``` php
$user = new User;
$user->name = 'thinkphp';
$user->email = 'thinkphp@qq.com';
$user->save();
// 获取自增ID
echo $user->id;
```

删除数据
``` php
// 删除状态为0的数据
User::destroy(['status' => 0]);
//条件删除
User::destroy(function($query){
    $query->where('id','>',10);
});
```

获取多个数据
``` php
// 使用数组查询
$list = User::all(['status'=>1]);
// 使用闭包查询
$list = User::all(function($query){
$query->where('status', 1)->limit(3)->order('id', 'asc');
});
foreach($list as $key=>$user){
echo $user->name;
}

```
或者在实例化模型后调用查询方法
``` php
$user = new User();
// 查询数据集
$user->where('name', 'thinkphp')
->limit(10)
->order('id', 'desc')
->select();
 ```

## 视图

``` php
use think\facade\View;

// 渲染模板输出
return $this->fetch('hello',['name'=>'thinkphp']);
return view('hello',['name'=>'thinkphp']);
```

### json 输出
默认类型 'default_return_type'=>'json'

指定 xml类型
``` php
return xml(['data'=>$data,'code'=>1,'message'=>'操作完成']);
```

### 模板渲染
``` php
return view();
```

## 模板
### 请求参数 
``` php
{$Request.get.id}
{$Request.param.name}
```
- 使用函数 {$data.name|md5}
- 默认值 {$Think.get.name|default="名称为空"}
- 运算符 {$user['score']+myFun($user['level'])} //正确的
- 包含文件 {include file="public/header" /} // 包含头部模版header

### 标签

| 标签名 |       作用       |           包含属性            |
| :----: | :--------------: | :---------------------------: |
| volist | 循环数组数据输出 | name,id,offset,length,key,mod |
|  for   |   循环数据输出   |   name,from,to,before,step    |

支持输出查询结果中的部分数据,例如输出其中的第5~15条记录
``` php
{volist name="list" id="vo" offset="5" length='10'}
{$vo.name}
{/volist}
```
输出偶数记录
``` php
{volist name="list" id="vo" mod="2" }
{eq name="mod" value="1"}{$vo.name}{/eq}
{/volist}
```
``` php
{for start="开始值" end="结束值" comparison="" step="步进值" name="循环变量名" }
{/for}

```
Case标签还有一个break属性,表示是否需要break,默认是会自动添加break,如果不要break,可以使用:
``` php
{switch name="Think.get.userId|abs"}
{case value="1" break="0"}admin{/case}
{case value="2"}admin{/case}
{default /}default
{/switch}
```

``` php
{between name="Think.post.id" value="1,5"}
输出内容1
{/between}
```

### url
``` html
{:url('aaa/bbb?id='.$vo.id)}
{:url('aaa/bbb',array('id'=>$vo.id))}
{:url('admin/group')}?id={$vo['id']}
```
## 验证

ThinkPHP5.0验证使用独立的\think\Validate类或者验证器进行验证
### 独立验证
任何时候，都可以使用Validate类进行独立的验证操作，例如：
``` php
$validate = new Validate([
    'name'  => 'require|max:25',
    'email' => 'email'
]);
$data = [
    'name'  => 'thinkphp',
    'email' => 'thinkphp@qq.com'
];
if (!$validate->check($data)) {
    dump($validate->getError());
}
```
### 验证器 (推荐方式)
这是扩展的方式，继承独立验证的功能，使得控制器内代码更少

``` php
namespace app\index\validate;

use think\Validate;

class User extends Validate
{
    protected $rule = [
        'name'  =>  'require|max:25',
        'email' =>  'email',
    ];

}
```
在需要进行User验证的地方，添加如下代码即可：
``` php
$data = [
    'name'=>'thinkphp',
    'email'=>'thinkphp@qq.com'
];

$validate = Loader::validate('User');

if(!$validate->check($data)){
    dump($validate->getError());
}
```
使用助手函数实例化验证器
``` php
$validate = validate('User');
```

> 验证 :在编辑修改的页面验证时，提交自身数据会提示数据重复

解决方法：
在编辑页面表单把主键id也作为数据传入到验证器中(name要和主键同名)。如
``` html
    <input type="hidden" name="row[id]" value="{$row.shopname|htmlentities}">
```
### 设置验证规则
## 安全
### 输入安全
### 上传安全 
### 文件上传
### 杂项
#### 缓存
Cache::set('name',$value,3600);

#### session
Session::set('name','thinkphp');
Session::get('name');

支持指定 Session 驱动,配置文件如下:
``` php
'session' => [
    'prefix' => 'module',
    'type' => 'redis',
    'auto_start' => true,
    // redis主机
    'host' => '127.0.0.1',
    // redis端口
    'port' => 6379,
    // 密码
    'password' => '',
]
 ```

``` php
// cookie初始化
Cookie::init(['prefix'=>'think_','expire'=>3600,'path'=>'/']);
// 指定当前前缀
Cookie::prefix('think_');

 ```

支持的参数及默认值如下:

``` php
// cookie 名称前缀
'prefix' => '',
// cookie 保存时间
'expire' => 0,
// cookie 保存路径
'path' => '/',
// cookie 有效域名
'domain' => '',
// cookie 启用安全传输
'secure' => false,
// httponly设置
'httponly' => '',
// 是否使用 setcookie
'setcookie' => true,
```

助手函数
系统也提供了助手函数session完成相同的功能，例如：

``` php
// 初始化session
session([
    'prefix'     => 'module',
    'type'       => '',
    'auto_start' => true,
]);

// 赋值（当前作用域）
session('name', 'thinkphp');

// 赋值think作用域
session('name', 'thinkphp', 'think');

// 判断（当前作用域）是否赋值
session('?name');

// 取值（当前作用域）
session('name');

// 取值think作用域
session('name', '', 'think');

// 删除（当前作用域）
session('name', null);

// 清除session（当前作用域）
session(null);

// 清除think作用域
session(null, 'think');
```
#### 多语言

``` php
// 开启语言切换
'lang_switch_on' => true,
```

如果在自动侦测语言的时候,希望设置允许的语言列表,不在列表范围的语言则仍然使用默认语言,可以使用:
``` php
// 设置允许的语言
Lang::setAllowLangList(['zh-cn','en-us']);
```

#### 分页
Thinkphp5 内置了分页对象。

``` php
// 查询状态为1的用户数据 并且每页显示10条数据
$list = Db::name('user')->where('status',1)->paginate(10);
// 把分页数据赋值给模板变量list
$this->assign('list', $list);
// 渲染模板输出
return $this->fetch();
```

返回值的分页对象:
```
[total] => 18
[per_page] => 10
[current_page] => 1
[last_page] => 2
[data] => Array()
```

也可以改成模型的分页查询代码:
``` php
// 查询状态为1的用户数据 并且每页显示10条数据
$list = User::where('status',1)->paginate(10);
// 获取总记录数
$count = $list->total();
// 把分页数据赋值给模板变量list
$this->assign('list', $list);
// 渲染模板输出
return $this->fetch();
```
模板文件中分页输出代码如下:
``` html
<div>
<ul>
{volist name='list' id='user'}
<li> {$user.nickname}</li>
{/volist}
</ul>
</div>
{$list->render()}
```

可以修改样式
``` html
<ul class="pagination">
<li><a href="?page=1">&laquo;</a></li>
<li><a href="?page=1">1</a></li>
<li class="active"><span>2</span></li>
<li class="disabled"><span>&raquo;</span></li>
</ul>

```

分页后数据处理 
``` php
$list = Db::name('user')->where('status',1)->paginate()->each(function($item, $key){$item['nickname'] = 'think'; return $item; });
```

如果要配置分页参数，可以总的配置

| 参数      | 描述        |
| --------- | ----------- |
| list_rows | 每页数量    |
| page      | 当前页      |
| path      | url路径     |
| query     | url额外参数 |
| fragment  | url锚点     |
| var_page  | 分页变量    |
| type      | 分页类名    |

```php
//分页配置
'paginate'               => [
    'type'     => 'bootstrap',
    'var_page' => 'page',
],
```
type属性支持命名空间，例如：
```php
'type'     => '\org\page\bootstrap',
```

也可以在调用分页方法的时候传入，例如：
```php
$list = Db::name('user')->where('status',1)->paginate(10,true,[
    'type'     => 'bootstrap',
    'var_page' => 'page',
    'page' =>3  //指定第几页
]);
```
#### 文件上传

``` html
<form action="/index/index/upload" enctype="multipart/form-data" method="post">
<input type="file" name="image" /> <br>
<input type="submit" value="上传" />
</form>
```

控制器:
``` php
public function upload(){
// 获取表单上传文件 例如上传了001.jpg
$file = request()->file('image');

// 移动到框架应用根目录/public/uploads/ 目录下
if($file){
$info = $file->move(ROOT_PATH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 输出 jpg
echo $info->getExtension();
// 输出 20160820/42a79759f284b767dfcb2a0197904287.jpg
echo $info->getSaveName();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}else{
// 上传失败获取错误信息
echo $file->getError();
}
}
```
move 方法成功的话返回的是一个 \think\File 对象,你可以对上传后的文件进行后续操作。


#### 多文件上传

``` html
<form action="/index/index/upload" enctype="multipart/form-data" method="post">
<input type="file" name="image[]" /> <br>
<input type="file" name="image[]" /> <br>
<input type="file" name="image[]" /> <br>
<input type="submit" value="上传" />
</form>

```

``` php
public function upload(){
// 获取表单上传文件
$files = request()->file('image');
foreach($files as $file){
// 移动到框架应用根目录/public/uploads/ 目录下
$info = $file->move(ROOT_PATH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 输出 jpg
echo $info->getExtension();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}else{
// 上传失败获取错误信息
echo $file->getError();
}
}
}

```

#### 上传验证
``` php
$info = $file->validate(['size'=>15678,'ext'=>'jpg,png,gif'])->move(ROOT_PA
TH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 输出 jpg
echo $info->getExtension();
// 输出 20160820/42a79759f284b767dfcb2a0197904287.jpg
echo $info->getSaveName();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}
```

#### 上传规则

默认情况下,会在上传目录下面生成以当前日期为子目录,以微秒时间的 md5 编码为文件名的文件,例如上面

生成的文件名可能是:
/home/www/upload/20160510/42a79759f284b767dfcb2a0197904287.jpg

我们可以指定上传文件的命名规则,使用 rule 方法即可,例如:
``` php
// 获取表单上传文件 例如上传了001.jpg
$file = request()->file('image');
// 移动到服务器的上传目录 并且使用md5规则
$file->rule('md5')->move('/home/www/upload/');
```

| 规则 | 描述                        |
|------+-----------------------------|
| date | 根据日期和微秒数生成        |
| md5  | 对文件使用md5_file散列生成  |
| sha1 | 对文件使用sha1_file散列生成 |

rule 后可自定义函数调用

#### 验证码

模版内验证码的显示

``` html+php
<div>{:captcha_img()}</div>
```

或者

``` html
<div><img src="{:captcha_src()}" alt="captcha" /></div>
```

验证

``` php
$this->validate($data,[
'captcha|验证码'=>'require|captcha'
]);
```
或者手动验证
``` php
if(!captcha_check($captcha)){
//验证失败
};
```

### 图像处理
#### 打开图像
``` php
$image = \think\Image::open('./image.png');
//也可以从直接获取当前请求中的文件上传对象,例如:
$image = \think\Image::open(request()->file('image'));
```

#### 获取图像信息
``` php

$image = \think\Image::open('./image.png');
// 返回图片的宽度
$width = $image->width();
// 返回图片的高度
$height = $image->height();
// 返回图片的类型
$type = $image->type();
// 返回图片的mime类型
$mime = $image->mime();
// 返回图片的尺寸数组 0 图片宽度 1 图片高度
$size = $image->size();
```

#### 裁剪图像
``` php
$image->crop(300, 300)->save('./crop.png');
//支持从某个坐标开始裁剪,例如下面从(100,30)开始裁剪,
$image->crop(300, 300,100,30)->save('./crop.png');
```

``` php
//缩略图
$image->thumb(150, 150)->save('./thumb.png');
// 按照原图的比例生成一个最大为150*150的缩略图并保存为thumb.png
$image->thumb(150,150,\think\Image::THUMB_CENTER)->save('./thumb.png');

//图像翻转
// 对图像进行以y轴进行翻转操作
$image->flip(\think\image::FLIP_Y)->save('./filp_image.png');

//图像旋转
// 对图像使用默认的顺时针旋转90度操作
$image->rotate()->save('./rotate_image.png');

//添加水印
// 给原图左上角添加水印并保存water_image.png，透明度 50%
$image->water('./logo.png',\think\Image::WATER_NORTHWEST,50)->save('water_image.pn
g');
//文字水印
// 给原图左上角添加水印并保存water_image.png
$image->text('十年磨一剑 - 为API开发设计的高性能框架','HYQingKongTiJ.ttf',20,'#ffffff')->save('text_image.png');

```

### 命令行 php think
- clear
- make:controller  index/Blog    [生成index 模块的 Blog 控制器类库文件]
- make:model

### 部署
#### 修改入口文件

``` php
// 应用目录
define('APP_PATH', __DIR__.'/apps/');
// 加载框架引导文件
require './thinkphp/start.php';
```

#### URL重写

[Apache]

``` apache
<IfModule mod_rewrite.c>
Options +FollowSymlinks -Multiviews
RewriteEngine on
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ index.php?/$1 [QSA,PT,L]
</IfModule>

```

[Nginx]
``` c
location / { // .....省略部分代码
if (!-e $request_filename) {
rewrite ^(.*)$ /index.php?s=/$1
 last;
break;
}
}

```
(/  3600 24)

### 设置session 时间
> ROOT\application\config.php

添加个字段  expire

``` php

 'session'                => [
        'id'             => '',
        // SESSION_ID的提交变量,解决flash上传跨域
        'var_session_id' => '',
        // SESSION 前缀
        'prefix'         => 'think',
        // 驱动方式 支持redis memcache memcached
        'type'           => '',
        // 是否自动开启 SESSION
        'auto_start'     => true,
        //设置session 时间
        'expire'             => 86400,  
        
        //3600 1小时
    ],
```
### redis
```php
use think\cache\driver\Redis;
$redis = new Redis;
$redis->set("name", "阿明");
```
### sql 日志

第一步：在Database.php文件中将数据库debug设置为true，（默认是true）
``` php
// 数据库调试模式
'debug'           => true,
```
第二步：在Config.php文件中写如下代码

``` php
  'log' => [
        // 日志记录方式，内置 file socket 支持扩展
        'type'  => 'File',
        // 日志保存目录
        'path'  => LOG_PATH,
        // 日志记录级别
        'level' => ['sql'],
    ],
```
一班这样设置之后就可以开启SQL日志记录了。

=======
---
title: ThinkPHP5.0完全开发手册
permalink: thinkphp5.html
theme: jekyll-theme-cayman
---

ThinkPHP是一个WEB开发框架，包含了路由、日志、异常、模型、数据库、模板引擎和验证等模块。

文档 http://static.kancloud.cn/manual/thinkphp5/118003

## 基础

### 项目目录

- application 应用目录
- extend 扩展类库目录
- public web部署目录
- -static 静态资源目录
- -index.php 应用入口
- runtime 应用运行时目录
- vendor 第三方类库
- thinkphp 框架系统目录

## 架构

入口文件 -> 转到应用 -> 判断模块 -> 调用控制器 -> 执行操作 -> 连接模型 -> 视图组装 -> 响应输出

## 命名空间

### 引用内置或没命名空间类库
> 需要在类库的前面加上 \ 

```php
// 错误的用法
$class = new stdClass();
$xml = new SimpleXmlElement($xmlstr);
// 正确的用法
$class = new \stdClass();
$xml = new \SimpleXmlElement($xmlstr);
```

### 引用有命名空间
``` php
$class = new \think\cache\driver\File();
```

## 配置

> 配置目录默认在 application 目录下

```php
// 定义配置文件目录和应用目录同级
define('CONF_PATH', __DIR__.'/../config/');
``` 

- config.php 应用配置
- database.php 数据库配置
- route.php 路由配置
- .env 环境变量配置

在ThinkPHP中，一般来说应用的配置文件是自动加载的，加载的顺序是：
> 惯例配置->应用配置->扩展配置->场景配置->模块配置->动态配置

``` php
use think\facade\Config;
// 设置配置参数
Config::set([
    'type'      =>  'file',
    'prefix'    =>  'think'
],'cache');
Config::set($config);
// 读取二级配置参数
echo Config::get('user.type');
  //获取所有配置内容，返回的是个Array
    dump(Config::get());
    //获取app中的配置内容，返回的是个Array
    dump(Config::get('app.'));
    //获取app中的配置内容，返回的是个Array
    dump(Config::pull('app'));
    //获取app中的debug中的配置内容
    dump(Config::get('app.app_debug'));
 //判断template下的type项是否存在，返回true或者false
    dump(Config::has('template.type'));
```

助手函数
``` php
 // 获取配置
    dump(config('database.hostname'));
    // 用'?'判断配置是否存在
    dump(config('?database.hostname'));
    // 设置配置
    config('database.hostname','localhost');
    // 获取配置
    dump(config('database.hostname'));
```
### .env 配置
```
数组
[app]
DEBUG = true

等价于
APP_DEBUG = true
忽略大小写
```

## 路由管理
路由的用途是简化URL访问地址

通过 \think\Route 对HTTP协议中的 URL  进行管理。

关闭路由模式
``` php
'url_route_on'  =>  false,
``` 

### 默认路由规则

- 多模块 
  - http://server/module/controller/action/param/value/
  - 或者 http://server?s=/module/controller/action/param/value/

- 单模块
  - http://server/controller/action/param/value/

命名空间也要修改

### 自定义规则
``` php
Route::get('/',function(){ return 'Hello,world!'; }); //首页规则
Route::get('new/:id','News/read'); // 定义GET请求路由规则
Route::get('new/:id','News/read'); // 定义GET请求路由规则
Route::post('new/:id','News/update'); // 定义POST请求路由规则
Route::put('new/:id','News/update'); // 定义PUT请求路由规则
Route::delete('new/:id','News/delete'); // 定义DELETE请求路由规则
Route::any('new/:id','News/read'); // 所有请求都支持的路由规则
```


## 控制器

控制器文件的命名规范是 : 首字母需要大写，如果是两个单词的组合，如 HelloWorld ，则 URL 为 hello_world

```php
namespace application\index\controller;

class Index 
{
    public function index()
    {
        return 'index';
    }
}
```

``` php
// 是否自动转换URL中的控制器和操作名
'url_convert'            => true,
```
### 初始化
```php
  public function _initialize()
    {
        echo 'init<br/>';
    }
```

### 前置操作
可以为某个操作指定前置操作，只要设置 **beforeActionList** 属性，键名为需要调用的前置方法名，无值的话为当前控制器下所有方法的前置方法。

``` php
protected $beforeActionList = [
        'first',
        'second' =>  ['except'=>'hello'],
        'three'  =>  ['only'=>'hello,data'],
    ];
    
```
['except' => '方法名,方法名'] 表示这些方法不使用前置方法
['only' => '方法名,方法名'] 表示只有这些方法使用前置方法

解释: 任何方法要调用 first 方法， second 方法除了 hello方法，都会调用

### 跳转和重定向

``` php
//设置成功后跳转页面的地址,默认的返回页面是$_SERVER['HTTP_REFERER']
$this->success('新增成功', 'User/list');

//错误页面的默认跳转页面是返回前一页,通常不需要设置 javascript:history.back(-1);
$this->error('新增失败');

//重定向到News模块的Category操作
$this->redirect('News/category', ['cate_id' => 2]);

```
### 空操作
空操作是指系统在找不到指定的操作方法的时候,会定位到空操作( _empty )方法来执行,利用这个机制,
我们可以实现错误页面和一些URL的优化。

### 空控制器
class Error

### 自动定位
``` php
 public function index()
    {
        return $this->fetch();
    }
    
    public function add()
    {
        return $this->fetch();
    }
    
    public function edit($id)
    {
        return $this->fetch('edit:'.$id);
    } 
```

## 请求 \think\Request
### 请求信息
要获取当前的请求信息，可以使用\think\Request 类 Request::instance() 或者助手函数 request()

#### 获取URL信息


``` php
$request = Request::instance();
// 获取当前域名
echo 'domain: ' . $request->domain() . '<br/>';
// 获取当前入口文件
echo 'file: ' . $request->baseFile() . '<br/>';
$request->param()
// 获取当前URL地址 不含域名
echo 'url: ' . $request->url() . '<br/>';
// 获取包含域名的完整URL地址
echo 'url with domain: ' . $request->url(true) . '<br/>';
// 获取当前URL地址 不含QUERY_STRING
echo 'url without query: ' . $request->baseUrl() . '<br/>';
// 获取URL访问的ROOT地址
echo 'root:' . $request->root() . '<br/>';
// 获取URL访问的ROOT地址
echo 'root with domain: ' . $request->root(true) . '<br/>';
// 获取URL地址中的PATH_INFO信息
echo 'pathinfo: ' . $request->pathinfo() . '<br/>';
// 获取URL地址中的PATH_INFO信息 不含后缀
echo 'pathinfo: ' . $request->path() . '<br/>';
// 获取URL地址中的后缀信息
echo 'ext: ' . $request->ext() . '<br/>';
```
#### 设置/获取 模块/控制器/操作名称
```php
$request = Request::instance();
echo "当前模块名称是" . $request->module();
echo "当前控制器名称是" . $request->controller();
echo "当前操作名称是" . $request->action();
```
#### 获取请求参数
```php
$request = Request::instance();
echo '请求方法：' . $request->method() . '<br/>';
echo '资源类型：' . $request->type() . '<br/>';
echo '访问ip地址：' . $request->ip() . '<br/>';
echo '是否AJax请求：' . var_export($request->isAjax(), true) . '<br/>';
echo '请求参数：';
dump($request->param());
echo '请求参数：仅包含name';
dump($request->only(['name']));
echo '请求参数：排除name';
dump($request->except(['name']));
```
#### 获取路由和调度信息
```php
$request = Request::instance();
echo '路由信息：';
dump($request->route());
echo '调度信息：';
dump($request->dispatch());
```
#### 设置请求信息
如果某些环境下面获取的请求信息有误，可以手动设置这些信息参数，使用下面的方式：
```php
$request = Request::instance();
$request->root('index.php');
$request->pathinfo('index/index/hello');
```

### 输入变量
可以通过 Request 对象完成对全局输入变量的检测、获取和安全过滤。支持包括 $_GET、$_POST、$_REQUEST、$_SERVER、$_SESSION、$_COOKIE、$_ENV 等系统变量，以及文件上传的信息。

#### 检测变量是否设置
```php
Request::instance()->has('id','get');
Request::instance()->has('name','post');
```
或者使用助手函数
```php
input('?get.id');
input('?post.name');
```
#### 变量获取
语法: 变量类型方法('变量名/变量修饰符','默认值','过滤方法')

变量类型方法包括：

| 方法    | 描述                           |
| ------- | ------------------------------ |
| param   | 获取当前请求的变量 (推荐)      |
| get     | 获取 $_GET 变量                |
| post    | 获取 $_POST 变量               |
| put     | 获取 PUT 变量                  |
| delete  | 获取 DELETE 变量               |
| session | 获取 $_SESSION 变量            |
| cookie  | 获取 $_COOKIE 变量             |
| request | 获取 $_REQUEST 变量            |
| server  | 获取 $_SERVER 变量             |
| env     | 获取 $_ENV 变量                |
| route   | 获取 路由（包括PATHINFO） 变量 |
| file    | 获取 $_FILES 变量              |


##### 获取PARAM变量
PARAM变量是框架提供的用于自动识别 GET、POST或者PUT 请求的一种方式，系统推荐

```php
// 获取当前请求的name变量
Request::instance()->param('name');
// 获取当前请求的所有变量（经过过滤）
Request::instance()->param();
// 获取当前请求的所有变量（原始数据）
Request::instance()->param(false);
// 获取当前请求的所有变量（包含上传文件）
Request::instance()->param(true);
```
助手函数:
```php
input('param.name');
input('param.');
或者
input('name');
input('');
```

获取 cookie 或 session
```php
Request::instance()->session('user_id'); // 获取某个session变量
input('cookie.user_id');
input('cookie.');// 获取全部的cookie变量
```

#### 变量过滤
> 框架默认没有设置过滤规则，可以自己设置
```php
// 默认全局过滤方法 用逗号分隔多个
'default_filter'         => 'htmlspecialchars',
```

使用 filter方法进行过滤，支持设置多个过滤方法，例如：
```php
Request::instance()->filter(['strip_tags','htmlspecialchars']),
```

也可以在获取变量的时候添加过滤方法，如:
``` php
Request::instance()->get('name','','htmlspecialchars'); // 获取get变量 并用htmlspecialchars函数过滤
Request::instance()->param('username','','strip_tags'); // 获取param变量 并用strip_tags函数过滤
Request::instance()->post('name','','org\Filter::safeHtml'); // 获取post变量 并用org\Filter类的safeHtml方法过滤

Request::instance()->param('username','','strip_tags,strtolower'); // 获取param变量 并依次调用strip_tags、strtolower函数过滤
Request::instance()->post('email','','email');
```
#### 获取部分变量
```php
// 只获取当前请求的id和name变量
Request::instance()->only(['id','name']);
```
#### 排除部分变量
```php
// 排除GET请求的id和name变量
Request::instance()->except(['id','name'],'get');
```
#### 变量修饰符
语法：input('变量类型.变量名/修饰符');
```php
input('get.id/d');
input('post.name/s');
input('post.ids/a');
```
| 修饰符 | 作用                 |
| ------ | -------------------- |
| s      | 强制转换为字符串类型 |
| d      | 强制转换为整型类型   |
| b      | 强制转换为布尔类型   |
| a      | 强制转换为数组类型   |
| f      | 强制转换为浮点类型   |

注意：如果你要获取的数据是数组，请一定要加上 /a 修饰符

#### 更改变量
```php
// 更改GET变量
Request::instance()->get(['id'=>10]);
```
注意：param 会无效
```php
//此方法无效
Request::instance()->param(['id'=>10]);
```
### 请求类型
#### 获取请求类型
```php
// 是否为 GET 请求
if (Request::instance()->isGet()) echo "当前为 GET 请求";
```

助手函数
```php
// 是否为 GET 请求
if (request()->isGet()) echo "当前为 GET 请求";
```
### HTTP头信息
```php
$info = Request::instance()->header();
echo $info['accept'];
echo $info['accept-encoding'];
echo $info['user-agent'];
```
### 方法注入
如果你需要在Request请求对象中添加自己的方法
```php
// 通过hook方法注入动态方法
Request::hook('user','getUserInfo');
```
getUserInfo函数定义如下

```php
function getUserInfo(Request $request, $userId)
{
    // 根据$userId获取用户信息
    return $info;
}
```
接下来，我们可以直接在控制器中使用：

```php
public function index()
{
    $info = Request::instance()->user($userId);
}
```
### 属性注入
```php
// 动态绑定属性
Request::instance()->bind('user',new User);
// 或者使用
Request::instance()->user = new User;
```
获取绑定的属性使用下面的方式：
```php
Request::instance()->user;
// 或者
request()->user;
```
### 参数绑定
方法的参数绑定是把URL地址（或者路由地址）中的变量作为操作方法的参数直接接入。

#### 操作方法参数绑定
##### 按名称绑定

方法的定义方式:
```php
//此参数没默认值，那参数值必填
 public function read($id)
 public function archive($year='2016',$month='01')
```
URL访问地址为：
```
http://serverName/index.php/index/blog/read/id/5
//参数顺序可变
http://serverName/index.php/index/blog/archive/year/2016/month/06
```
可以配置参数顺序是否严格：
```
// URL参数方式改成顺序解析
'url_param_type'         => 1,
```
### 依赖注入（用于控制器）
可在控制器的构造函数或者操作方法（指访问请求的方法）中类型声明任何（对象类型）依赖，这些依赖会被自动解析并注入到控制器实例或方法中。
#### 自动注入请求对象
##### 架构方法注入
在控制器的架构方法中会自动注入当前请求对象，例如：
```php
namespace app\index\controller;

use think\Request;

class Index
{
	protected $request;
    
	public function __construct(Request $request)
    {
    	$this->request = $request;
    }
    
    public function hello()
    {
        return 'Hello,' . $this->request->param('name') . '！';
    }
    
}
```

##### 操作方法注入
方法中如需调用 Request,可定义 Request 参数，无关顺序
```php
  public function hello(Request $request)
    {
        return 'Hello,' . $request->param('name') . '！';
    }
```
如继承 Controller类，可以直接调用
```php
use think\Controller;

class Index extends Controller
{
    public function hello()
    {
        return 'Hello,'.$this->request->param('name');
    }
    
}
```

## 数据库

### 连接数据库
ThinkPHP 内置了抽象抽象数据库访问层，把不同的数据库操作封装起来，我们只需要使用公共的Db类进行操作，而无需针对不同的数据库写不同的代码和底层实现,Db类会自动调用相应的数据库驱动来处理。包含了对 Mysql ,SqlServer,PgSQL, Sqlite 等数据库的支持.

如果要使用数据库，需要先进行连接信息的配置，有多种配置方式
#### 1.使用配置文件 database.php
```php
return [
    // 数据库类型
    'type'        => 'mysql',
    // 下面表示数据库的连接器采用 \org\db\Mysql 类作为数据库连接驱动
    'type'        => '\org\db\Mysql',
    // 数据库连接DSN配置
    'dsn'         => '',
    // 服务器地址
    'hostname'    => '127.0.0.1',
    // 数据库名
    'database'    => 'thinkphp',
    // 数据库用户名
    'username'    => 'root',
    // 数据库密码
    'password'    => '',
    // 数据库连接端口
    'hostport'    => '',
    // 数据库连接参数
    'params'      => [],
    // 数据库编码默认采用utf8
    'charset'     => 'utf8',
    // 数据库表前缀
    'prefix'      => 'think_',
    // 数据库调试模式
    'debug'       => false,
    // 数据库部署方式:0 集中式(单一服务器),1 分布式(主从服务器)
    'deploy'      => 0,
    // 数据库读写是否分离 主从式有效
    'rw_separate' => false,
    // 读写分离后 主服务器数量
    'master_num'  => 1,
    // 指定从服务器序号
    'slave_no'    => '',
    // 是否严格检查字段是否存在
    'fields_strict'  => true,    
];
```

每个模块可以设置独立的数据库连接参数，并且相同的配置参数无需重复设置，例如，我们可以在admin模块的database.php 配置文件中定义：
```php
return [
    // 服务器地址
    'hostname'    => '192.168.1.100',
    // 数据库名
    'database'    => 'admin',    
];
```

表示 amin 模块的数据库使用上面的配置。
从v5.0.6开始，支持mysql的断线重连机制 

``` php
//开启断线重连
'break_reconnect' =>true,
```


#### 2.方法配置
我们可以在调用 Db类的时候动态定义连接信息，如
```php
Db::connect([
    // 数据库类型
    'type'        => 'mysql',
    // 数据库连接DSN配置
    'dsn'         => '',
    // 服务器地址
    'hostname'    => '127.0.0.1',
    // 数据库名
    'database'    => 'thinkphp',
    // 数据库用户名
    'username'    => 'root',
    // 数据库密码
    'password'    => '',
    // 数据库连接端口
    'hostport'    => '',
    // 数据库连接参数
    'params'      => [],
    // 数据库编码默认采用utf8
    'charset'     => 'utf8',
    // 数据库表前缀
    'prefix'      => 'think_',
]);
```
或者使用字符串方式:
``` php
Db::connect('mysql://root:1234@127.0.0.1:3306/thinkphp#utf8');
```
字符串连接的定义格式为:  
数据库类型://用户名:密码@数据库地址:数据库端口/数据库名#字符集


### 基本使用(原生写法)
可以直接使用数据库原生SQL操作，支持 query(查询操作)和 excute(写入操作)方法，并且支持参数绑定

``` php
//使用参数绑定
Db::query('select * from think_user where id=?',[8]);
//使用命名占位符
Db::query('select * from think_user where id=:id',['id'=>8]);
Db::execute('insert into think_user (id, name) values (:id, :name)',['id'=>8,'n
ame'=>'thinkphp']);
```

可以使用多个数据库连接
``` php
Db::connect($config)->query('select * from think_user where id=:id',['id'=>8]);
```
$config是一个单独的数据库配置，支持数组和字符串，也可以是数据库连接的配置参数名。

### 查询构造器 (非原生写法)
#### 查询数据
##### 基本查询
查询一个数据使用find，查询数据集使用 select;
``` php
// table方法必须指定完整的数据表名
Db::table('think_user')->where('id',1)->find();
Db::name('user')->where('id',1)->find();
```

###### 主从查询
如果你使用了分布式数据库，默认都是在从数据库进行查询，如果你在一些特殊情况下需要从主库查询，可以：
``` php
Db::name('user')->master()->where('id',1)->find();
```

如果你想处理  一旦某个表写入了数据，那么当前请求的后续查询都自动从主库读取。
可以配置:
```php
// 从主库读取数据
'read_master'	=>	true,
```
或者使用方法 readMaster
```php
$data = ['foo' => 'bar', 'bar' => 'foo'];
Db::table('think_user')
	->readMaster(true)
    ->insert($data);
// 后续所有数据表的查询都会走主库
```

###### 助手函数
```php
db('user')->where('id',1)->find();
```
注意：使用db助手函数默认每次都会重新连接数据库,而使用 Db::name 或 Db::table 的话都是单例的。 db 函数如果需要采用相同的链接，可以传入第三个参数:
``` php
db('user',[],false)->where('id',1)->find();
```
就可以使用同一个数据库连接，第二个参数是数据库的连接参数，留空表示采用数据库配置文件的配置。
注意：5.0.9 后 db 助手不再默认强制重新连接

###### 值和列查询
```php
// 返回某个字段的值
Db::table('think_user')->where('id',1)->value('name');
// 返回数组
Db::table('think_user')->where('status',1)->column('name');
// 指定索引
Db::table('think_user')->where('status',1)->column('name','id');
```

###### 数据集分批处理
对于大量的数据，可以考虑 chunk 方法，该方法一次获取结果集的一小块，然后填充每一小块数据到要处理的闭包，处理大量数据库记录时非常有用。

比如，我们对用户表进行分批处理，每次处理100个用户记录：

```php
Db::table('user')->chunk(100,function($users){
foreach($users as $user){
    //
}
});

//或者交给回调方法myUserIterator处理
Db::table('user')->chunk(100, 'myUserIterator');
```

可以通过在闭包函数中返回 false 来中止对数据集的处理
```php
Db::table('think_user')->chunk(100, function($users) {
    // 处理结果集...
    return false;
});
```
也支持在 chunk 方法之前调用其它查询方法。
```php
Db::table('think_user')->where('score','>',80)->chunk(100, function($users) {
```

chunk方法的处理默认是根据主键查询，但支持指定处理数据的顺序。
```php
Db::table('think_user')->chunk(100, function($users) {
    // 处理结果集...
    return false;
},'create_time', 'desc');
```
##### JSON类型数据查询
```php
// 查询JSON类型字段 （info字段为json类型）
Db::table('think_user')->where('info$.email','thinkphp@qq.com')->find();
```
#### 添加/更新/删除 数据

添加一条数据
```php
Db::name('user')->insert($data);
```

- insert / insertGetId($data) /insertAll($data)
- update/setInc('field',value,time)/setDec/
- delete

延时更新

setInc/setDec支持延时更新，如果需要延时更新则传入第三个参数
下例中延时10秒，给score字段增加1
```php
Db::table('think_user')->where('id', 1)->setInc('score', 1, 10);
```

删除数据
```php
// 根据主键删除
Db::table('think_user')->delete(1);
// 条件删除    
Db::table('think_user')->where('id',1)->delete();
```
### 查询方法
#### 条件查询 where 与 whereOr
``` php
->where('name&title','like','%thinkphp')
->whereOr('title','like','%thinkphp')
->where('name|title','like','%thinkphp')
```

#### 混合查询 (where 与 whereOr混合使用在复杂场景下)
``` php
$result = Db::table('think_user')->where(function ($query) {
$query->where('id', 1)->whereor('id', 2);
})->whereOr(function ($query) {
$query->where('name', 'like', 'think')->whereOr('name', 'like', 'thinkphp');
})->select();
```
生成的sql 语句为：
```mysql
SELECT * FROM `user` WHERE (
 `id` = 1 OR `id` = 2 ) OR (
 `name` LIKE '
think' OR `name` LIKE 'thinkphp' )
```

#### getTableInfo 获取表的信息
``` php 
// 获取`think_user`表所有信息
Db::getTableInfo('think_user');
// 获取`think_user`表所有字段
Db::getTableInfo('think_user', 'fields');
// 获取`think_user`表所有字段的类型
Db::getTableInfo('think_user', 'type');
// 获取`think_user`表的主键
Db::getTableInfo('think_user', 'pk');
```
### 查询语法
#### 查询表达式
``` php
where('id','between','1,8');
$map['id'] = array('not between','1,8');
where('id','not in','1,5,8');
where('name','not null');
where('id','exp',' IN (1,3,8) ');
// 正确 推荐写法
$model->whereExp('id', '>score')->find();
```
### 链式操作(连贯操作)

| 连贯操作      | 作用                                 |
| ------------- | ------------------------------------ |
| where*        | 用于AND查询                          |
| whereOr*      | 用于OR查询                           |
| wheretime*    | 用于时间日期的快捷查询               |
| table         | 用于定义要操作的数据表名称           |
| alias         | 用于给当前数据表定义别名             |
| field*        | 用于定义要查询的字段（支持字段排除） |
| order*        | 用于对结果排序                       |
| limit         | 用于限制查询结果数量                 |
| page          | 用于查询分页（内部会转换成limit）    |
| group         | 用于对查询的group支持                |
| having        | 用于对查询的having支持               |
| join*         | 用于对查询的join支持                 |
| union*        | 用于对查询的union支持                |
| view*         | 用于视图查询                         |
| distinct      | 用于查询的distinct支持               |
| lock          | 用于数据库的锁机制                   |
| cache         | 用于查询缓存                         |
| relation*     | 用于关联查询                         |
| with*         | 用于关联预载入                       |
| bind*         | 用于数据绑定操作                     |
| comment       | 用于SQL注释                          |
| force         | 用于数据集的强制索引                 |
| master        | 用于设置主服务器读取数据             |
| strict        | 用于设置是否严格检测字段名是否存在   |
| sequence      | 用于设置Pgsql的自增序列名            |
| failException | 用于设置没有查询到数据是否抛出异常   |
| partition     | 用于设置分表信息                     |


所有的连贯操作都返回当前的模型实例对象（this），其中带*标识的表示支持多次调用。
#### field 

``` php
//可以用于合法性写入
Db::table('think_user')->field('title,email,content')->insert($data);

//在 field中还可以使用函数
Db::table('think_user')->field('id,nickname as name,SUM(score)')->select();
```

#### limit
limit 方法主要用于指定查询和操作的数量，特别是在分页查询的时候。

##### 限制结果数量
```php
->limit(10)
```

##### 分页查询
```php
Db::table('think_article')->limit('10,25')->select();
//或者 ->limit(10,25)
```
表示查找从第10行开始的25条数据

#### page
page 方法是为分页查询而创建的一个人性化操作的方法。

``` php
// 查询第一页数据，page的第一个参数指定页号，比limit更人性
Db::table('think_article')->page('1,10')->select();

```

获取总页数 totalPages

### group

``` php
Db::table('think_user')
->field('user_id,username,max(score)')
->group('user_id')
->select();
```

### having
``` php
Db::table('think_user')
->field('username,max(score)')
->group('user_id')
->having('count(test_time)>3')
->select();
```

### cache
``` php
Db::table('think_user')->cache(true,60)->find();
// 或者使用下面的方式 是等效的
Db::table('think_user')->cache(60)->find();
```

### 时间
``` php
// 获取今天的博客
Db::table('think_blog') ->whereTime('create_time', 'today')->select();
// 获取昨天的博客
Db::table('think_blog')->whereTime('create_time', 'yesterday')->select();
// 获取本周的博客
Db::table('think_blog')->whereTime('create_time', 'week')->select();
// 获取上周的博客

```
### 子查询
1.构造
``` php
$subQuery = Db::table('think_user')
->field('id,name')
->where('id','>',10)
->buildSql();
```

2. 执行
``` php
Db::table($subQuery.' a')
->where('a.name','like','thinkphp')
->order('id','desc')
->select();
```
闭包构造
``` php
Db::table('think_user')
->where('id','IN',function($query){
$query->table('think_profile')->where('status',1)->field('id');
})
->select();

```
### with 连接两个表

``` php
   $list = $this->model
                ->with('taocan,account')
                ->where($where)
                ->order($sort, $order)
                ->paginate($limit);
                
                //model
  public function account()
    {
        return $this->belongsTo("app\admin\model\ShopAccount"[关联表], "shop_account_id"[主表字段], 'id'[关联字段], [], 'LEFT')->setEagerlyType(0);
    }
                
 $data = [
            'total'     => $r->total(),         // 总记录数
            'cur'       => $r->currentPage(),   // 当前页码
            'size'      => $r->listRows(),      // 每页记录数
            'list'      => $r->items()          // 分页数据
        ];
```

## 模型

``` php
$user = new User;
$user->name = 'thinkphp';
$user->email = 'thinkphp@qq.com';
$user->save();
// 获取自增ID
echo $user->id;
```

删除
``` php
// 删除状态为0的数据
User::destroy(['status' => 0]);

```

获取多个数据
``` php
// 使用数组查询
$list = User::all(['status'=>1]);
// 使用闭包查询
$list = User::all(function($query){
$query->where('status', 1)->limit(3)->order('id', 'asc');
});
foreach($list as $key=>$user){
echo $user->name;
}

```
或者在实例化模型后调用查询方法
``` php
$user = new User();
// 查询数据集
$user->where('name', 'thinkphp')
->limit(10)
->order('id', 'desc')
->select();
 ```

## 视图
``` php
// 渲染模板输出
return $this->fetch('hello',['name'=>'thinkphp']);
return view('hello',['name'=>'thinkphp']);
```

### json 输出
默认类型 'default_return_type'=>'json'

指定 xml类型
``` php
return xml(['data'=>$data,'code'=>1,'message'=>'操作完成']);
```

### 模板渲染
``` php
return view();
```

## 模板
### 请求参数 
``` php
{$Request.get.id}
{$Request.param.name}
```
- 使用函数 {$data.name|md5}
- 默认值 {$Think.get.name|default="名称为空"}
- 运算符 {$user['score']+myFun($user['level'])} //正确的
- 包含文件 {include file="public/header" /} // 包含头部模版header

### 标签

| 标签名 |       作用       |           包含属性            |
| :----: | :--------------: | :---------------------------: |
| volist | 循环数组数据输出 | name,id,offset,length,key,mod |
|  for   |   循环数据输出   |   name,from,to,before,step    |
|        |                  |                               |

支持输出查询结果中的部分数据,例如输出其中的第5~15条记录
``` php
{volist name="list" id="vo" offset="5" length='10'}
{$vo.name}
{/volist}
```
输出偶数记录
``` php
{volist name="list" id="vo" mod="2" }
{eq name="mod" value="1"}{$vo.name}{/eq}
{/volist}
```
``` php
{for start="开始值" end="结束值" comparison="" step="步进值" name="循环变量名" }
{/for}

```
Case标签还有一个break属性,表示是否需要break,默认是会自动添加break,如果不要break,可以使用:
``` php
{switch name="Think.get.userId|abs"}
{case value="1" break="0"}admin{/case}
{case value="2"}admin{/case}
{default /}default
{/switch}
```

``` php
{between name="Think.post.id" value="1,5"}
输出内容1
{/between}
```

### url
``` html
{:url('aaa/bbb?id='.$vo.id)}
{:url('aaa/bbb',array('id'=>$vo.id))}
{:url('admin/group')}?id={$vo['id']}
```
## 验证

ThinkPHP5.0验证使用独立的\think\Validate类或者验证器进行验证。
### 独立验证
任何时候，都可以使用Validate类进行独立的验证操作，例如：
``` php
$validate = new Validate([
    'name'  => 'require|max:25',
    'email' => 'email'
]);
$data = [
    'name'  => 'thinkphp',
    'email' => 'thinkphp@qq.com'
];
if (!$validate->check($data)) {
    dump($validate->getError());
}
```
### 验证器 (推荐方式)
这是扩展的方式，继承独立验证的功能，使得控制器内代码更少

``` php
namespace app\index\validate;

use think\Validate;

class User extends Validate
{
    protected $rule = [
        'name'  =>  'require|max:25',
        'email' =>  'email',
    ];

}
```
在需要进行User验证的地方，添加如下代码即可：
``` php
$data = [
    'name'=>'thinkphp',
    'email'=>'thinkphp@qq.com'
];

$validate = Loader::validate('User');

if(!$validate->check($data)){
    dump($validate->getError());
}
```
使用助手函数实例化验证器
``` php
$validate = validate('User');
```

### 设置验证规则
## 安全
### 输入安全
### 上传安全 


### 文件上传
### 杂项
#### 缓存
Cache::set('name',$value,3600);

#### session
Session::set('name','thinkphp');
Session::get('name');

支持指定 Session 驱动,配置文件如下:
``` php
'session' => [
    'prefix' => 'module',
    'type' => 'redis',
    'auto_start' => true,
    // redis主机
    'host' => '127.0.0.1',
    // redis端口
    'port' => 6379,
    // 密码
    'password' => '',
]
 ```

``` php
// cookie初始化
Cookie::init(['prefix'=>'think_','expire'=>3600,'path'=>'/']);
// 指定当前前缀
Cookie::prefix('think_');

 ```

支持的参数及默认值如下:

``` php
// cookie 名称前缀
'prefix' => '',
// cookie 保存时间
'expire' => 0,
// cookie 保存路径
'path' => '/',
// cookie 有效域名
'domain' => '',
// cookie 启用安全传输
'secure' => false,
// httponly设置
'httponly' => '',
// 是否使用 setcookie
'setcookie' => true,
```

助手函数
系统也提供了助手函数session完成相同的功能，例如：

``` php
// 初始化session
session([
    'prefix'     => 'module',
    'type'       => '',
    'auto_start' => true,
]);

// 赋值（当前作用域）
session('name', 'thinkphp');

// 赋值think作用域
session('name', 'thinkphp', 'think');

// 判断（当前作用域）是否赋值
session('?name');

// 取值（当前作用域）
session('name');

// 取值think作用域
session('name', '', 'think');

// 删除（当前作用域）
session('name', null);

// 清除session（当前作用域）
session(null);

// 清除think作用域
session(null, 'think');
```
#### 多语言

``` php
// 开启语言切换
'lang_switch_on' => true,
```

如果在自动侦测语言的时候,希望设置允许的语言列表,不在列表范围的语言则仍然使用默认语言,可以使用:
``` php
// 设置允许的语言
Lang::setAllowLangList(['zh-cn','en-us']);
```

#### 分页
Thinkphp5 内置了分页对象。

``` php
// 查询状态为1的用户数据 并且每页显示10条数据
$list = Db::name('user')->where('status',1)->paginate(10);
// 把分页数据赋值给模板变量list
$this->assign('list', $list);
// 渲染模板输出
return $this->fetch();
```

返回值的分页对象:
```
[total] => 18
[per_page] => 10
[current_page] => 1
[last_page] => 2
[data] => Array()
```

也可以改成模型的分页查询代码:
``` php
// 查询状态为1的用户数据 并且每页显示10条数据
$list = User::where('status',1)->paginate(10);
// 获取总记录数
$count = $list->total();
// 把分页数据赋值给模板变量list
$this->assign('list', $list);
// 渲染模板输出
return $this->fetch();
```
模板文件中分页输出代码如下:
``` html
<div>
<ul>
{volist name='list' id='user'}
<li> {$user.nickname}</li>
{/volist}
</ul>
</div>
{$list->render()}
```

可以修改样式
``` html
<ul class="pagination">
<li><a href="?page=1">&laquo;</a></li>
<li><a href="?page=1">1</a></li>
<li class="active"><span>2</span></li>
<li class="disabled"><span>&raquo;</span></li>
</ul>

```

分页后数据处理 
``` php
$list = Db::name('user')->where('status',1)->paginate()->each(function($item, $key){$item['nickname'] = 'think'; return $item; });
```

如果要配置分页参数，可以总的配置

| 参数      | 描述        |
| --------- | ----------- |
| list_rows | 每页数量    |
| page      | 当前页      |
| path      | url路径     |
| query     | url额外参数 |
| fragment  | url锚点     |
| var_page  | 分页变量    |
| type      | 分页类名    |

```php
//分页配置
'paginate'               => [
    'type'     => 'bootstrap',
    'var_page' => 'page',
],
```
type属性支持命名空间，例如：
```php
'type'     => '\org\page\bootstrap',
```

也可以在调用分页方法的时候传入，例如：
```php
$list = Db::name('user')->where('status',1)->paginate(10,true,[
    'type'     => 'bootstrap',
    'var_page' => 'page',
    'page' =>3  //指定第几页
]);
```
#### 文件上传

``` html
<form action="/index/index/upload" enctype="multipart/form-data" method="post">
<input type="file" name="image" /> <br>
<input type="submit" value="上传" />
</form>
```

控制器:
``` php
public function upload(){
// 获取表单上传文件 例如上传了001.jpg
$file = request()->file('image');

// 移动到框架应用根目录/public/uploads/ 目录下
if($file){
$info = $file->move(ROOT_PATH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 获取扩展名
echo $info->getExtension();
// 输出 20160820/42a79759f284b767dfcb2a0197904287.jpg
echo $info->getSaveName();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}else{
// 上传失败获取错误信息
echo $file->getError();
}
}
```
move 方法成功的话返回的是一个 \think\File 对象,你可以对上传后的文件进行后续操作。


#### 多文件上传

``` html
<form action="/index/index/upload" enctype="multipart/form-data" method="post">
<input type="file" name="image[]" /> <br>
<input type="file" name="image[]" /> <br>
<input type="file" name="image[]" /> <br>
<input type="submit" value="上传" />
</form>

```

``` php
public function upload(){
// 获取表单上传文件
$files = request()->file('image');
foreach($files as $file){
// 移动到框架应用根目录/public/uploads/ 目录下
$info = $file->move(ROOT_PATH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 输出 jpg
echo $info->getExtension();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}else{
// 上传失败获取错误信息
echo $file->getError();
}
}
}

```

#### 上传验证
``` php
$info = $file->validate(['size'=>15678,'ext'=>'jpg,png,gif'])->move(ROOT_PA
TH . 'public' . DS . 'uploads');
if($info){
// 成功上传后 获取上传信息
// 输出 jpg
echo $info->getExtension();
// 输出 20160820/42a79759f284b767dfcb2a0197904287.jpg
echo $info->getSaveName();
// 输出 42a79759f284b767dfcb2a0197904287.jpg
echo $info->getFilename();
}
```

#### 上传规则

默认情况下,会在上传目录下面生成以当前日期为子目录,以微秒时间的 md5 编码为文件名的文件,例如上面

生成的文件名可能是:
/home/www/upload/20160510/42a79759f284b767dfcb2a0197904287.jpg

我们可以指定上传文件的命名规则,使用 rule 方法即可,例如:
``` php
// 获取表单上传文件 例如上传了001.jpg
$file = request()->file('image');
// 移动到服务器的上传目录 并且使用md5规则
$file->rule('md5')->move('/home/www/upload/');
```

| 规则 | 描述                        |
|------+-----------------------------|
| date | 根据日期和微秒数生成        |
| md5  | 对文件使用md5_file散列生成  |
| sha1 | 对文件使用sha1_file散列生成 |

rule 后可自定义函数调用

#### 验证码

模版内验证码的显示

``` html+php
<div>{:captcha_img()}</div>
```

或者

``` html
<div><img src="{:captcha_src()}" alt="captcha" /></div>
```

验证

``` php
$this->validate($data,[
'captcha|验证码'=>'require|captcha'
]);
```
或者手动验证
``` php
if(!captcha_check($captcha)){
//验证失败
};
```

### 图像处理
#### 打开图像
``` php
$image = \think\Image::open('./image.png');
//也可以从直接获取当前请求中的文件上传对象,例如:
$image = \think\Image::open(request()->file('image'));
```

#### 获取图像信息
``` php

$image = \think\Image::open('./image.png');
// 返回图片的宽度
$width = $image->width();
// 返回图片的高度
$height = $image->height();
// 返回图片的类型
$type = $image->type();
// 返回图片的mime类型
$mime = $image->mime();
// 返回图片的尺寸数组 0 图片宽度 1 图片高度
$size = $image->size();
```

#### 裁剪图像
``` php
$image->crop(300, 300)->save('./crop.png');
//支持从某个坐标开始裁剪,例如下面从(100,30)开始裁剪,
$image->crop(300, 300,100,30)->save('./crop.png');
```

``` php
//缩略图
$image->thumb(150, 150)->save('./thumb.png');
// 按照原图的比例生成一个最大为150*150的缩略图并保存为thumb.png
$image->thumb(150,150,\think\Image::THUMB_CENTER)->save('./thumb.png');

//图像翻转
// 对图像进行以y轴进行翻转操作
$image->flip(\think\image::FLIP_Y)->save('./filp_image.png');

//图像旋转
// 对图像使用默认的顺时针旋转90度操作
$image->rotate()->save('./rotate_image.png');

//添加水印
// 给原图左上角添加水印并保存water_image.png，透明度 50%
$image->water('./logo.png',\think\Image::WATER_NORTHWEST,50)->save('water_image.pn
g');
//文字水印
// 给原图左上角添加水印并保存water_image.png
$image->text('十年磨一剑 - 为API开发设计的高性能框架','HYQingKongTiJ.ttf',20,'#ffffff')->save('text_image.png');

```

### 命令行 php think
- clear
- make:controller  index/Blog    [生成index 模块的 Blog 控制器类库文件]
- make:model

### 部署
#### 修改入口文件

``` php
// 应用目录
define('APP_PATH', __DIR__.'/apps/');
// 加载框架引导文件
require './thinkphp/start.php';
```

#### URL重写

[Apache]

``` apache
<IfModule mod_rewrite.c>
Options +FollowSymlinks -Multiviews
RewriteEngine on
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ index.php?/$1 [QSA,PT,L]
</IfModule>

```

[Nginx]
``` c
location / { // .....省略部分代码
if (!-e $request_filename) {
rewrite ^(.*)$ /index.php?s=/$1
 last;
break;
}
}

```
(/  3600 24)

### 设置session 时间
> ROOT\application\config.php

添加个字段  expire

``` php

 'session'                => [
        'id'             => '',
        // SESSION_ID的提交变量,解决flash上传跨域
        'var_session_id' => '',
        // SESSION 前缀
        'prefix'         => 'think',
        // 驱动方式 支持redis memcache memcached
        'type'           => '',
        // 是否自动开启 SESSION
        'auto_start'     => true,
        //设置session 时间
        'expire'             => 86400,  
        
        //3600 1小时
    ],
```

### sql 日志

第一步：在Database.php文件中将数据库debug设置为true，（默认是true）
``` php
// 数据库调试模式
'debug'           => true,
```
第二步：在Config.php文件中写如下代码

``` php
  'log' => [
        // 日志记录方式，内置 file socket 支持扩展
        'type'  => 'File',
        // 日志保存目录
        'path'  => LOG_PATH,
        // 日志记录级别
        'level' => ['sql'],
    ],
```
一班这样设置之后就可以开启SQL日志记录了。

## 登录方案
### controller\Login.php
``` php
namespace app\admin\controller;
use think\Controller;
use app\admin\model\Login as Log;

class Login extends Controller
{
    public function index()
    {
        // $linkres= \think\Db::name('link')->paginate(3);
        // $this->assign('linkres',$linkres);
        if(request()->isPost()){
            $login=new Log;
            $status=$login->login(input('username'),input('password'));
            if($status==1){
                return $this->success('登录成功，正在跳转！','Index/index');
            }elseif($status==2){
                return $this->error('账号或者密码错误!');
            }else{
                return $this->error('用户不存在!');
            }
        }
        return $this->fetch('login');
    }

    public function logout(){
        session(null);
        return $this->success('退出成功！',url('index'));
    }
}
```

### model\Login.php
``` php
namespace app\admin\model;
use think\Model;
class Login extends Model
{
    public function login($username,$password){
        $admin= \think\Db::name('admin')->where('username','=',$username)->find();
        if($admin){
            if($admin['password']==md5($password)){
                \think\Session::set('id',$admin['id']);
                \think\Session::set('username',$admin['username']);
                return 1;
            }else{
                return 2;
            }
        }else{
            return 3;
        }
    }
}
```
### login.html

### 数据库操作
concat as 

->field(['id','concat("abc",path)'=>'path'])
