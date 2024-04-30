- 启动服务器  catalina run
- 修改配置端口  server.xml  ,查找端口


部署web 工程
- 1. 复制 web 工程目录 到 tomcat 的  webapps 目录下面
- 2. conf\Catalina\localhost 创建 xml文件，内容如下
```xml
<Context path="/baidu" docBase="F:/www/baidu" />
```