---
title: ThinkPHP6.0完全开发手册
permalink: thinkphp6.html
theme: jekyll-theme-cayman
---
https://www.kancloud.cn/manual/thinkphp6_0/1037479

> 轻量级PHP开发框架
> 进行敏捷web应用开发、简化企业应用开发
> 基于5.1基础优化

web程序的特点: 要处理客户端和服务器端的交互（全栈）

## MVC架构

控制器(控制流程)
-> 模型(处理业务逻辑)
-> 视图(处理外观)

目录结构
- 定义应用目录，来放置不同应用
- 定义配置目录，来配置应用
- 定义视图目录，来放置客户端文件
- 定义路由目录，进行路由定义
- 定义 public 目录，放置 web端其他文件
- 定义运行时目录 runtime ，放置临时文件
- 定义插件目录 vendor

## 请求流程

![](./images/request.png)


## 架构总览

### 定义入口文件，进入不同应用

- public/index.php (前台)
- public/admin.php (后台)

``` php
// $http->name()用于设置当前入口文件绑定的应用
$response = $http->name('api')->run();
```

## 安装 
```shell
 composer create-project topthink/think tp 
 cd tp  
 composer require topthink/think-multi-app 
 composer require topthink/think-view  

 开启调试 .env
 APP_DEBUG=true

 php think run -p 80 
```

## 命名规范

### 目录和文件

- 目录使用小写+下划线；
- 类库、函数文件统一以`.php`为后缀；
- 类的文件名均以命名空间定义，并且命名空间的路径和类库文件所在路径一致；
- 类（包含接口和Trait）文件采用驼峰法命名（首字母大写），其它文件采用小写+下划线命名；
- 类名（包括接口和Trait）和文件名保持一致，统一采用驼峰法命名（首字母大写）；

### 函数和类、属性命名

- 类的命名采用驼峰法（首字母大写），例如 `User`、`UserType`；
- 函数的命名使用小写字母和下划线（小写字母开头）的方式，例如 `get_client_ip`；
- 方法的命名使用驼峰法（首字母小写），例如 `getUserName`；
- 属性的命名使用驼峰法（首字母小写），例如 `tableName`、`instance`；
- 特例：以双下划线`__`打头的函数或方法作为魔术方法，例如 `__call` 和 `__autoload`；

### 常量和配置

- 常量以大写字母和下划线命名，例如 `APP_PATH`；
- 配置参数以小写字母和下划线命名，例如 `url_route_on` 和`url_convert`；
- 环境变量定义使用大写字母和下划线命名，例如`APP_DEBUG`；

### 数据表和字段

- 数据表和字段采用小写加下划线方式命名，并注意字段名不要以下划线开头，例如 `think_user` 表和 `user_name`字段，不建议使用驼峰和中文作为数据表及字段命名。

## config (设置)
### environment-variables

think\facade\Env

```
Env::get('database.username');
```
### config-file
think\facade\Config;
```
 Config::get('app.app_name');
 Config::has('route.route_rule_merge');
```
      
### system-config-files

| 文件           | 配置                     |
| -------------- | ------------------------ |
| app.php        | 'show_error_msg' => true |
| cache.php      |                          |
| console.php    |                          |
| cookie.php     |                          |
| database.php   |                          |
| filesystem.php |                          |
| lang.php       |                          |
| log.php        |                          |
| middleware.php | 中间件配置               |
| route.php      |                          |
| session.php    |                          |
| trace.php      |                          |
| view.php       | 视图配置                 |

  
### 多应用
> 每个应用相对保持独立，并且可以支持多个入口文件，应用下面还可以通过多级控制器来维护控制器分组。

``` php
// [ 应用入口文件 ]
namespace think;
 
require __DIR__ . '/../vendor/autoload.php';
 
// 执行HTTP应用并响应
$http = (new  App())->http;
$response = $http->name('admin')->run();
$response->send();
$http->end($response);
```

## 路由
### 路由

路由地址不能跨 应用 (除非采用重定向路由) 
    
```
// 关闭应用的路由功能
'with_route' =>false,
```

### 路由定义

```
Route::get('new/<id>','News/read'); // 定义GET请求路由规则
Route::post('new/<id>','News/update'); // 定义POST请求路由规则
Route::put('new/:id','News/update'); // 定义PUT请求路由规则
Route::delete('new/:id','News/delete'); // 定义DELETE请求路由规则
Route::any('new/:id','News/read'); // 所有请求都支持的路由规则
```

