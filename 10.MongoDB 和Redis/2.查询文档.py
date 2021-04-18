import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId   #用于Id查询

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.mydbs

#获取集合
collection = db.student

#查询文档

#过滤查询部分文档，必须加引号
# res = collection.find({"age":{"$gt":18}})
# for row in res:
#     print(row)

#查询所有文档，
# res1 = collection.find()
# print(res1[0:3])
# for i in res1:
#     print(i)

#统计查询
# res2 = collection.count_documents({"age":{"$gt":18}})
# print(res2)

#根据ID查询

# res3 = collection.find({"_id":ObjectId("5ee9dbba4dbd84cc1c4e2195")})
# print(res3[0])

#排序
# res4 = collection.find().sort("age",)  #升序  倒叙-1
# for row in res4:
#     print(row)

print("##############")

# res4 = collection.find().sort("age",pymongo.DESCENDING)  #倒叙
# for row in res4:
#     print(row)

#分页查询
res5 = collection.find().skip(1).limit(5)
for row in res5:
    print(row)

#断开
conn.close()