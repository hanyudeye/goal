# 基于thinkphp5小功能设计与实现
## 基础知识
### 数据库

#### 数据库创建
主要采取关键字有：
save
create
insert
insertAll

添加一条数据
第一种是实例化模型对象后赋值并保存：

$user           = new User;
$user->name     = 'thinkphp';
$user->email    = 'thinkphp@qq.com';
$user->save();

//也可以使用data方法批量赋值
$user = new User;
$user->data([
    'name'  =>  'thinkphp',
    'email' =>  'thinkphp@qq.com'
]);

在实例化的时候传入数据
$user = new User([
    'name'  =>  'thinkphp',
    'email' =>  'thinkphp@qq.com'
]);
$user->save();

静态调用create方法创建并写入
$user = User::create([
    'name'  =>  'thinkphp',
    'email' =>  'thinkphp@qq.com'
]);

使用 Db 类的 insert 方法向数据库提交数据
$data = ['foo' => 'bar', 'bar' => 'foo'];
Db::table('think_user')->insert($data);
添加多条数据
$user = new User;
$list = [
    ['name'=>'thinkphp','email'=>'thinkphp@qq.com'],
    ['name'=>'onethink','email'=>'onethink@qq.com']
];
$user->saveAll($list);
添加多条数据直接向 Db 类的 insertAll 方法传入需要添加的数据
$data = [
    ['foo' => 'bar', 'bar' => 'foo'],
    ['foo' => 'bar1', 'bar' => 'foo1'],
    ['foo' => 'bar2', 'bar' => 'foo2']
];
Db::name('user')->insertAll($data);
过遍历批量新增数据
$user = new User;
$list = [
    ['name'=>'thinkphp','email'=>'thinkphp@qq.com'],
    ['name'=>'onethink','email'=>'onethink@qq.com']
];
foreach($list as $data){
    $user->data($data,true)->isUpdate(false)->save();
}

#### 数据库删除
主要采取关键字有：
delete
destroy

根据主键删除
Db::table('think_user')->delete(1);
Db::table('think_user')->delete([1,2,3]);
//或则助手函数
db('user')->delete(1);//助手函数
删除模型数据，可以在实例化后调用delete方法。
$user = User::get(1);
$user->delete();
调用静态destroy方法实现删除
User::destroy(1);

// 支持批量删除多个数据
User::destroy('1,2,3');
// 或者
User::destroy([1,2,3]);

// 删除状态为0的数据
User::destroy(['status' => 0]);
用闭包函数设置删除条件
User::destroy(function($query){
    $query->where('id','>',10);
});
//等同于
User::where('id','>',10)->delete();

#### 数据库更新
主要采取关键字有：
update
setField
setInc
setDec
save
update

更新数据表中的数据
Db::table('think_user')
    ->where('id', 1)
    ->update(['name' => 'thinkphp']);
    //或则根据主键更新
    Db::table('think_user')
    ->update(['name' => 'thinkphp','id'=>1]);
更新某个字段的值
Db::table('think_user')
    ->where('id',1)
    ->setField('name', 'thinkphp');
自增或自减一个字段的值
// score 字段加 1
Db::table('think_user')
    ->where('id', 1)
    ->setInc('score');
// score 字段加 5
Db::table('think_user')
    ->where('id', 1)
    ->setInc('score', 5);
// score 字段减 1
Db::table('think_user')
    ->where('id', 1)
    ->setDec('score');
// score 字段减 5
Db::table('think_user')
    ->where('id', 1)
    ->setDec('score', 5);
延迟更新
Db::table('think_user')->where('id', 1)->setInc('score', 1, 10);
查找并更新
$user = User::get(1);
$user->name     = 'thinkphp';
$user->email    = 'thinkphp@qq.com';
$user->save();
直接更新数据
$user = new User;
// save方法第二个参数为更新条件
$user->save([
    'name'  => 'thinkphp',
    'email' => 'thinkphp@qq.com'
],['id' => 1]);
批量更新数据
$user = new User;
$list = [
    ['id'=>1, 'name'=>'thinkphp', 'email'=>'thinkphp@qq.com'],
    ['id'=>2, 'name'=>'onethink', 'email'=>'onethink@qq.com']
];
$user->saveAll($list);

//或则(遍及更新)
foreach($list as $data){
    $user->data($data,true)->isUpdate(true)->save();
}
通过数据库类更新数据
$user = new User;
$user->where('id', 1)
    ->update(['name' => 'thinkphp']);
//或则
$user->update(['id' => 1, 'name' => 'thinkphp']);
静态方法
User::where('id', 1)
    ->update(['name' => 'thinkphp']);
    //或则
    User::update(['id' => 1, 'name' => 'thinkphp']);
闭包更新
$user = new User;
$user->save(['name' => 'thinkphp'],function($query){
    // 更新status值为1 并且id大于10的数据
    $query->where('status', 1)->where('id', '>', 10);
});

#### 数据库查询
主要采取关键字有：
get
find
all
getBy字段名
chunk
value
column
Loader

获取表中单条记录:get方法
取出主键为1的数据
$user = User::get(1);
echo $user->name;

// 使用数组查询
$user = User::get(['name' => 'thinkphp']);

// 使用闭包查询
$user = User::get(function($query){
    $query->where('name', 'thinkphp');
});
echo $user->name;
Model对象查询单条记录:find方法
$user = new User();
// 查询单个数据
$user->where('name', 'thinkphp')
    ->find();
取出多个数据：all静态方法
// 根据主键获取多个数据
$list = User::all('1,2,3');
// 或者使用数组
$list = User::all([1,2,3]);
foreach($list as $key=>$user){
    echo $user->name;
}
// 使用数组查询
$list = User::all(['status'=>1]);
// 使用闭包查询
$list = User::all(function($query){
    $query->where('status', 1)->limit(3)->order('id', 'asc');
});
foreach($list as $key=>$user){
    echo $user->name;
}
动态查询
根据字段名动态查询:getBy字段名( )

// 根据name字段查询用户
$user = User::getByName('thinkphp');

// 根据email字段查询用户
$user = User::getByEmail('thinkphp@qq.com');
通过Query类查询
User::where('id','>',10)->select();
User::where('name','thinkphp')->find();
数据分批处理
User::chunk(100,function($users){
    foreach($users as $user){
        // 处理user模型对象
    }
});
获取字段值:value( )
// 获取某个用户的积分
User::where('id',10)->value('score');

//模型静态调用【模型查询方法】
User::get(1)->getData('name');
获取单列或多列字段值:column( )
// 获取某个列的所有值
User::where('status',1)->column('name');
// 以id为索引
User::where('status',1)->column('name','id');
加载器Loader类中查询
利用Loader类model静态方法自动加载自定义模型并实例化，得到模型对象。
 $data = Loader::model('User')  //加载模型类并创建模型对象
         ->where('id = 1')    //设置查询条件
         ->find();       //获取查询结果
         
利用Loader类db静态方法自动数据库类并创建连接对象。
 $data = Loader::db()       //加载数据库类并创建连接对象
            ->table('tp5_user')  //设置当前数据表
            ->where('id = 1')    //设置查询条件
            ->find();       //获取查询结果
            
利用Loader类model静态方法得到模型对象后，不调用数据库方法，而是直接调用模型方法来完成查询。
  //创建查询闭包函数
    $closure = function ($query){  //闭包匿名函数
      $query -> where('id = 1');  //设置查询条件       
    };
   //获取满足条件的单个记录:返回一个数据对象     
   $data = Loader::model('User')->get($closure);

### 路由
thinkphp5路由设置
执行流程

注册路由(可以理解为开启路由功能)
// 开启路由功能
'url_route_on'    =>  true,
配置路由(你使用路由功能当然要配置路由)
// 开启路由功能
'url_route_on'    =>  true,

// 设置路由配置文件列表
'route_config_file'    =>  ['home','admin'],
application/home.php配置home模块的路由规则，application/admin.php则配置admin模块的路由规则

注册方法
方法名	描述
rule	基本路由注册
any	任意请求路由注册
get	GET请求路由注册
post	POST请求路由注册
put	PUT请求路由注册
patch	PATCH请求路由注册
delete	DELETE请求路由注册
alias	别名路由注册
group	路由分组注册
controller	控制器方法路由注册
resource	资源路由注册
pattern	全局路由变量规则注册
import	静态注册路由（导入路由配置）
domain	域名路由注册或者域名绑定
miss	MISS路由注册
auto	AUTO路由注册
use think\Route;
Route::get('/','index/index/index');
路由缓存(避免重复请求路由，所以需要进行路由缓存)
php think optimize:route
参数检查()
路由检查：
路由检查指的是把当前的请求URL地址依次和注册的路由规则进行变量和条件检查，如果不匹配则进行下一个路由规则的检查，直到匹配到正确的路由规则则进入下一步：路由解析。如果没有匹配到任何路由规则，则按照系统默认的规则进行URL解析

路由参数检查：
路由变量检查，其实也就是通常说的路由规则匹配检查，当路由参数（路由生效条件）检测通过后，就要对当前访问的URL地址进行路由规则匹配检查，包括路由变量个数、变量规则约束，如果是静态路由规则的话就进行字符串匹配（不区分大小写）。

路由别名检查：
路由别名允许我们给控制器注册一个唯一的路由标识，然后该控制器下面的所有操作方法都不需要再定义具体的路由，这个路由标识就称为别名路由

域名部署检测
接下来会检查是否配置了域名部署，如果有匹配当前的域名，会检查域名是否定义相关的路由绑定。
域名部署检测由Route类的checkDomain方法完成，具体用法我们会在（十）域名路由一节为你讲解。

路由绑定检查
在这个步骤，系统会检查当前的是否有进行路由绑定，如果有绑定的话按照绑定类型进行解析。具体内容会在（十一）路由绑定中为你讲解。

静态路由检查
系统会优先检查是否存在和当前访问URL地址相同的静态路由（注意是完整匹配，不含URL后缀），如果有定义，则进行静态路由的参数检查，如果通过表示路由有效，则进行路由地址解析。
也就是说静态路由规则虽然和动态路由是使用相同的方式一起注册的，但检查的时候是提前检查的。

路由解析
路由解析的主要工作就是解析匹配到的路由规则中定义的路由地址（例如控制器的操作方法或者闭包等），并且解析URL地址中的其它路由参数以及路由绑定的其它数据，而且会把相关信息和变量保存到当前请求对象中，最后会告诉系统下一步如何对URL请求进行正确的调度执行，这个时候路由的使命全部完成，正式交权给App类。
路由的解析操作由Route类的parseRule方法完成。


### 常用方法清单
think\Controller控制器基类
fetch：渲染模板输出

fetch('模板文件','模板变量（数组）','替换规则（数组）','模板参数（数组）')

display：渲染内容输出

display('内容','模板变量（数组）','替换规则（数组）','模板参数（数组）')

assign：模板变量赋值

assign('模板变量（数组）')
assign('模板变量名','变量值')

engine：模板引擎初始化（或切换）

engine('模板引擎参数')

validateFailException：设置验证出错是否抛异常

validateFailException('是否抛异常（布尔值）')

validate：验证数据

validate('数据（数组）','验证规则（数组或者字符串）','错误信息（数组）','是否批量验证（布尔值）','验证回调')

think\Request请求类
domain：设置或获取当前域名

设置当前域名
domain('设置的域名')
获取当前域名（包含协议）
domain()

url：设置或获取当前完整URL

设置完整URL地址
url('URL地址')
获取当前完整URL
url()
获取当前完整URL（包含域名）
url(true)

baseUrl：设置或获取当前URL（不含QUERY_STRING）

设置当前URL
baseUrl('URL地址')
获取当前URL（不含QUERY_STRING）
baseUrl()
获取当前URL（含域名）
baseUrl(true)

baseFile：设置或获取当前执行的文件

设置当前执行文件
baseFile('URL地址')
获取当前执行的文件
baseFile()
获取当前执行的文件 （含域名）
baseFile(true)

root：设置或获取当前URL访问根地址

设置当前URL访问根地址
root('URL地址')
获取当前URL访问根地址
root()
获取当前URL访问根地址（含域名）
root(true)

pathinfo：获取当前请求的pathinfo信息（含URL后缀）

pathinfo()

path：获取当前请求的pathinfo信息（不含URL后缀）

path()

ext：获取当前请求URL的后缀

ext()

time：获取当前请求开始的时间戳

获取当前请求开始的时间戳（秒）
time()
获取当前请求开启的时间戳（微秒）
time(true)

type：获取当前请求的资源类型

type()

mimeType：设置额外的资源类型

mimeType('资源类型','资源类型值')
mimeType(['资源类型'=>'资源类型值'])
method：获取当前请求类型
获取当前请求类型（支持伪装）
method()
获取当前请求类型（原始）
method(true)

isGet：是否GET请求

isGet()

isPost：是否POST请求

isPost()

isPut：是否PUT请求

isPut()

isDelete：是否DELETE请求

isDelete()

isHead：是否HEAD请求

isHead()

isPatch：是否PATCH请求

isPatch()

isOptions：是否OPTIONS请求

isOptions()

isCli：是否命令行执行

isCli()

isCgi：是否为CGI模式

isCgi()

param：获取当前请求的参数

获取当前请求的所有参数
param('','默认值','过滤方法')
获取当前请求的所有参数（包含上传信息）
param(true,'默认值','过滤方法')
获取当前请求的某个参数
param('变量名（字符串）','默认值','过滤方法')

route：获取当前请求的路由变量

获取当前请求的全部路由变量
route('','默认值','过滤方法')
获取当前请求的某个路由变量
route('变量名（字符串）','默认值','过滤方法')
get：获取或者设置GET变量
get('','默认值','过滤方法')
获取当前请求的某个GET变量>
get('变量名（字符串）','默认值','过滤方法')
追加当前请求的GET变量
get('数组')

post：获取或者设置POST变量

获取当前请求的全部POST变量
post('','默认值','过滤方法')
获取当前请求的某个POST变量

post('变量名（字符串）','默认值','过滤方法')

追加当前请求的POST变量

post('数组')

put：获取或者设置PUT变量
获取当前请求的全部PUT变量

put('','默认值','过滤方法')

获取当前请求的某个PUT变量

put('变量名（字符串）','默认值','过滤方法')

追加当前请求的PUT变量

put('数组')

delete：获取或者设置当前请求的DELETE变量

获取当前请求的全部DELETE变量

delete('','默认值','过滤方法')

获取当前请求的某个DELETE变量

delete('变量名（字符串）','默认值','过滤方法')

追加当前请求的DELETE变量

delete('数组')

patch：获取或者设置当前请求的PATCH变量

获取当前请求的全部PATCH变量

patch('','默认值','过滤方法')

获取当前请求的某个PATCH变量

patch('变量名（字符串）','默认值','过滤方法')

追加当前请求的PATCH变量

patch('数组')

request：获取当前请求的全部REQUEST变量

request('','默认值','过滤方法')

获取当前请求的某个REQUEST变量

request('变量名（字符串）','默认值','过滤方法')

追加当前请求的REQUEST变量

request('数组')

session：获取或者设置当前请求的SESSION变量

获取当前请求的全部SESSION变量

session('','默认值','过滤方法')

获取当前请求的某个SESSION变量

session('变量名（字符串）','默认值','过滤方法')

追加当前请求的SESSION变量

session('数组')

cookie：获取或者设置当前请求的COOKIE变量
获取当前请求的全部COOKIE变量

cookie('','默认值','过滤方法')

获取当前请求的某个COOKIE变量

cookie('变量名（字符串）','默认值','过滤方法')

追加当前请求的COOKIE变量

cookie('数组')

server：获取当前请求的SERVER变量
获取当前请求的全部SERVER变量

server('','默认值','过滤方法')

获取当前请求的某个SERVER变量

server('变量名（字符串）','默认值','过滤方法')

追加当前请求的SERVER变量

server('数组')

env：获取当前请求的ENV变量

获取当前请求的全部ENV变量

env('','默认值','过滤方法')

获取当前请求的某个ENV变量

env('变量名（字符串）','默认值','过滤方法')

追加当前请求的ENV变量

env('数组')

file：获取上传文件信息

获取全部上传文件信息

file()

获取单个上传文件信息

file('名称')

header：设置或获取当前请求的头信息

设置或获取当前请求的全部头信息

header()

获取当前请求的某个头信息

header('变量名','默认值')

追加当前请求的头信息

header('数组')

input：获取数据变量

input('数据源（数组）','变量名（字符串）','默认值','过滤方法')

filter：设置当前请求变量的过滤方法

filter('过滤方法（字符串或者数组）')

has：是否存在某个变量
has('变量名（字符串）','变量类型','是否检测空值')

only：获取指定请求参数

only('变量名（字符串）','变量类型')

except：排除某些请求参数

except('变量名（字符串）','变量类型')

isSsl：当前请求是否Ssl

isSsl()

isAjax：当前请求是否Ajax

isAjax()

isPjax：当前请求是否Pjax

isPjax()

isMobile：当前请求是否手机访问

isMobile()

ip：获取客户端IPv4地址

ip()

scheme：获取当前请求的scheme

scheme()

query：获取当前请求的query

query()

host：获取当前请求的host

host()

port：获取当前请求的port

port()

protocol：获取当前请求的protocol

protocol()

remotePort：获取当前请求的remotePort

remotePort()

routeInfo：设置或获取当前请求的路由信息

获取当前路由信息

routeInfo()

设置当前请求的路由信息

routeInfo('路由信息')

dispatch：设置或获取当前请求的调度信息

获取调度信息

dispatch()

设置当前请求的调度信息

dispatch('调度信息')

设置或获取当前请求的模块名

获取当前模块名

module()

设置当前请求的模块名

module('模块名')

controller：设置或获取当前请求的控制器名
获取当前控制器名

controller()

设置当前请求的控制器名

controller('控制器名')

action：设置或获取当前请求的操作名

设置当前请求的操作名

action('操作名')

获取当前操作

action()

langset：设置或设置当前请求的语言

获取当前请求的语言

langset()

设置语言

langset('语言名')

getContent：获取当前请求的内容

getContent()

getInput：获取当前请求的php://input
getInput()

token：生成当前请求的令牌

token('令牌名称','令牌生成方法')

cache：设置当前请求的缓存

cache('缓存标识','缓存有效期')

getCache：获取当前请求缓存的设置信息

getCache()

bind：绑定请求属性

bind('属性名','绑定对象实例')

think\Response响应类
data：设置响应输出的原始数据

data('数据')

content：设置响应输出的最终数据

content('数据（字符串）')

options：设置响应输出的额外参数

options('参数（数组）')

code：设置响应输出的状态码

code('状态码（数字）')

header：设置响应输出的Header数据

header('头信息（数组）')

header('头信息名','值')

lastModified：设置响应输出的Last-Modified

lastModified('值')

expires：设置响应输出的Expires

expires('值')

eTag：设置响应输出的ETag

eTag('值')

cacheControl：设置响应输出的Cache-control

cacheControl('值')

contentType：设置响应输出的Content-Type

contentType('输出类型','输出编码')

getHeader：获取响应输出的头信息（留空获取全部）

getHeader('值')

getData：获取响应输出的原始数据

getData()

getContent：获取响应输出的最终数据

getContent()

getCode：获取响应输出的状态码

getCode()

think\response\View响应类
getVars：获取模板变量（留空获取所有）

getVars('变量名')

assign：设置模板变量

assign('参数名','参数值')

assign('参数（数组）')

replace：设置输出替换

replace('被替换内容','替换内容')

replace('替换数组')

think\response\Redirect响应类
with：设置响应输出的隐式参数

with('参数名','参数值')

with('参数（数组）')

params：设置额外参数

params('参数（数组）')

remember：记住当前URL地址

remember()

restore：跳转到上次记住的url

restore()

## 环境搭建
### lnmp
1：查看环境：

[root@localhost]# cat /etc/redhat-release

2.关掉防火墙

[root@localhost]# chkconfig iptables off
3.配置CentOS 6.0 第三方yum源

[root@localhost]#wget http://www.atomicorp.com/installers/atomic

[root@localhost]#sh ./atomic

[root@localhost]#yum check-update
4.安装开发包和库文件

[root@localhost]# yum -y install ntp make openssl openssl-devel pcre pcre-devel libpng libpng-devel libjpeg-6b libjpeg-devel-6b freetype freetype-devel gd gd-devel zlib zlib-devel gcc gcc-c++ libXpm libXpm-devel ncurses ncurses-devel libmcrypt libmcrypt-devel libxml2 libxml2-devel imake autoconf automake screen sysstat compat-libstdc++-33 curl curl-devel
5.卸载已安装的apache、mysql、php

[root@localhost]#  yum remove httpd
[root@localhost]# yum remove mysql
[root@localhost]# yum remove php
6.安装nginx

[root@localhost]#  yum install nginx
[root@localhost]#  service nginx start
[root@localhost]#  chkconfig --levels 235 nginx on
//设2、3、5级别开机启动
7.安装mysql

[root@localhost]# yum install mysql mysql-server mysql-devel
[root@localhost]#  service mysqld start
[root@localhost]# chkconfig --levels 235 mysqld on
8.安装php

[root@localhost]#yum install php lighttpd-fastcgi php-cli php-mysql php-gd php-imap php-ldap php-odbc php-pear php-xml php-xmlrpc php-mbstring php-mcrypt php-mssql php-snmp php-soap

[root@localhost]#yum install  php-tidy php-common php-devel php-fpm php-mysql

[root@localhost]#service php-fpm start

[root@localhost]#chkconfig --levels 235 php-fpm on
9.配置nginx支持php

[root@localhost]#  mv /etc/nginx/nginx.conf /etc/nginx/nginx.confbak
//将配置文件改为备份文件
 
[root@localhost]#  cp /etc/nginx/nginx.conf.default /etc/nginx/nginx.conf
//由于原配置文件要自己去写因此可以使用默认的配置文件作为配置文件
 
//修改nginx配置文件，添加fastcgi支持
[root@localhost]#  vi /etc/nginx/nginx.conf
index index.php index.html index.htm;
//加入index.php
 
location ~ \.php$ {
            root           /usr/share/nginx/html;
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  /usr/share/nginx/html$fastcgi_script_name;
            include        fastcgi_params;
        }
//将以上代码注释去掉，并修改成nginx默认路径
10.配置php

//编辑文件php.ini，在文件末尾添加cgi.fix_pathinfo = 1
[root@localhost]#  vi /etc/php.ini
11.重启nginx php-fpm

[root@localhost]#  service nginx restart
[root@localhost]#  service php-fpm restart
12：建立info.php文件

[root@localhost]#  vi /usr/share/nginx/html/info.php
<?php
   phpinfo();
?>


## Thinkphp小案例
### 分类管理

#### 数据库设计
使用navicat新建一个简单的数据库testdata
在数据库配置文件Application/Common/Config/config.php中写好配置
<?php
return array(
    //以下是数据库的配置，请在安装前配置
	'DB_TYPE' => 'mysql',
    'DB_HOST' => 'localhost',	//数据库地址
    'DB_USER' => 'root',	//数据库用户名
    'DB_PWD' => '123456',		//数据库密码
    'DB_NAME' => 'testdata',		//数据库名
    'DB_PORT' => 3306,	//数据库端口
    'DB_PREFIX' => 'tp_',			//数据库表前缀
    'DB_CHARSET' => 'utf8',			//数据库编码
);
插入数据的sql语句
DROP TABLE IF EXISTS `tp_cate`;
CREATE TABLE `tp_cate` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `pid` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '上级分类ID',
  `catename` varchar(50) NOT NULL COMMENT '分类名称',
  `sort` smallint(5) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`catename`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COMMENT='分类表';
#### 模型
实现数据库中的增删查改这就是模型
模型在ThinkPHP中基础的模型类就是Think\Model类，该类完成了基本的CURD、ActiveRecord模式、连贯操作和统计查询，一些高级特性被封装到另外的模型扩展中。
　　基础模型类的设计非常灵活，甚至可以无需进行任何模型定义，就可以进行相关数据表的ORM和CURD操作，只有在需要封装单独的业务逻辑的时候，模型类才是必须被定义的。
　　
1.在Application/Admin/Mode/目录下创建CateModel.class.php默认代码如下

  <?php
      namespace Admin\Model;
      use Think\Model;

      class CateModel extends Model{

      }
2.在模型添加如下函数

    //作用：获取分类信息
   public function getLevelList() {
         $list= $this->order('sort asc')->select();
         return tree($list);
    }
     //作用：添加分类信息
    public function addcate($data){
        if (!$this->create($data)){
            return $this->getError();
        }else{
            return $this->add($data);
        }
    }
3.在Application/Common/Common/目录下创建function.php添加tree函数

/**
 * 数组层级缩进转换
 * @param array $array
 * @param int   $pid
 * @param int   $level
 * @return array
 */
function tree($array, $pid = 0, $level = 1) {
    static $list = [];
    foreach ($array as $v) {
        if ($v['pid'] == $pid) {
            $v['level'] = $level;
            $list[]     = $v;
            tree($array, $v['id'], $level + 1);
        }
    }
    return $list;
}
#### 控制器
1.在Application/Admin/Controller/目录下创建CateController.class.phpp默认代码如下

2.在cate控制器添加如下方法

    //_initialize()的出现只是方便程序员在写子类的时候避免频繁的使用
    public function _initialize(){
        $cate=D('Cate');
        $catelist=$cate->getLevelList();
        $this->assign('catelist', $catelist);
    }
    // 分类首页，就开始对分类信息进行查询
    public function index(){
        $this->display();
    }
    //分类添加
    public function ajax_addcate(){
        $cate=D('Cate');
        $info=$cate->addcate(I('post.'));
        $this->ajaxReturn(YesorNo($info));
    }
    //修改页面
    public function edi(){
        $cate=D('Cate');
        $cateinfo=$cate->find(I('get.id'));

        $this->assign('cateinfo', $cateinfo);
        $this->display();
    }
    //ajax提交修改方法
    public function ajax_edicate(){
        $cate=D('Cate');
        $info=$cate->where('id='.I('post.id'))->save(I('post.')); 
        $this->ajaxReturn(YesorNo($info));
    }
    //ajax提交删除方法
    public function ajax_delcate(){
        $cate=D('Cate');
        $info=$cate->where('id='.I('post.id'))->delete();
        $this->ajaxReturn(YesorNo($info));
    }
3.在数据库配置文件Application/Common/Config/config.php添加一个配置项

    // 默认JSONP格式返回的处理方法
    'DEFAULT_JSONP_HANDLER' =>  'myJsonpReturn',
4.在Application/Common/Common/目录下创建function.php添加tree函数

function YesorNo($info){
    if (is_numeric($info)){
        $msg['status']  = 200;
        $msg['content'] = '成功';
        return $msg;
    }else{
        $msg['status']  = 201;
        $msg['content'] = $info;
        return $msg;
    }
}
#### 视图
多余的不解释，实战才是检验标准唯一准则
1.在Application/Admin/View/目录下创建Cate目录
2..在Application/Admin/View/Cate目录下创建index.html代码如下

<!--分类信息展示部分-->
<table>
        <tr>
            <th>ID</th>
            <th>一级分类</th>
            <th>排序</th>
            <th>操作</th>
        </tr>
<foreach name="catelist" item="vo" >
        <tr>
            <td>{$vo.id}</td>
            <td><for start="1" end="$vo.level">┡</for>{$vo.catename}</td>
            <td>{$vo.sort}</td>
            <td>
             <div class="button-group"> 
                 <a href="{:U('Admin/Cate/edi?id='.$vo['id'])}"> 修改</a>
                 <a  href="javascript:void(0)" onClick="delCate({$vo.id})">删除</a> 
            </td>
        </tr>
</foreach>
</table>
    
    <!--分类信息添加-->

	<label>上级分类：</label>
		<select name="pid" >
			<option value="0">请选择分类</option>不选择上级分类默认为一级分类
				<foreach name="catelist" item="vo" >
					<option value="{$vo.id}"> <for start="1" end="$vo.level">┡</for>{$vo.catename}</option>
				</foreach>
		</select>
		<label>分类标题：</label><input type="text" class="input w50" name="catename" />
		<button class="button bg-main icon-check-square-o" type="button" onClick="addCate()"> 提交</button>

    
<!--JS函数部分-->
<script>
function delCate(id) {
        layer.confirm('您确定删除此分类吗？', {
            btn: ['删除','取消'] //按钮
        }, function(){
            $.post("{:U('Admin/Cate/ajax_delcate')}",{id:id},function(data){
                if(data.status==200){
                    location.href = location.href;
                    layer.msg('分类删除：'+data.content, {icon: 6});
                }
            })

        }, function(){
        });
    }

    function addCate() {
        var aray = {
            "pid":$("select[name=pid]").val(),
            "catename":$("input[name=catename]").val(),
            "sort":$("input[name=sort]").val(),
        }
        //询问框
        layer.confirm('您确定添加此分类吗？', {
            btn: ['添加','取消'] //按钮
        }, function(){
            $.post("{:U('Admin/Cate/ajax_addcate')}",aray,function(data){
                if(data.status==200){
                    location.href = location.href;
                    layer.msg('分类添加：'+data.content, {icon: 6});
                }else{
                    layer.msg('错误：'+data.content, {icon: 5});
                }
            })

        }, function(){
          
        });
    }
</script>    
2..在Application/Admin/View/Cate目录下创建edi.html代码如下

<!--Html代码部分-->

<form method="post" class="form-x" action="">
	<label>上级分类：</label>
		<select name="pid" >
			<option value="0">请选择分类</option>不选择上级分类默认为一级分类
          <foreach name="catelist" item="vo" >
              <option value="{$vo.id}" <if condition="$vo['id'] eq $cateinfo['pid']"> selected="selected"</if>> <for start="1" end="$vo.level">┡</for>{$vo.catename}						</option>
          </foreach>
		</select>
	<label>分类标题：</label><input type="text" class="input w50" name="catename"  value="{$cateinfo.catename}"/>
	<label>排序：</label><input type="text" class="input w50" name="sort" value="{$cateinfo.sort}"  data-validate="number:排序必须为数字" />
	<button class="button bg-main icon-check-square-o" type="button" onClick="edicate()"> 提交</button>
</form>


