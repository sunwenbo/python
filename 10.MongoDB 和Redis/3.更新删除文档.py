import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId   #用于Id查询

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.mydbs

#获取集合
collection = db.student
#collection.update_one({"name":"chenglong"},{"$set":{"age":51}})
#删除文档，不加条件默认删除所有文档
collection.delete_one({"name":"chenglong"})


conn.close()