#mysql教程：https://www.runoob.com/mysql/mysql-tutorial.html
#sql教程：https://www.runoob.com/sql/sql-and-or.html
'''
    buffered = True

  执行sql语句查询后,MySQLCursorBuffered游标标从服务器获取整个结果集并将他们放在缓冲区中。
  Buffered游标适用于多个小结果集的查询,且多个结果集之间的数据需要一起使用。
  使用buffered游标执行查询语句时 ,取行方法（如fetchone()，fechcall()等）返回的是缓冲区中的行。
  nonbuffered游标不从服务器获取数据,直到调用了某个获取数据行的方法, 在使用nonbuffered游标时,必须确保取出的结果是结果集中的所有行，
  才能再用同一连接执行其他语句,否则会报错InternalError(Unread result found)。
  '''


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="Fqs@123456",  # 数据库密码
    database = "runoob_db",
    buffered = True
)

mycursor = mydb.cursor()

#创建数据库
# mycursor.execute("CREATE DATABASE runoob_db")

#创建表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

#创建表，同时增加主键
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

#设置主键，如果创建时没有设置
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#插入一条数据
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")

#查看
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]

mycursor.executemany(sql,val)

mydb.commit()
print(f"{mycursor.rowcount} 记录插入成功。ID:{mycursor.lastrowid}")

#查询
mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
  print(x)

print("\n")
#查看特定字段
mycursor.execute("SELECT name, url FROM sites")
myresult = mycursor.fetchmany(5)  # fetchmany 查询5条
for x in myresult:
  print(x)

#where
print("\nwhere")
#这儿要加buffered=true，不然会报错
mycursor.execute("SELECT * FROM sites WHERE name='RUNOOB'")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("为了防止sql注入")
sql = ("SELECT name,id FROM sites WHERE name=%s")
val = ("RUNOOB",)
mycursor.execute(sql, val)
myresult = mycursor.fetchone()
for x in myresult:
    print(x)

#排序
#查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC。
sql = "SELECT * FROM sites ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

print(sql)
for x in myresult:
    print(x)

#LIMIT
#如果我们要设置查询的数据量，可以通过 "LIMIT" 语句来指定
sql = "SELECT * FROM sites LIMIT 3"
mycursor.execute(sql)
myresult = mycursor.fetchall()

print(sql)
for x in myresult:
    print(x)

#指定起始位OFFSET
sql = "SELECT * FROM sites LIMIT 3 OFFSET 1"
mycursor.execute(sql)  # 0 为 第一条，1 为第二条，以此类推
myresult = mycursor.fetchall()
print(sql)

for x in myresult:
    print(x)

#删除记录
#删除记录使用 "DELETE FROM" 语句：
sql = "DELETE FROM sites WHERE name = 'RUNOOB'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")

try:
    # 更新表数据
    # 数据表更新使用 "UPDATE" 语句：
    sql = "UPDATE sites SET name = %s WHERE name = %s "
    val = ("ZH", "stackoverflow")

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, " 条记录被修改")

    # 删除表
    # 删除表使用 "DROP TABLE" 语句， IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删除：
    # sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
    # mycursor.execute(sql)
except:
    mydb.rollback()

mydb.close()