<!--JS部分-->
<script>
    function edicate() {
        var aray = {
			"id":{$cateinfo.id},
            "pid":$("select[name=pid]").val(),
            "catename":$("input[name=catename]").val(),
            "sort":$("input[name=sort]").val(),
        }
        //询问框
        layer.confirm('您确定修改此分类吗？', {
            btn: ['添加','取消'] //按钮
        }, function(){
            $.post("{:U('Admin/Cate/ajax_edicate')}",aray,function(data){
            	if(data.status==200){
                    location.href = location.href;
                    layer.msg('分类修改：'+data.content, {icon: 6});
                }else{
                    layer.msg('错误：'+data.content, {icon: 5});
                }
            })

        }, function(){
            
        });
    }
</script>
重点提醒：
1.需要导入jq库，至少需要1.8以上
　　jQ下载地址：http://jquery.com/

2.需要导入layer
　　layer下载地址：http://layer.layui.com/

3.其他文件就是你模板样式
### 文件上传
#### 上传接口
<?php
namespace app\api\controller;

use think\Controller;
use think\Session;

class Upload extends Controller {

    protected function _initialize() {
      //此处要要进行是否进行登陆，如果没有登录跳转到登录部分，如果登录才能执行下面的上传操作
    }
    /**
     * 上传缩略图
     * @return \think\response\Json
     */
    public function uploadThumb() {
        $file = $this->request->file('file');
        $info = $file->move(ROOT_PATH . 'public' . DS . 'uploads');

        if ($info) {
            $result = [
                'code'     => 0,
                'msg'      => '上传成功',
                'filename' => '/public/uploads/' . str_replace('\\', '/', $info->getSaveName())
            ];
        } else {
            $result = [
                'code' => -1,
                'msg'  => $file->getError()
            ];
        }

        return json($result);
    }
#### 视图
导入必要文件

<link rel="stylesheet" href="/tp5/public/static/layui/css/layui.css">
<script src="/tp5/public/static/js/jquery.min.js"></script>
<script src="/tp5/public/static/layui/layui.js"></script>
html源代码

<div class="layui-form-item">
    <label class="layui-form-label">缩略图</label>
    <div class="layui-input-block">
        <input type="text" name="thumb" value="" class="layui-input layui-input-inline" id="thumb">
        <input type="file" name="file" class="layui-upload-file">
    </div>
</div>
js源代码

<script>
 layui.use('upload', function(){
    layui.upload({
        url: "URL",//上传接口
        ext: 'jpg|png|gif',//限制文件
        success: function (result) {
            document.getElementById('thumb').value = result.filename;
        }
    });
 });
</script>
### 表单提交
#### 视图设计
1.导入必要的CSS和JS文件

<link rel="stylesheet" href="/tp5/public/static/layui/css/layui.css">
<script src="/tp5/public/static/js/jquery.min.js"></script>
<script src="/tp5/public/static/layui/layui.js"></script>
2.HTML源代码

<form class="layui-form" action="">
    <div class="layui-form-item">
        <label class="layui-form-label">sms_type</label>
        <div class="layui-input-block">
            <input type="text" name="sms_type" required  lay-verify="required" placeholder="请输入短信类型，传入值请填写normal" autocomplete="off" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item">
        <div class="layui-input-block">
            <button class="layui-btn" lay-submit lay-filter="demo">提 交</button>
            <button type="reset" class="layui-btn layui-btn-primary">重置</button>
        </div>
    </div>
</form>
2.JS源代码

<script>
    layui.use('form', function(){
        var form = layui.form();
        //监听提交
        form.on('submit(*)', function(data){
            $.ajax({
                url:data.form.action,
                type:data.form.method,
                data: data.field,
                success: function (info) {
                   if (info.code === 1) {
                       setTimeout(function () {
                          location.href = info.url;
                       }, 1000);
                  }
                    layer.msg(info.msg);
                }
            });
            return false;
        });
    });
</script>
#### 控制器
//复杂的的业务逻辑，最终得到$info变量
 if($info){
	$this->success('成功');
 }else{
	$this->error('失败');
 }
### 清除缓存
清除缓存
准备条件
layui插件 http://www.layui.com/

html代码

<a href="javascript::void(0)" onclick="clearPhp(this)" data-GetUrl="{:url('login/clear')}">清楚缓存</a>
js代码

<script>
    function clearPhp(obj) {
        var url=obj.getAttribute('data-GetUrl');
        //询问框
        layer.confirm('您确定要清除吗？', {
                    btn: ['确定','取消'] //按钮
                },
                function(){
                    $.get(url,function(info){
                        if(info.code === 1){
                            setTimeout(function () {location.href = info.url;}, 1000);
                        }
                        layer.msg(info.msg);
                    });
                },
                function(){});
    }
</script>
控制器中的方法

    /**
     * 清除缓存
     */
    public function clear() {
        if (delete_dir_file(CACHE_PATH) || delete_dir_file(TEMP_PATH)) {
            $this->success('清除缓存成功');
        } else {
            $this->error('清除缓存失败');
        }
    }
common中的方法

/**
 * 循环删除目录和文件
 * @param string $dir_name
 * @return bool
 */
function delete_dir_file($dir_name) {
    $result = false;
    if(is_dir($dir_name)){
        if ($handle = opendir($dir_name)) {
            while (false !== ($item = readdir($handle))) {
                if ($item != '.' && $item != '..') {
                    if (is_dir($dir_name . DS . $item)) {
                        delete_dir_file($dir_name . DS . $item);
                    } else {
                        unlink($dir_name . DS . $item);
                    }
                }
            }
            closedir($handle);
            if (rmdir($dir_name)) {
                $result = true;
            }
        }
    }

    return $result;
}
### 状态值修改
状态值修改
异步修改状态值
准备条件
http://www.layui.com/

粘贴代码开始

html前端部分

<td class="layui-form">
 <font color="green"><strong>
         <input type="checkbox" {if condition="$vo.open==1"} checked{/if}   name="switch" lay-skin="switch" data-urls='{:url('Spcpackage/updatestatus',['id'=>$vo['id']])}' lay-text="开启|关闭">
 </strong></font>
</td>
后台控制器部分

    function updatestatus($id){
        Db('Spcpackage')->where(['id' => $id])->update(['open'=>input('open')]);
        $info=Db('Spcpackage')->where(['id' => $id])->find();
        if ($info['open']==1){
            $this->success('正在开启');
        }else{
            $this->error('正在关闭');
        }
    }
layui+js部分

	layui.use(['form'], function(){
	  var form = layui.form
	  //监听指定开关
	  form.on('switch', function(data){
	  	var url=this.getAttribute('data-urls');
	    var open=this.checked ? '1' : '0'
	  			//询问框
		layer.confirm('您确定要更改吗？', {
			  	btn: ['确定','取消'] //按钮
			}, 
			function(){
				$.get(url,{open:open},function(info){
					if(info.code === 1){
						setTimeout(function () {location.href = info.url;}, 1000);
					}
					layer.msg(info.msg);
				});
			}, 
			function(){});
	  });
	});
### 数据库备份还原
### 完整的增删查改
完整的增删查改
准备条件
下载thinkphp5框架http://www.thinkphp.cn/

模型

<?php

namespace app\model;

use think\Model;
class Placard extends Model
{
    // 定义时间戳字段名

    protected $autoWriteTimestamp = true;// 关闭自动写入时间戳
}
验证机制

<?php
namespace app\common\validate;
use think\Validate;

class Placard extends Validate{
    protected $rule=[


    ];
    protected $message=[

    ];
    
    /**
     * 自定义验证规则
     * @param $value
     * @return bool
     */
    protected function checkPhone($value)
    {
       return preg_match("/^1[0345789]{1}\d{9}$/",$value)?true:false;
    }
}
增加操作


function add(){
    $data['agent_id']= input('agent_id');
    $data['textarea']= input('textarea');
    $validate_result = $this->validate($data,'Placard');
    if ($validate_result!==true){
        $this->error($validate_result);
    }else{
        if (PlacardMoble::create($data)){
            $this->success('发布成功');
        }else{
            $this->error('发布失败');
        }
    }
}
修改操作

    public function update()
    {
        $placard = PlacardMoble::get(11);
        $placard->agent_id=1;
        $placard->textarea=33;
        $validate_result = $this->validate($placard,'Placard');
        if ($validate_result!==true){
            $this->error($validate_result);
        }else{
            if ( $placard->save()){
                $this->success('更新成功');
            }else{
                $this->error('更新失败');
            }
        }
    }
删除操作

   public function del($id){
       if ( @PlacardMoble::get($id)->delete()){
           $this->success('删除成功');
       }else{
           $this->error('删除失败');
       }
   }
### 查询语句
查询语句
文章表tp_article

CREATE TABLE `tp_article` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '文章ID',
  `cid` smallint(5) unsigned NOT NULL DEFAULT '1' COMMENT '分类ID',
  `title` varchar(255) NOT NULL DEFAULT '' COMMENT '标题',
  `content` longtext COMMENT '内容',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='文章表';
文章分类表tp_cate

CREATE TABLE `tp_cate` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `pid` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '上级分类ID',
  `name` varchar(50) NOT NULL COMMENT '分类名称',
   signed NOT NULL DEFAULT '0' COMMENT '排序',
   PRIMARY KEY (`id`),
   UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='分类表';
查询语句总结
1.JOIN查询

INNER JOIN: 等同于 JOIN（默认的JOIN类型）,如果表中有至少一个匹配，则返回行
LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
FULL JOIN: 只要其中一个表中存在匹配，就返回行
$resul=Db::table('tp_Article')
       ->join('tp_cate', 'tp_article.cid=tp_cate.id')
       ->select();
       
//完整sql语句       
SELECT * FROM `tp_Article` INNER JOIN `tp_cate` ON `tp_Article`.`cid`=`tp_cate`.`id`
2.distinct查询
用于返回唯一不同的值

$result=  Db::table('tp_Article')->distinct(true)->field('title')->select();

//完整sql语句   
SELECT DISTINCT  `title` FROM `tp_Article`
3.fetchSql查询
用于直接返回SQL语句

$result = Db::table('tp_Article')->fetchSql(true)->find(1);

输入
 string(53) "SELECT * FROM `tp_Article` WHERE  `id` = 1 LIMIT 1   "
4.getTableInfo查询
可以获取表信息，信息类型 包括 fields,type,bind,pk，

result= Db::getTableInfo('tp_Article');

//完整sql语句 
SHOW COLUMNS FROM `tp_Article`
5.view视图查询
视图查询可以实现不依赖数据库视图的多表查询，并不需要数据库支持视图

result=  Db::view('tp_Article',['id'=>'aid','cid','title'])
         ->view('tp_cate','id,pid,name','tp_cate.id=tp_Article.cid','LEFT')
         ->select();
### 多语言支持
多语言支持
1.多语言通过行为Behavior支持/ThinkPHP/Library/Behavior/CheckLangBehavior.class.php

2.语言包一共有4种，后定义的要覆盖先定义的(类似配置文件Config.php覆盖/ThinkPHP/Conf/convention.php)

3.在config.php里面开启多语言支持

'LANG_SWITCH_ON'   =>  true,    // 开启语言包功能
'LANG_AUTO_DETECT' =>  true,    // 自动侦测语言开启多语言功能后有效
 'LANG_LIST'           =>  'zh-cn,zh-tw',  // 允许切换的语言列表用逗号分隔
 'VAR_LANGUAGE'      =>  'la',     // 默认语言切换变量
4.确保行为Behavior代码执行

4.1手动启动该CheckLangBehavior.class.php行为

4.2 home/Common/conf/tags.php

<?php        
    returnarray(   
    // 添加下面一行定义即可    
    // 'app_begin' =>array('Behavior\CheckLang'),  
    // 如果是3.2.1版本 需要改成    //
    'app_begin' =>array('Behavior\CheckLangBehavior'),
           
     );
5语言包4个等级

"./ThinkPHP/Lang/zh-cn.php"//默认调用的语言包

"./Application/Common/Lang/zh-cn.php"//读取公共语言包

"./Application/Home/Lang/zh-cn.php"//读取指定模块语言包

"./Application/Home/Lang/zh-cn/index.php"//读取指定模块具体控制器对于的语言包

6获取语言变量信息

6.1 L()快捷函数获取所有的语言变量

6.2 Assign()传递语言变量到模版进行输出

6.3 {$Think.lang.变量名称 }

6.4 每个语言对应一个语言包

7URL访问和展示

cn的访问路径：http://localhost/index.php/home/Index/index/la/zh-cn

tw的访问路径：http://127.0.0.1/index.php/home/Index/index/la/zh-tw
### JpGraph图表类库
JpGraph图表类库
专门提供图表的类库。它使得作图变成了一件非常简单的事情，你只需从数据库中取出相关数据，定义标题，图表类型，然后的事情就交给JpGraph，只需掌握为数不多的JpGraph内置函数（可以参照JpGraph附带例子学习），就可以画出非常炫目的图表！

下载地址
https://github.com/huasofoundries/jpgraph

引入类库

require_once "/src/jpgraph.php";                  //核心文件
require_once "/src/jpgraph_line.php";             //线性图文件
引入数据

$data=array(1=>1,...);
得到Graph对象(创建画布)
$graph=new Graph(w,h); //w-画布长；h-画布宽

设置X和Y轴样式及Y轴的最大值最小值

$graph->SetScale($aAxisType,$min,$max);//如：$aAxisType='textint';则x坐标样式为text，y坐标样式为int
设置图像样式，如加入阴影
$graph->SetShadow();

设置图像边界范围
$graph->img->setMargin($up,$right,$down,$left);//顺时针填充值

设置标题
$graph->title->Set($title);//中文参见问题解决

得到曲线实例(插入数据)
$linePlot=new LinePlot($data);

将曲线加入到图像中
$graph->Add($linePlot);

设置曲线的颜色
$linePlot->setColor($color);//代码位置参见问题解决

设置坐标轴名称

$graph->xaxis->title->Set($xName); //X坐标轴名称
$graph->yaxis->title->Set($yName);//y坐标轴名称
设置曲线的图例

$linePlot->SetLegend($legend);//中文参见问题解决

设置图例样式
$graph->legend->setlayout(LEGEND_HOR);

设置图例位置
$graph->legend->Pos(0.45,0.9,"center","bottom");

输出

$graph->Stroke();//将图像输出到浏览器
$graph->Stroke($path);//如：$graph->Stroke('./test.png');保存到当前目录下
### 微信支付
微信支付
需要吧下面的源码复制到extend/weixin/wxpay目录下，或者自己修改命名空间。
	   $wxconfig=[
        'APPID'=>'',
        'MCHID'=>'',
        'KEY'=>'',
        'APPSECRET'=>'',
        'SSLCERT_PATH'=>'',
        'SSLKEY_PATH'=>''
      ];
参数说明
appid和APPSECRET2个参数的作用：获取微信用户必备的2个参数
MCHID和KEY一起配合appid和APPSECRET才能完成整个支付
SSLCERT_PATH和SSLKEY_PATH

JSPAY支付demo
获取用户的openid
$Oauth=new \weixin\wxpay\Oauth($wxconfig);
	    if(Cookie::has('openid')){	
			  $openid=Cookie::get('openid');

        }else{
        	    $userinfo= $Oauth->getWxuser();
			     $openid=$userinfo['openid'];
			     Cookie::set('openid',$openid,3600);
        }
统一下单
       $values['openid']=$openid;
       $values['attach']='支付测试';
       $values['body']='JSAPI支付测试';
       $values['notify_url']='http://www.kkk.cn/';
	   $values['spbill_create_ip']=$_SERVER['REMOTE_ADDR'];
	   $values['time_start']=date("YmdHis");
	   $values['time_expire']=date("YmdHis", time() + 600);
       $values['out_trade_no']=time();
       $values['total_fee']=1;
	   $values['trade_type']='JSAPI';
       $o=new \weixin\wxpay\Order($wxconfig);
	   $order=$o->setrequests($values)->unifiedorder();
根据统一下单的订单号 获取获取JsApi$getParameters参数，展示到前台模板
	   $jspay=new \weixin\wxpay\Jspay($wxconfig);
	   $jsApiParameters = $jspay->GetJsApiParameters($order);
       return $this->fetch('index',['jsApiParameters'=>$jsApiParameters]);
前台页面进行点击支付，或者自动弹出支付，需要自己定义
  <center><h1 onclick='callpay()'>点击支付</h1></center>
  <script type="text/javascript">	
    function callpay()
	{
		if (typeof WeixinJSBridge == "undefined"){
		    if( document.addEventListener ){
		        document.addEventListener('WeixinJSBridgeReady', jsApiCall, false);
		    }else if (document.attachEvent){
		        document.attachEvent('WeixinJSBridgeReady', jsApiCall); 
		        document.attachEvent('onWeixinJSBridgeReady', jsApiCall);
		    }
		}else{
		    jsApiCall();
		}
	}
    	
	//调用微信JS api 支付
	function jsApiCall()
	{
		WeixinJSBridge.invoke(
			'getBrandWCPayRequest',{$jsApiParameters},
			function(res){
				WeixinJSBridge.log(res.err_msg);
				alert(res.err_code+res.err_desc+res.err_msg);
			}
		);
	}
	</script>
支付回调
$raw_xml = file_get_contents('php://input');
libxml_disable_entity_loader(true); //libxml_disable_entity_loader()作用是设置是否禁止从外部加载XML实体，设为true就是禁止，目的是防止XML注入攻击（详情自行百度）
 $ret = json_decode(json_encode(simplexml_load_string($raw_xml, 'SimpleXMLElement', LIBXML_NOCDATA)), true);
//支付成功之后处理
if($ret['return_code'] == "SUCCESS"){
   //自己系统业务逻辑
   
   //给微信支付返回成功操作
	echo '<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg></xml>';
}
退款
//退款申请接口中，out_trade_no、transaction_id至少填一个！
       $values['out_trade_no']='';
//商户退款单号
       $values['out_refund_no']=;
//订单金额	
       $values['total_fee']=
 //退款金额
       $values['refund_fee']=
//退款账户
	   $values['op_user_id']=$wxconfig['MCHID'];

       $o=new \weixin\wxpay\Order($wxconfig);
	   $refund=$o->setrequests($values)->refund();
### 下载远程地址中的图片
下载远程地址中的图片
需要准备2个类

效仿微擎Ihttp请求方法

效仿微擎File方法

实现方法

    $imgUrl="http://p9.pstatp.com/large/pgc-image/1528195330859d2ea3d329a";
    $imgUrl = htmlspecialchars($imgUrl);
    $imgUrl = str_replace("&amp;","&",$imgUrl);
    $f=new Jqfile();
    $f->file_remote_attach_fetch($imgUrl);
### URL重写隐藏入口文件
URL重写隐藏入口文件
一、Apache
httpd.conf配置文件中加载了mod_rewrite.so模块
AllowOverride None 将None改为 All
把下面的内容保存为.htaccess文件放到应用入口文件的同级目录下
<IfModule mod_rewrite.c>
  Options +FollowSymlinks -Multiviews
  RewriteEngine On
 
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteRule ^(.*)$ index.php/$1 [QSA,PT,L]
</IfModule>
如果用的phpstudy，规则如下：

<IfModule mod_rewrite.c> 
    Options +FollowSymlinks -Multiviews 
    RewriteEngine on 
    RewriteCond %{REQUEST_FILENAME} !-d 
    RewriteCond %{REQUEST_FILENAME} !-f 
    RewriteRule ^(.*)$ index.php [L,E=PATH_INFO:$1] 
</IfModule>
二、Nginx
在Nginx低版本中，是不支持PATHINFO的，但是可以通过在Nginx.conf中配置转发规则实现：

location / { // …..省略部分代码
   if (!-e $request_filename) {
   rewrite  ^(.*)$  /index.php?s=/$1  last;
   break;
    }
}
其实内部是转发到了ThinkPHP提供的兼容URL，利用这种方式，可以解决其他不支持PATHINFO的WEB服务器环境。

如果你的应用安装在二级目录，Nginx的伪静态方法设置如下，其中youdomain是所在的目录名称。

location /youdomain/ {
    if (!-e $request_filename){
        rewrite  ^/youdomain/(.*)$  /youdomain/index.php?s=/$1  last;
    }
}
三、IIS
如果你的服务器环境支持ISAPI_Rewrite的话，可以配置httpd.ini文件，添加下面的内容：
RewriteRule (.*)$ /index.php?s=$1 [I]
在IIS的高版本下面可以配置web.Config，在中间添加rewrite节点：

<rewrite>
 <rules>
 <rule name="OrgPage" stopprocessing="true">
 <match url="^(.*)$">
 <conditions logicalgrouping="MatchAll">
 <add input="{HTTP_HOST}" pattern="^(.*)$">
 <add input="{REQUEST_FILENAME}" matchtype="IsFile" negate="true">
 <add input="{REQUEST_FILENAME}" matchtype="IsDirectory" negate="true">
 </add></add></add></conditions>
 <action type="Rewrite" url="index.php/{R:1}">
 </action></match></rule>
 </rules>
</rewrite>
四、其他情况
如果你没有修改服务器的权限，可以在index.php入口文件做修改，这不是正确的做法，并且不一定成功，视服务器而定，只是在框架执行前补全$_SERVER['PATH_INFO']参数。

$_SERVER['PATH_INFO'] = $_SERVER['REQUEST_URI' ];
原来的访问URL：

http://serverName/index.php/模块/控制器/操作/[参数名/参数值...]
设置后，我们可以采用下面的方式访问：

http://serverName/模块/控制器/操作/[参数名/参数值...]
### 图片水印
图片水印
    const WATER_NORTHWEST = 1; //常量，标识左上角水印
    const WATER_NORTH     = 2; //常量，标识上居中水印
    const WATER_NORTHEAST = 3; //常量，标识右上角水印
    const WATER_WEST      = 4; //常量，标识左居中水印
    const WATER_CENTER    = 5; //常量，标识居中水印
    const WATER_EAST      = 6; //常量，标识右居中水印
    const WATER_SOUTHWEST = 7; //常量，标识左下角水印
    const WATER_SOUTH     = 8; //常量，标识下居中水印
    const WATER_SOUTHEAST = 9; //常量，标识右下角水印


    function mark_pic($imgurl){
        $image = \think\Image::open($imgurl);
        $source='./header_logo.png';
       return $image->water($source,\think\Image::WATER_SOUTHEAST,80)->save($imgurl);
    }
### 整合百度编辑器
整合百度编辑器
    <script type="text/javascript" charset="utf-8" src="/static/ueditor/ueditor.config.js"></script>
    <script type="text/javascript" charset="utf-8" src="/static/ueditor/ueditor.all.min.js"> </script>

    <script id="editor" type="text/plain" ></script>



    <script type="text/javascript">

    //实例化编辑器
        var ue = UE.getEditor('editor',{
            //initialFrameWidth: 1100,   //初始化宽度
            initialFrameHeight: 500,   //初始化高度

            serverUrl:"{:url('index/index/baidu')}",
        });
    </script>
接口

    public function  baidu(){
        $action = $_GET['action'];
        $baidu=new Ueditor();
        switch ($action){
            case "config":
                $result=$baidu->config();
                break;
            case  "uploadimage":
                $result=$baidu->uploadimage();
                break;
            case  "catchimage":
                $result=$baidu->catchimage();
                break;
            default:
                $result = json_encode(['state'=> '请求地址出错']);
                break;
        }
        return json($result);
    }
### 配置信息常见的方式
配置信息常见的方式
写入配置文件
前台

	  <input type="text" name="WEB_COM" value="{:config('web.WEB_COM')}" placeholder="后面不要加斜杠/" autocomplete="off" class="layui-input">

后台

        $path = 'application/extra/web.php';
        $file = (include $path);
        $config = array(
        	'WEB_TIT' => input('WEB_TIT'), 
            'WEB_COM' => input('WEB_COM'));
        $res = array_merge($file, $config);
        $str = '<?php return [';
        foreach ($res as $key => $value) {
            $str .= '\'' . $key . '\'' . '=>' . '\'' . $value . '\'' . ',';
        }
        $str .= ']; ';
        if (file_put_contents($path, $str)) {
            return tpta('修改成功');
        } else {
            return tptb('修改失败');
        }
写入数据库
前台代码

 <input type="text" name="site_config[site_title]" value="{$site_config.site_title}" required  lay-verify="required" placeholder="请输入网站标题" autocomplete="off" class="layui-input">

后台代码

    /**
     * 显示资源列表
     *
     * @return \think\Response
     */
    public function index()
    {
        if (Cache::has('site_config')){
            //查询缓存
            $System['value']=Cache::get('site_config');
        }else{
            //查询数据库
            $System=SystemModel::where('name', 'site_config') -> field('value')->find();
        }
        $site_config = unserialize($System['value']);
        return $this->fetch('index', ['site_config' => $site_config]);
    }

    /**
     * 提交配置
     */
    public function updateSiteConfig() {
        $site_config   = $this->request->post('site_config/a');
        $value=serialize($site_config);
        if (SystemModel::where('name', 'site_config')->setField('value' , $value)) {
            Cache::set('site_config', $value);
            $this->success('提交成功');
        } else {
            $this->error('提交失败');
        }
    }

### HTTP 断点续传（PHP实现）
HTTP 断点续传（PHP实现）
所谓断点续传，也就是要从文件已经下载的地方开始继续下载。在以前版本的 HTTP 协议是不支持断点的，HTTP/1.1 开始就支持了。一般断点下载时才用到 Range 和 Content-Range 实体头。

不使用断点续传

get /down.zip http/1.1
accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-
excel, application/msword, application/vnd.ms-powerpoint, */*
accept-language: zh-cn
accept-encoding: gzip, deflate
user-agent: mozilla/4.0 (compatible; msie 5.01; windows nt 5.0)
connection: keep-alive
服务器收到请求后，按要求寻找请求的文件，提取文件的信息，然后返回给浏览器，返回信息如下：

HTTP/1.1 200 Ok
content-length=106786028
accept-ranges=bytes
date=mon, 30 apr 2001 12:56:11 gmt
etag=w/"02ca57e173c11:95b"
content-type=application/octet-stream
server=microsoft-iis/5.0
last-modified=mon, 30 apr 2001 12:56:11 gmt
使用断点续传

GET /down.zip HTTP/1.0
User-Agent: NetFox
RANGE: bytes=2000070-
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
服务器收到这个请求以后，返回的信息如下：

HTTP/1.1 206 Partial Content
content-length=106786028
content-range=bytes 2000070-106786027/106786028
date=mon, 30 apr 2001 12:55:20 gmt
etag=w/"02ca57e173c11:95b"
content-type=application/octet-stream
server=microsoft-iis/5.0
last-modified=mon, 30 apr 2001 12:55:20 gmt
和前面服务器返回的信息比较一下，就会发现增加了一行：

Content-Range=bytes 2000070-106786027/106786028

返回的代码也改为206了，而不再是200了。

HTTP/1.1 206 Partial Content

PHP实现

/**  php下载类,支持断点续传
 *   download: 下载文件
 *   setSpeed: 设置下载速度
 *   getRange: 获取header中Range
 */

class FileDownload{

    /** 下载
     * @param String  $file   要下载的文件路径
     * @param String  $name   文件名称,为空则与下载的文件名称一样
     * @param boolean $reload 是否开启断点续传
     */
    public function download($file, $name='', $reload=false){
        $fp = @fopen($file, 'rb');
        if($fp){
            if($name==''){
                $name = basename($file);
            }
            $header_array = get_headers($file, true);
            //var_dump($header_array);die;
            // 下载本地文件，获取文件大小
            if (!$header_array) {
                $file_size = filesize($file);
            } else {
                $file_size = $header_array['Content-Length'];
            }
            $ranges = $this->getRange($file_size);
            $ua = $_SERVER["HTTP_USER_AGENT"];//判断是什么类型浏览器
            header('cache-control:public');
            header('content-type:application/octet-stream');    

            $encoded_filename = urlencode($name);
            $encoded_filename = str_replace("+", "%20", $encoded_filename);

            //解决下载文件名乱码
            if (preg_match("/MSIE/", $ua) ||  preg_match("/Trident/", $ua) ){               
                header('Content-Disposition: attachment; filename="' .$encoded_filename . '"');
            } else if (preg_match("/Firefox/", $ua)) {
                header('Content-Disposition: attachment; filename*="utf8\'\'' . $name . '"');
            }else if (preg_match("/Chrome/", $ua)) {
                header('Content-Disposition: attachment; filename="' . $encoded_filename . '"');
            } else {
                header('Content-Disposition: attachment; filename="' . $name . '"');
            }
            //header('Content-Disposition: attachment; filename="' . $name . '"');

            if($reload && $ranges!=null){ // 使用续传
                header('HTTP/1.1 206 Partial Content');
                header('Accept-Ranges:bytes');

                // 剩余长度
                header(sprintf('content-length:%u',$ranges['end']-$ranges['start']));

                // range信息
                header(sprintf('content-range:bytes %s-%s/%s', $ranges['start'], $ranges['end'], $file_size));
                //file_put_contents('test.log',sprintf('content-length:%u',$ranges['end']-$ranges['start']),FILE_APPEND);
                // fp指针跳到断点位置
                fseek($fp, sprintf('%u', $ranges['start']));
            }else{
                file_put_contents('test.log','2222',FILE_APPEND);
                header('HTTP/1.1 200 OK');
                header('content-length:'.$file_size);
            }

            while(!feof($fp)){
                //echo fread($fp, round($this->_speed*1024,0));
                //echo fread($fp, $file_size);
                echo fread($fp, 4096);
                ob_flush();
            }

            ($fp!=null) && fclose($fp);
        }else{
            return '';
        }
    }

    /** 设置下载速度
     * @param int $speed
     */
    public function setSpeed($speed){
        if(is_numeric($speed) && $speed>16 && $speed<4096){
            $this->_speed = $speed;
        }
    }

