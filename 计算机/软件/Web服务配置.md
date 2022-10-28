
## 服务器隐藏入口文件

Nginx：
```
location / {
    if (!-e $request_filename){
        rewrite  ^(.*)$  /index.php?s=$1  last;   break;
    }
}
```
Apache：

```
<IfModule mod_rewrite.c>
 RewriteEngine on
 RewriteBase /
 RewriteCond %{REQUEST_FILENAME} !-d
 RewriteCond %{REQUEST_FILENAME} !-f
 RewriteRule ^(.*)$ index.php?s=/$1 [QSA,PT,L]
</IfModule>
```


## 内网穿透
可以使用域名之间访问本地搭建的服务器环境
natapp -authtoken=e4eb817e91aeee83  

由于微信屏蔽了natapp的三级域名，所以如果需要进行微信支付或者微信小程序的联调时需要注册一个二级域名
如果用于联调微信小程序的话，则需要注册带有SSL证书的，因为微信小程序仅支持https协议。


