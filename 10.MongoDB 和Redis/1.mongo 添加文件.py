from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.mydbs

#获取集合
collection = db.student

#添加文档
collection.insert_one( { "id":4,"name":"chenglong","age":18 } )
collection.insert_one( { "id":5,"name":"zhenzidan","age":19 } )
collection.insert_one( { "id":6,"name":"zhouxinchi","age":21} )
collection.insert_one( { "id":7,"name":"wumengda","age":31 } )
collection.insert_one( { "id":8,"name":"gutianle","age":25 } )


#断开
conn.close()