    /** 获取header range信息
     * @param  int   $file_size 文件大小
     * @return Array
     */
    private function getRange($file_size){
        //file_put_contents('range.log', json_encode($_SERVER), FILE_APPEND);
        if(isset($_SERVER['HTTP_RANGE']) && !empty($_SERVER['HTTP_RANGE'])){
            $range = $_SERVER['HTTP_RANGE'];
            $range = preg_replace('/[\s|,].*/', '', $range);
            $range = explode('-', substr($range, 6));
            if(count($range)<2){
                $range[1] = $file_size;
            }
            $range = array_combine(array('start','end'), $range);
            if(empty($range['start'])){
                $range['start'] = 0;
            }
            if(empty($range['end'])){
                $range['end'] = $file_size;
            }
            return $range;
        }
        return null;
    }
}

$obj = new FileDownload();
$obj->download('http://down.golaravel.com/laravel/laravel-master.zip','', true);
### layui.upload上传文件或图片
layui.upload上传文件或图片
1）充分了解三个状态：choose，before，done。
choose）表示文件选择后的回调，注意此时并没有加入上传队列；
before）表示文件上传前的回调，注意此时已经加入上传队列；
done）表示文件上传成功的回调；

2）要使用choose，必须设置为auto为false
这一步就是精华所在了，很多人都不会设置auto，而默认值是true自动上传，自动上传就无法阻止不上传了。
所以，必须要设置auto:false，这样就可以配合choose了，在choose，如果不执行obj.upload(index, file)就不会上传了。

3）代码分享

layui.use(['layer', 'upload'], function () {
    var upload = layui.upload;
    upload.render({
                elem: '#divUpload'
              , url: '/ashx/upload.ashx'
              , multiple: true  //多文件上传
              , accept: "file"
              , data: { action: 'layupload' }
              , auto: false
              , choose: function (obj) {
                  obj.preview(function (index, file, result) {
                      if ($(".fileName[data-filename='" + file.name.toLowerCase() + "']").length > 0) 
                          alert("文件已存在");
                      else
                          obj.upload(index, file);//文件上传
                  });
              }
              , before: function (obj) {
                  alert("文件开始上传，请等待");
              }
              , done: function (res, index, upload) {
                  alert("文件上传成功");
              }, error: function (a, b) {
                  alert("文件上传发生错误");
              }
            });
});
### QQ微信域名防封 预防域名封禁 强制跳转至浏览器
QQ微信域名防封 预防域名封禁 强制跳转至浏览器
打开index 里面输入网址把红名网址加进去就行了
然后打开你的域名在手机QQ里面你就看不到拦截了！
主要是QQ浏览器和手机版的，手机版不拦截了！
源代码下载地址：https://github.com/tp5er/qqweixinfeng

<?php
error_reporting(0);
header('Content-Type: text/html; charset=UTF-8');
header("Cache-Control: no-store, no-cache");
include 'txprotect.php';
if($_GET["r"]==""){
$target =  'http://www.baidu.com/';
}else{
$target =  $_GET["r"];
}


function checkmobile() {
	$useragent = strtolower($_SERVER['HTTP_USER_AGENT']);
	$ualist = array('android', 'midp', 'nokia', 'mobile', 'iphone', 'ipod', 'blackberry', 'windows phone');
	foreach($ualist as $v) {
		if(strpos($useragent, $v) !== false) {
			return true;
		}
	}
	if(strpos($_SERVER['HTTP_ACCEPT'], "VND.WAP") !== false || strpos($_SERVER['HTTP_VIA'],"wap") !== false){
		return true;
	}
	return false;
}
if(strpos($_SERVER['HTTP_USER_AGENT'], 'MicroMessenger')!==false){
echo '<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" style="font-size: 100px;">
<head id="Head1"><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>站点提示</title>
    <!--禁止全屏缩放-->
    <meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" />
    <!--不显示成手机号-->
    <meta name="format-detection" content="telephone=no" />
    <!--删除默认的苹果工具栏和菜单栏-->
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <!--解决UC手机字体变大的问题-->
    <meta name="wap-font-scale" content="no" />
    <!--控制状态栏显示样式-->
    <meta name="apple-mobile-web-app-status-bar-style" content="black" />
	<link href="css/index.css" rel="stylesheet" type="text/css" />
    <script type="text/javascript" src="//cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
    <script type="text/javascript">
$(function ($) {
    setRootFontSize();
});
window.onresize = function () {
    setRootFontSize();
}
function setRootFontSize() {
    $(\'html\').css(\'font-size\', document.body.clientWidth / 15 + \'px\');
}
    </script>
</head>
<body style="background-color: #f5f5f5;">
    <div id="Pan_WX">
        <!--微信访问-->
        <div class="fc_jt">
            <img src="img/jt.png"></div>
               <div class="fc_wz">
                点击屏幕右上角[...]<br />
                用 浏览器 打开 
            </div>  
          <div class="fc_tp">
            <img src="img/wx_az.png"></div>
		</div>
</body>
</html>';}
elseif(strpos($_SERVER['HTTP_USER_AGENT'], 'QQ')!==false){
	echo '<!DOCTYPE html>
<html>
 <head>
  <title>正在打开浏览器....</title>
  <script src="https://open.mobile.qq.com/sdk/qqapi.js?_bid=152"></script>
  <script type="text/javascript"> mqq.ui.openUrl({ target: 2,url: "'.$target.'"}); </script>
 </head>
 <body></body>
</html>';
exit;
}
else{
	exit('<script>window.location.href="'.$target.'";</script>');
}
?>
txprotect.php

<?php
/*
反腾讯网址安全检测系统
Description:屏蔽腾讯电脑管家网址安全检测
Version:2.6
Author:消失的彩虹海
*/
//IP屏蔽
$iptables='977012992~977013247|977084416~977084927|1743654912~1743655935|1949957632~1949958143|2006126336~2006127359|2111446272~2111446527|3418570752~3418578943|3419242496~3419250687|3419250688~3419275263|3682941952~3682942207|3682942464~3682942719|3682986660~3682986663|1707474944~1707606015|1709318400~1709318655|1884967642|1884967620|1893733510|1709332858|1709325774|1709342057|1709341968|1709330358|1709335492|1709327575|1709327041|1709327557|1709327573|1975065457|1902908741|1902908705|3029946827';
$remoteiplong=bindec(decbin(ip2long(real_ip())));
foreach(explode('|',$iptables) as $iprows){
	if($remoteiplong==$iprows)exit('我是阔爱的小承诺。！');
	$ipbanrange=explode('~',$iprows);
	if($remoteiplong>=$ipbanrange[0] && $remoteiplong<=$ipbanrange[1])
		exit('我是阔爱的小承诺。！');
}
//HEADER特征屏蔽
if(preg_match("/manager/", strtolower($_SERVER['HTTP_USER_AGENT'])) || strpos($_SERVER['HTTP_USER_AGENT'], 'Mozilla')===false && strpos($_SERVER['HTTP_USER_AGENT'], 'ozilla')!==false || isset($_SERVER['HTTP_REFERER']) && strpos($_SERVER['HTTP_REFERER'], 'urls.tr.com')!==false || isset($_COOKIE['ASPSESSIONIDQASBQDRC']) || empty($_SERVER['HTTP_USER_AGENT']) || strpos($_SERVER['HTTP_USER_AGENT'], 'HUAWEI G700-U00')!==false && !isset($_SERVER['HTTP_ACCEPT']) || preg_match("/Alibaba.Security.Heimdall/", $_SERVER['HTTP_USER_AGENT'])) {
	exit('我是阔爱的小承诺。！');
}
if(strpos($_SERVER['HTTP_USER_AGENT'], 'iPhone OS 9_3_4')!==false && $_SERVER['HTTP_ACCEPT']=='*/*' || strpos($_SERVER['HTTP_USER_AGENT'], 'iPhone OS 8_4')!==false && $_SERVER['HTTP_ACCEPT']=='*/*' || strpos($_SERVER['HTTP_USER_AGENT'], 'Android 6.0.1')!==false && strpos($_SERVER['HTTP_USER_AGENT'], 'MQQBrowser/6.8')!==false && $_SERVER['HTTP_ACCEPT']=='*/*' || strpos($_SERVER['HTTP_ACCEPT_LANGUAGE'], 'en')!==false && strpos($_SERVER['HTTP_ACCEPT_LANGUAGE'], 'zh')===false || strpos($_SERVER['HTTP_USER_AGENT'], 'iPhone')!==false && strpos($_SERVER['HTTP_USER_AGENT'], 'en-')!==false && strpos($_SERVER['HTTP_USER_AGENT'], 'zh')===false) {
	exit('我是阔爱的小承诺。');
}
if(preg_match("/Windows NT 6.1/", $_SERVER['HTTP_USER_AGENT']) && $_SERVER['HTTP_ACCEPT']=='*/*'|| preg_match("/Windows NT 5.1/", $_SERVER['HTTP_USER_AGENT']) && $_SERVER['HTTP_ACCEPT']=='*/*' || preg_match("/vnd.wap.wml/", $_SERVER['HTTP_ACCEPT']) && preg_match("/Windows NT 5.1/", $_SERVER['HTTP_USER_AGENT'])){
	exit('我是阔爱的小承诺。');
}
function real_ip(){
$ip = $_SERVER['REMOTE_ADDR'];
if(isset($_SERVER['HTTP_X_FORWARDED_FOR']) && preg_match_all('#\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}#s', $_SERVER['HTTP_X_FORWARDED_FOR'], $matches)) {
	foreach ($matches[0] AS $xip) {
		if (!preg_match('#^(10|172\.16|192\.168)\.#', $xip)) {
			$ip = $xip;
			break;
		}
	}
} elseif (isset($_SERVER['HTTP_CLIENT_IP']) && preg_match('/^([0-9]{1,3}\.){3}[0-9]{1,3}$/', $_SERVER['HTTP_CLIENT_IP'])) {
	$ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (isset($_SERVER['HTTP_CF_CONNECTING_IP']) && preg_match('/^([0-9]{1,3}\.){3}[0-9]{1,3}$/', $_SERVER['HTTP_CF_CONNECTING_IP'])) {
	$ip = $_SERVER['HTTP_CF_CONNECTING_IP'];
} elseif (isset($_SERVER['HTTP_X_REAL_IP']) && preg_match('/^([0-9]{1,3}\.){3}[0-9]{1,3}$/', $_SERVER['HTTP_X_REAL_IP'])) {
	$ip = $_SERVER['HTTP_X_REAL_IP'];
}
return $ip;
}
body, div, form, input, li, ol, p, textarea, ul
{
    margin: 0;
    padding: 0;
}

body
{
    background: #ffffff;
    color: #3f3f3f;
    font-family: Apple LiGothic Medium,SimHei,Geneva,Arial,Helvetica,sans-serif;
    -webkit-tap-highlight-color: transparent;
    -webkit-tap-highlight-color: transparent;
    -webkit-touch-callout: none;
    -webkit-appearance: none;
    width: 100%;
    font-size: 16px;
}

a, button, input
{
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    -webkit-tap-highlight-color: transparent;
    -webkit-user-modify: read-write-plaintext-only;
    -webkit-touch-callout: none;
    -webkit-appearance: none;
    outline: none;
}
a: focus, input: focus
{
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    -webkit-tap-highlight-color: transparent;
    -webkit-user-modify: read-write-plaintext-only;
    -webkit-touch-callout: none;
    -webkit-appearance: none;
    border: 1px solid #FFFFFF;
    outline: none;
}


ul li
{
    padding: 0px;
    margin: 0px;
}

li
{
    list-style: none;
}

img
{
    border: 0 none;
}
span
{
    padding: 0px;
    margin: 0px;
}




.tx_top
{
    height: 2.8rem;
    margin: 0 auto;
    position: relative;
    background: url(../img/tx_bg.png) no-repeat;
    background-size: 15rem auto;
    overflow: hidden;
}
.top_bg
{
    width: 15rem;
    height: 5.8rem;
    margin: 0 auto;
    position: relative;
    background: url(../img/top_bg.png) no-repeat;
    background-size: 15rem auto;
    overflow: hidden;
}

.srk_bg
{
    width: 15rem;
    height: 7.4rem;
    margin: 0 auto;
    position: relative;
    background: url(../img/srk_bg.png) no-repeat;
    background-size: 15rem auto;
    overflow: hidden;
}
.hdgz_bg
{
    width: 15rem;
    height: 8.28rem;
    margin: 0 auto;
    position: relative;
    background: url(../img/hdgz_bg.png) no-repeat;
    background-size: 15rem auto;
    overflow: hidden;
}

.tx_con
{
    padding-left: 0.8rem;
    padding-top: 0.9rem;
}
.tx_top_tx
{
    width: 1.7rem;
    height: 1.7rem;
    border-radius: 1.6rem;
    border: 0.12rem solid #f6dbdd;
    float: left;
}
.tx_top_tx img
{
    width: 1.7rem;
    height: 1.7rem;
    border-radius: 1.6rem;
}
.tx_top_wz
{
    font-size: 0.52rem;
    color: #FFF;
    line-height: 0.6rem;
    padding-left: 2.8rem;
    padding-right: 0.9rem;
    padding-top: 0.5rem;
}





.wxhd_con_srk
{
    width: 12.4rem;
    margin: 0 auto;
    padding-top: 0.8rem;
}
.wxhd_con_srk_l
{
    background-color: #ffffff;
    border-radius: 0.1rem; height: 1.38rem;
    width: 12.4rem;
}

.wxhd_con_srk_l ul li.srk_nr
{
    float: left;
    width: 12rem;
    padding-left: 0.4rem;
}
.wxhd_con_srk_l ul li.srk_nr input
{ height: 1.38rem;
    width: 12rem;
    border: 0px;
    font-size: 0.6rem;
    text-align: center;
}

.wxhd_con_srk_l ul li.srk_nr2
{
    float: left;
    width: 7rem;
    padding-left: 0.4rem;
}
.wxhd_con_srk_l ul li.srk_nr2 input
{ height: 1.38rem;
    width: 7rem;
    border: 0px;
    font-size: 0.6rem;
}
.wxhd_con_srk_l ul li.srk_nr3
{
    float: right;
    width: 5rem;
    text-align: center;
    line-height: 1.38rem;
    font-size: 0.6rem;
    color: #FFF;
    background-color: #e74129;
    cursor: pointer;
    border-radius: 0rem 0.1rem 0.1rem 0rem;
}
.wxhd_wc
{
    width: 100%;
    padding-top: 1.4rem;
}
.wxhd_wc_an
{
    width: 12.4rem;
    margin: 0 auto;
    text-align: center; height: 1.38rem;
    line-height: 1.38rem;
    font-size: 0.7rem;
    color: #b71f2d;
    border-radius: 0.1rem;
    background-color: #fcc602;
}
.cwts
{
    height: 0.6rem;
    color: #F00;
    font-size: 0.6rem;
    padding-top: 0.4rem;
    text-align: center;
}
.xxtjh
{
    padding-top: 1.5rem;
    text-align: center;
    font-size: 0.6rem;
    padding-bottom: 0.15rem;
    line-height: 1.0rem;
    color: #b91422;
}
.xxtjh span
{
    color: #ff0003;
    font-size: 0.7rem;
}
.wxhd_wc_an2
{
    width:12.4rem;
    margin: 0 auto;
    text-align:center; height: 1.38rem;
    line-height: 1.38rem;
    font-size: 0.7rem;
    color: #fdcb5e;
    border-radius: 0.1rem;
    background-color: #e74129;
}
.fc_jt
{
    width: 15rem;
    height: 4.28rem;
}
.fc_jt img
{
    width: 15rem;
    height: 4.28rem;
}

.fc_wz
{
    height: 6.9rem;
    line-height: 1.0rem;
    font-size: 0.7rem;
    text-align: center;
    color: #333333;
}
.fc_tp
{
    width: 12.44rem;
    height: 10.rem;
    margin: 0 auto;
}
.fc_tp img
{
    width: 12.44rem;
    height: 10.rem;
    text-align: center;
}
.wxhd_wc2
{
    width: 100%;
    padding-top: 0.3rem;
}



.all_main
{
    text-align: center;
    padding-top: 130px;
}
.all_main01
{
    text-align: center;
    padding-top: 30px;
    font-size: 28px;
    color: #999595;
    margin-bottom: 20px;
}
.all_main01 span
{
    color: #9dbad0;
}
.all_main01 a
{
    text-decoration: none;
}

.all_main02
{
    border-radius: 40px;
    -moz-border-radius: 40x; /* Firefox */
    -webkit-border-radius: 40px; /* Safari 和 Chrome */
    background-color: #9dbad0;
    width: 400px;
    height: 60px;
    line-height: 60px;
    margin: 0 auto;
    color: #FFF;
    font-size: 24px;
    cursor: pointer;
    text-align: center;
}

.zxyq
{
   
    width: 15rem;
    background-color: #dd3149;
}
.zxyq_title
{
    height: 2.06rem;
    width: 15rem;
    text-align: center;
    background: url(../img/zxyq_title.jpg) center center no-repeat;
    background-size: 5.3rem auto;
}
.zxyq_main
{
    margin: 0 auto;
    width: 12.82rem;
    background-color: #e1485e;
    padding-left: 0.8rem;
    padding-right: 0.8rem;
    padding-top: 0.8rem;
	padding-bottom: 0.8rem;
}

.zxyq_main ul li
{
    clear: both;
    color: #ffffff;
    font-size: 0.56rem;
    line-height: 1.45rem;
	overflow:hidden;
}
.imgtx
{
    width: 1rem;
    height: 1rem;
    border-radius: 50%;
    overflow: hidden;
    border: #FFF 0.04rem solid;
    float: left;
    margin-top: 0.2rem;
}
.imgtx img
{
    width: 1rem;
    height: 1rem;
}
.nicheng
{
    width: 2.4rem;
    height: 1rem;
    margin-left: 0.4rem;
    float: left;
}
.mes
{
    width: 5.3rem;
    float: left;
}
.time
{
    width:3rem;
    height: 1rem;
    margin-left: 0.4rem;
    color: #f5adb7;
    float: right;
    text-align: right;
}

### 蜘蛛篇
蜘蛛篇
微软
“msnbot-media/1.1 (+http://search.msn.com/msnbot.htm)”
msnbot，大多数已经被bingbot替代了，现在偶尔还可以看到。

“Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)”
bing，必应

搜搜
“Sosospider+(+http://help.soso.com/webspider.htm)”
腾讯搜搜

“Sosoimagespider+(+http://help.soso.com/soso-image-spider.htm)”
搜搜图片

雅虎
“Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)”
雅虎英文

“Yahoo! Slurp China”
“Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)”
雅虎中国

搜狗
“http://pic.sogou.com” “Sogou Pic Spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07)”
搜狗图片

“Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)”
搜狗，搜狗的蜘蛛程序做的很不好，总是进入死循环，已经分别在 robots.txt 和 设置中屏蔽掉

Google
“Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)”
Google

“Googlebot-Image/1.0”
Google图片搜索

“Mediapartners-Google”
未知

“FeedBurner/1.0 (http://www.FeedBurner.com)”
feedburner

“AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 3 0 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari”
Adwords移动网络

百度
“Baiduspider-image+(+http://www.baidu.com/search/spider.htm)”
百度图片

“Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)”
亲爱的百度蜘蛛

“Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.8;baidu Transcoder) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729)”
baidu+Transcoder 是用户用手机浏览网站留下的记录，Transcoder 是代码转换器，把网站转码成手机用户上网看到的网页留下的记录

360
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider
360搜索

其他搜索引擎
“Mozilla/5.0 (compatible; YoudaoBot/1.0; http://www.youdao.com/help/webmaster/spider/; )”
网易有道

“Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)”
来自瑞典的搜索引擎，网站看起来很不错，http://www.entireweb.com

~“jikespider \”Mozilla/5.0”~
即刻搜索，原人民搜索，搜索引擎国家队，已倒闭

“Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)”
俄罗斯yandex

Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)
宜搜，不认识，一直不停抓取，已屏蔽

