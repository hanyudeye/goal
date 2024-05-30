## 文件安全与权限

权限：读，写，执行
权限所属： owner,group,other

改变文件属性： chmodk
suid/guid: 设置为超级管理权限

符号链接： ln [-s] source_path target_path


## 使用 find 和 xargs

find pathname -options [-print -exec -ok]
 find /var/logs -type f -mtime +7 -exec rm {} \;

在整个系统中查找内存信息转储文件( coredump ) ,然后把结果保存到 /tmp/core.log 文件中:
find . -name "core" -print | xargs echo "" >/tmp/core.log

## 后台执行命令

crontab
nohup

## 正则表达式

^ 只只匹配行首
$ 只只匹配行尾
* 只一个单字符后紧跟 *,匹配0个或多个此单字符
[ ] 只匹配 [ ]内字符。可以是一个单字符,也可以是字符序列。可以使用 - 表示[]内字符序列范围,如用 [1 -5]代替[1 234 5 ]
\ 只用来屏蔽一个元字符的特殊含义。因为有时在 s h el l中一些元字符有 特殊含义。 \可以使其失去应有意义
. 只匹配任意单字符
pattern\{ n \} 只用来匹配前面 patter n出现次数。 n为次数
pattern\{n,\ }m 只含义同上,但次数最少为 n
pattern\{n,m\} 只含义同上,但 patter n出现次数在 n与m之间

## grep ,awk,sed
对文本查找和过滤

## 合并与分割

sort
uniq
join
cut
paste
split

## 登录环境和shell变量

登录流程：
1. /etc/passwd 检查帐号
2. /etc/profile  , $HOME.profile 执行配置文件

stty: 设置终端特性

## 配置shell 脚本,运行级脚本

确定当前的运行级别： who -r  或者 runlevel

## cgi脚本搭建web服务器