规则表达式

```
Route::rule('/', 'index'); // 首页访问路由
Route::rule('my', 'Member/myinfo'); // 静态地址路由
Route::rule('blog/:id', 'Blog/read'); // 静态地址和动态地址结合
Route::rule('new/:year/:month/:day', 'News/read'); // 静态地址和动态地址结合
Route::rule(':user/:blog_id', 'Blog/read'); // 全动态地址
```
### 路由地址
#### 重定向路由
```
Route::redirect('blog/:id', 'http://blog.thinkphp.cn/read/:id', 302);
```
#### 路由到模板
```
// 路由到模板文件
Route::view('hello/:name', 'index/hello');
```

### 资源路由
![](../image/computer/language/php/Snipaste_2021-05-27_16-59-46.png)
### 路由绑定
  可以使用路由绑定简化 URL 或者路由规则的定义
#### 绑定到控制器/操作


#### 绑定到命名空间
## 控制器
### 控制器定义

渲染输出
> halt('输出测试');

### 资源控制器

资源控制器可以让你轻松的创建RESTFul资源控制器，可以通过命令行生成需要的资源控制器，例如生成index应用的Blog资源控制器使用：
php think make:controller index@Blog

或者使用完整的命名空间生成
php think make:controller app\index\controller\Blog

如果只是用于接口开发，可以使用
php think make:controller index@Blog --api

然后你只需要为资源控制器注册一个资源路由：
Route::resource('blog', 'Blog');

## 请求
### 请求对象 
``` php
<?php
namespace app\index\controller;
use think\Request;

class Index
{
    
    public function index(Request $request)
    {
		return $request->param('name');
    }    
}
```

助手函数
``` php
<?php

namespace app\index\controller;

class Index
{
    public function index()
    {
        return request()->param('name');
    }
}
```
### 请求信息

``` php
use think\facade\Request;
// 获取完整URL地址 不带域名
Request::url();
// 获取完整URL地址 包含域名
Request::url(true);
// 获取当前URL（不含QUERY_STRING） 不带域名
Request::baseFile();
// 获取当前URL（不含QUERY_STRING） 包含域名
Request::baseFile(true);
// 获取URL访问根地址 不带域名
Request::root();
// 获取URL访问根地址 包含域名
Request::root(true);
```

获取当前控制器/操作

``` php
Request::controller();
Request::action();
//如果使用了多应用模式，可以通过下面的方法来获取当前应用
app('http')->getName();
```

### 输入变量

``` php
// 获取当前请求的name变量
Request::param('name');
// 获取当前请求的所有变量(经过过滤)
Request::param();
// 获取当前请求未经过滤的所有变量
Request::param(false);
// 获取部分变量
Request::param(['name', 'email']);
// 获取param变量 并用strip_tags函数过滤
Request::param('username','','strip_tags'); 
 // 获取post变量 并用org\Filter类的s
input('post.name','','org\Filter::safeHtml');
afeHtml方法过滤
```
### 请求类型

获取请求类型
| 用途                | 方法      |
|---------------------+-----------|
| 获取当前请求类型    | method    |
| 判断是否GET请求     | isGet     |
| 判断是否POST请求    | isPost    |
| 判断是否PUT请求     | isPut     |
| 判断是否DELETE请求  | isDelete  |
| 判断是否AJAX请求    | isAjax    |
| 判断是否PJAX请求    | isPjax    |
| 判断是否JSON请求    | isJson    |
| 判断是否手机访问    | isMobile  |
| 判断是否HEAD请求    | isHead    |
| 判断是否PATCH请求   | isPatch   |
| 判断是否OPTIONS请求 | isOptions |
| 判断是否为CLI执行   | isCli     |
| 判断是否为CGI模式   | isCgi     |


HTTP 头信息

``` php
$info = Request::header();
echo $info['accept'];
echo $info['accept-encoding'];
echo $info['user-agent'];
```

## 响应
大多数情况,我们不需要关注 Response 对象本身,只需要在控制器的操作方法中返回数据即可
> 使用 return  返回响应类型的数据 return json($data);

