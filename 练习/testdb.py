import sqlite3

conn = sqlite3.connect("/Users/sunwenbo/Desktop/1300-0001-0008-0013.db")
cursor = conn.cursor()
sql = """select name from sqlite_master where type='table' order by name"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))
conn.close()

