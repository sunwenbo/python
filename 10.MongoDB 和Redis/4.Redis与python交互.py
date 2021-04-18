import redis
#连接
r = redis.StrictRedis(host="39.106.133.114",port=6381)

#方法1：根据数据类型的不同，调用响应的方法
#设置新增
r.set("p1","good")
#取值
print(r.get("p1"))

#方法2：pipline
#缓冲多条命令，然后一次执行，减少服务器--客户端的TCP数据包
# pipe = r.pipeline()
# pipe.set("p2","nice")
# pipe.set("p3","cool")
# #保存至redis
# pipe.execute()

class SunwenboRedis():
    def __init__(self,host="39.106.133.114",port=6381):
        self.__redis = redis.StrictRedis(host=host,port=port)
    def set(self,key,value):
        self.__redis.set(key,value)
    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""
    def delete(self,key):
        self.__redis.delete(key)
    def all(self):
        self.__redis.keys()
        return self.__redis.keys()

abc = SunwenboRedis()
abc.set("bbb","222")
print(abc.get("bbb"))
abc.delete("bbb")
print("#########")
print(abc.get("bbb"))
print(abc.all())