| 输出类型     | 快捷方法 | 对应Response类           |
|--------------+----------+--------------------------|
| HTML输出     | response | \think\Response          |
| 渲染模板输出 | view     | \think\response\View     |
| JSON输出     | json     | \think\response\Json     |
| JSONP输出    | jsonp    | \think\response\Jsonp    |
| XML输出      | xml      | \think\response\Xml      |
| 页面重定向   | redirect | \think\response\Redirect |
| 附件下载     | download | \think\response\File     |


响应参数和状态码
``` php
json($data,201);
view($data,401);
```

使用 Response 类的 header 设置响应的头信息
``` php
json($data)->code(201)->header([
'Cache-control' => 'no-cache,must-revalidate'
]);
```

写入Cookie
``` php
response()->cookie('name', 'value', 600);
```

文件下载

``` php
//如果需要设置文件下载的有效期,可以使用
public function download()
{
// 设置300秒有效期
return download('image.jpg', 'my')->expire(300);
}
```

## 数据库
### 删除数据
``` php
// 软删除数据 使用delete_time字段标记删除
Db::name('user')
->where('id', 1)
->useSoftDelete('delete_time',time())
->delete();
```
实际生成的SQL语句可能如下(执行的是 UPDATE 操作):
``` sql
UPDATE `think_user` SET `delete_time` = '1515745214' WHERE `id` = 1
```

## 模型

``` php
//指定主键
protected $pk = 'uid';
// 定义默认的表后缀(默认查询中文数据)
protected $suffix = _cn';

// 设置字段信息
//模型的数据字段和对应数据表的字段是对应的,默认会自动获取(包括字段类型),但自动获取会导致增加一次查询

protected $schema = [
'id' => 'int',
'name' => 'string',
'status' => 'int',
'score' => 'float',
'create_time' => 'datetime',
'update_time' => 'datetime',
];
```
## 视图

``` php
// 模板变量赋值
View::assign('name','ThinkPHP');
View::assign('email','thinkphp@qq.com');
// 或者批量赋值
View::assign([
'name' => 'ThinkPHP',
'email' => 'thinkphp@qq.com'
]);
// 模板输出
return View::fetch('index');
```

``` php
return view('index', [
'name' => 'ThinkPHP',
'email' => 'thinkphp@qq.com'
]);

```

## 上传文件

如果是多应用的话，上传根目录默认是runtime/index/storage，如果你希望上传的文件是可以直接访问或者下载的话，可以使用public存储方式。

$savename = \think\facade\Filesystem::disk('public')->putFile( 'topic', $file);

你可以在config/filesystem.php配置文件中配置上传根目录及上传规则，例如：

return [
    'default' =>  'local',
    'disks'   => [
        'local'  => [
            'type' => 'local',
            'root'   => app()->getRuntimePath() . 'storage',
        ],
        'public' => [
            'type'     => 'local',
            'root'       => app()->getRootPath() . 'public/storage',
            'url'        => '/storage',
            'visibility' => 'public',
        ],
        // 更多的磁盘配置信息
    ],
];
我们可以指定上传文件的命名规则，例如：

$savename = \think\facade\Filesystem::putFile( 'topic', $file, 'md5');


系统默认提供了几种上传命名规则，包括：

| 规则 | 描述                        |
| ---- | --------------------------- |
| date | 根据日期和微秒数生成        |
| md5  | 对文件使用md5_file散列生成  |
| sha1 | 对文件使用sha1_file散列生成 |

### 上传验证
支持使用验证类对上传文件的验证，包括文件大小、文件类型和后缀：

``` php
public function upload(){
    // 获取表单上传文件
    $files = request()->file();
    try {
        validate(['image'=>'fileSize:10240|fileExt:jpg|image:200,200,jpg'])
            ->check($files);
        $savename = [];
        foreach($files as $file) {
            $savename[] = \think\facade\Filesystem::putFile( 'topic', $file);
        }
    } catch (\think\exception\ValidateException $e) {
        echo $e->getMessage();
    }
}
```

| 验证参数 | 说明                                 |
| -------- | ------------------------------------ |
| fileSize | 上传文件的最大字节                   |
| fileExt  | 文件后缀，多个用逗号分割或者数组     |
| fileMime | 文件MIME类型，多个用逗号分割或者数组 |
| image    | 验证图像文件的尺寸和类型             |

具体用法可以参考验证章节的内置规则-> 上传验证。