其他已知bot
“HuaweiSymantecSpider/1.0+DSE-support@huaweisymantec.com+(compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR ; http://www.huaweisymantec.com/cn/IRL/spider)”
华为赛门铁克蜘蛛，是华为赛门铁克科技有限公司网页信誉分析系统的一个页面爬取程序，其作用是用于爬取互联网网页并进行信誉分析，从而检查该网站上的是否含有恶意代码。
http://baike.baidu.com/view/5994606.htm

qiniu-imgstg-spider-1.0
七牛镜像蜘蛛

“xFruits/1.0 (http://www.xfruits.com)”
xFruits，聚合rss用的

Feedly/1.0 (+http://www.feedly.com/fetcher.html; like FeedFetcher-Google)
Feedly，Google Reader 关闭后一直用这个

Mozilla/5.0 (compatible;YoudaoFeedFetcher/1.0;http://www.youdao.com/help/reader/faq/topic006/;1 subscribers;)
有道阅读

FeedDemon/4.5 (http://www.feeddemon.com/; Microsoft Windows)
一款离线RSS阅读器

“Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; JianKongBao Monitor 1.1)”
监控宝

DNSPod-Monitor/2.0
DNSPod监控

“Mozilla 5.0 (compatible; Feedsky crawler /1.0; http://www.feedsky.com)”
Feedsky

“Xianguo.com 1 Subscribers”
鲜果

360spider(http://webscan.360.cn)
360网站安全检测

“yrspider Mozilla/5.0 (compatible; YRSpider; +http://www.yunrang.com/yrspider.html)”
云壤公司，http://www.yunrang.com/yrspider.html

其他未知bot
“Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; EmbeddedWB 14.52 from: http://www.bsalsa.com/ EmbeddedWB 14.52; .NET CLR 2.0.50727)”
怀疑为发布SPAM用的，因为总是在获取注册页面和验证码

Mozilla/5.0 (compatible; LinkpadBot/1.06; +http://www.linkpad.ru)
LinkpadBot，看域名知道是来自俄罗斯的

Mozilla/5.0 (compatible; SISTRIX Crawler; http://crawler.sistrix.net/)
又一个国外的

“Mozilla/5.0 (compatible; MJ12bot/v1.4.0; http://www.majestic12.co.uk/bot.php?+)”
来自英国的未知bot

“Mozilla/5.0 (compatible; Ezooms/1.0; ezooms.bot@gmail.com)”
未知

“IS Alpha/Nutch-1.1”
未知

Nutch Spider/Nutch-2.2.1
貌似是上面那个进化来的

“BlogPulseLive (support@blogpulse.com)”

“findlinks/2.0.2 (+http://wortschatz.uni-leipzig.de/findlinks/)”
来自德国的未知bot

“Mozilla/4.0 (compatible; MSIE 6.0; AugustBot/augstbot@163.com)”
未知，貌似与网易有关

“InternetSeer.com”
未知

“Mozilla/5.0 (compatible; DotBot/1.1; http://www.dotnetdotcom.org/, crawler@dotnetdotcom.org)”
未知，已更新为下面的

Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)
DotBot，不认识

“http://www.internet-zarabotok.net/” “Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; Win64; AMD64)”
来自俄罗斯的未知bot

Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.19; aggregator:Spinn3r (Spinn3r 3.1); http://spinn3r.com/robot) Gecko/2010040121 Firefox/3.0.19
Spinn3r，不认识

Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)
Exabot，还是不认识

Mozilla/5.0 (compatible; Exabot/3.0 (BiggerBetter); +http://www.exabot.com/go/robot)
Exabot，不认识

psbot/0.1 (+http://www.picsearch.com/bot.html)
psbot，不认识

TurnitinBot/3.0 (http://www.turnitin.com/robot/crawlerinfo.html)
TurnitinBot，不认识### 微软

“msnbot-media/1.1 (+http://search.msn.com/msnbot.htm)”
msnbot，大多数已经被bingbot替代了，现在偶尔还可以看到。

“Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)”
bing，必应

搜搜
“Sosospider+(+http://help.soso.com/webspider.htm)”
腾讯搜搜

“Sosoimagespider+(+http://help.soso.com/soso-image-spider.htm)”
搜搜图片

雅虎
“Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)”
雅虎英文

“Yahoo! Slurp China”
“Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)”
雅虎中国

搜狗
“http://pic.sogou.com” “Sogou Pic Spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07)”
搜狗图片

“Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)”
搜狗，搜狗的蜘蛛程序做的很不好，总是进入死循环，已经分别在 robots.txt 和 设置中屏蔽掉

Google
“Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)”
Google

“Googlebot-Image/1.0”
Google图片搜索

“Mediapartners-Google”
未知

“FeedBurner/1.0 (http://www.FeedBurner.com)”
feedburner

“AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 3 0 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari”
Adwords移动网络

百度
“Baiduspider-image+(+http://www.baidu.com/search/spider.htm)”
百度图片

“Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)”
亲爱的百度蜘蛛

“Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.8;baidu Transcoder) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729)”
baidu+Transcoder 是用户用手机浏览网站留下的记录，Transcoder 是代码转换器，把网站转码成手机用户上网看到的网页留下的记录

360
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider
360搜索

其他搜索引擎
“Mozilla/5.0 (compatible; YoudaoBot/1.0; http://www.youdao.com/help/webmaster/spider/; )”
网易有道

“Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)”
来自瑞典的搜索引擎，网站看起来很不错，http://www.entireweb.com

~“jikespider \”Mozilla/5.0”~
即刻搜索，原人民搜索，搜索引擎国家队，已倒闭

“Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)”
俄罗斯yandex

Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)
宜搜，不认识，一直不停抓取，已屏蔽

其他已知bot
“HuaweiSymantecSpider/1.0+DSE-support@huaweisymantec.com+(compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR ; http://www.huaweisymantec.com/cn/IRL/spider)”
华为赛门铁克蜘蛛，是华为赛门铁克科技有限公司网页信誉分析系统的一个页面爬取程序，其作用是用于爬取互联网网页并进行信誉分析，从而检查该网站上的是否含有恶意代码。
http://baike.baidu.com/view/5994606.htm

qiniu-imgstg-spider-1.0
七牛镜像蜘蛛

“xFruits/1.0 (http://www.xfruits.com)”
xFruits，聚合rss用的

Feedly/1.0 (+http://www.feedly.com/fetcher.html; like FeedFetcher-Google)
Feedly，Google Reader 关闭后一直用这个

Mozilla/5.0 (compatible;YoudaoFeedFetcher/1.0;http://www.youdao.com/help/reader/faq/topic006/;1 subscribers;)
有道阅读

FeedDemon/4.5 (http://www.feeddemon.com/; Microsoft Windows)
一款离线RSS阅读器

“Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; JianKongBao Monitor 1.1)”
监控宝

DNSPod-Monitor/2.0
DNSPod监控

“Mozilla 5.0 (compatible; Feedsky crawler /1.0; http://www.feedsky.com)”
Feedsky

“Xianguo.com 1 Subscribers”
鲜果

360spider(http://webscan.360.cn)
360网站安全检测

“yrspider Mozilla/5.0 (compatible; YRSpider; +http://www.yunrang.com/yrspider.html)”
云壤公司，http://www.yunrang.com/yrspider.html

其他未知bot
“Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; EmbeddedWB 14.52 from: http://www.bsalsa.com/ EmbeddedWB 14.52; .NET CLR 2.0.50727)”
怀疑为发布SPAM用的，因为总是在获取注册页面和验证码

Mozilla/5.0 (compatible; LinkpadBot/1.06; +http://www.linkpad.ru)
LinkpadBot，看域名知道是来自俄罗斯的

Mozilla/5.0 (compatible; SISTRIX Crawler; http://crawler.sistrix.net/)
又一个国外的

“Mozilla/5.0 (compatible; MJ12bot/v1.4.0; http://www.majestic12.co.uk/bot.php?+)”
来自英国的未知bot

“Mozilla/5.0 (compatible; Ezooms/1.0; ezooms.bot@gmail.com)”
未知

“IS Alpha/Nutch-1.1”
未知

Nutch Spider/Nutch-2.2.1
貌似是上面那个进化来的

“BlogPulseLive (support@blogpulse.com)”

“findlinks/2.0.2 (+http://wortschatz.uni-leipzig.de/findlinks/)”
来自德国的未知bot

“Mozilla/4.0 (compatible; MSIE 6.0; AugustBot/augstbot@163.com)”
未知，貌似与网易有关

“InternetSeer.com”
未知

“Mozilla/5.0 (compatible; DotBot/1.1; http://www.dotnetdotcom.org/, crawler@dotnetdotcom.org)”
未知，已更新为下面的

Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)
DotBot，不认识

“http://www.internet-zarabotok.net/” “Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; Win64; AMD64)”
来自俄罗斯的未知bot

Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.19; aggregator:Spinn3r (Spinn3r 3.1); http://spinn3r.com/robot) Gecko/2010040121 Firefox/3.0.19
Spinn3r，不认识

Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)
Exabot，还是不认识

Mozilla/5.0 (compatible; Exabot/3.0 (BiggerBetter); +http://www.exabot.com/go/robot)
Exabot，不认识

psbot/0.1 (+http://www.picsearch.com/bot.html)
psbot，不认识

TurnitinBot/3.0 (http://www.turnitin.com/robot/crawlerinfo.html)
TurnitinBot，不认识

  static String[] spiders = { "Sogou", "Googlebot", "MJ12bot", "YodaoBot", "Yahoo!", "Sosospider",
      "Baiduspider", "msnbot-media", "Sosoimagespider", "Feedfetcher-Google",
      "Mediapartners-Google", "Googlebot-Image", "ia_archiver", "sohu-search",
      "Oracle Ultra Search", "ASPSeek", "YahooSeeker", "Baidu-Transcoder/", "Sosoimagespider" };
<?php

$botlist=array (
  1 => 
  array (
    'name' => '百度',
    'biaoji' => 'baiduspider',
  ),
  2 => 
  array (
    'name' => '谷歌',
    'biaoji' => 'googlebot',
  ),
  3 => 
  array (
    'name' => '搜狗',
    'biaoji' => 'sogou spider',
  ),
  4 => 
  array (
    'name' => '雅虎',
    'biaoji' => 'slurp',
  ),
  5 => 
  array (
    'name' => 'MSN',
    'biaoji' => 'msnbot',
  ),
  6 => 
  array (
    'name' => '搜狐',
    'biaoji' => 'sohu-search',
  ),
  7 => 
  array (
    'name' => '有道',
    'biaoji' => 'youdaobot',
  ),
  8 => 
  array (
    'name' => 'SOSO',
    'biaoji' => 'sosospider',
  ),
  9 => 
  array (
    'name' => 'Alexa',
    'biaoji' => 'alexa',
  ),
);



$useragent=strtolower($_SERVER['HTTP_USER_AGENT']);
foreach($botlist as $k=>$v){
	if(stripos($useragent,$botlist[$k]['biaoji'])!==false){
		SpiderRecord($botlist[$k]['name']);
	}
}


function SpiderRecord($spider=''){
	$ip=getonlineip();
	$logFormat = "%date $spider %ip %url";
	date_default_timezone_set("PRC");
	$Spiders = str_replace(explode(' ', $logFormat), array(
		"time:".date('Y-m-d H:i:s'),
		"|| spider:".$spider,
		"|| ip:".$ip,
		"|| url:".$_SERVER['HTTP_HOST'].$_SERVER["PHP_SELF"] . "?" . $_SERVER["QUERY_STRING"],
	), $logFormat);
	 $fileName=$spider.date('Ym').'.log';
	  return file_put_contents(__dir__.DIRECTORY_SEPARATOR.$fileName, $Spiders . "\r\n", FILE_APPEND);
}

function getonlineip(){
	if(isset($_SERVER['REMOTE_ADDR']) && $_SERVER['REMOTE_ADDR'] && strcasecmp($_SERVER['REMOTE_ADDR'], 'unknown')){
		$ip = $_SERVER['REMOTE_ADDR'];
	}elseif(getenv('HTTP_CLIENT_IP') && strcasecmp(getenv('HTTP_CLIENT_IP'), 'unknown')){
		$ip = getenv('HTTP_CLIENT_IP');
	}elseif(getenv('HTTP_X_FORWARDED_FOR') && strcasecmp(getenv('HTTP_X_FORWARDED_FOR'), 'unknown')){
		$ip = getenv('HTTP_X_FORWARDED_FOR');
	}elseif(getenv('REMOTE_ADDR') && strcasecmp(getenv('REMOTE_ADDR'), 'unknown')){
		$ip = getenv('REMOTE_ADDR');
	}
	preg_match("/[\d\.]{7,15}/", isset($ip) ? $ip : NULL, $match);
	return isset($match[0]) ? $match[0] : 'unknown';
}
### 超简单实现php谷歌验证
超简单实现php谷歌验证
首先保存以下源码为GoogleAuthenticator.php文件
<?php

/**
 * PHP Class for handling Google Authenticator 2-factor authentication.
 *
 * @author Michael Kliewe
 * @copyright 2012 Michael Kliewe
 * @license http://www.opensource.org/licenses/bsd-license.php BSD License
 *
 * @link http://www.phpgangsta.de/
 */
class PHPGangsta_GoogleAuthenticator
{
    protected $_codeLength = 6;

    /**
     * Create new secret.
     * 16 characters, randomly chosen from the allowed base32 characters.
     *
     * @param int $secretLength
     *
     * @return string
     */
    public function createSecret($secretLength = 16)
    {
        $validChars = $this->_getBase32LookupTable();

        // Valid secret lengths are 80 to 640 bits
        if ($secretLength < 16 || $secretLength > 128) {
            throw new Exception('Bad secret length');
        }
        $secret = '';
        $rnd = false;
        if (function_exists('random_bytes')) {
            $rnd = random_bytes($secretLength);
        } elseif (function_exists('mcrypt_create_iv')) {
            $rnd = mcrypt_create_iv($secretLength, MCRYPT_DEV_URANDOM);
        } elseif (function_exists('openssl_random_pseudo_bytes')) {
            $rnd = openssl_random_pseudo_bytes($secretLength, $cryptoStrong);
            if (!$cryptoStrong) {
                $rnd = false;
            }
        }
        if ($rnd !== false) {
            for ($i = 0; $i < $secretLength; ++$i) {
                $secret .= $validChars[ord($rnd[$i]) & 31];
            }
        } else {
            throw new Exception('No source of secure random');
        }

        return $secret;
    }

    /**
     * Calculate the code, with given secret and point in time.
     *
     * @param string   $secret
     * @param int|null $timeSlice
     *
     * @return string
     */
    public function getCode($secret, $timeSlice = null)
    {
        if ($timeSlice === null) {
            $timeSlice = floor(time() / 30);
        }

        $secretkey = $this->_base32Decode($secret);

        // Pack time into binary string
        $time = chr(0).chr(0).chr(0).chr(0).pack('N*', $timeSlice);
        // Hash it with users secret key
        $hm = hash_hmac('SHA1', $time, $secretkey, true);
        // Use last nipple of result as index/offset
        $offset = ord(substr($hm, -1)) & 0x0F;
        // grab 4 bytes of the result
        $hashpart = substr($hm, $offset, 4);

        // Unpak binary value
        $value = unpack('N', $hashpart);
        $value = $value[1];
        // Only 32 bits
        $value = $value & 0x7FFFFFFF;

        $modulo = pow(10, $this->_codeLength);

        return str_pad($value % $modulo, $this->_codeLength, '0', STR_PAD_LEFT);
    }

    /**
     * Get QR-Code URL for image, from google charts.
     *
     * @param string $name
     * @param string $secret
     * @param string $title
     * @param array  $params
     *
     * @return string
     */
    public function getQRCodeGoogleUrl($name, $secret, $title = null, $params = array())
    {
        $width = !empty($params['width']) && (int) $params['width'] > 0 ? (int) $params['width'] : 200;
        $height = !empty($params['height']) && (int) $params['height'] > 0 ? (int) $params['height'] : 200;
        $level = !empty($params['level']) && array_search($params['level'], array('L', 'M', 'Q', 'H')) !== false ? $params['level'] : 'M';

        $urlencoded = urlencode('otpauth://totp/'.$name.'?secret='.$secret.'');
        if (isset($title)) {
            $urlencoded .= urlencode('&issuer='.urlencode($title));
        }

        return 'https://chart.googleapis.com/chart?chs='.$width.'x'.$height.'&chld='.$level.'|0&cht=qr&chl='.$urlencoded.'';
    }

    /**
     * Check if the code is correct. This will accept codes starting from $discrepancy*30sec ago to $discrepancy*30sec from now.
     *
     * @param string   $secret
     * @param string   $code
     * @param int      $discrepancy      This is the allowed time drift in 30 second units (8 means 4 minutes before or after)
     * @param int|null $currentTimeSlice time slice if we want use other that time()
     *
     * @return bool
     */
    public function verifyCode($secret, $code, $discrepancy = 1, $currentTimeSlice = null)
    {
        if ($currentTimeSlice === null) {
            $currentTimeSlice = floor(time() / 30);
        }

        if (strlen($code) != 6) {
            return false;
        }

        for ($i = -$discrepancy; $i <= $discrepancy; ++$i) {
            $calculatedCode = $this->getCode($secret, $currentTimeSlice + $i);
            if ($this->timingSafeEquals($calculatedCode, $code)) {
                return true;
            }
        }

        return false;
    }

    /**
     * Set the code length, should be >=6.
     *
     * @param int $length
     *
     * @return PHPGangsta_GoogleAuthenticator
     */
    public function setCodeLength($length)
    {
        $this->_codeLength = $length;

        return $this;
    }

    /**
     * Helper class to decode base32.
     *
     * @param $secret
     *
     * @return bool|string
     */
    protected function _base32Decode($secret)
    {
        if (empty($secret)) {
            return '';
        }

        $base32chars = $this->_getBase32LookupTable();
        $base32charsFlipped = array_flip($base32chars);

        $paddingCharCount = substr_count($secret, $base32chars[32]);
        $allowedValues = array(6, 4, 3, 1, 0);
        if (!in_array($paddingCharCount, $allowedValues)) {
            return false;
        }
        for ($i = 0; $i < 4; ++$i) {
            if ($paddingCharCount == $allowedValues[$i] &&
                substr($secret, -($allowedValues[$i])) != str_repeat($base32chars[32], $allowedValues[$i])) {
                return false;
            }
        }
        $secret = str_replace('=', '', $secret);
        $secret = str_split($secret);
        $binaryString = '';
        for ($i = 0; $i < count($secret); $i = $i + 8) {
            $x = '';
            if (!in_array($secret[$i], $base32chars)) {
                return false;
            }
            for ($j = 0; $j < 8; ++$j) {
                $x .= str_pad(base_convert(@$base32charsFlipped[@$secret[$i + $j]], 10, 2), 5, '0', STR_PAD_LEFT);
            }
            $eightBits = str_split($x, 8);
            for ($z = 0; $z < count($eightBits); ++$z) {
                $binaryString .= (($y = chr(base_convert($eightBits[$z], 2, 10))) || ord($y) == 48) ? $y : '';
            }
        }

        return $binaryString;
    }

    /**
     * Get array with all 32 characters for decoding from/encoding to base32.
     *
     * @return array
     */
    protected function _getBase32LookupTable()
    {
        return array(
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', //  7
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', // 15
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', // 23
            'Y', 'Z', '2', '3', '4', '5', '6', '7', // 31
            '=',  // padding char
        );
    }

    /**
     * A timing safe equals comparison
     * more info here: http://blog.ircmaxell.com/2014/11/its-all-about-time.html.
     *
     * @param string $safeString The internal (safe) value to be checked
     * @param string $userString The user submitted (unsafe) value
     *
     * @return bool True if the two strings are identical
     */
    private function timingSafeEquals($safeString, $userString)
    {
        if (function_exists('hash_equals')) {
            return hash_equals($safeString, $userString);
        }
        $safeLen = strlen($safeString);
        $userLen = strlen($userString);

        if ($userLen != $safeLen) {
            return false;
        }

        $result = 0;

        for ($i = 0; $i < $userLen; ++$i) {
            $result |= (ord($safeString[$i]) ^ ord($userString[$i]));
        }

        // They are only identical strings if $result is exactly 0...
        return $result === 0;
    }
}
保存以下代码为logo.php
<?php 
if(!empty($_POST['user'])&&!empty($_POST['pass'])&&!empty($_POST['Verification'])){
	require_once './GoogleAuthenticator.php';

	$ga = new PHPGangsta_GoogleAuthenticator();

	//"安全密匙SecretKey" 入库,和账户关系绑定,客户端也是绑定这同一个"安全密匙SecretKey"
	$secret = 'QLE4O7GHUJLT63ARS';

	$oneCode = $_POST['Verification'];
	$checkResult = $ga->verifyCode($secret, $oneCode, 2);
	if($checkResult){
		$user = $_POST['user'];
		$pass = $_POST['pass'];
		if($user=='admin'&&$pass=='admin000'){
			exit('登录成功');
		}else{
			exit('密码错误');
		}
	}else{
		exit('验证码错误');
	}
}
?>
<!DOCTYPE html>
<html>
<head>
	<title>登录</title>
</head>
<body>
	<div>
		<form action="login.php" method="post">
			<p>账号：<input type="text" name="user" placeholder="账号"></p>
			<p>密码：<input type="pass" name="pass"></p>
			<p>验证码：<input type="number" name="Verification"></p>
			<input type="submit" value="提交">
		</form>
	</div>
</body>
</html>

此时安装Google身份验证器到手机上(安卓版可以去网上下载，苹果可以在商城应用商城搜到)，然后绑定SecretKey即可使用。

当然多用户也可以使用该功能，只需要给每个用户绑定一个SecretKey即可。

如果需要生成二维码可以使用以下代码生成

$qrCodeUrl = $ga->getQRCodeGoogleUrl('localhost', $secret); //第一个参数是"标识",第二个参数为"安全密匙SecretKey" 生成二维码信息

echo '<img src="'.$qrCodeUrl.'">';
### 采集金山词霸每日一句
采集金山词霸每日一句
每日：http://open.iciba.com/dsapi/

查指定时间：http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title=2018-11-06&_=1541655200812

<?php 
header("Content-type: text/html; charset=utf-8"); //设置编码 utf-8 
$t1 = microtime(true);
$utime = date("Y-m-d");//api的尾缀时间
$translation = '0';//翻译语句，0不采集，1采集
$content = '1';//英语版，0不采集，1采集
//使用curl提高运行速度 不用动
function httpGet($url) {
	$curl = curl_init();
	$httpheader[] = "Accept:*/*";
	$httpheader[] = "Accept-Language:zh-CN,zh;q=0.8";
	$httpheader[] = "Connection:close";
	curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20041001 Firefox/0.10.1" );
	curl_setopt($curl, CURLOPT_HTTPHEADER, $httpheader);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($curl, CURLOPT_TIMEOUT, 3);
	curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($curl, CURLOPT_URL, $url);
	$res = curl_exec($curl);
	curl_close($curl);
	return $res;
}
$myfile = fopen("iciba.txt", "a+");//创建文件保存抓取的句子
//循环次数 2018-7-31 至现在日期相差的天数 
for ($i=1; $i<100; $i++) { 
    $json_string =httpGet('http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title='.$utime.'&_='.time());//curl 自定义函数访问api

    $data= json_decode($json_string,true);//解析json 转为php
    if (isset($data['note'])) {
    	$text1= $data['note']."\n"; 
    	fwrite($myfile, $text1);
    }

    if (isset($data['translation'])&&$translation==1) {
    	$text2= str_replace('小编的话：', '', $data['translation'])."\n";
    	fwrite($myfile, $text2);
    }
    if (isset($data['content'])&&$content==1) {
    	$text3= $data['content']."\n"; 
    	fwrite($myfile, $text3);
    }
    $utime= date("Y-m-d",strtotime("-".strval($i)." day")); //每循环一次 当前日期减去循环变量
} 
fclose($myfile);
$t2 = microtime(true);
echo 'ok，耗时'.round($t2-$t1,3).'秒';

?>
一言接口
<?php
//获取句子文件的绝对路径
//如果你介意别人可能会拖走这个文本，可以把文件名自定义一下，或者通过Nginx禁止拉取也行。
$path = dirname(__FILE__);
$file = file($path."/iciba.txt");
 
//随机读取一行
$arr  = mt_rand( 0, count( $file ) - 1 );
$content  = trim($file[$arr]);
 
//编码判断，用于输出相应的响应头部编码
if (isset($_GET['charset']) && !empty($_GET['charset'])) {
    $charset = $_GET['charset'];
    if (strcasecmp($charset,"gbk") == 0 ) {
        $content = mb_convert_encoding($content,'gbk', 'utf-8');
    }
} else {
    $charset = 'utf-8';
}
 
//格式化判断，输出js或纯文本
if (isset($_GET['encode'])&&$_GET['encode'] === 'js') {
	header('Content-type: text/javascript;charset=utf-8'); 
    echo "function iciba(){document.write('" . $content ."');}";
} else {
    echo $content;
}
每日采集接口
<?php
header("Content-type: text/html; charset=utf-8"); //设置编码 utf-8 
$utime = date("Y-m-d");
$file_data = 'data.txt';
if(!file_exists($file_data)){
    fopen($file_data, "w");
}
$str = file_get_contents('data.txt');
$d=date('Y/m/d H:i',strtotime($str));

$translation = '0';//翻译语句，0不采集，1采集
$content = '1';//英语版，0不采集，1采集
//请更改监控key 默认iciba
if($_GET['p']==='iciba'){
//判断今天是否已爬
    if(strtotime($utime)>strtotime($d)){
//爬虫开始    
//使用curl提高运行速度 不用动
function httpGet($url) {
    $curl = curl_init();
    $httpheader[] = "Accept:*/*";
    $httpheader[] = "Accept-Language:zh-CN,zh;q=0.8";
    $httpheader[] = "Connection:close";
    curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20041001 Firefox/0.10.1" );
    curl_setopt($curl, CURLOPT_HTTPHEADER, $httpheader);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_TIMEOUT, 3);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
    curl_setopt($curl, CURLOPT_URL, $url);
    $res = curl_exec($curl);
    curl_close($curl);
    return $res;
}
//定义写入函数 
function myfile($txt){
    $myfile = fopen("iciba.txt", "a+");
    fwrite($myfile,$txt);
    fclose($myfile);
}

$json_string =httpGet('http://open.iciba.com/dsapi/');//curl 自定义函数访问api
$data= json_decode($json_string,true);//解析json 转为php
//2018-4-11之前只有一条数据 so 加判断 
if (isset($data['note'])) {
    $text1= $data['note']."\n"; 
    myfile($text1);
}

if (isset($data['translation'])&&$translation==1) {
    $text2= str_replace('小编的话：', '', $data['translation'])."\n";
    myfile($text2);
}
if (isset($data['content'])&&$content==1) {
    $text3= $data['content']."\n"; 
    myfile($text3);
}
$myfile = fopen("data.txt", "w");
fwrite($myfile,$utime);
fclose($myfile);
echo "ok";
//爬虫结束
}else{
    echo "已爬";
}
}else
echo "老铁 搞事情吗";
?>
### think-swoole
    
think-swoole
官网文档
thinkphp6文档
https://www.kancloud.cn/manual/thinkphp6_0/1037479
swoole文档
https://wiki.swoole.com/#/
think-swoole文档
https://www.kancloud.cn/manual/thinkphp6_0/1359700

安装
composer require topthink/think-swoole
命令行
php think swoole [start|stop|reload|restart]
服务启动
当你在命令行php think swoole下执行完成之后就会启动一个HTTP Server，可以直接访问当前的应用

'server'     => [
    'host'      => env('SWOOLE_HOST', '0.0.0.0'), // 监听地址
    'port'      => env('SWOOLE_PORT', 9501), // 监听端口
    'mode'      => SWOOLE_PROCESS, // 运行模式 默认为SWOOLE_PROCESS
    'sock_type' => SWOOLE_SOCK_TCP, // sock type 默认为SWOOLE_SOCK_TCP
    'options'   => [
    	// 服务启动后，进程ID存放文件
        'pid_file'              => runtime_path() . 'swoole.pid',
        // swoole 的日志文件
        'log_file'              => runtime_path() . 'swoole.log',
        // 守护进程模式设置 true 后台运行
        'daemonize'             => false,
        // 设置启动的reactor线程数
        'reactor_num'           => swoole_cpu_num(),
        // 设置启动的worker进程数
        'worker_num'            => swoole_cpu_num(),
        //配置Task进程的数量
        'task_worker_num'       => swoole_cpu_num(),
        //开启静态文件请求处理，需配合document_root
        'enable_static_handler' => true,
        //静态文件根目录
        'document_root'         => root_path('public'),
        // 设置最大数据包尺寸，单位字节
        'package_max_length'    => 20 * 1024 * 1024,
        //配置发送输出缓冲区内存尺寸
        'buffer_output_size'    => 10 * 1024 * 1024,
        //设置客户端连接最大允许占用的内存数量
        'socket_buffer_size'    => 128 * 1024 * 1024,
    ],
],
热更新
swoole服务器运行过程中php文件是常驻内存运行，这样就可以避免重复的读取磁盘，重复的解释编译php，以便达到最高的性能，所以修改代码需要重启服务

think-swoole扩展提供热更新功能，在检测相关文件有更新会自动重启，不在需要手动完成重启，方便开发调试

生产环境下不建议开始文件监控，性能损耗，正常情况下你所修改的文件需要确认无误才能进行更新部署

.env里面设置APP_DEBUG = true会默认开启热更新

'hot_update' => [
    'enable'  => env('APP_DEBUG', false),
    'name'    => ['*.php'],
    'include' => [app_path()],
    'exclude' => [],
],
参数说明

参数	说明
enable	是否开启热更新
name	监听哪些类型的文件变动
include	监听哪些目录下的文件变动
exclude	排除目录
websocket
先来一个官方的例子

$server = new Swoole\WebSocket\Server("0.0.0.0", 9501);
$server->on('open', function (Swoole\WebSocket\Server $server, $request) {
    echo "server: handshake success with fd{$request->fd}\n";
});
$server->on('message', function (Swoole\WebSocket\Server $server, $frame) {
    echo "receive from {$frame->fd}:{$frame->data}\n";
    $server->push($frame->fd, "this is server");
});
$server->on('close', function ($ser, $fd) {
    echo "client {$fd} closed\n";
});
$server->start();
开启think-swoole的websocket功能 \config\swoole.php

'websocket'  => [
	'enable'        => true,
],
创建三个事件

php think make:listener SwWsConnect
php think make:listener SwWsClose
php think make:listener SwWsMessage
然后将这三个事件写到到事件监听中，分别有以下2中文件可以修改方式，注意二选一

thinkphp6自带的事件绑定app\event.php

    'listen'    => [
		........
        // 监听链接
        'swoole.websocket.Connect' => [
            \app\listener\SwWsConnect::class
        ],
        //关闭连接
        'swoole.websocket.Close' => [
            \app\listener\SwWsClose::class
        ],
        //发送消息场景
        'swoole.websocket.Message' => [
            \app\listener\SwWsMessage::class
        ]
    ],
think-swoole事件绑定config\swoole.php

'listen'        => [
    'connect'=>\app\listener\SwWsConnect::class,
    'close'=>\app\listener\SwWsClose::class,
    'message'=> \app\listener\SwWsMessage::class
],
怎么选择是保存在config\swoole.php还是app\event.php配置中呢？

首先我们 我们确定一下我们这个项目中存在有几个实时通讯，

如果只是存在一个实时通讯 个人建议 保存在config\swoole.php

如果是存在多个实时通讯，就保存在app\event.php

key值 必须是swoole.websocket.事件名称 例如 swoole.websocket.Message

开始写事件中中方法

连接事件app\listener\SwWsConnect.php

public function handle($event, \think\swoole\websocket $ws)
{
    // 获取当前发送者的fd
    $fd = $ws->getSender();
    echo "server: handshake success with fd{$fd}\n";
}
关闭事件app\listener\SwWsClose.php


public function handle($event, \think\swoole\websocket $ws)
{
    $fd = $ws->getSender();
    echo "client {$fd} closed\n";
}
message事件app\listener\SwWsMessage.php

public function handle($event, \think\swoole\websocket $ws)
{
	$fd = $ws->getSender();
	$data = json_encode($event);
	echo "receive from {$fd}:{$data}\n";
    $ws->emit("this is server", $fd);
}
启动php think swoole进行测试

think-swoole中的websocket方法总结

//给自己发消息
$ws->emit("this is server", $ws->getSender());
//给指定一个fd发消息
$ws->to($to)->emit("messagecallback",$data);
//给指定多个人发消息
$ws->to([1,2,3])->emit("messagecallback",$data);
//发送给所有的(不包含自己)
$ws->broadcast()->emit("messagecallback",$data);
//模拟formfd 给tofd 发送消息
$ws->setSender($formfd)->to($tofd)->emit("messagecallback",$data);
注意：在多个实时通讯场景下使用 emit

第一个参数传入 传入 事件名称callback 例如 messagecallback

如果你发现你think-swoole中有些没有swoole中的方法可以这么干

$sw = app('swoole.server');
$sw = app("think\swoole\Manager")->getServer();
//以上二选一

$es = $sw->isEstablished($fd); //检查连接是否为有效的WebSocket客户端连接
var_dump($es);
聊天室room实现
前端文件参考 html\room.html 或 html\room-socket-io.html

php think make:listener SwRoomJoin
php think make:listener SwRoomLeave
php think make:listener SwRoomMessage
事件绑定

// 加入房间
'swoole.websocket.RoomJoin' => [
	\app\listener\SwRoomJoin::class
],
// 离开房间
'swoole.websocket.Roomleave' => [
	\app\listener\SwRoomLeave::class
],
// 在房间发消息
'swoole.websocket.RoomMessage' => [
	\app\listener\SwRoomMessage::class
]
加入房间逻辑

public function handle($event, \think\swoole\websocket $ws, \think\swoole\websocket\room $room)
{
    $fd = $ws->getSender();
    //客户端假如定的room
    $roomid = $event['room'];
    //获取指定房间下有哪些客户端
    $roomfds = $room->getClients($roomid);
    // 判断这个房间有没有自己 如果有自己就不需要再次发送通知
    if (in_array($fd, $roomfds)) {
        $ws->to($roomfds)->emit("roomjoincallback", "房间{$roomid}已加入");
        return;
    }
    //加入房间
    $ws->join($roomid);
    $ws->to($roomfds)->emit("roomjoincallback", "{$fd}加入房间{$roomid}成功");
}
离开房间逻辑

public function handle($event, \think\swoole\websocket $ws, \think\swoole\websocket\Room $room)
{
    $roomid = $event['room'];
    $fd = $ws->getSender();
    $roomfds = $room->getClients($roomid);
    if (!in_array($fd, $roomfds)) {
        $ws->emit("roomleavecallback", "{$fd}不在{$roomid}房间内，怎么离开~");
        return;
    }
    //离开房间
    $ws->leave($roomid);
    //获取当前客户端加入了哪些客户端
    $rooms = $room->getRooms($fd);
    $ws->to($roomfds)->emit("roomleavecallback", "{$fd}已离开了~~");
}
在房间发布聊天逻辑

    public function handle($event, \think\swoole\websocket $ws, \think\swoole\websocket\room $room)
    {
        //
        $roomid = $event['room'];
        $text = $event['text'];
        $fd = $ws->getSender();
        $roomfds = $room->getClients($roomid);
        if (!in_array($fd, $roomfds)) {
            $ws->emit("roommessagecallback", "{$fd}不在{$roomid}房间内，无法进入发布聊天~");
            return;
        }
        $ws->to($roomfds)->emit("roommessagecallback",  $text);
    }
事件订阅
php think make:listener SwSubscribe
app\listener\SwSubscribe.php

<?php
declare (strict_types = 1);

namespace app\listener;

class SwSubscribe
{
    protected $ws = null;

    // public function __construct()
    // {
    //     $this->ws = app('think\swoole\Websocket');
    // }

    public function __construct(\think\Container $c)
    {
        $this->ws = $c->make(\think\swoole\Websocket::class);
    }
    
    public function onConnect()
    {
        $fd = $this->ws->getSender();
        echo "server: handshake success with fd{$fd}\n";
    }
    public function onClose()
    {
        $fd = $this->ws->getSender();
        echo "client {$fd} closed\n";
    }
    public function onMessage($event)
    {
        $fd = $this->ws->getSender();
        var_dump($event);
        echo "server: handshake success with fd{$fd}\n";
        $this->ws->emit("this is server", $fd);
    }
}

有点类似 将原生的swoole代码改成面向对象代码，生效方法 config\swoole.php中在subscribe 加入\app\listener\SwSubscribe::class

'subscribe'     => [
	\app\listener\SwSubscribe::class
],
在app\event.php文件中的 swoole.websocket.Connect 相当于 app\listener\SwSubscribe.php文件中的onConnect函数。如果同时存在的存在的话，就会向客户端发送2次以上的消息

Task任务投递
https://wiki.swoole.com/#/start/start_task

生成事件

php think make:listener SwSendEmailTask
编写发送邮件方法app\listener\SwSendEmailTask.php

public function handle($event)
{
    var_dump($event);
    //
    echo "开发发送邮件".time();
    sleep(3);
    echo "结束发送邮件".time();
}  
注册事件app\event.php

'swoole.task'=>[
	\app\listener\SwSendEmailTask::class
],
在控制器中投递任务

public function doRegister()
{
    $server = app('swoole.server');
    $server->task(\app\listener\SwSendEmailTask::class);
    return "注册成功";
}

public function doRegister(\think\swoole\Manager $manager)
{
    $server = $manager->getServer();
    $server->task(\app\listener\SwSendEmailTask::class);
    return "注册成功";
}
public function doRegister(\Swoole\Server $server)
{
    $server->task(\app\listener\SwSendEmailTask::class);
    return "注册成功";
}
三种获取\Swoole\Server,任意选其一

在swoole中还有一个事件叫finish，它的作用就是把异步任务的结果返回，在think-swool是这么处理的

定义一个发送邮件异步任务处理结果的事件

php think make:listener SwSendEmailFinish
注册事件app\event.php

'swoole.finish'=>[
	\app\listener\SwSendEmailFinish::class
],
在task任务中调用

public function handle($event)
{
    var_dump($event);
    //
    echo "开发发送邮件".time();
    sleep(3);
    echo "结束发送邮件".time();
    $event->finish(\app\listener\SwSendEmailFinish::class);
} 
高性能共享内存 Table
https://wiki.swoole.com/#/memory/table

先定结构在进行操作数据（原生swoole操作）

$table = new Swoole\Table(1024);
//创建表
$table->column("id", Swoole\Table::TYPE_INT);
$table->column("name", Swoole\Table::TYPE_STRING);
$table->column("money", Swoole\Table::TYPE_FLOAT);
$table->create();

//添加数据
$table->set("zq", [
    'id' => 1,
    'name' => "zhiqiang",
    'money' => 100,
]);
//获取一行数据
$table->get("zq");
// 修改数据
// 字段递增
$table->incr("zq","money",2);
//递减
$table->decr("zq","money",2);
// 返回 table 中存在的条目数。
$table->count();
//遍历table中的数据
foreach($table as $item){
    var_dump($item);
}
think-swoole中的操作

先对table表结构进行初始化config\swoole.php

    'tables'     => [
        'user'=>[
            'size'=>1024,
            'columns'=>[
                [
                    'name'=>'id',
                    'type'=>\Swoole\Table::TYPE_INT
                ],
                [
                    'name'=>'name',
                    'type'=>\Swoole\Table::TYPE_STRING,
                    'size'=>32
                ],
                [
                    'name'=>'money',
                    'type'=>\Swoole\Table::TYPE_FLOAT
                ],

            ],
        ],
    ],
操作数据

$table =  app('swoole.table.user');
$table->set("zq", [
    'id' => 1,
    'name' => "zhiqiang",
    'money' => 100
]);
//获取一行数据
$table->get("zq");
// 修改数据
// 字段递增
$table->incr("zq", "money", 2);
//递减
$table->decr("zq", "money", 2);
// 返回 table 中存在的条目数。
$table->count();
//遍历table中的数据
foreach ($table as $item) {
var_dump($item);
}
// 检查 table 中是否存在某一个 key。
$table->exist('zq');
//获取实际占用内存尺寸,单位字节
$table->momorySize();
RPC
RPC(Remote Procedure Call)：远程过程调用，它是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的思想。

详细介绍：https://developer.51cto.com/art/201906/597963.htm

解决分布式系统中，服务之间的调用问题。
远程调用时，要能够像本地调用一样方便，让调用者感知不到远程调用的逻辑。
节点角色说明：
Server: 暴露服务的服务提供方
Client: 调用远程服务的服务消费方
Registry: 服务注册与发现的注册中心
think-swoole实现RPC功能

服务器端
接口定义app/rpc/interfaces/UserInterface.php
<?php
namespace app\rpc\interfaces;
interface UserInterface
{
    public function create();
    public function find(int $id);
}
实现接口app/rpc/services/UserService.php
<?php
namespace app\rpc\services;
use app\rpc\interfaces\UserInterface;
class UserService implements UserInterface
{
    public function create()
    {
        // TODO: Implement create() method.
        return "service create success";
    }
    public function find(int $id)
    {
        // TODO: Implement find() method.
        return $id. "查询数据遍历";
    }
}
注册rpc服务config/swoole.php
    'rpc'        => [
        'server' => [
        	//开启rpc服务
            'enable'   => true,
            //rpc端口
            'port'     => 9000,
            'services' => [
            	//注册服务
                \app\rpc\services\UserService::class
            ],
        ],
        // 如果填写也是可以调用其他服务端
        'client' => [
        ],
    ],
启动服务端

php think swoole start /  php think swoole:rpc
客户端
    'rpc'        => [
        'server' => [
        ],
        'client' => [
            'tp6'=>[
            	//服务端的ip地址
                'host'=>'127.0.0.1',
                //服务端对应的端口
                'port'=>'9000'
            ]
            // 更多服务端
        ],
    ],
运行php think rpc:interface生成RPC接口文件app\rpc.php

<?php
/**
 * This file is auto-generated.
 */
declare(strict_types=1);
namespace rpc\contract\tp6;
interface UserInterface
{
	public function create();
	public function find(int $id);
}
return ['tp6' => ['rpc\contract\tp6\UserInterface']];
在控制器调用

    public function index(\rpc\contract\tp6\UserInterface $user)
    {
        //
        $user->find(1);
//        $user->create();
    }
杀死所有指定名称进程

ps -ef | grep swoole | grep -v grep | awk '{print $2}' | xargs kill -9

## 前端小案例
### html快捷查询
jp
html快捷查询
1.radio选中

<input type="radio" name="sex" value="1" title="男" {if condition="$ulist.sex==1"} checked="checked"{/if}>
<input type="radio" name="sex" value="2" title="女" {if condition="$ulist.sex==2"} checked="checked"{/if}>
<input type="radio" name="sex" value="0" title="变种人" {if condition="$ulist.sex==0"} checked="checked"{/if}>
2.select中option选中

<select name="groupid">
       <option value="0"></option>
             {foreach name="glist" item="vo"}
                  <option value="{$vo.id}" {if condition="$ulist.groupid==$vo['id']"} selected="selected"{/if}>{$vo.title}</option>
               {/foreach}
</select>
### layui经验总结
layui经验总结
一、遇到的问题及解决方案（心得）
1.让select下拉列表项目中的文字居中

.layui-form-select dl dd{
    text-align: center;
}
2.让表单label标签的宽度自动取其自身宽度

.layui-form-pane .layui-form-label {
    width: auto;
}
3.数据表格行背景色设置
数据表格中有开启隔行变色的效果，设置隔行变色的背景如下：

.layui-table[lay-even] tr:nth-child(even){
    background-color: #fafafa;
}
设置鼠标悬浮的行背景色：

.layui-table tbody tr:hover,.layui-table-hover{
    background-color: #e4efff!important;
}
设置鼠标点击（或选择）某行后的背景色：

.layui-table-click{
    background-color:#f2f2f2!important;
}
4.让弹出层信息框宽度自动取其自身宽度

.layui-layer-msg{
    min-width: auto!important;
}
5.让弹出层按钮分散居中对齐，并让其中表单元素宽度自动调整
这个稍稍有些复杂，直接上代码
CSS：

.layui-form-pane .layui-form-label {
    width: auto;
}
.layui-form-radio{
    padding-right: 0;
    margin-right:0;
}
.layui-form-select dl dd{
    text-align: center;
}
.layui-form-pane .layui-input-inline, .layui-form-pane .layui-inline,.layui-form-pane .layui-form-mid {
    margin-right: 0;
}
.layui-form-item .layui-input-block{
    float:left;
    margin-left: 0!important;
}
HTML/JS

<form class="layui-form layui-form-pane" id="layerform" style="display: none;padding:5px">
    <input type="hidden" name="id">
    <div class="layui-form-item" widthoffset="15">
        <div class="layui-inline">
            <label class="layui-form-label">姓名</label>
            <div class="layui-input-inline col12">
                <input type="text" name="name" autocomplete="off" placeholder="请输入姓名" class="layui-input" lay-verify="required" lay-verType="tips">
            </div>
        </div>
        <div class="layui-inline">
            <label class="layui-form-label">年龄</label>
            <div class="layui-input-inline" width="45">
                <input type="text" name="age"  autocomplete="off" class="layui-input" lay-verify="positiveInteger" lay-verType="tips">
            </div>
        </div>
        <div class="layui-inline">
            <label class="layui-form-label">性别</label>
            <div class="layui-input-inline" width="70">
                <select name="sex">
                    <option value="-1">保密</option>
                    <option value="1">男</option>
                    <option value="0">女</option>
                </select>
            </div>
        </div>
        <div class="layui-inline">
            <label class="layui-form-label">是否饮酒</label>
            <div class="layui-input-inline" width="132">
                <input type="radio" name="drink" value="1" title="是">
                <input type="radio" name="drink" value="0" title="否" checked>
            </div>
        </div>
    </div>
    <div class="layui-form-item" widthoffset="15">
        <div class="layui-inline">
            <label class="layui-form-label">身高（cm）</label>
            <div class="layui-input-inline" width="45">
                <input type="text" name="height"  autocomplete="off" class="layui-input" lay-verify="positiveInteger" lay-verType="tips">
            </div>
        </div>
        <div class="layui-inline">
            <label class="layui-form-label">体重（kg）</label>
            <div class="layui-input-inline" width="45">
                <input type="text" name="weight" autocomplete="off" class="layui-input" lay-verify="positiveInteger" lay-verType="tips">
            </div>
        </div>
        <div class="layui-inline">
            <label class="layui-form-label">电话</label>
            <div class="layui-input-inline col12">
                <input type="text" name="telphone" autocomplete="off" placeholder="手机或电话" class="layui-input">
            </div>
        </div>
        <div class="layui-inline">
            <label class="layui-form-label">是否吸烟</label>
            <div class="layui-input-inline" width="132">
                <input type="radio" name="smoke" value="1" title="是">
                <input type="radio" name="smoke" value="0" title="否" checked>
            </div>
        </div>
    </div>
    <div class="layui-form-item" widthoffset="10">
        <div class="layui-inline">
            <label class="layui-form-label">微信</label>
            <div class="layui-input-inline col4">
                <input type="text" name="wechat"  autocomplete="off" placeholder="请输入微信" class="layui-input">
            </div>
        </div>
        <div class="layui-inline">
            <label class="layui-form-label">QQ</label>
            <div class="layui-input-inline col4">
                <input type="text" name="qq"  autocomplete="off" placeholder="请输入QQ" class="layui-input">
            </div>
        </div>
        <div class="layui-inline">
            <label class="layui-form-label">电子邮箱</label>
            <div class="layui-input-inline col4">
                <input type="text" name="email"  autocomplete="off" placeholder="请输入Email" class="layui-input" lay-verify="email" lay-verType="tips">
            </div>
        </div>
    </div>
    <div class="layui-form-item" widthoffset="4">
        <label class="layui-form-label">地址</label>
        <div class="layui-input-block col12">
            <input type="text" name="address" autocomplete="off" placeholder="请输入地址" class="layui-input">
        </div>
    </div>
    <div class="layui-form-item" widthoffset="4">
        <label class="layui-form-label">备注</label>
        <div class="layui-input-block col12">
            <input type="text" name="comment" autocomplete="off" class="layui-input">
        </div>
    </div>
    <!--<div class="layui-form-item btns">
        <div class="layui-input-block">
            <button class="layui-btn layui-btn-radius" lay-submit lay-filter="layerForm">确定</button>
            <button class="layui-btn layui-btn-radius layui-btn-primary cancel" type="button">取消</button>
        </div>
    </div>-->
</form>

<script>
//按钮分散对齐
function locateBtns(layero, $) {
    var layerBtns = layero.find(".layui-layer-btn a");
    var btns = layero.find(".btns .layui-btn");
    var sumWidth = 0;
    layui.each(layerBtns, function (i, e) {
        sumWidth += $(e).outerWidth();
    });
    var gap = (layero.width() - sumWidth) / (layerBtns.length + 1);
    layui.each(layerBtns, function (i, e) {
        $(e).css({
            position: "relative",
            left: gap * (i + 1)
        });
    });
    sumWidth = 0;
    layui.each(btns, function (i, e) {
        sumWidth += $(e).outerWidth();
    });
    var pLeft = parseInt(layero.find(".layui-layer-wrap").css("padding-left"));
    var pRight = parseInt(layero.find(".layui-layer-wrap").css("padding-right"));
    gap = (layero.width() - pLeft - pRight - sumWidth) / (btns.length + 1);
    layui.each(btns, function (i, e) {
        $(e).css({
            position: "relative",
            left: gap * (i + 1)
        });
    });
}
//表单元素宽度自适应
function resizeForm(layero, $) {
    var items=layero.find(".layui-form-item");
    layui.each(items,function (i,e) {
        var widthoffset=$(e).attr("widthoffset");
        var widthSum=0;
        layui.each($(e).find(".layui-form-label"),function (i,e) {
            widthSum+=$(e).outerWidth(true);
        });
        layui.each($(e).find(".layui-input-inline[width]"),function (i,e) {
            var jdom=$(e);
            jdom.width(jdom.attr("width"));
            widthSum+=jdom.outerWidth(true);
        });
        var totalWidth=$(e).width()-widthSum;
        if(widthoffset){
            totalWidth-=widthoffset;
        }
        for (var i = 0; i < 12; i++) {
            var cells=$(e).find(".col"+(i+1));
            cells.width(totalWidth*(i+1)/12);
        }
    });
    locateBtns(layero, $);
}
//入口函数，绑定事件并调用弹出层
function layerForm(layer,jquery,options){
    var resizing=options.resizing;
    var full=options.full;
    var restore=options.restore;
    var success=options.success;
    var $=jquery;
    options.btnAlign="l";
    options.resizing=function(layero){
        resizeForm(layero, $);
        resizing && resizing(layero);
    }
    options.full=function(layero){
        resizeForm(layero, $);
        full && full(layero);
    }
    options.restore=function(layero){
        resizeForm(layero, $);
        restore && restore(layero);
    }

    options.success=function(layero, index){
        resizeForm(layero, $);
        success && success(layero, index);
    }

    return layer.open(options);
}

//弹出层调用
var index=layerForm(layer,$,{
                    title:"查看",
                    content:$("#layerform"),
                    type:1,
                    area: "710px",
                    maxmin: true,
					btn:['确定','取消']
                });
</script>
6.让加载层文字居中，宽度自适应不会换行

.layui-layer-loading .layui-layer-content{
    padding-top: 40px!important;
    width: auto!important;
    height: auto!important;
    background-position-x: 50%!important;
    color:#FF5722;
}
7.修复数据表格初始化时不会显示加载提示BUG

版本layui-v2.2.5
layui table首次加载没有显示loading，通过修改源码可以实现
方法：在layui.all.js文件中的下面位置添加js代码

if(n.url){i=i||a.loading();}

8.表单增强插件，主要使用表单自动填充功能

首先这里须要修改几行代码，否则无法在同一个页面使用该插件同时操作多个表单（多个EnhanceForm对象）！
代码中原有前10行内容如下：

layui.define(['jquery', 'form'],
    function(exports) {
        var $ = layui.jquery,
            form = layui.form,
            formObj,
            hint = layui.hint();
        var EnhanceForm = function(options) {
            this.options = options;
            formObj = $(options.elem);
        };
将其替换为如下内容：

layui.define(['jquery', 'form'],
    function(exports) {
        var $ = layui.jquery,
            form = layui.form,
            hint = layui.hint();
        var EnhanceForm = function(options) {
            this.options = options;
            this.formObj = $(options.elem);
        };
并且将后续代码中出现的所有formObj变量改为this.formObj
同时我在其基础上添加了几个功能：

//将表单转化为json对象
EnhanceForm.prototype.serializeJson = function() {
            var serializeObj={};
            var array=this.formObj.serializeArray();
            var str=this.formObj.serialize();
            layui.each(array,function(i,e){
                if(serializeObj[e.name]){
                    if($.isArray(serializeObj[e.name])){
                        serializeObj[e.name].push(e.value);
                    }else{
                        serializeObj[e.name]=[serializeObj[e.name],e.value];
                    }
                }else{
                    serializeObj[e.name]=e.value;
                }
            });
            return serializeObj;
        };
//禁用所有表单元素
EnhanceForm.prototype.disableAll = function() {
   var eles=this.formObj.find("input,select,textarea");
   eles.attr("disabled","disabled");
   form.render();
};
//启用所有表单元素
EnhanceForm.prototype.enableAll = function() {
   var eles=this.formObj.find("input,select,textarea");
   eles.removeAttr("disabled");
   form.render();
};

9.form表单提交事件bug
表单绑定提交事件如下：

form.on('submit(filterName)', function(data){
});
其中参数data.field包含当前表单容器的全部表单字段，名值对形式：{name: value}
但是如果表单中含有checkbox则会出现bug，如：
表单中含有如下3个checkbox：

<input type="checkbox" name="interest" title="写作" value="writing">
<input type="checkbox" name="interest" title="音乐" value="music">
<input type="checkbox" name="interest" title="电影" value="movie">
用户同时选中“写作”、“电影”两项
此时data.field中只有{interest:"movie"}这一项。
解决方案：
修改layui的form模块源码form.js
原来477-478行代码如下：

if(/^checkbox|radio$/.test(item.type) && !item.checked) return;      
field[item.name] = item.value;
将其修改为：
if(/^checkbox|radio$/.test(item.type) && !item.checked) return;
if(field[item.name]){
if(!(field[item.name] instanceof  Array)){
	field[item.name]=[field[item.name]];
}
field[item.name].push(item.value);
}else{
  field[item.name] = item.value;
}  
这是data.field中为{interest:["writing","movie"]}
PS：如果你的表单中有多个name相同的其他类型表单元素也同理！同时不会影响类似于下面这种数组name表单：

<input type="text" name="test[0]">
<input type="text" name="test[1]">
<input type="text" name="test[2]">
10.关于laydate控件
首先，用一个页面绑定多个laydate控件bug，这个问题貌似有很多人提出过，其中有人已经给出了解决方案：http://fly.layui.com/jie/14329/。
不过貌似版本升级后源码已经发生了变化，现在需要做如下修改，原来的laydate.js的1802-1806行代码如下：

if(e.target === options.elem[0] 
      || e.target === options.eventElem[0]
      || e.target === lay(options.closeStop)[0]){
        return;
 }
修改后如下：

var elem=options.elem.some(function (el) { return e.target === el });
var eventElem=options.eventElem.some(function (el) { return e.target === el });
var closeStop=lay(options.closeStop).some(function (el) { return e.target === el });
if(elem||eventElem||closeStop){
	return;
}
有时还会报如下错误：

laydate.js:797 Uncaught TypeError: Cannot read property 'appendChild' of undefined
at Class.hint (VM13097 laydate.js:797)
at Class.checkDate (VM13097 laydate.js:922)
at Class.remove (VM13097 laydate.js:742)
at HTMLDocument.<anonymous> (VM13097 laydate.js:1809)
可以修改源码修复，源码834-837行如下：

Class.prototype.checkDate = function(fn){
    var that = this
    ,thisDate = new Date()
    ,options = that.config
添加一个非空判断，修改如下：

Class.prototype.checkDate = function(fn){
    if(!this.elem){
      return ;
    }
    var that = this
    ,thisDate = new Date()
    ,options = that.config
另外，我还在原有done、change回调基础上添加了一个参数

done: function(dom,value, date, endDate){
    console.log(dom);//触发当前时期选择事件的dom对象
    console.log(value); //得到日期生成的值，如：2017-08-18
    console.log(date); //得到日期时间对象：{year: 2017, month: 8, date: 18, hours: 0, minutes: 0, seconds: 0}
    console.log(endDate); //得结束的日期时间对象，开启范围选择（range: true）才会返回。对象成员同上。
}
源码1473行如下：

param = param || 【that.parse(), start, end】;//（这里貌似是社区编辑器的一个bug，源码中【】符号为英文中括号[]）

修改如下：


param = param || 【that.bindElem,that.parse(), start, end】;//（这里貌似是社区编辑器的一个bug，源码中【】符号为英文中括号[]）

11.调整layui-btn按钮之间的间距

.layui-btn+.layui-btn{
    margin-left: 1px;
}
12.关于数据表格修改行数据后模版渲染的BUG
数据表格可以定义模板以便以自己的方式显示数据，模板有三种方式：绑定模版选择器、函数转义、直接赋值模版字符
如果使用函数转义如：

{field:'sex', title: '性别',width:60,align:'center'
	, templet:function(d){
		if(d.sex==1){
			return "男";
		}else if(d.sex==0){
			return "女";
		}else{
			return "保密";
		}
	}
}
并且此时再修改行数据时就会出现BUG，修改后性别直接显示1、0、-1，而不会经过函数转义了。
使用绑定模版选择器或直接赋值模版字符不会出现此BUG
修改table.js源码如下：
源码1140行如下：
templet ? laytpl($(templet).html() || value).render(data) : value
将其修改为：
templet ?(typeof templet === 'function'?templet(data):laytpl($(templet).html() || value).render(data)):value
13.关于数据表格排序
目前数据表格排序功能最多只能针对某一列做排序，但是有时可能需要同时对多列排序，并且需要根据排序参数重新请求后台，为了实现这个功能，我对table.js源码修改如下：
源码403-405行如下：

if(typeof options.initSort === 'object'){
	that.sort(options.initSort.field, options.initSort.type);
}
修改如下：

if(options.initSort instanceof Array){
	layui.each(options.initSort,function (i,e) {
		that.sort(e.field, e.sort);
	})
}
源码416行如下：
params[request.limitName] = options.limit;
在其后插入如下代码：

if(options.initSort!=null && options.initSort.length>0){
	  params["sorts"]=JSON.stringify(options.initSort);
}
源码694行如下：
that.layHeader.find('th').find(ELEM_SORT).removeAttr('lay-sort'); //清除其它标题排序状态
将其删除或注释

源码702-705行如下：

that.sortKey = {
  field: field
  ,sort: type
};
在其后插入如下代码：

var sortIndex=-1;
if(options.initSort instanceof Array){
	layui.each(options.initSort,function (i,e) {
		if(e.field==field){
		  sortIndex=i;
		  return false;
		}
	});
}else{
	options.initSort=[];
}
if(sortIndex==-1){
	options.initSort.push(that.sortKey);
	sortIndex=options.initSort.length-1;
}

if(type){
	options.initSort[sortIndex].sort=type;
}else{
	options.initSort.splice(sortIndex,1);
}
源码719-724行如下：

if(formEvent){
  layui.event.call(th, MOD_NAME, 'sort('+ filter +')', {
	field: field
	,type: type
  });
}
修改如下：

if(formEvent){
	  layui.event.call(th, MOD_NAME, 'sort('+ filter +')', {
		field: field
		,type: type
		,sorts:  options.initSort
	  });
	}
};
修改后数据表格可以同时对多列排序，并结合排序事件监听实现后台排序。
同时数据表格在翻页或重载时，会自动以sorts为键值自动向后台传递排序请求参数，形如：{sorts:[{"field":"height","sort":"asc"},{"field":"age","sort":"desc"}]}
并且排序事件的参数obj会增加一个属性sorts，内容与排序请求参数一致，如：

table.on('sort(test)', function(obj){ //注：tool是工具条事件名，test是table原始容器的属性 lay-filter="对应的值"
  console.log(obj.field); //当前排序的字段名
  console.log(obj.type); //当前排序类型：desc（降序）、asc（升序）、null（空对象，默认排序）
  console.log(this); //当前排序的 th 对象
  console.log(obj.sorts)//排序参数
  
  //尽管我们的 table 自带排序功能，但并没有请求服务端。
  //有些时候，你可能需要根据当前排序的字段，重新向服务端发送请求，从而实现服务端排序，如：
  table.reload('idTest');
});
二、建议
我原来是使用EasyUI的，所以初次使用layui时很多思路还是和原来一样，但是有时候layui很多功能没有EasyUI完善，用起来就很不爽，希望心姐多多借鉴一下EasyUI的做法
1.为什么不把表单元素设计成类似于下面的形式

<div class="layui-form-item">
	<div class="layui-input-block">
            <label class="layui-form-label">地址
                <input type="text" name="address" autocomplete="off" placeholder="请输入地址" class="layui-input">
	    </label>
	</div>
</div>
这样用户直接点击标签的文字光标就能直接定位到相应的文本框，用户体验更好
2.添加一个类似于如下的日历控件
3.关于form表单
EasyUI中有个form模块可以直接以ajax方式提交表单及自动填充表单（自动渲染），非常简单两行代码就搞定了，现在layui实现相同功能需要自己手动写代码或依赖大量插件辅助，很麻烦！我在EnhanceForm插件中已经实现了简单的ajax提交表单，不过没有充分测试，心姐可以完善后整合到layui中！
现在表单验证只能在点击提交按钮时提交表单时才会触发，但是有时候项目中表单验证并不是通过表单提交触发的，程序员希望自己手动调用js方法触发验证效果，所以建议为form添加一个validate方法，用于在表单验证框架基础上做表单验证，返回true、false表示验证是否通过，同时如果验证不通过自动显示提示等。
4.建议为数据表格增加一个添加行的方法（类似于EasyUI的appendRow、insertRow方法）
5.为数据表格增加获取所有行数据的方法（类似于EasyUI的getRows方法）
6.数据表格列宽度权重
建议为数据表格增加一个列宽度设置为权重的功能，假设数据表格共A、B、C、D四列，其中A、C列为固定宽度50px，B列宽度权重为1，D列宽度权重为2，则渲染效果为，B列宽度=（数据表格总宽度-100px）*1/3，D列宽度=（数据表格总宽度-100px）*2/3
7.添加功能：数据表格数据行区域也能实现类似于复杂表头跨行跨列的功能
8.单元格编辑类型目前只支持：text（输入框），建议添加下拉列表、日期选择、文件上传等类型，或者开发接口可以让用户自定义编辑器，同时可以添加验证规则，添加进入编辑状态前的触发事件，添加让单元格进入编辑状态的方法
9.添加功能：弹出层左上角标题文字旁也可以设置一个可爱的小图标^_^
10.添加类似于EasyUI中ComboTree（树形下拉框）和ComboGrid（数据表格下拉框）控件
11.添加属性：数据表格开启复选框时，可以设置singleSelect模式，即只允许选择一行
12.添加属性：数据表格开启复选框时，可以设置checkOnSelect，如果为true，当用户点击行的时候该复选框就会被选中或取消选中。如果为false，当用户仅在点击该复选框的时候才会被选中或取消。
### layui 表单增强插件
layui 表单增强插件
/**
 * Created by  Doyle on 2018年3月6日17点09分
 * layui表单增加插件
 * 
 * 
 * 
 */
layui.define(['jquery', 'form'],
    function(exports) {
        var $ = layui.jquery,
            form = layui.form,
            formObj,
            hint = layui.hint();
        var EnhanceForm = function(options) {
            this.options = options;
            formObj = $(options.elem);
        };
        /**
         * 设置select选中值
         * @param {String} name 对象名称，指“name”
         * @param {String} val 值
         * @param {Boolean} isOnSelect 是否触发选中事件
         * @returns {} 
         */
        EnhanceForm.prototype.setSelectVal = function(name, val, isOnSelect) {
            if (name === undefined) {
                throw "name no undefined";
            }
            formObj.find('select[name="' + name + '"]').val(val);
            form.render('select');
            if (typeof (isOnSelect) === "boolean") {
                if (isOnSelect) {
                    formObj.find("dd[lay-value='" + val + "']").trigger("click");
                }
            }
            return this;
        };
        /**
         * 设置radio选中
         * @param {String} name 对象名称，指“name”
         * @param {String} val 对象值
         * @returns {} 
         */
        EnhanceForm.prototype.setRadioVal = function(name, val) {
            if (name === undefined) {
                throw "name no undefined";
            }
            formObj.find('input[type="radio"][name="' + name + '"][value="' + val + '"]').prop("checked", true);
            form.render('radio');
            return this;
        };
        /**
         * 设置checkbox选中
         * @param {String} name 对象名称，指“name”
         * @returns {} 
         */
        EnhanceForm.prototype.setCheckboxVal = function(name) {
            if (name === undefined) {
                throw "name no undefined";
            }
            formObj.find('input[type="checkbox"][name="' + name + '"]').prop("checked", true);
            form.render('checkbox');
            return this;
        }
        /**
         * 设置表单元素禁用
         * @param {String} type 类型，select、checkbox、radio
         * @param {String} name  对象名称，指“name”
         * @param {String} val 值，radio元素需要用到
         * @returns {} 
         */
        EnhanceForm.prototype.setElemDisabled = function(type, name, val) {
            switch (type) {
            case "select":
                formObj.find('select[name="' + name + '"]').prop("disabled", true);
                form.render('select');
                break;
            case "checkbox":
                formObj.find('input[type="checkbox"][name="' + name + '"]').prop("disabled", true);
                form.render('checkbox');
                break;
            case "radio":
                if (val === undefined) {
                    throw "val不能为undefined";
                }
                formObj.find('input[type="radio"][name="' + name + '"][value="' + val + '"]').prop("disabled", true);
                form.render('radio');
                break;
            default:
                hint.error('layui.enhanceform 不支持该类型，type：' + type);
            }
            return this;
        }
        /**
         * 表单填充
         * @param {Object} data 
         * @returns {} 
         */
        EnhanceForm.prototype.filling = function(data) {
            if (typeof data !== "object") {
                throw "data no object";
            }
            for (var key in data) {
                if (data.hasOwnProperty(key)) {
                    var inputs = formObj.find('input[name = "' + key + '"]');
                    if (inputs.length > 0) {
                        var input = inputs[0];
                        switch (input.type) {
                        case "text":
                            input.value = data[key];
                            break;
                        case "hidden":
                            input.value = data[key];
                            break;
                        case "radio":
                            this.setRadioVal(key, data[key]);
                            break;
                        case "checkbox":
                            if (data[key] === true) {
                                this.setCheckboxVal(key, data[key]);
                            }
                            break;
                        }
                    } else {
                        var select = formObj.find('select[name="' + key + '"]');
                        if (select.length > 0) {
                            this.setSelectVal(key, data[key], true);
                        }
                    }
                }
            }
            return this;
        };
        /**
         * 接口输出
         */
        exports('enhanceform',
            function(options) {
                var enhance = new EnhanceForm(options = options || {});
                var elem = $(options.elem);
                if (!elem[0]) {
                    return hint.error('layui.enhanceform 没有找到' + options.elem + '元素');
                }
                return enhance;
            });
    });
1、包含select、radio、checkbox设置选中值，后自动渲染，
2、select、checkbox、radio对象设置禁用，后自动渲染
3、表单填充值
使用方法

<script type="text/javascript">
    layui.config({
        base: '../Scripts/layui-expand/' //插件路径
    }).extend({
        enhanceform: 'enhanceform'
    });
    layui.use(['form', 'enhanceform'],
        function() {
            var form = layui.form,
                enhanceForm = layui.enhanceform;
            var enhance = new enhanceForm({
                elem: '#mainForm' //表单选择器
            });
        /**
         * 设置select选中值
         * @param {String} name 对象名称，指“name”
         * @param {String} val 值
         * @param {Boolean} isOnSelect 是否触发选中事件
         * @returns {} 
         */
          1、enhance.setSelectVal
         /**
         * 设置radio选中
         * @param {String} name 对象名称，指“name”
         * @param {String} val 对象值
         * @returns {} 
         */
         2、enhance.setRadioVal
         /**
         * 设置checkbox选中
         * @param {String} name 对象名称，指“name”
         * @returns {} 
         */
          3、 enhance.setCheckboxVal
           /**
         * 设置表单元素禁用
         * @param {String} type 类型，select、checkbox、radio
         * @param {String} name  对象名称，指“name”
         * @param {String} val 值，radio元素需要用到
         * @returns {} 
         */
          4、enhance.setElemDisabled
         /**
         * 表单填充
         * @param {Object} data 
         * @returns {} 
         */
          5、 enhance.filling({ testSelect: 2 }); //表单填充
        });

</script>
### Vue列表Ajax实战教程
Vue列表Ajax实战教程
Html代码

<tbody id="itemtr">
	<tr  is="item-row"  v-for="item in items" v-on:editclick="editclick"  v-on:removeclick="removeclick" v-bind:item="item"></tr>
	<!-- more data -->
</tbody>
定义JavaScript模板


<script type="text/x-template" id="item-tr" >
	<tr v-bind:id="'tr_' +item.id">
		<td>{{item.id}}</td>
		<td>{{item.name}}</td>

		<td>
			<button  v-on:click="editclick">编辑</button>
			<button  v-on:click="removeclick">删除</button>
		</td>
	</tr>
</script>
components组件


Vue.component("item-row", {
	props: ["item"],
	template: "#item-tr",
	methods: {
		editclick: function () {
			this.$emit('editclick', this.item)
		},
		removeclick: function () {
			this.$emit('removeclick', this.item)
		}
	}
})
Ajax请求数据


function loadItems() { 
	$.ajax({
		method: "GET",
		url: "/Article/getallArticle",
		data: {},
		success: function (backData) {
			console.log(backData);
			if (backData.code == 1) {

				new Vue({
					el: '#itemtr',
					data: {
						items: backData.data
					},
					methods: {
						editclick: function (itemObject) {
							console.log(itemObject)
						},
						removeclick: function (itemObject) {
							console.log(itemObject)
						}
					}   
				})

			} else { 
				layer.msg(backData.msg);
			}
		   
		},
		error: function (error) {

			layer.msg(error.statusText);
		}
	})
}
执行函数

$(function () {
    loadItems();
})

## PHP基础
### 类的自动载入
类的自动载入
A类
<?php
class A{
　　public function __construct(){
　　       echo 'fff';
　　}
}
?>
自动导入php文件（__autoload）
<?php   
function __autoload($class)   
{   
	$file = $class . '.php';   
	if (is_file($file)) {   
		require_once($file);   
	}   
}   
自动导入php文件（require_once）
<?php
function loader($class)
{
	$file = $class . '.php';
	if (is_file($file)) {
       require_once($file);
    }
}
spl_autoload_register('loader'); //注册一个自动加载方法，覆盖原有的__autoload
$a = new A();
?>
自动导入php文件（spl_autoload_register）
<?php   
class Loader   
{   
	public static function loadClass($class)   
	{   
		$file = $class . '.php';   
		if (is_file($file)) {   
			require_once($file);   
		}   
	}   
}   
spl_autoload_register(array('Loader', 'loadClass'));   
$a = new A();
?>
自动导入php文件（最佳）
if(function_exist('spl_autoload_register')){

　　spl_autoload_register(array('core','autoload'));  //如果是php5以上，存在注册函数，则注册自己写的core类中的autoload为自动加载函数

}else{

　　function __autoload($class){         //如果不是，则重写php原生函数__autoload函数，让其调用自己的core中函数。

　　　　return core::autoload($class);

　　}

}

### php基础函数- 字符串函数
k
php基础函数- 字符串函数
去空格或或其他字符:
trim() 删除字符串两端的空格或其他预定义字符

"\r\nHello World!\r\n";
echo trim($str);
目标字串 清除后的字符串

rtrim() 删除字符串右边的空格或其他预定义字符

$str = "Hello World!\n\n";
echo rtrim($str);
chop() rtrim()的别名

ltrim() 删除字符串左边的空格或其他预定义字符

$str = "\r\nHello World!";
echo ltrim($str);	

dirname() 返回路径中的目录部分
echo dirname("c:/testweb/home.php");
一个包含路径的字符串
返回文件路径的目录部分//c:/testweb

字符串生成与转化:
str_pad() 把字符串填充为指定的长度

$str = "Hello World";
echo str_pad($str,20,".");	
要填充的字符串|新字符串的长度|供填充使用的字符串，默认是空白 完成后的字符串

str_repeat() 重复使用指定字符串

echo str_repeat(".",13);	
要重复的字符串|字符串将被重复的次数 13个点

str_split() 把字符串分割到数组中

print_r(str_split("Hello"));	
要分割的字符串|每个数组元素的长度，默认1 拆分后的字符串数组

strrev() 反转字符串

echo strrev("Hello World!");
目标字符串 颠倒顺序后的字符串!dlroW olleH

wordwrap() 按照指定长度对字符串进行折行处理

$str = "An example on a long word is: Supercalifragulistic";
echo wordwrap($str,15);	
目标字符串|最大宽数 折行后的新字符串

str_shuffle() 随机地打乱字符串中所有字符

echo str_shuffle("Hello World");	
目标字符串 顺序打乱后的字符串

parse_str() 将字符串解析成变量

parse_str("id=23&name=John%20Adams",$myArray);
print_r($myArray);	
要解析的字符串|存储变量的数组名称 返回

Array(
[id] => 23
[name] => John Adams)	　
number_format() 通过千位分组来格式化数字
要格式化的数字|规定多少个小数|规定用作小数点的字符串|规定用作千位分隔符的字符串

1,000,000
1,000,000.00
1.000.000,00	
大小写转换:
strtolower() 字符串转为小写

echo strtolower("Hello WORLD!");
目标字符串 小写字符串

strtoupper() 字符串转为大写

echo strtoupper("Hello WORLD!");	　	
大写字符串

ucfirst() 字符串首字母大写

echo ucfirst("hello world");	　
Hello world

ucwords() 字符串每个单词首字符转为大写

echo ucwords("hello world");	　
Hello World	　
html标签关联:
htmlentities() 把字符转为HTML实体

$str = "John & 'Adams'";
echo htmlentities($str, ENT_COMPAT);	　	
John & 'Adams'
htmlspecialchars() 预定义字符转html编码

nl2br()

\n转义为<br>标签	echo nl2br("One line.\nAnother line.");	　	
处理后的字符串

strip_tags() 剥去 HTML、XML 以及 PHP 的标签

echo strip_tags("Hello <b>world!</b>");	　	　	　	
addcslashes() 在指定的字符前添加反斜线转义字符串中字符

$str = "Hello, my name is John Adams.";
echo $str;
echo addcslashes($str,'m');	
目标字符串|指定的特定字符或字符范围 　 　
stripcslashes() 删除由addcslashes()添加的反斜线

echo stripcslashes("Hello, \my na\me is Kai Ji\m.");
目标字符串	
Hello, my name is Kai Jim.	　					
addslashes() 指定预定义字符前添加反斜线

$str = "Who's John Adams?";
echo addslashes($str);	
把目标串中的' " \和null进行转义处理 　
stripslashes() 删除由addslashes()添加的转义字符

echo stripslashes("Who\'s John Adams?");	　	
清除转义符号Who's John Adams?	
quotemeta() 在字符串中某些预定义的字符前添加反斜线

$str = "Hello world. (can you hear me?)";
echo quotemeta($str);	　	
Hello world\. \(can you hear me\?\)	. \ + * ? [] ^ $ () 
chr() 从指定的 ASCII 值返回字符

echo chr(052);	
ASCII 值 返回对应的字符//*

ord() 返回字符串第一个字符的 ASCII 值

echo ord("hello");	
字符串 第一个字符的 ASCII 值

字符串比较:
strcasecmp() 不区分大小写比较两字符串

echo strcasecmp("Hello world!","HELLO WORLD!");	
两个目标字符串 大1|等0|小-1

strcmp() 区分大小写比较两字符串

strncmp() 比较字符串前n个字符,区分大小写

int strncmp ( string $str1 , string $str2 , int $len )	
strncasecmp() 比较字符串前n个字符,不区分大小写

int strncasecmp ( string $str1 , string $str2 , int $len )	
strnatcmp() 自然顺序法比较字符串长度,区分大小写

int strnatcmp ( string $str1 , string $str2 )	

strnatcasecmp() 自然顺序法比较字符串长度,不区分大小写

int strnatcasecmp ( string $str1 , string $str2 )	
字符串切割与拼接:
chunk_split() 将字符串分成小块

str chunk_split(str $body[,int $len[,str $end]])	
$body目标字串,$len长度,$str插入结束符	分割后的字符串	
strtok() 切开字符串
str strtok(str $str,str $token)	目标字符串$str，以$token为标志切割	返回切割后的字符串
explode() 使用一个字符串为标志分割另一个字符串

array explode(str $sep,str $str[,int $limit])	
$sep为分割符,$str目标字符串,$limit返回数组最多包含元素数	字符串被分割后形成的数组	
implode() 同join,将数组值用预订字符连接成字符串

string implode ( string $glue , array $pieces )	$glue默认，用''则直接相连	　	　				
substr() 截取字符串

string substr ( string $string , int $start [, int $length ] )	　
字符串查找替换:
str_replace() 字符串替换操作,区分大小写

mix str_replace(mix $search,,mix $replace,mix $subject[,int &$num])	
$search查找的字符串,$replace替换的字符串,$subject被查找字串,&$num	
返回替换后的结果
str_ireplace() 字符串替换操作,不区分大小写

mix str_ireplace ( mix $search , mix $replace , mix $subject [, int &$count ] )	
$search查找的字符串,$replace替换的字符串,$subject被查找字串,&$num	
返回替换后的结果	　
substr_count() 统计一个字符串,在另一个字符串中出现次数

int substr_count ( string $haystack , string $needle [, int $offset = 0 [, int $length ]] )
~~~	　	　

substr_replace()	替换字符串中某串为另一个字符串	
mixed substr_replace ( mixed $string , string $replacement , int $start [, int $length ] )


similar_text()	返回两字符串相同字符的数量
int similar_text(str $str1,str $str2)
两个比较的字符串 整形,相同字符数量


strrchr()	返回一个字符串在另一个字符串中最后一次出现位置开始到末尾的字符串	
string strrchr ( string $haystack , mixed $needle )


strstr()	返回一个字符串在另一个字符串中开始位置到结束的字符串	
string strstr ( string $str, string $needle , bool $before_needle )


strchr()	strstr()的别名,返回一个字符串在另一个字符串中首次出现的位置开始到末尾的字符串	

string strstr ( string $haystack , mixed $needle [, bool $before_needle = false ] )


stristr()	返回一个字符串在另一个字符串中开始位置到结束的字符串，不区分大小写	string
stristr ( string $haystack , mixed $needle [, bool $before_needle = false ] )


strtr()	转换字符串中的某些字符	
string strtr ( string $str , string $from , string $to )


strpos()	寻找字符串中某字符最先出现的位置	
int strpos ( string $haystack , mixed $needle [, int $offset = 0 ] )


stripos()	寻找字符串中某字符最先出现的位置,不区分大小写	

int stripos ( string $haystack , string $needle [, int $offset ] )


strrpos()	寻找某字符串中某字符最后出现的位置	
int strrpos ( string $haystack , string $needle [, int $offset = 0 ] )


strripos()	寻找某字符串中某字符最后出现的位置,不区分大小写	
int strripos ( string $haystack , string $needle [, int $offset ] )

strspn()	返回字符串中首次符合mask的子字符串长度	

int strspn ( string $str1 , string $str2 [, int $start [, int $length ]] )


strcspn()	返回字符串中不符合mask的字符串的长度	
int strcspn ( string $str1 , string $str2 [, int $start [, int $length ]] )
$str1被查询，$str2查询字符串，$start开始查询的字符，$length查询长度 返回从开始到第几个字符


## 字符串统计:	
str_word_count()	统计字符串含有的单词数	
mix str_word_count(str $str,[])
目标字符串 统计处的数量


strlen()	统计字符串长度	
int strlen(str $str)
目标字符串 整型长度


count_chars()	统计字符串中所有字母出现次数(0..255)	
mixed count_chars ( string $string [, int $mode ] )


## 字符串编码:	　	　	　	　	　								
md5()	字符串md5编码	
$str = "Hello";
echo md5($str);
### php基础函数-数学函数
php基础函数-数学函数
数学函数
函数名	描述	实例	输入	输出
abs()	求绝对值	$abs = abs(-4.2); //4.2	数字	绝对值数字
ceil()	进一法取整	echo ceil(9.999); // 10	浮点数	进一取整
floor()	舍去法取整	echo floor(9.999); // 9	浮点数	直接舍去小数部分
pi()	获取圆周率值	echo pi(); // 3.1415926535898	无	获取圆周率
rand()	随机数	最小	最大,随机数	随机返回范围内的值
mt_rand()	更好的随机数	echo mt_rand(0,9);//n 最小	最大,随机数	随机返回范围内的值
pow()	返回数的n次方	echo pow(-1, 20); // 1	基础数	n次方 乘方值
sqrt()	求平方根	echo sqrt(9); //3	被开方的数	平方根
min()	求最小值		多个数字或数组	返回其中的最小值
max()	求最大值	"echo max(1, 3, 5, 6, 7); // 7 echo max(array(2, 4, 5)); // 5"	多个数字或数组	返回其中的最大值
round()	浮点数四舍五入	echo round(1.95583, 2);// 1.96	一个数值	保留小数点后多少位,默认为0 舍入后的结果
fmod()	浮点数取余	$x = 5.7;$y = 1.3;$r = fmod($x, $y); // $r equals 0.5, because 4 * 1.3 + 0.5 = 5.7	两个浮点数,x>y
### php基础函数-数组函数
php基础函数-数组函数
数组创建:
array()生成一个数组

"$a=array(""Dog"",""Cat"",""Horse"");
print_r($a);"
数组值或,键=>值
一个数组型变量

array_combine()生成一个数组,用一个数组的值作为键名,另一个数组值作为值

"$a1=array(""a"",""b"",""c"",""d"");
$a2=array(""Cat"",""Dog"",""Horse"",""Cow"");
print_r(array_combine($a1,$a2));"
$a1为提供键,$a2提供值
合成后的数组

range()创建并返回一个包含指定范围的元素的数组。

"$number = range(0,50,10);
print_r ($number);"
0是最小值,50是最大值,10是步长
合成后的数组

compact()创建一个由参数所带变量组成的数组

"$firstname = ""Peter"";
$lastname = ""Griffin"";
$age = ""38"";
$result = compact(""firstname"", ""lastname"", ""age"");
print_r($result);
"
变量或数组
返回由变量名为键,变量值为值的数组,变量也可以为多维数组.会递归处理

array_fill()用给定的填充(值生成)数组

"$a=array_fill(2,3,""Dog"");
print_r($a);"
2是键,3是填充的数量,'Dog'为填充内容
返回完成的数组

数组合并和拆分：
array_chunk() 把一个数组分割为新的数组块

"$a=array(""a""=>""Cat"",""b""=>""Dog"",""c""=>""Horse"",""d""=>""Cow"");
print_r(array_chunk($a,2));"
一个数组
分割后的多维数组，规定每个新数组包含2个元素

array_merge()	把两个或多个数组合并为一个数组。	
"$a1=array(""a""=>""Horse"",""b""=>""Dog"");
$a2=array(""c""=>""Cow"",""b""=>""Cat"");
print_r(array_merge($a1,$a2));"	
两个数组
返回完成后的数组

array_slice() 在数组中根据条件取出一段值，并返回。

"$a=array(0=>""Dog"",1=>""Cat"",2=>""Horse"",3=>""Bird"");
print_r(array_slice($a,1,2));"	
一个数组
1为从'Cat'开始，2为返回两个元素

数组比较：
array_diff() 返回两个数组的差集数组

"$a1=array(0=>""Cat"",1=>""Dog"",2=>""Horse"");
$a2=array(3=>""Horse"",4=>""Dog"",5=>""Fish"");
print_r(array_diff($a1,$a2));"	
两个或多个数组
返回'Cat'，$a1与$a2的不同之处

array_intersect()
返回两个或多个数组的交集数组
返回'Dog'和'Horse',$a1与$a2的相同之处

数组查找替换：
array_search() 在数组中查找一个键值

"$a=array(""a""=>""Dog"",""b""=>""Cat"",""c""=>""Horse"");
echo array_search(""Dog"",$a);"	
一个数组
成功返回键名,失败返回false
等同于in_array()

array_splice() 把数组中一部分删除用其他值替代

"$a1=array(0=>""Dog"",1=>""Cat"",2=>""Horse"",3=>""Bird"");
$a2=array(0=>""Tiger"",1=>""Lion"");
array_splice($a1,0,2,$a2);
print_r($a1);"	
一个或多个数组 $a1被移除的部分由$a2补全
将原数组替换,注意替换后数组中键名不保留

array_sum() 返回数组中所有值的总和

"$a=array(0=>""5"",1=>""15"",2=>""25"");
echo array_sum($a);"	
一个数组
返回和

in_array() 在数组中搜索给定的值,区分大小写

"$people = array(""Peter"", ""Joe"", ""Glenn"", ""Cleveland"");
if (in_array(""Glenn"",$people){
  echo ""Match found"";}else{
  echo ""Match not found"";}"	
需要搜索的值|数组
true/false

array_key_exists()
判断某个数组中是否存在指定的 key
需要搜索的键名|数组

数组指针操作:
key() 返回数组内部指针当前指向元素的键名

current() 返回数组中的当前元素（单元）。 别名pos()

next() 把指向当前元素的指针移动到下一个元素的位置，并返回当前元素的值

prev() 把指向当前元素的指针移动到上一个元素的位置，并返回当前元素的值

end() 将数组内部指针指向最后一个元素，并返回该元素的值（如果成功）

reset() 把数组的内部指针指向第一个元素，并返回这个元素的值

list() 用数组中的元素为一组变量赋值

"$my_array=array(""Dog"",""Cat"",""Horse"");
list($a, $b, $c) = $my_array;"	
$a, $b, $c为需要赋值的变量
变量分别匹配数组中的值

array_shift() 删除数组中的第一个元素，并返回被删除元素的值

"$a=array(""a""=>""Dog"",""b""=>""Cat"",""c""=>""Horse"");
echo array_shift($a);
print_r ($a);"	
array_unshift() 在数组开头插入一个或多个元素

"$a=array(""a""=>""Cat"",""b""=>""Dog"");
array_unshift($a,""Horse"");
print_r($a);"	
array_push() 向数组最后压入一个或多个元素

"$a=array(""Dog"",""Cat"");
array_push($a,""Horse"",""Bird"");
print_r($a);"	
目标数组|需要压入的值 返回新的数组

array_pop() 删除数组中的最后一个元素

"$a=array(""Dog"",""Cat"",""Horse"");
array_pop($a);
print_r($a);"	
$a为目标数组 返回数组剩余元素 可赋给一个变量输出被弹出的元素

数组键值操作:
shuffle() 将数组打乱,保留键名

"$my_array = array(""a"" => ""Dog"", ""b"" => ""Cat"");
shuffle($my_array);
print_r($my_array);"	
一个或多个数组 顺序打乱后的数组 打乱顺序后键名不会有变化

count() 计算数组中的单元数目或对象中的属性个数

"$people = array(""Peter"", ""Joe"", ""Glenn"", ""Cleveland"");
$result = count($people);
echo $result;"	
数组 输出元素个数

array_flip() 返回一个键值反转后的数组 "$a=array(0=>""Dog"",1=>""Cat"",2=>""Horse"");print_r(array_flip($a));"
返回完成后的数组

array_keys() 返回数组所有的键,组成一个数组

"$a=array(""a""=>""Horse"",""b""=>""Cat"",""c""=>""Dog"");
print_r(array_keys($a));"	
返回由键名组成的数组

array_values() 返回数组中所有值，组成一个数组 同上 返回由键值组成的数组
array_reverse() 返回一个元素顺序相反的数组 同上 元素顺序相反的一个数组，键名和键值依然匹配
array_count_values() 统计数组中所有的值出现的次数

"$a=array(""Cat"",""Dog"",""Horse"",""Dog"");
print_r(array_count_values($a));"
原键值为新键名，次数为新键值
array_rand() 从数组中随机抽取一个或多个元素,注意是键名!!!

"$a=array(""a""=>""Dog"",""b""=>""Cat"",""c""=>""Horse"");
print_r(array_rand($a,1));"	
$a为目标数组，1为抽取第几个元素的键名 返回第1个元素的键名b
each(

array_unique() 删除重复值，返回剩余数组

"$a=array(""a""=>""Cat"",""b""=>""Dog"",""c""=>""Cat"");
print_r(array_unique($a));"
数组 返回无重复值数组，键名不变 当几个数组元素的值相等时，只保留第一个元素，其他的元素被删除

数组排序:
sort() 按升序对给定数组的值排序,不保留键名

"$my_array = array(""a"" => ""Dog"", ""b"" => ""Cat"", ""c"" => ""Horse"");
sort($my_array);
print_r($my_array);"	
true/false 对数组元素进行重排,同时改变键名

rsort() 对数组逆向排序,不保留键名 对数组元素进行重排,同时改变键名

asort() 对数组排序,保持索引关系 对数组进行排序,保留原来的索引或键

arsort() 对数组逆向排序,保持索引关系

ksort() 按键名对数组排序 对键名排序,保留键值对应关系

krsort() 将数组按照键逆向排序 保留原来的键

natsort() 用自然顺序算法对数组中的元素排序 对值进行自然排序,保留键值对应关系

natcasesort() 自然排序,不区分大小写 =A2:F53小写的对值进行自然法排序,保持键值对应关系
### PHP常见排序算法学习
PHP常见排序算法学习
【一】.冒泡排序
思路分析：

想象一个大水池里有N多还未排好的序列的氢气球，较大的先冒出来，然后依次是较小的往上冒。即，每次比较相邻的两个数，小的在前大的在后，否则进行位置互换。

代码实现：（举例几种写法，注意循环体的判断条件）建议使用第一、二种。

   /**
     * 交换方法
     * @param array $arr 目标数组
     * @param $a 索引a
     * @param $b 索引b
     * @param bool $flag 交换标志
     * @return bool
     */
    function swap(array &$arr,$a,$b,$flag = false){
        // 遍历i后面的元素，只要该元素小于当前元素，就把较小的往前冒泡
        if($arr[$a] > $arr[$b]){
            $temp = $arr[$a];
            $arr[$a] = $arr[$b];
            $arr[$b] = $temp;
            $flag = true;
        }
        return $flag;
    }
    /**
     * 第一种写法
     * @param $arr 所要排序的数组
     * @return mixed 返回的数组
     */
    function bubbleSort($arr) {
        $len = count($arr);
        if ($len <= 1) {return $arr;}
        //该层循环控制 需要冒泡的轮数
        for ($i = 0; $i < $len-1; $i++) {
            //该层循环用来控制每轮 冒出一个数 需要比较的次数
            for ($j = $i + 1; $j < $len; $j++) {
                // 或者 $this->swap($arr,$j,$j+1);
                $this->swap($arr,$i,$j);
            }
        }
        return $arr;
    }
    //第二种写法
    public function BubbleSort2($arr){
        $len = count($arr);
        if ($len <= 1) {return $arr;}
        for ($i = 0;$i < $len-1;$i++){
            //TODO 本趟排序开始前，交换标志应为假
            $flag = false;
            for ($j = 0;$j <= $len-2;$j++){
                $flag = $this->swap($arr,$j,$j+1,$flag);
            }
            if(!$flag) return $arr;
        }
        return $arr;
    }
    //第三种写法
    function BubbleSort3(array &$arr){
        $len = count($arr);
        if ($len <= 1) {return $arr;}
        for($i = 0;$i < $len-1;$i++){
            //从后往前逐层上浮小的元素 $j >= 0
            for($j = $len - 2;$j >= $i ;$j --){
                $this->swap($arr,$j,$j+1);
            }
        }
        return $arr;
    }
    //第四种写法
    function bubbleSort4($arr)
    {
        $len = count($arr);
        if ($len <= 1) {return $arr;}
        for($i = 0;$i < $len-1;$i++) {
            for($j = 0;$j < $len-$i-1;$j++) {
                $this->swap($arr,$j,$j+1);
            }
        }
        return $arr;
    }

小结：

时间复杂度：O(n^2)
补充：可使用PHP内置函数 sort()或rsort().
上述函数对索引数组按照键值进行排序，为 array 中的单元赋予新的键名，这将删除原有的键名而不仅是重新排序。如果成功则返回 TRUE，否则返回 FALSE

【二】.选择排序
思路分析：

每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完

代码实现

   /*
    * @param 选择排序法
    * 每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完
    * */
    function selectSort($arr){
        //双重循环完成，外层控制轮数，内层控制比较次数
        $len = count($arr);
        if ($len <= 1) {return $arr;}
        for ($i = 0; $i < $len-1; $i++) {
            $minIndex = $i;
            // 找出i后面最小的元素与当前元素交换
            for ($j = $i + 1; $j < $len; $j++) {
                if ($arr[$minIndex] > $arr[$j]){
                    $minIndex = $j;
                }
            }
            if ($minIndex != $i) {
                $temp = $arr[$i];
                $arr[$i] = $arr[$minIndex];
                $arr[$minIndex] = $temp;
            }
        }
        return $arr;
    }

小结：

时间复杂度：O(n^2)
不稳定的排序方法（比如序列[5， 5， 3]第一次就将第一个[5]与[3]交换，导致第一个5挪动到第二个5后面）。
在一趟选择，如果一个元素比当前元素小，而该小的元素又出现在一个和当前元素相等的元素后面，那么交换后稳定性就被破坏了
最好情况是，已经有序，交换0次；最坏情况交换n-1次，逆序交换n/2次。交换次数比冒泡排序少多了，由于交换所需CPU时间比比较所需的CPU时间多，n值较小时，选择排序比冒泡排序快

【三】.插入排序
思路分析：

每步将一个待排序的纪录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。(从而得到一个新的、个数加一的有序数据)

描述：
⒈ 从第一个元素开始，该元素可以认为已经被排序
⒉ 取出下一个元素，在已经排序的元素序列中从后向前扫描
⒊ 如果该元素（已排序）大于新元素，将该元素移到下一位置
⒋ 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
⒌ 将新元素插入到下一位置中
⒍ 重复步骤 2~5



代码实现

  /*
    * 插入排序法
    * 每步将一个待排序的记录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。
    * */
    function insertSort($arr){
        $len = count($arr);
        if ($len <= 1) {return $arr;}
        //先默认$array[0]，已经有序，是有序表
        for($i = 1;$i < $len;$i++){
            if ($arr[$i] < $arr[$i-1]){
                $insertVal = $arr[$i]; //$insertVal是准备插入的数
                $insertIndex = $i - 1; //有序表中准备比较的数的下标
                while($insertIndex >= 0 && $insertVal < $arr[$insertIndex]){
                    $arr[$insertIndex + 1] = $arr[$insertIndex]; //将数组往后挪
                    $insertIndex--; //将下标往前挪，准备与前一个进行比较
                }
                if($insertIndex + 1 !== $i){
                    $arr[$insertIndex + 1] = $insertVal;
                }
            }
        }
        return $arr;
    }
    function insertSort2($arr){
        $len = count($arr);
        if ($len <= 1) {return $arr;}
        //先默认$array[0]，已经有序，是有序表
        for($i = 1;$i < $len;$i++){
            if ($arr[$i] < $arr[$i-1]){
                $insertVal = $arr[$i]; //$insertVal是准备插入的数
                //$j 有序表中准备比较的数的下标
                //$j-- 将下标往前挪，准备与前一个进行比较
                for ($j = $i-1;$j >= 0 && $insertVal < $arr[$j];$j--){
                    $arr[$j+1]= $arr[$j];//将数组往后挪
                }
                $arr[$j + 1] = $insertVal;
            }
        }
        return $arr;
    }
小结：

时间复杂度：O(n^2)
空间复杂度：O(1) (用于记录需要插入的数据)
稳定的排序方法
算法适用于少量数据的排序
如果比较操作的代价比交换操作大的话，可以采用二分查找法来减少比较操作的数目。该算法可以认为是插入排序的一个变种，称为二分查找排序。

【四】.快速排序
思路分析：

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列

代码实现

   /**
     * @param $arr 目标数组
     * @param int $l 左起坐标
     * @param $r 右起坐标 初始化传入数组时，$r = count($arr)-1
     * @return mixed
     */
    public  function quick_sort(&$arr, $l=0, $r)
    {
        $length = count($arr);
        //先判断是否需要继续进行 递归出口:数组长度为1，直接返回数组
        if(!is_array($arr)||$length <= 1) {return $arr;}
        if ($l < $r)
        {
            $i = $l;
            $j = $r;
            $baseVal = $arr[$l];
            while ($i < $j)
            {
                // 从右向左找第一个小于$baseVal的数
                while($i < $j && $arr[$j] >= $baseVal)
                    $j--;
                if($i < $j)
                    $arr[$i++] = $arr[$j];
                // 从左向右找第一个大于等于$baseVal的数
                while($i < $j && $arr[$i] < $baseVal)
                    $i++;
                if($i < $j)
                    $arr[$j--] = $arr[$i];
            }
            $arr[$i] = $baseVal;
            $this->quick_sort($arr, $l, $i - 1); // 递归调用
            $this->quick_sort($arr, $i + 1, $r);
            return $arr;
        }
    }
    /*
    * 快速排序法
    * */
    public function quick_sort2($arr) {
        $length = count($arr);
        //先判断是否需要继续进行 递归出口:数组长度为1，直接返回数组
        if(!is_array($arr)||$length <= 1) {return $arr;}
        //选择第一个元素作为基准
        $baseValue = $arr[0];
        //遍历除了标尺外的所有元素，按照大小关系放入两个数组内
        //初始化两个数组
        $leftArr = array();  //小于基准的
        $rightArr = array();  //大于基准的
        //使用for循环进行遍历，把选定的基准当做比较的对象
        for($i = 1; $i<$length; $i++) {
            if( $arr[$i] < $baseValue) {
                //放入左边数组
                $leftArr[] = $arr[$i];
            } else {
                //放入右边数组
                $rightArr[] = $arr[$i];
            }
        }
        //再分别对左边和右边的数组进行相同的排序处理方式递归调用这个函数
        $leftArr = $this->quick_sort2($leftArr);
        $rightArr = $this->quick_sort2($rightArr);
        //合并 左边 标尺 右边， 注意：array($baseValue),关联着重复数据
        return array_merge($leftArr, array($baseValue), $rightArr);
    }
小结：

既不浪费空间又可以快一点的排序算法
最差时间复杂度O(N^2)，平均时间复杂度为O(NlogN)

【五】.计数排序
思路分析

计数排序使用一个额外的数组C，其中第i个元素是待排序数组A中值等于i的元素的个数。然后根据数组C来将A中的元素排到正确的位置。它只能对整数进行排序

算法描述：
找出待排序的数组中最大和最小的元素；
统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1


代码实现

    /**
     * 计数排序
     * @param $arr
     * @return array
     */
    function countingSort($arr)
    {
        $len = count( $arr );
        if( $len <= 1 ) return $arr;
        // 找出待排序的数组中最大值和最小值
        $min = min($arr);
        $max = max($arr);
        // 计算待排序的数组中每个元素的个数
        $countArr = array();
        for($i = $min; $i <= $max; $i++)
        {
            $countArr[$i] = 0;
        }
        foreach($arr as $v)
        {
            $countArr[$v] +=  1;
        }
        $resArr = array();
        foreach ($countArr as $k=>$c) {
            for($i = 0; $i < $c; $i++)
            {
                $resArr[] = $k;
            }
        }
        return $resArr;
    }
小结：

计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
计数排序不是比较排序，排序的速度快于任何比较排序算法
最佳情况：T(n) = O(n+k)
最差情况：T(n) = O(n+k)
平均情况：T(n) = O(n+k)

【六】.桶排序
思路分析

假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序(有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排)

算法描述
设置一个定量的数组当作空桶；
遍历输入数据，并且把数据一个一个放到对应的桶里去；
对每个不是空的桶进行排序；
从不是空的桶里把排好序的数据拼接起来。

代码实现

  /**
     * 木桶排序设计
     * @param $arr 目标数组
     * @param int $bucketCount 分配的木桶数目（整数）
     * @return array
     */
    public function bucketSort($arr,$bucketCount = 10)
    {
        $len = count($arr);
        $max = max($arr)+1;
        if ($len <= 1) {return $arr;}
        //填充木桶
        $arrFill = array_fill(0, $bucketCount, []);
        //开始标示木桶
        for($i = 0; $i < $len ; $i++)
        {
            $key = intval($arr[$i]/($max/$bucketCount));
            array_push($arrFill[$key] , $arr[$i]);
            //TODO 测试发现：如果此处调用，耗时翻倍
            /*if(count($arrFill[$key])){
                $arrFill[$key] = $this->insertSort($arrFill[$key]);
            }*/
        }
        //对每个不是空的桶进行排序
        foreach ($arrFill as $key=>$f){
            if (count($f)){
                $arrFill[$key] = $this->insertSort($f);
            }
        }
        //开始从木桶中拿出数据
        for($i = 0; $i < count($arrFill); $i ++)
        {
            if($arrFill[$i]){
                for($j = 0; $j <= count($arrFill[$i]); $j++)
                {   //这一行主要用来控制输出多个数字
                    if ($arrFill[$i][$j]){
                        $arrBucket[] = $arrFill[$i][$j];
                    }
                }
            };
        }
        return $arrBucket;
    }

上述代码是我根据对木桶排序的定义进行的设计，因为网上多数的PHP代码感觉不合规范，其中的insertSort()为借用的文中所写的插入排序
通过测试发现，此方法耗时比countingSort()要长好多，此处仅做参考不做推荐。

总结：

当输入的元素是n 个0到k之间的整数时，它的运行时间是 O(n + k)。计数排序不是比较排序，排序的速度快于任何比较排序算法。由于用来计数的数组C的长度取决于待排序数组中数据的范围（等于待排序数组的最大值与最小值的差加上1），这使得计数排序对于数据范围很大的数组，需要大量时间和内存。
稳定的排序方法
桶排序是计数排序的升级版
最佳情况：T(n) = O(n+k)
最差情况：T(n) = O(n^2)
平均情况：T(n) = O(n+k)

## PHP函数
### 获取文章图片
$pattern="/<[img|IMG].*?src=[\'|\"](.*?(?:[\.gif|\.jpg|\.png]))[\'|\"].*?[\/]?>/";  
获取文章第一张图片

/**
 * 字符串加密、解密函数
 * @param	string	$content		内容
 */
function getpic($content){
    preg_match('/<\s*img\s+[^>]*?src\s*=\s*(\'|\")(.*?)\\1[^>]*?\/?\s*>/i',$content,$matc);
    print_r($matc);
    }
打印结果

Array
(
    [0] => <img src="/public/uploads/20161221/7.jpg" alt="">
    [1] => "
    [2] => /public/uploads/20161221/7.jpg
)
3.获取文章所有的图片

function getpic($content){
     preg_match('/<img.+src=\"?(.+\.(jpg|gif|bmp|bnp|png|jpeg))\"?.+>/i',$str,$match);
     print_r($matc);
    }
打印结果

Array
(
    [0] => <img src="/public/uploads/20161221/7.jpg" alt=""><img src="/public/uploads/20161220/a.jpeg" alt="">
    [1] => /public/uploads/20161220/a.jpeg
    [2] => jpeg
)

### 加密解密
加密解密函数

/**
 * 字符串加密、解密函数
 * @param	string	$txt		字符串
 * @param	string	$operation	ENCODE为加密，DECODE为解密，可选参数，默认为ENCODE，
 * @param	string	$key		密钥：数字、字母、下划线
 * @param	string	$expiry		过期时间
 * @return	string
 */
function encry_code($string, $operation = 'ENCODE', $key = '', $expiry = 0) {
    $ckey_length = 4;
    $key = md5($key != '' ? $key : config('encry_key'));
    $keya = md5(substr($key, 0, 16));
    $keyb = md5(substr($key, 16, 16));
    $keyc = $ckey_length ? ($operation == 'DECODE' ? substr($string, 0, $ckey_length) : substr(md5(microtime()), -$ckey_length)) : '';

    $cryptkey = $keya . md5($keya . $keyc);
    $key_length = strlen($cryptkey);

    $string = $operation == 'DECODE' ? base64_decode(strtr(substr($string, $ckey_length), '-_', '+/')) : sprintf('%010d', $expiry ? $expiry + time() : 0) . substr(md5($string . $keyb), 0, 16) . $string;
    $string_length = strlen($string);

    $result = '';
    $box = range(0, 255);

    $rndkey = array();
    for ($i = 0; $i <= 255; $i++) {
        $rndkey[$i] = ord($cryptkey[$i % $key_length]);
    }

    for ($j = $i = 0; $i < 256; $i++) {
        $j = ($j + $box[$i] + $rndkey[$i]) % 256;
        $tmp = $box[$i];
        $box[$i] = $box[$j];
        $box[$j] = $tmp;
    }

    for ($a = $j = $i = 0; $i < $string_length; $i++) {
        $a = ($a + 1) % 256;
        $j = ($j + $box[$a]) % 256;
        $tmp = $box[$a];
        $box[$a] = $box[$j];
        $box[$j] = $tmp;
        $result .= chr(ord($string[$i]) ^ ($box[($box[$a] + $box[$j]) % 256]));
    }

    if ($operation == 'DECODE') {
        if ((substr($result, 0, 10) == 0 || substr($result, 0, 10) - time() > 0) && substr($result, 10, 16) == substr(md5(substr($result, 26) . $keyb), 0, 16)) {
            return substr($result, 26);
        } else {
            return '';
        }
    } else {
        return $keyc . rtrim(strtr(base64_encode($result), '+/', '-_'), '=');
    }
}

onethink提供加密解密


/**
 * 系统非常规MD5加密方法
 * @param  string $str 要加密的字符串
 * @return string 
 */
function think_ucenter_md5($str, $key = 'ThinkUCenter'){
	return '' === $str ? '' : md5(sha1($str) . $key);
}

/**
 * 系统加密方法
 * @param string $data 要加密的字符串
 * @param string $key  加密密钥
 * @param int $expire  过期时间 (单位:秒)
 * @return string 
 */
function think_ucenter_encrypt($data, $key, $expire = 0) {
	$key  = md5($key);
	$data = base64_encode($data);
	$x    = 0;
	$len  = strlen($data);
	$l    = strlen($key);
	$char =  '';
	for ($i = 0; $i < $len; $i++) {
		if ($x == $l) $x=0;
		$char  .= substr($key, $x, 1);
		$x++;
	}
	$str = sprintf('%010d', $expire ? $expire + time() : 0);
	for ($i = 0; $i < $len; $i++) {
		$str .= chr(ord(substr($data,$i,1)) + (ord(substr($char,$i,1)))%256);
	}
	return str_replace('=', '', base64_encode($str));
}

/**
 * 系统解密方法
 * @param string $data 要解密的字符串 （必须是think_encrypt方法加密的字符串）
 * @param string $key  加密密钥
 * @return string 
 */
function think_ucenter_decrypt($data, $key){
	$key    = md5($key);
	$x      = 0;
	$data   = base64_decode($data);
	$expire = substr($data, 0, 10);
	$data   = substr($data, 10);
	if($expire > 0 && $expire < time()) {
		return '';
	}
	$len  = strlen($data);
	$l    = strlen($key);
	$char = $str = '';
	for ($i = 0; $i < $len; $i++) {
		if ($x == $l) $x = 0;
		$char  .= substr($key, $x, 1);
		$x++;
	}
	for ($i = 0; $i < $len; $i++) {
		if (ord(substr($data, $i, 1)) < ord(substr($char, $i, 1))) {
			$str .= chr((ord(substr($data, $i, 1)) + 256) - ord(substr($char, $i, 1)));
		}else{
			$str .= chr(ord(substr($data, $i, 1)) - ord(substr($char, $i, 1)));
		}
	}
	return base64_decode($str);
}

encrypt加密解密

//encrypt加密decrypt解密,支持js
function encode_base64($sData){ 
    $sBase64 = base64_encode($sData); 
    return strtr($sBase64, '+/', '-_'); 
} 

function decode_base64($sData){ 
    $sBase64 = strtr($sData, '-_', '+/'); 
    return base64_decode($sBase64); 
}
function encrypt($sData, $sKey){ 
    $sResult = ''; 
    for($i=0;$i<strlen($sData);$i++){ 
        $sChar    = substr($sData, $i, 1); 
        $sKeyChar = substr($sKey, ($i % strlen($sKey)) - 1, 1); 
        $sChar    = chr(ord($sChar) + ord($sKeyChar)); 
        $sResult .= $sChar; 
    } 
    return encode_base64($sResult); 
} 

function decrypt($sData, $sKey){ 
    $sResult = ''; 
    $sData   = decode_base64($sData); 
    for($i=0;$i<strlen($sData);$i++){ 
        $sChar    = substr($sData, $i, 1); 
        $sKeyChar = substr($sKey, ($i % strlen($sKey)) - 1, 1); 
        $sChar    = chr(ord($sChar) - ord($sKeyChar)); 
        $sResult .= $sChar; 
    } 
    return $sResult; 
}

### JSON数据输出（适合在tp中）
JSON数据输出

/**
 * 数据输出
 * @param	string	$status		状态码
 * @param	string	$data		数据
 * @param	string	$format  输出方式
 * @return	string
 */
 public function output( $status, $data, $format = 'json' )
    {
        $_return_array = [];

        if ( $status == 's' ) {
            $_return_array['status'] = 'success';
        } elseif ( $status == 'f' ) {
            $_return_array['status'] = 'failure';
        } elseif ( $status == 'p' ) {
            $_return_array['status'] = 'pending';
        } else {
            $_return_array['status'] = $status;
        }

        if ( is_array( $data ) ) {
            $_return_array['result'] = $data;
        } else {
            $_return_array['result'] = trim( $data );
        }

        switch ( $format ) {
            case 'json':
                return json( $_return_array, 201 );
                break;
            case 'jsonp':
                return jsonp( $_return_array, 201 );
                break;
            case 'view':
            case 'html':
                return view( $_return_array, 201 );
                break;
            case 'xml':
                return xml( $_return_array, 201 );
                break;
            default:
                return json_encode( $_return_array, JSON_UNESCAPED_UNICODE );
        }
    }

return $this->output('s'，$result)

### 删除目录和文件
/**
 * 循环删除目录和文件
 * @param string $dir_name
 * @return bool
 */
function delete_dir_file($dir_name) {
    $result = false;
    if(is_dir($dir_name)){
        if ($handle = opendir($dir_name)) {
            while (false !== ($item = readdir($handle))) {
                if ($item != '.' && $item != '..') {
                    if (is_dir($dir_name . DS . $item)) {
                        delete_dir_file($dir_name . DS . $item);
                    } else {
                        unlink($dir_name . DS . $item);
                    }
                }
            }
            closedir($handle);
            if (rmdir($dir_name)) {
                $result = true;
            }
        }
    }

    return $result;
}

function destroyDir($dir){
        $ds = DIRECTORY_SEPARATOR;
        $dir = substr($dir, -1) == $ds ? substr($dir, 0, -1) : $dir;
        if(is_dir($dir) && $handle = opendir($dir)){
                while($file = readdir($handle)){
                        if($file == '.' || $file == '..'){
                                continue;
                        }elseif(is_dir($dir.$ds.$file)){
                                destroyDir($dir.$ds.$file);
                        }else{
                                unlink($dir.$ds.$file);
                        }
                }
                closedir($handle);
                rmdir($dir);
        }
}

### 判断是否为手机访问
/**
 * 判断是否为手机访问
 * @return  boolean
 */
function is_mobile() {
    static $is_mobile;

    if (isset($is_mobile)) {
        return $is_mobile;
    }

    if (empty($_SERVER['HTTP_USER_AGENT'])) {
        $is_mobile = false;
    } elseif (strpos($_SERVER['HTTP_USER_AGENT'], 'Mobile') !== false
              || strpos($_SERVER['HTTP_USER_AGENT'], 'Android') !== false
              || strpos($_SERVER['HTTP_USER_AGENT'], 'Silk/') !== false
              || strpos($_SERVER['HTTP_USER_AGENT'], 'Kindle') !== false
              || strpos($_SERVER['HTTP_USER_AGENT'], 'BlackBerry') !== false
              || strpos($_SERVER['HTTP_USER_AGENT'], 'Opera Mini') !== false
              || strpos($_SERVER['HTTP_USER_AGENT'], 'Opera Mobi') !== false
    ) {
        $is_mobile = true;
    } else {
        $is_mobile = false;
    }

    return $is_mobile;
}
function checkmobile(){
	$useragent = strtolower($_SERVER['HTTP_USER_AGENT']);
	$touchbrowser_list = array('ipod', 'ipad', 'iphone', 'android', 'phone', 'mobile', 'wap', 'netfront', 'java', 'opera mobi', 'opera mini', 'ucweb', 'windows ce', 'symbian', 'series', 'webos', 'sony', 'blackberry', 'dopod', 'nokia', 'samsung', 'palmsource', 'xda', 'pieplus', 'meizu', 'midp', 'cldc', 'motorola', 'foma', 'docomo', 'up.browser', 'up.link', 'blazer', 'helio', 'hosin', 'huawei', 'novarra', 'coolpad', 'webos', 'techfaith', 'palmsource', 'alcatel', 'amoi', 'ktouch', 'nexian', 'ericsson', 'philips', 'sagem', 'wellcom', 'bunjalloo', 'maui', 'smartphone', 'iemobile', 'spice', 'bird', 'zte-', 'longcos', 'pantech', 'gionee', 'portalmmm', 'jig browser', 'hiptop', 'benq', 'haier', '^lct', '320x320', '240x320', '176x220', 'windows phone');
	$wmlbrowser_list = array('cect', 'compal', 'ctl', 'lg', 'nec', 'tcl', 'alcatel', 'ericsson', 'bird', 'daxian', 'dbtel', 'eastcom', 'pantech', 'dopod', 'philips', 'haier', 'konka', 'kejian', 'lenovo', 'benq', 'mot', 'soutec', 'nokia', 'sagem', 'sgh', 'sed', 'capitel', 'panasonic', 'sonyericsson', 'sharp', 'amoi', 'panda', 'zte');
	$brower = array('mozilla', 'chrome', 'safari', 'opera', 'm3gate', 'winwap', 'openwave', 'myop');
	
	if(dstrpos($useragent, $touchbrowser_list)){
		return true;
	}elseif(dstrpos($useragent, $wmlbrowser_list)){
		return true;
	}elseif(dstrpos($useragent, $brower)){
		return false;
	}else{
		return false;
	}
}
function dstrpos($string, $arr){
	if(empty($string)){return false;}
	foreach((array)$arr as $v){
		if(strpos($string, $v) !== false){
			return true;
		}
	}
	return false;
}

### 获取客户端真实IP
dede方法获取用户真实地址

    function GetIP()
    {
        static $realip = NULL;
        if ($realip !== NULL)
        {
            return $realip;
        }
        if (isset($_SERVER))
        {
            if (isset($_SERVER['HTTP_X_FORWARDED_FOR']))
            {
                $arr = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
                /* 取X-Forwarded-For中第x个非unknown的有效IP字符? */
                foreach ($arr as $ip)
                {
                    $ip = trim($ip);
                    if ($ip != 'unknown')
                    {
                        $realip = $ip;
                        break;
                    }
                }
            }
            elseif (isset($_SERVER['HTTP_CLIENT_IP']))
            {
                $realip = $_SERVER['HTTP_CLIENT_IP'];
            }
            else
            {
                if (isset($_SERVER['REMOTE_ADDR']))
                {
                    $realip = $_SERVER['REMOTE_ADDR'];
                }
                else
                {
                    $realip = '0.0.0.0';
                }
            }
        }
        else
        {
            if (getenv('HTTP_X_FORWARDED_FOR'))
            {
                $realip = getenv('HTTP_X_FORWARDED_FOR');
            }
            elseif (getenv('HTTP_CLIENT_IP'))
            {
                $realip = getenv('HTTP_CLIENT_IP');
            }
            else
            {
                $realip = getenv('REMOTE_ADDR');
            }
        }
        preg_match("/[\d\.]{7,15}/", $realip, $onlineip);
        $realip = ! empty($onlineip[0]) ? $onlineip[0] : '0.0.0.0';
        return $realip;
    }
获取用户真实IP

function getIp() { 
    if (getenv("HTTP_CLIENT_IP") && strcasecmp(getenv("HTTP_CLIENT_IP"), "unknown")) 
        $ip = getenv("HTTP_CLIENT_IP"); 
    else 
        if (getenv("HTTP_X_FORWARDED_FOR") && strcasecmp(getenv("HTTP_X_FORWARDED_FOR"), "unknown")) 
            $ip = getenv("HTTP_X_FORWARDED_FOR"); 
        else 
            if (getenv("REMOTE_ADDR") && strcasecmp(getenv("REMOTE_ADDR"), "unknown")) 
                $ip = getenv("REMOTE_ADDR"); 
            else 
                if (isset ($_SERVER['REMOTE_ADDR']) && $_SERVER['REMOTE_ADDR'] && strcasecmp($_SERVER['REMOTE_ADDR'], "unknown")) 
                    $ip = $_SERVER['REMOTE_ADDR']; 
                else 
                    $ip = "unknown"; 
    return ($ip); 
}
获取在线IP

/**
 * 获取在线IP
 * @return String
 */
function getOnlineIp($format=0) {
 global $S_GLOBAL;
 if(empty($S_GLOBAL['onlineip'])) {
  if(getenv('HTTP_CLIENT_IP') && strcasecmp(getenv('HTTP_CLIENT_IP'), 'unknown')) {
   $onlineip = getenv('HTTP_CLIENT_IP');
  } elseif(getenv('HTTP_X_FORWARDED_FOR') && strcasecmp(getenv('HTTP_X_FORWARDED_FOR'), 'unknown')) {
   $onlineip = getenv('HTTP_X_FORWARDED_FOR');
  } elseif(getenv('REMOTE_ADDR') && strcasecmp(getenv('REMOTE_ADDR'), 'unknown')) {
   $onlineip = getenv('REMOTE_ADDR');
  } elseif(isset($_SERVER['REMOTE_ADDR']) && $_SERVER['REMOTE_ADDR'] && strcasecmp($_SERVER['REMOTE_ADDR'], 'unknown')) {
   $onlineip = $_SERVER['REMOTE_ADDR'];
  }
  preg_match("/[\d\.]{7,15}/", $onlineip, $onlineipmatches);
  $S_GLOBAL['onlineip'] = $onlineipmatches[0] ? $onlineipmatches[0] : 'unknown';
 }

 if($format) {
  $ips = explode('.', $S_GLOBAL['onlineip']);
  for($i=0;$i<3;$i++) {
   $ips[$i] = intval($ips[$i]);
  }
  return sprintf('%03d%03d%03d', $ips[0], $ips[1], $ips[2]);
 } else {
  return $S_GLOBAL['onlineip'];
 }
}
获取客户端IP

/**
 * 获取客户端IP
 * @return [string] [description]
 */
function getClientIp() {
 $ip = NULL;
 if (isset($_SERVER['HTTP_X_FORWARDED_FOR'])) {
  $arr = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
  $pos = array_search('unknown',$arr);
  if(false !== $pos) unset($arr[$pos]);
  $ip = trim($arr[0]);
 }elseif (isset($_SERVER['HTTP_CLIENT_IP'])) {
  $ip = $_SERVER['HTTP_CLIENT_IP'];
 }elseif (isset($_SERVER['REMOTE_ADDR'])) {
  $ip = $_SERVER['REMOTE_ADDR'];
 }
 // IP地址合法验证
 $ip = (false !== ip2long($ip)) ? $ip : '0.0.0.0';
 return $ip;
}
### 随机生成ip地址
function ip()
{
    $ip_long = array(
        array('607649792', '608174079'), // 36.56.0.0-36.63.255.255
        array('1038614528', '1039007743'), // 61.232.0.0-61.237.255.255
        array('1783627776', '1784676351'), // 106.80.0.0-106.95.255.255
        array('2035023872', '2035154943'), // 121.76.0.0-121.77.255.255
        array('2078801920', '2079064063'), // 123.232.0.0-123.235.255.255
        array('-1950089216', '-1948778497'), // 139.196.0.0-139.215.255.255
        array('-1425539072', '-1425014785'), // 171.8.0.0-171.15.255.255
        array('-1236271104', '-1235419137'), // 182.80.0.0-182.92.255.255
        array('-770113536', '-768606209'), // 210.25.0.0-210.47.255.255
        array('-569376768', '-564133889'), // 222.16.0.0-222.95.255.255
        );
    $rand_key = mt_rand(0, 9);
    return $ip = long2ip(mt_rand($ip_long[$rand_key][0], $ip_long[$rand_key][1]));
} 
简单使用
echo ip();

### 字符串与二进制进行转换
function StrToBin($str){
    //1.列出每个字符
    $arr = preg_split('/(?<!^)(?!$)/u', $str);
    //2.unpack字符
    foreach($arr as &$v){
        $temp = unpack('H*', $v);
        $v = base_convert($temp[1], 16, 2);
        unset($temp);
    }

    return join(' ',$arr);
}

function BinToStr($str){
    $arr = explode(' ', $str);
    foreach($arr as &$v){
        $v = pack("H".strlen(base_convert($v, 2, 16)), base_convert($v, 2, 16));
    }

    return join('', $arr);
}

简单实用

  echo StrToBin("小知识大道理");
  echo BinToStr('111001011011000010001111 111001111001111110100101 111010001010111110000110 111001011010010010100111 111010011000000110010011 111001111001000010000110');
### 对数组进行排序
	/**
	* 对结果集进行排序
	* @access public
	* @param array $list 查询结果
	* @param string $field 排序的字段名
	* @param array $sortby 排序类型
	* asc正向排序 desc逆向排序 nat自然排序
	* @return array
	*/
	function list_sort_by($list,$field, $sortby='asc') {
	   if(is_array($list)){
		   $refer = $resultSet = array();
		   foreach ($list as $i => $data)
			   $refer[$i] = &$data[$field];
		   switch ($sortby) {
			   case 'asc': // 正向排序
					asort($refer);
					break;
			   case 'desc':// 逆向排序
					arsort($refer);
					break;
			   case 'nat': // 自然排序
					natcasesort($refer);
					break;
		   }
		   foreach ( $refer as $key=> $val)
			   $resultSet[] = &$list[$key];
		   return $resultSet;
	   }
	   return false;
	}
    
###  格式化字节大小
	/**
	 * 格式化字节大小
	 * @param  number $size      字节数
	 * @param  string $delimiter 数字和单位分隔符
	 * @return string            格式化后的带单位的大小
	 */
	function format_bytes($size, $delimiter = '') {
		$units = array('B', 'KB', 'MB', 'GB', 'TB', 'PB');
		for ($i = 0; $size >= 1024 && $i < 5; $i++) $size /= 1024;
		return round($size, 2) . $delimiter . $units[$i];
	}

function formatsize($size){
	$prec = 3;
	$size = round(abs($size));
	$units = array(0 => " B", 1 => " KB", 2 => " MB", 3 => " GB", 4 => " TB");
	if($size == 0){
		return str_repeat(" ", $prec)."0".$units[0];
	}
	$unit = min(4, floor(log($size) / log(2) / 10));
	$size = $size * pow(2, -10 * $unit);
	$digi = $prec - 1 - floor(log($size) / log(10));
	$size = round($size * pow(10, $digi)) * pow(10, -$digi);
	return $size.$units[$unit];
}

### 时间戳格式化
	/**
	 * 时间戳格式化
	 * @param int $time
	 * @return string 完整的时间显示
	 */
	function time_format($time = NULL,$format='Y-m-d H:i'){
		$time = $time === NULL ? NOW_TIME : intval($time);
		return date($format, $time);
	}
格式化时间线

/**
* 
* @param 时间戳 $time
* 
* 格式化时间线
*/
function timeline($time){
    if(time()<=$time){
    return date("Y-m-d H:i:s",$time);
    }else{
    $t = time()-$time;  
    $f = array(  
        '31536000'=>'年',  
        '2592000'=>'个月',  
        '604800'=>'星期',  
        '86400'=>'天',  
        '3600'=>'小时',  
        '60'=>'分钟',  
        '1'=>'秒'  
    );  
    foreach($f as $k=>$v){  
        if(0 != $c = floor($t/(int)$k)){  
            return $c.$v.'前';  
        }  
    }
    }
}
date_default_timezone_set('PRC'); //默认时区 
//当前的时间增加5天
$date1 = "2018-5-20";
echo date('Y-m-d',strtotime("$date1 +5 day"));  //输出结果：2018-5-25
//相应地,要增加月,年,将day改成month或year即可
 
 
//+++ 今天、昨天、明天 、上一周、下一周 +++++++++
echo "今天:",date("Y-m-d",time()),"<hr>"; 
echo "昨天:",date("Y-m-d",strtotime("-1 day")), "<hr>"; 
echo "明天:",date("Y-m-d",strtotime("+1 day")), "<hr>"; 
echo "一周后:",date("Y-m-d",strtotime("+1 week")), "<hr>"; 
echo "一周零两天四小时两秒后:",date("Y-m-d G:H:s",strtotime("+1 week 2 days 4 hours 2 seconds")), "<hr>"; 
echo "下个星期四:",date("Y-m-d",strtotime("next Thursday")), "<hr>"; 
echo "上个周一:".date("Y-m-d",strtotime("last Monday"))."<hr>"; 
echo "一个月前:".date("Y-m-d",strtotime("last month"))."<hr>"; 
echo "一个月后:".date("Y-m-d",strtotime("+1 month"))."<hr>"; 
echo "十年后:".date("Y-m-d",strtotime("+10 year"))."<hr>";

### 获取数据的所有子孙数据的id值
/**
	 * 获取数据的所有子孙数据的id值
	 */

	function get_stemma($pids,Model &$model, $field='id'){
		$collection = array();

		//非空判断
		if(empty($pids)){
			return $collection;
		}

		if( is_array($pids) ){
			$pids = trim(implode(',',$pids),',');
		}
		$result     = $model->field($field)->where(array('pid'=>array('IN',(string)$pids)))->select();
		$child_ids  = array_column ((array)$result,'id');

		while( !empty($child_ids) ){
			$collection = array_merge($collection,$result);
			$result     = $model->field($field)->where( array( 'pid'=>array( 'IN', $child_ids ) ) )->select();
			$child_ids  = array_column((array)$result,'id');
		}
		return $collection;
	}
    
### 取得视频文件的缩略图
public function fileupload(){
        //执行视频的上传使用thinkphp上传类即可
        if (!$upload->upload()) {
            //上传错误
        }else{
        	//得到上传文件的信息
            $info = $upload->getUploadFileInfo();
            //================取得视频文件的缩略图=================
            //需要生成视频图片的大小分别为 200*140 首页的大图需要1024*450的
            //利用ffmpeg命令取得缩略图
            //首先获取上传视频所在目录的绝对路径
            $dir = explode("\\",rtrim(THINK_PATH,"/"));//删除路径最后的"/"
            array_pop($dir);
            $dir = implode("\\",$dir);//当前项目所在的目录
            $reslibdir = $dir."\\Public\\Uploads\\video\\";//拼装上传视频所在的目录
            $dstlibdir = $dir."\\Public\\Uploads\\videopic\\";//把视频的缩略图放进该目录

            $resFile = $reslibdir.$info[0]['savename'];//上传资源路径+文件名
            $randname = substr($info[0]['savename'],0,strpos($info[0]['savename'],"."));//获取资源名的随机数字
            $dstFile1 = $dstlibdir.$randname.".jpg";//生成缩略图后的路径加图片名
            //$dstFile2 = $dstlibdir."l_".$randname.".jpg";//生成1024*450的缩略图
            //调用函数exec()调用dos命令
            //$arr返回执行的结果数组 $status为请求结果 0表示成功 1表示失败
            //获取视频的缩略图
            exec("{$dir}\\Public\\ffmpeg\\bin\\ffmpeg -i {$resFile} -y -f mjpeg -ss 5 -t 0.01 -s 200*140 {$dstFile1}"); //小图
            //exec("{$dir}\\Public\\ffmpeg\\bin\\ffmpeg -i {$resFile} -y -f mjpeg -ss 100 -t 0.01 -s 1024*450 {$dstFile2}");//大图
            //================取得视频文件的缩略图=================

            $file['name'] = $info[0]['savename'];
            $file['size'] = $_FILES['Filedata']['size'];//取得文件的大小
            $fileinfo = pathinfo($_FILES['Filedata']['name']);
            $file['type'] = $fileinfo['extension'];//取得文件的类型
            $file['picname'] = $randname.".jpg";//视频的缩略图
            echo json_encode($file);
        }
    }

### 图片裁剪函数
/**
 * 图片裁剪函数
 * @param string $picname 被裁剪的图片名称。 如："a.jpg"
 * @param string $path 被裁剪图片的存放路径。如："uploads/images"目录
 * @param int $sx 被裁图片的起始坐标位置x值
 * @param int $sy 被裁图片的起始坐标位置y值
 * @param int $sw 被裁图片的宽度
 * @param int $sh 被裁图片的高度
 * @param string $prix 裁剪后图片名的前缀名。默认为: "s_"
 * @return 无返回值
 */
 
function cropImage($picname,$path,$sx,$sy,$sw,$sh,$prix="s_"){
	//1. 定义获取基本信息
	$path = rtrim($path,"/"); //去除后面多余的"/"
	$info = getimagesize($path."/".$picname);  //获取图片文件的属性信息
	//$width = $info[0]; //原图片的宽度
	//$height = $info[1]; //原图片的高度
	
	//2. 创建图像源
	$newim =imagecreateTrueColor($sw,$sh); //新图片源
	//根据原图片类型来创建图片源
	switch($info[2]){
		case 1: //gif格式
			$srcim = imageCreateFromgif($path."/".$picname);
			break;
		case 2: //jpeg格式
			$srcim = imageCreateFromjpeg($path."/".$picname);
			break;
		case 3: //png格式
			$srcim = imageCreateFrompng($path."/".$picname);
			break;
		default:
			exit("无效的图片格式!");
			break;
	}

	//3. 执行缩放处理
	imagecopyresampled($newim,$srcim,0,0,$sx,$sy,$sw,$sh,$sw,$sh);

	//4. 输出保存绘画
	//header("Content-Type:".$info['mime']); //设置响应类型为图片格式
	//根据原图片类型来保存新图片
	switch($info[2]){
		case 1: //gif格式
			imagegif($newim,$path."/".$prix.$picname); //保存
			//imagegif($newim);//输出
			break;
		case 2: //jpeg格式
			imagejpeg($newim,$path."/".$prix.$picname);
			//imagejpeg($newim);
			break;
		case 3: //png格式
			imagepng($newim,$path."/".$prix.$picname);
			//imagepng($newim);
			break;
	}
	
	//5. 销毁资源
	imageDestroy($newim);
	imageDestroy($srcim);
	
}

### 按照每过0:00算一天
按照每过0:00算一天
        function maketime($date)
        {
            list($year, $month, $day) = explode('-', $date);
            return mktime(0, 0, 0, $month, $day, $year);
        }

        $date1 = '2007-01-08';
        $date2 = '2007-01-09';
        echo $d = (maketime($date2) - maketime($date1)) / (3600 * 24);
mktime(hour,minute,second,month,day,year,is_dst)函数

is_dst 可选。如果时间在日光节约时间(DST)期间，则设置为1，否则设置为0，若未知，则设置为-1。自 5.1.0 起，is_dst 参数被废弃，因此应该使用新的时区处理特性。

### 下载文件
  /**
     * @param $id
     * @return int
     */
    public function download($id)
    {

        $map['id'] = $id;
        $book = M('books')->where($map)->find();
        $filename = $book['path'];
        var_dump(__ROOT__ . $filename);
        if (!file_exists($this->writeDecode($filename))) {
            $this->error("文件不存在");
        }
        // http headers
        header('Content-Type: application-x/force-download');
        header('Content-Disposition: attachment; filename="' . basename($filename) . '"');
        ob_end_clean();
        return readfile($this->writeDecode($filename));
    }
### PHP随机密码生成
产生随机字串，可用来自动生成密码。
特点：

可以指定密码包含数字或字符，默认为混和模式
指定随意密码长度，默认长度为6位
代码如下：

#-------------------------------------------
# 产生随机字串，可用来自动生成密码 
# 默认长度6位 字母和数字混合
# $format ALL NUMBER CHAR 字串组成格式
#-------------------------------------------
 function randStr($len=6,$format='ALL') { 
 switch($format) { 
 case 'ALL':
 $chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-@#~'; break;
 case 'CHAR':
 $chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-@#~'; break;
 case 'NUMBER':
 $chars='0123456789'; break;
 default :
 $chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-@#~'; 
 break;
 }
 mt_srand((double)microtime()*1000000*getmypid()); 
 $password="";
 while(strlen($password)<$len)
    $password.=substr($chars,(mt_rand()%strlen($chars)),1);
 return $password;
 } 
 
###  判断数字大小
判断数字的大小是否在某个范围内，如果仅仅是判断是否为数字无需使用。

 #---------------------------------------------------------- 
 # 判断数字大小，无大小的判断可以用系统带的 is_numeric($str)
 #----------------------------------------------------------
 Function isNumber ($fNum, $fMin="", $fMax="") { 
  if ( eregi("^[0-9]+$", $fNum) ) { 
   if ( "" == $fMax && "" == $fMin ) { 
   Return True;
   } elseif ( "" == $fMin && $fNum <= $fMax ) { 
   Return True;
   } elseif ( "" == $fMax && $fNum >= $fMin ) { 
   Return True;
   } elseif ( $fNum >= $fMin && $fNum <= $fMax ) { 
   Return True;
   } else { 
   Return False;
   }
  } else { 
  Return False;
  }
 }
 
###  报文组成
/**

组装报文

@param unknown_type $params

@return string

*/

function getRequestParamString($params) {

$params_str = '';

foreach ( $params as $key => $value ) {

$params_str .= ($key . '=' . (!isset ( $value ) ? '' : urlencode( $value )) . '&');

}

return substr ( $params_str, 0, strlen ( $params_str ) - 1 );

}
使用

$params = array (
	 "seller_email" =>'jqiang3@gail.com',           
	 "notify_url" =>'127.0.0.1',
);
echo getRequestParamString($params);
输出

seller_email=jqiang3%40gail.com¬ify_url=127.0.0.1

### 通过ip定位城市
/**
 * 获取城市
 */
function getCity(){
	
	$ip = request()->ip();
	$taobaoUrl = 'http://ip.taobao.com/service/getIpInfo.php?ip=' . $ip;
	
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $taobaoUrl);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt ( $ch,  CURLOPT_NOSIGNAL,true);//支持毫秒级别超时设置
	curl_setopt($ch, CURLOPT_TIMEOUT, 1200);   //1.2秒未获取到信息，视为定位失败
	$myCity = curl_exec($ch);
	curl_close($ch);
	
	$myCity = json_decode($myCity, true);
	
	return $myCity;
}

### PHP使用星号替代用户名手机和邮箱
function hideStar($str) { //用户名、邮箱、手机账号中间字符串以*隐藏 
    if (strpos($str, '@')) { 
        $email_array = explode("@", $str); 
        $prevfix = (strlen($email_array[0]) < 4) ? "" : substr($str, 0, 3); //邮箱前缀 
        $count = 0; 
        $str = preg_replace('/([\d\w+_-]{0,100})@/', '***@', $str, -1, $count); 
        $rs = $prevfix . $str; 
    } else { 
        $pattern = '/(1[3458]{1}[0-9])[0-9]{4}([0-9]{4})/i'; 
        if (preg_match($pattern, $str)) { 
            $rs = preg_replace($pattern, '$1****$2', $str); // substr_replace($name,'****',3,4); 
        } else { 
            $rs = substr($str, 0, 3) . "***" . substr($str, -1); 
        } 
    } 
    return $rs; 
} 
demo

$account = "phpfensi.com"; 
$email = "416148489@qq.com"; 
$phone = "18005152525"; 
<?php echo hideStar($account); ?>
<?php echo hideStar($email); ?>
<?php echo hideStar($phone); ?>

### 获取毫秒级别的时间戳
    /**
     * 获取毫秒级别的时间戳
     */
    private static function getMillisecond()
    {
        //获取毫秒的时间戳
        $time = explode ( " ", microtime () );
        $time = $time[1] . ($time[0] * 1000);
        $time2 = explode( ".", $time );
        $time = $time2[0];
        return $time;
    }
### 随机颜色生成器
function randomColor() { 
    $str = '#'; 
    for($i = 0 ; $i < 6 ; $i++) { 
        $randNum = rand(0 , 15); 
        switch ($randNum) { 
            case 10: $randNum = 'A'; break; 
            case 11: $randNum = 'B'; break; 
            case 12: $randNum = 'C'; break; 
            case 13: $randNum = 'D'; break; 
            case 14: $randNum = 'E'; break; 
            case 15: $randNum = 'F'; break; 
        } 
        $str .= $randNum; 
    } 
    return $str; 
} 
$color = randomColor();

### 常见PHP 正则表达式
验证域名检验一个字符串是否是个有效域名

$url = "http://komunitasweb.com/"; 
if (preg_match('/^(http|https|ftp)://([A-Z0-9][A-Z0-9_-]*(?:.[A-Z0-9][A-Z0-9_-]*)+):?(d+)?/?/i', $url)) { 
  echo "Your url is ok."; 
} else { 
  echo "Wrong url."; 
}
从一个字符串中 突出某个单词
这是一个非常有用的在一个字符串中匹配出某个单词 并且突出它，非常有效的搜索结果

$text = "Sample sentence from KomunitasWeb, regex has become popular in web programming. Now we learn regex. According to wikipedia, Regular expressions (abbreviated as regex or 

regexp, with plural forms regexes, regexps, or regexen) are written in a formal language that can be interpreted by a regular expression processor"; 
$text = preg_replace("/b(regex)b/i", '<span style="background:#5fc9f6">1</span>', $text); 
echo $text;
突出查询结果在你的 WordPress 博客里就像刚才我说的，上面的那段代码可以很方便的搜索出结果，而这里是一个更好的方式去执行搜索在某个WordPress的博客上打开你的文件 search.php ，然后找到 方法 the_title() 然后用下面代码替换掉它

echo $title; 
Now, just before the modified line, add this code: 

<?php 
  $title   = get_the_title(); 
  $keys= explode(" ",$s); 
  $title   = preg_replace('/('.implode('|', $keys) .')/iu', 
    '<strong>\0</strong>', 
    $title); 
?> 

Save the search.php file and open style.css. Append the following line to it: 

strong.search-excerpt { background: yellow; }
　　从HTML文档中获得全部图片

　　如果你曾经希望去获得某个网页上的全部图片，这段代码就是你需要的，你可以轻松的建立一个图片下载机器人

$images = array(); 
preg_match_all('/(img|src)=("|')[^"'>]+/i', $data, $media); 
unset($data); 
$data=preg_replace('/(img|src)("|'|="|=')(.*)/i',"$3",$media[0]); 
foreach($data as $url) 
{ 
  $info = pathinfo($url); 
  if (isset($info['extension'])) 
  { 
    if (($info['extension'] == 'jpg') || 
    ($info['extension'] == 'jpeg') || 
    ($info['extension'] == 'gif') || 
    ($info['extension'] == 'png')) 
    array_push($images, $url); 
  } 
}
删除重复字母

经常重复输入字母? 这个表达式正适合.

$text = preg_replace("/s(w+s)1/i", "$1", $text);
删除重复的标点

功能同上，但只是面对标点，白白重复的逗号

$text = preg_replace("/.+/i", ".", $text);
匹配一个XML或者HTML标签

这个简单的函数有两个参数：第一个是你要匹配的标签，第二个是包含XML或HTML的变量，再强调下，这个真的很强大

function get_tag( $tag, $xml ) { 
 $tag = preg_quote($tag); 
 preg_match_all('{<'.$tag.'[^>]*>(.*?)</'.$tag.'>.'}', 
          $xml, 
          $matches, 
          PREG_PATTERN_ORDER); 

 return $matches[1]; 
}
匹配具有属性值的XML或者HTML标签

这个功能和上面的非常相似，但是它允许你匹配的标签内部有属性值，例如你可以轻松匹配

function get_tag( $attr, $value, $xml, $tag=null ) { 
 if( is_null($tag) ) 
  $tag = '\w+'; 
 else 
  $tag = preg_quote($tag); 

 $attr = preg_quote($attr); 
 $value = preg_quote($value); 

 $tag_regex = "/<(".$tag.")[^>]*$attr\s*=\s*". 
        "(['\"])$value\\2[^>]*>(.*?)<\/\\1>/" 

 preg_match_all($tag_regex, 
         $xml, 
         $matches, 
         PREG_PATTERN_ORDER); 

 return $matches[3]; 
}
　　匹配十六进制颜色值

　　web开发者的另一个有趣的工具，它允许你匹配和验证十六进制颜色值.

$string = "#555555"; 
if (preg_match('/^#(?:(?:[a-fd]{3}){1,2})$/i', $string)) { 
echo "example 6 successful."; 
}
查找页面 title

这段代码方便查找和打印 网页 之间的内容

$fp = fopen("http://www.catswhocode.com/blog","r"); 
while (!feof($fp) ){ 
  $page .= fgets($fp, 4096); 
} 

$titre = eregi("<title>(.*)</title>",$page,$regs); 
echo $regs[1]; 
fclose($fp);
解释 Apache 日志

大多数网站使用的都是著名的Apache服务器，如果你的网站也是，那么使用PHP正则表达式解析 apache 服务器日志 怎么样？

//Logs: Apache web server 
//Successful hits to HTML files only. Useful for counting the number of page views. 
'^((?#client IP or domain name)S+)s+((?#basic authentication)S+s+S+)s+[((?#date and time)[^]]+)]s+"(?:GET|POST|HEAD) ((?#file)/[^ ?"]+?.html?)??((?#parameters)[^ ?"]+)? HTTP/[0-9.]+"s+(?#status code)200s+((?#bytes transferred)[-0-9]+)s+"((?#referrer)[^"]*)"s+"((?#user agent)[^"]*)"$' 

//Logs: Apache web server 
//404 errors only 
'^((?#client IP or domain name)S+)s+((?#basic authentication)S+s+S+)s+[((?#date and time)[^]]+)]s+"(?:GET|POST|HEAD) ((?#file)[^ ?"]+)??((?#parameters)[^ ?"]+)? HTTP/[0-9.]+"s+(?#status code)404s+((?#bytes transferred)[-0-9]+)s+"((?#referrer)[^"]*)"s+"((?#user agent)[^"]*)"$'
使用智能引号代替双引号

如果你是一个印刷爱好者，你将喜欢这个允许用智能引号代替双引号的正则表达式，这个正则被WORDPRESS在其内容上使用

preg_replace('B"b([^"x84x93x94rn]+)b"B', '?1?', $text);
检验密码的复杂度

这个正则表达式将检测输入的内容是否包含6个或更多字母，数字，下划线和连字符. 输入必须包含至少一个大写字母，一个小写字母和一个数字

'A(?=[-_a-zA-Z0-9]*?[A-Z])(?=[-_a-zA-Z0-9]*?[a-z])(?=[-_a-zA-Z0-9]*?[0-9])[-_a-zA-Z0-9]{6,}z'
WordPress: 使用正则获得帖子上的图片

我知道很多人是WORDPRESS的使用者，你可能会喜欢并且愿意使用 那些从帖子的内容检索下来的图像代码。使用这个代码在你的BLOG只需要复制下面代码到你的某个文件里

<?php if (have_posts()) : ?> 
<?php while (have_posts()) : the_post(); ?> 

<?php 
$szPostContent = $post->post_content; 
$szSearchPattern = '~<img [^>]* />~'; 

// Run preg_match_all to grab all the images and save the results in $aPics 
preg_match_all( $szSearchPattern, $szPostContent, $aPics ); 

// Check to see if we have at least 1 image 
$iNumberOfPics = count($aPics[0]); 

if ( $iNumberOfPics > 0 ) { 
   // Now here you would do whatever you need to do with the images 
   // For this example the images are just displayed 
   for ( $i=0; $i < $iNumberOfPics ; $i++ ) { 
     echo $aPics[0][$i]; 
   }; 
}; 

endwhile; 
endif; 
?>
自动生成笑脸图案

被WordPress使用的另一个方法, 这段代码可使你把图像自动更换一个笑脸符号

$texte='A text with a smiley '; 
echo str_replace(':-)','<img src="smileys/souriant.png">',$texte);
　　移除图片的链接

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
<?php 
  $str = ' 
    <a href="http://www.jobbole.com/">jobbole</a>其他字符 
    <a href="http://www.sohu.com/">sohu</a> 
    <a href="http://www.sohu.com/"><img src="http://www.fashion-press.net/img/news/3176/mot_06.jpg" /></a> 
    <br>'; 

  //echo preg_replace("/(<a.*?>)(<img.*?>)(<\/a>)/", '$2', $str);  
  echo preg_replace("/(<a.*?>)(<img.*?>)(<\/a>)/", '\2', $str);  
?>

### php获取浏览器类型
/**
 * 获取浏览器类型
 */
function getBrowser() {
    $user_OSagent = $_SERVER['HTTP_USER_AGENT'];
    if (strpos($user_OSagent, "Maxthon") && strpos($user_OSagent, "MSIE")) {
        $visitor_browser = "Maxthon(Microsoft IE)";
    } elseif (strpos($user_OSagent, "Maxthon 2.0")) {
        $visitor_browser = "Maxthon 2.0";
    } elseif (strpos($user_OSagent, "Maxthon")) {
        $visitor_browser = "Maxthon";
    } elseif (strpos($user_OSagent, "Edge")) {
        $visitor_browser = "Edge";
    } elseif (strpos($user_OSagent, "Trident")) {
        $visitor_browser = "IE";
    } elseif (strpos($user_OSagent, "MSIE")) {
        $visitor_browser = "IE";
    } elseif (strpos($user_OSagent, "MSIE")) {
        $visitor_browser = "MSIE 较高版本";
    } elseif (strpos($user_OSagent, "NetCaptor")) {
        $visitor_browser = "NetCaptor";
    } elseif (strpos($user_OSagent, "Netscape")) {
        $visitor_browser = "Netscape";
    } elseif (strpos($user_OSagent, "Chrome")) {
        $visitor_browser = "Chrome";
    } elseif (strpos($user_OSagent, "Lynx")) {
        $visitor_browser = "Lynx";
    } elseif (strpos($user_OSagent, "Opera")) {
        $visitor_browser = "Opera";
    } elseif (strpos($user_OSagent, "MicroMessenger")) {
        $visitor_browser = "微信浏览器";
    } elseif (strpos($user_OSagent, "Konqueror")) {
        $visitor_browser = "Konqueror";
    } elseif (strpos($user_OSagent, "Mozilla/5.0")) {
        $visitor_browser = "Mozilla";
    } elseif (strpos($user_OSagent, "Firefox")) {
        $visitor_browser = "Firefox";
    } elseif (strpos($user_OSagent, "U")) {
        $visitor_browser = "Firefox";
    } else {
        $visitor_browser = "其它";
    }
    return $visitor_browser;
}

### 邮件发送
安装phpmailer

composer require phpmailer/phpmailer
使用函数

/**
 * @param $FromName 发件人昵称
 * @param array $toaddres 发送人邮箱
 * @param string $title 发送人标题
 * @param string $Body 发送人内容
 * @param array $conf 配置项
 * @return bool
 * @throws \PHPMailer\PHPMailer\Exception
 */
function sendEmail($FromName, $toaddres=[], $Subject, $Body, $conf=[]){
    $def=[
        'Host'=>'smtp.qq.com',//链接域名邮箱的服务器地址
        'SMTPSecure'=>'ssl',//设置使用ssl加密方式登录鉴权
        'Port'=>465,//TCP端口连接
        'SMTPDebug'=>1,//启用详细的调试输出
        'Username'=>'',//SMTP用户名
        'Password'=>''//SMTP密码
    ];
    $config=array_merge($def,$conf);
    $mail= new PHPMailer\PHPMailer\PHPMailer();
    // 是否启用smtp的debug进行调试 开发环境建议开启 生产环境注释掉即可 默认关闭debug调试模式
     $mail->SMTPDebug = $config['SMTPDebug'];
    // 使用smtp鉴权方式发送邮件
    $mail->isSMTP();
    // smtp需要鉴权 这个必须是true
    $mail->SMTPAuth = true;
    // 链接qq域名邮箱的服务器地址
    $mail->Host = $config['Host'];
    // 设置使用ssl加密方式登录鉴权
    $mail->SMTPSecure = $config['SMTPSecure'];
    $mail->Port = $config['Port'];
    // 设置发送的邮件的编码
    $mail->CharSet = 'UTF-8';
    // 设置发件人昵称 显示在收件人邮件的发件人邮箱地址前的发件人姓名
    $mail->FromName = '发送人昵称';
    // smtp登录的账号 QQ邮箱即可
    $mail->Username = $config['Username'];
    // smtp登录的密码 使用生成的授权码
    $mail->Password = $config['Password'];
    // 设置发件人邮箱地址 同登录账号
    $mail->From = $config['Username'];
    // 邮件正文是否为html编码 注意此处是一个方法
    $mail->isHTML(true);
    // 设置收件人邮箱地址
  if (is_array($toaddres)){
        foreach ( $toaddres as $v){
           $mail->addAddress($v);
         }
       }else{
       $mail->addAddress($toaddres);
   }
    // 添加该邮件的主题
//    $mail->Subject = $Subject;
    $mail->Subject = '主题';
    // 添加邮件正文
//    $mail->Body = $Body;
    $mail->Body = 'das';
    // 为该邮件添加附件
    // $mail->addAttachment('./example.pdf');
    // 发送邮件 返回状态
    $status = $mail->send();
    return $status;
}

### 获取qq昵称
<?php
function getQQNick($qq){
 $str = file_get_contents('http://r.pengyou.com/fcg-bin/cgi_get_portrait.fcg?uins='.$qq);
 $pattern = '/'.preg_quote('0,0,0,"','/').'(.*?)'.preg_quote('",','/').'/i';
 preg_match ( $pattern,$str, $result );
 return $result[1];
}

$instr = getQQNick(1751212020);
//echo $instr;
//header("content-Type: text/html; charset=Utf-8"); 
//做一个GBK To UTF-8
echo mb_convert_encoding($instr, "UTF-8", "GBK"); 
?>

### 正则获取手机号归属地
<?php
/**
 * 手机号归属地查询
 */
header("Access-Control-Allow-Origin:*");
header('Content-type: application/json');
error_reporting(0);

if(isset($_GET['tel'])&&is_numeric($_GET['tel'])){
	$tel = $_GET['tel'];
}else{
	echo json_encode(array('code'=>'201','msg'=>'不是正确的手机号'));
	exit();
}
/*获取接口数据*/
$string = httpGet('https://shouji.supfree.net/fish.asp?cat='.$tel);
/*编码转换*/
$string = mb_convert_encoding($string,'utf-8', 'gbk');
/*正则查找*/
preg_match_all('/<p>(.*)<\/p>/',$string,$str);

$local = strip_tags($str[1][0]);
$duan = strip_tags($str[1][1]);
$type = strip_tags($str[1][2]);
$yys = strip_tags($str[1][3]);
$bz = strip_tags($str[1][5]);

if($local!=''){
	echo json_encode(array('code'=>'200','tel'=>$tel,'local'=>$local,'duan'=>$duan,'type'=>$type,'yys'=>$yys,'bz'=>$bz));
}else{
	echo json_encode(array('code'=>'202','msg'=>'该手机号无数据'));
	exit();
}

function httpGet($a, $b = '', $c = '', $d = ''){
	/*curl模拟get请求*/
	$e = curl_init();
	$f = mt_rand(11, 191) . "." . mt_rand(0, 240) . "." . mt_rand(1, 240) . "." . mt_rand(1, 240);
	$i[] = "CLIENT-IP:" . $f;
	$i[] = "X-FORWARDED-FOR:" . $f;
	$i[] = "User-agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11";
	$i[] = "X-Requested-With: XMLHttpRequest";
	if (!empty($d)) {
		$i[] = "Cookie: " . $d;
	}
	curl_setopt($e, CURLOPT_HTTPHEADER, $i);
	curl_setopt($e, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($e, CURLOPT_TIMEOUT, 180);
	curl_setopt($e, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($e, CURLOPT_SSL_VERIFYHOST, false);
	if (!empty($c)) {
		curl_setopt($e, CURLOPT_REFERER, $c);
	}
	if (!empty($b)) {
		curl_setopt($e, CURLOPT_POST, 1);
		curl_setopt($e, CURLOPT_POSTFIELDS, $b);
	}
	curl_setopt($e, CURLOPT_URL, $a);
	curl_setopt($e, CURLOPT_ENCODING, "gzip");
	$j = curl_exec($e);
	curl_close($e);
	return $j;
}

### 判断是否是移动客户端 移动设备
//判断是否是移动客户端 移动设备
    function isMobile() { 
      // 如果有HTTP_X_WAP_PROFILE则一定是移动设备
      if (isset($_SERVER['HTTP_X_WAP_PROFILE'])) {
        return true;
      } 
      // 如果via信息含有wap则一定是移动设备,部分服务商会屏蔽该信息
      if (isset($_SERVER['HTTP_VIA'])) { 
        // 找不到为flase,否则为true
        return stristr($_SERVER['HTTP_VIA'], "wap") ? true : false;
      } 
      // 脑残法，判断手机发送的客户端标志,兼容性有待提高。其中'MicroMessenger'是电脑微信
      if (isset($_SERVER['HTTP_USER_AGENT'])) {
        $clientkeywords = array('nokia','sony','ericsson','mot','samsung','htc','sgh','lg','sharp','sie-','philips','panasonic','alcatel','lenovo','iphone','ipod','blackberry','meizu','android','netfront','symbian','ucweb','windowsce','palm','operamini','operamobi','openwave','nexusone','cldc','midp','wap','mobile','MicroMessenger'); 
        // 从HTTP_USER_AGENT中查找手机浏览器的关键字
        if (preg_match("/(" . implode('|', $clientkeywords) . ")/i", strtolower($_SERVER['HTTP_USER_AGENT']))) {
          return true;
        } 
      } 
      // 协议法，因为有可能不准确，放到最后判断
      if (isset ($_SERVER['HTTP_ACCEPT'])) { 
        // 如果只支持wml并且不支持html那一定是移动设备
        // 如果支持wml和html但是wml在html之前则是移动设备
        if ((strpos($_SERVER['HTTP_ACCEPT'], 'vnd.wap.wml') !== false) && (strpos($_SERVER['HTTP_ACCEPT'], 'text/html') === false || (strpos($_SERVER['HTTP_ACCEPT'], 'vnd.wap.wml') < strpos($_SERVER['HTTP_ACCEPT'], 'text/html')))) {
          return true;
        } 
      } 
      return false;
    }

    // 判断是否是微信内置浏览器
    function isWeixin() { 
      if (strpos($_SERVER['HTTP_USER_AGENT'], 'MicroMessenger') !== false) { 
        return true; 
      } else {
        return false; 
      }
    }
### 人性化时间显示
//人性化时间显示
function formatTime($time){
    return $time;
    $rtime = date("m月d日 H:i",$time);
    $htime = date("H:i",$time);
    $year  = date("Y")-date("Y",$time);
    $time  = time() - $time;

    if ($time < 60){
        $str = '刚刚';
    }elseif($time < 60 * 60){
        $min = floor($time/60);
        $str = $min.'分钟前';
    }elseif($time < 60 * 60 * 24){
        $h = floor($time/(60*60));
        $str = $h.'小时前 ';
    }elseif($time < 60 * 60 * 24 * 3){
        $d = floor($time/(60*60*24));
        if($d==1){
            $str = '昨天 '.$rtime;
        }else{
            $str = '前天 '.$rtime;
        }
    }elseif($year >0){
        $str = $rtime;
    }
    else{
        $str = date("Y年m月d日 H:i",$time);
    }
    return $str;
}

### 请求API接口
get方法

/**
 * get方法
 * @param string $url 地址
 * @return string 返回页面信息
 */
function get_url($url)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL,$url);  //设置访问的url地址
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);//不输出内容
    $result =  curl_exec($ch);
    curl_close ($ch);
    return $result;
}
post方法

/**
 * post方法
 * @param string $url 地址
 * @param string $data 提交的数据
 * @return string 返回结果
 */
function post_url($url, $data)
{
    $curl = curl_init(); // 启动一个CURL会话
    curl_setopt($curl, CURLOPT_URL, $url); // 要访问的地址
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, FALSE); // 对认证证书来源的检查
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, FALSE); // 从证书中检查SSL加密算法是否存在
    curl_setopt($curl, CURLOPT_USERAGENT, 'Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)'); // 模拟用户使用的浏览器
    //curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1); // 使用自动跳转
    //curl_setopt($curl, CURLOPT_AUTOREFERER, 1);    // 自动设置Referer
    curl_setopt($curl, CURLOPT_POST, 1);             // 发送一个常规的Post请求
    curl_setopt($curl, CURLOPT_POSTFIELDS, $data);   // Post提交的数据包x
    curl_setopt($curl, CURLOPT_TIMEOUT, 30);         // 设置超时限制 防止死循环
    curl_setopt($curl, CURLOPT_HEADER, 0);           // 显示返回的Header区域内容
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);   // 获取的信息以文件流的形式返回

    $tmpInfo = curl_exec($curl); // 执行操作
    if(curl_errno($curl))
    {
       echo 'Errno'.curl_error($curl);//捕捉异常
    }
    curl_close($curl); // 关闭CURL会话
    return $tmpInfo; // 返回数据
}
对象转化为数组

/**
 * 对象转化为数组
 * @param object $obj 对象
 * @return array 数组
 */
function object_to_array($obj){
    $_arr = is_object($obj) ? get_object_vars($obj) :$obj;
    foreach ($_arr as $key=>$val){
        $val = (is_array($val) || is_object($val)) ? object_to_array($val):$val;
        $arr[$key] = $val;
    }
    return $arr;
}
数组转xml

/**
 * 数组转xml
 * @param string $arr array
 * @return string XML
 */
function arrayToXml($arr)
{
    $xml = "<xml>";
    foreach ($arr as $key=>$val)
    {
         if (is_numeric($val))
         {
            $xml.="<".$key.">".$val."</".$key.">";
         }
         else
            $xml.="<".$key."><![CDATA[".$val."]]></".$key.">";
    }
    $xml.="</xml>";
    return $xml;
}
封装

/**
 * 调用api接口
 * @param url $apiurl api.muxiangdao.cn/Article/articleList 接口地址
 * @param array $param ['status'=>'1','page'=>'2','pageshow'=>'10']; 参数(数组格式)
 * @param string $format eg:array(arr),object(obj),json;defalut = array 返回数据格式
 * @param string $method get or post 请求方法
 */
 function get_api($apiurl, $param, $format = 'array', $method = 'get'){
     if (is_array($param)) {
         $string = '?';
         foreach ($param as $key => $val){
             $string .= $key.'='.$val.'&';
         }
         $param = substr($string, 0, -1);
     }
     $url = $apiurl.$param;
     switch (strtolower($method)){
         case '':$json = get_url($url);break;
         case 'get':$json = get_url($url);break;
         case 'g':$json = get_url($url);break;
         case 'post':$json = post_url($apiurl,$param);break;
         case 'p':$json = post_url($apiurl,$param);break;
         default:$json = get_url($url);break;
     }
     $start = strpos($json, '{');
     $end = -1*(strlen(strrchr($json, '}'))-1);
     if ($end) {
        $json = substr($json, $start, $end);
     }else {
         $json = substr($json, $start);
     }
     $obj = json_decode($json);
    $array = object_to_array($obj);
    $xml = arrayToXml($array);
    switch ($format){
        case 'array':$data = $array;break;
        case 'arr':$data = $array;break;
        case 'obj':$data = $obj;break;
        case 'object':$data = $obj;break;
        case 'json':$data = $json;break;
        default:$data = $array;
    }
    return $data;
}

### PHP利用百度当图床
本地的图片果然是通过这个接口进行上传的。上传表单的文件name为 “file"。接口地址如下：
http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true

代码

<?php
 
/**
 * 上传图片到百度识图接口，获取图片外链
 * 
 * @param     $file 图片文件
 * @return    图片链接(上传成功)    NULL(上传失败)
 * @copyright (c) mengkun(https://mkblog.cn/1619/)
 */
function uploadToBaidu($file) {
    // API 接口地址
    $url = 'http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true';
    
    // 文件不存在
    if(!file_exists($file)) return '';
    
    // POST 文件
    if (class_exists('CURLFile')) {     // php 5.5
        $post['file'] = new CURLFile(realpath($file));
    } else {
        $post['file'] = '@'.realpath($file);
    }
    
    // CURL 模拟提交
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL , $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    $output = curl_exec($ch);
    curl_close($ch);
    
    // 返回结果为空（上传失败）
    if($output == '') return '';
    
    // 解析数据
    $output = json_decode($output, true);
    if(isset($output['url']) && $output['url'] != '') {
        return $output['url'];
    }
    return '';
}
 
// 使用示例：
$url = uploadToBaidu('1.jpg');
echo $url;

### 秒/分钟/小时前
function time_tran($time,$timetype=1,$showtype="Y-m-d H:i:s"){
    $now_time = time();
    if($timetype==2){//非时间戳，格式为 Y-m-d H:i:s
        $show_time = strtotime($time);
    }else{
        $show_time = $time;
    }
    $default_time = date($showtype,$show_time);
    $dur = $now_time - $show_time;
    if($dur < 0){
        return $default_time; 
    }else{
        if($dur < 60){
            return $dur.'秒前'; 
        }else{
            if($dur < 3600){
                return floor($dur/60).'分钟前'; 
            }else{
                if($dur < 86400){
                    return floor($dur/3600).'小时前'; 
                }else{
                    if($dur < 259200){//3天内
                        return floor($dur/86400).'天前';
                    }else{
                        return $default_time; 
                    }
                }
            }
        }
    }
}

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
