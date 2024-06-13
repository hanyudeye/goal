## 源码分析

wordpress 是单入口文件，通过修改web 服务器的 rewrite 规则导向到 index.php 文件。

## 初始化阶段

初始化常量、环境、加载核心文件

index.php
``` php
//该常量定义为false时，不使用主题，站点会显示为空白，为true则正常显示
define('WP_USE_THTME',true);

```
wp-blog-header.php

用于加载WP环境和模版
``` php
$wp_did_eader=true;
//加载 wordpress library
require_once __DIR__.'/wp-load.php' //这些是加载 wp-config.php,wp-settings.php 配置
调用wp(); // 分析，并配置请求的参数
加载 wp-includes/template-loader.php //根据配置加载正确的模版

```

## 内容处理阶段

根据请求，调用相关函数获取和处理数据，为前端展示准备数据

## 主题应用阶段

根据用户请求加载相应主题模版


