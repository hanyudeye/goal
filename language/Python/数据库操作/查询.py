import pymysql

# 打开数据库
db=pymysql.connect(host="localhost",user="root",password="123456",database="test",port=3306)

try:    
    # 创建查询游标
    cursor=db.cursor()
    cursor.execute("select * from books")
    result=cursor.fetchall()
    # 打印结果
    for row in result:
        print(row)


finally:
    # 关闭数据库
    db.close()