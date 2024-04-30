- 配置环境变量  MAVEN_HOME
- 可以将bin目录加入环境path %MAVEN_HOME%\bin
- 打包 maven package

- 修改配置   conf/settings.xml
- 配置本地仓库 

  <localRepository>F:\mavenrepo</localRepository>

- 修改下载镜像


jar 包信息查询 http://mvnrepository.com


## 构建管理
java 测试命名 org.hanyudeye

- 清理 mvn clean 清理 target 文件夹
- 编译 mvn compile  生成 target 文件夹
- 测试 mvn test 执行测试源码
- 报告 mvn site 生成项目依赖展示页面
- 打包 mvn package 生成 war / jar 文件
- 本地部署 mvn install  打包上传到 maven 本地仓库
- 私服部署 mvn deploy 打包上传到 maven 私服仓库