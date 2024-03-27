from pymysql import Connection

conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    passwd="root"
)

# print(conn.get_server_info())

cursor=conn.cursor()
conn.select_db("pymysql")

# cursor.execute("create table test1(id int)")

cursor.execute("select * from students")

result : tuple =cursor.fetchall()
# print(result)

for t in result:
    print("id 是 ",t[0],f"name 是 {t[1]}")


conn.close()