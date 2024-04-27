---
layout: default
toc: true
title: thinkphp6 
date:  2023-11-19T13:44:59+08:00
categories: ['编程']
---

ThinkPHP 6 是一款基于 PHP 开发的开源框架，用于快速开发 Web 应用程序。它具有以下主要用途和特点：

1. **快速开发**：ThinkPHP 6 提供了丰富的功能和工具，使开发人员能够快速构建功能强大的 Web 应用程序。它包括诸如路由、数据库操作、模板引擎等功能，大大简化了开发流程。

2. **灵活性**：框架提供了高度灵活的架构，允许开发人员根据项目的需求进行定制和扩展。同时，它支持多种开发范式，如 MVC（Model-View-Controller）等，使得开发人员能够按照最适合项目的方式组织代码。

3. **高性能**：ThinkPHP 6 在性能方面进行了优化，通过缓存、路由、数据库查询优化等手段提高了系统的响应速度和并发能力，能够处理大量的并发请求。

4. **安全性**：框架内置了安全机制，如数据过滤、输入验证、跨站脚本攻击（XSS）防护等，帮助开发人员构建更加安全可靠的应用程序。

5. **社区支持**：作为一款广泛使用的 PHP 框架，ThinkPHP 拥有庞大的社区支持和活跃的开发者社群。这意味着开发人员可以轻松获得帮助、学习新技术，并参与开源社区的建设。

ThinkPHP 6 的实现原理主要基于 PHP 语言，它采用了一系列的设计模式和技术来实现其功能，包括但不限于：

- **面向对象编程**：ThinkPHP 6 使用了面向对象的编程思想，将应用程序划分为不同的模块、控制器和视图，并通过对象之间的交互实现应用程序的功能。

- **MVC 架构**：框架采用了 MVC 架构模式，将应用程序划分为模型（Model）、视图（View）和控制器（Controller），以提高代码的可维护性和可扩展性。

- **路由机制**：ThinkPHP 6 使用路由机制将 URL 请求映射到相应的控制器和方法，实现了灵活的 URL 美化和路由参数的处理。

- **数据库操作**：框架提供了丰富的数据库操作功能，支持多种数据库类型，并封装了常用的数据库操作方法，简化了数据的增删改查操作。

- **模板引擎**：ThinkPHP 6 内置了强大的模板引擎，用于将数据和视图进行分离，提高了代码的可读性和可维护性。

总的来说，ThinkPHP 6 通过优化性能、提高安全性、提供灵活的开发方式等特点，帮助开发人员快速构建高质量的 Web 应用程序。
服务端程序，客户计算机（客户端）向某个服务器 发信息，服务器进行信息回馈。

最好把 客户端 和 服务端 分离 开发设计。
<!--more-->

## 程序配置

### 安装

``` sh
composer create-project topthink/think tp
```

如果是之前已经安装过，则可以进入根目录进行 **更新**

```sh
composer update topthink/framework
```

更新操作会删除 thinkphp 目录并重新下载安装新版本，但不会影响 **app** 目录，因此不要在核心框架目录添加任何应用代码或类库。

### 调试

应用默认是部署模式，如需开启调试模式，可以在 /.env 环境文件，修改 APP_DEBUG 的值

或在代码中打开调试

```php
ini_set("display_errors", "On");//打开错误提示
ini_set("error_reporting",E_ALL);//显示所有错误
```
### 运行程序

```sh
php think run
```
然后在浏览器中输入地址

```
http://localhost:8000/
```

如果 **8000** 端口被占用，则可以指定某个端口

```sh
php think run -p xxx
```

实际部署中，应该绑定域名到 **public** 目录

### 获取配置

获取环境变量

```php
Env::get('database.username');
```

可以直接在配置文件中使用环境变量函数进行本地环境和服务器环境的自动配置，如:

```php
return [
    'hostname'=>Env::get('hostname','127.0.0.1'),
];
```

get 的定义方法

```php
public function get(string $name = null, $default=null){
    if(is_null($name)){
        return $this->data;
    }

    $name=strtoupper(str_replace('.','_',$name));
   if(isset($this->data[$name])) {
    $result=$this->data[$name];

    if(is_string($result) && isset($this->convert[$result])){
        return $this->convert[$result];
    }
    return $result;
   }

return $this->getEnv($name,$default);
}

```

使用 **Config** 类, use think\facade\Config;

```php

// 获取 config/app.php 文件的配置
Config::get('app');
```


##  程序架构

### 请求流程

HTTP 请求流程，从用户发起请求到响应输出，大致如下

1. 载入 Composer 的自动加载 autoload 文件
2. 实例化系统应用基础类 think\App
3. 获取应用目录等相关路径信息
4. 加载全局的服务提供 provider.php 文件
5. ...
6. 加载环境变量文件 .env 和全局初始化文件
7. 判断应用模式
8. 注册异常处理
...
9. 路由检测
10. 执行数据验证
11. 获取控制器实例
11. 执行响应对象的send 方法输出
12. 写入当前请求的日志信息

模板引擎

模板文件中可以使用一些特殊的模板标签，这些标签的解析通常由模板引擎负责实现。
新版不再内置 **think-template** 模板引擎，如需使用，需要安装 **think-view** 扩展库。

## 路由

服务器 根据 消息类型，进入不同的 控制器，这个需要路由配置。

> 默认有套路由规则了

```
服务器->主入口->控制器->方法
http://serverName/index.php/hello/think
```

自定义路由规则
```php
Route::rule('hello/:name', 'index/hello');
```

## 控制器

```php
<?php
namespace app\controller;
class User
{
public function login()
{
return 'login';
}
}
```
## 请求

```php
<?php
namespace app\index\controller;
use think\Request;
class Index
{
/**
* @var \think\Request Request实例
*/
protected $request;
/**
* 构造方法
* @param Request $request Request对象
* @access public
*/
public function __construct(Request $request)
{
$this->request = $request;
}
}
```


## 响应

```php
<?php
namespaceapp\controller;
class Index
{
public function hello($name='thinkphp')
{
return 'Hello,' . $name . '!';
}
}
```

| 输出类型     | 快捷方法 | 对应Response类           |
| ------------ | -------- | ------------------------ |
| HTML输出     | response | \think\Response          |
| 渲染模板输出 | view     | \think\response\View     |
| JSON输出     | json     | \think\response\Json     |
| JSONP输出    | jsonp    | \think\response\Jsonp    |
| XML输出      | xml      | \think\response\Xml      |
| 页面重定向   | redirect | \think\response\Redirect |
| 附件下载     | download | \think\response\File     |


## 数据库


## 模型

```php
<?php
namespace app\model;
use think\Model;
class User extends Model
{
}
```

## 视图

通常可以直接使用 think\facade\View 来操作视图

```php
namespace app\controller;
use think\facade\View;
class Index
{
public function index()
{
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
}
}
```

