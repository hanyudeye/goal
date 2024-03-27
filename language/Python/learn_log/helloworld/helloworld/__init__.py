
# 在这个初始化文件中，引入mysql数据库
import pymysql
pymysql.install_as_MySQLdb()

# 软后创建数据库对应的模型
# django-admin startapp TestModel