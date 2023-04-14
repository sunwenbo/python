#!/usr/bin/env python

import redis
a = redis.Redis(host='10.138.20.100',
                db=1,port=6380,decode_responses=True) #0-16
from rediscluster import RedisCluster
startup_nodes = [
    {"host":"10.140.1.131", "port":6379},  # 主
    {"host":"10.140.1.106", "port":6379},  # 主
    {"host":"10.140.1.53", "port":6379}   # 主
]
redis_store= RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
for k in a.keys():   #循环取每条数据，并判断类型
    if k.startswith("prod"):
        ttl_time = a.ttl(k)
        if redis_store.exists(k) > 0:            # 如果存在了这个键，先删除它
            redis_store.delete(k)
        if a.type(k)=='zset':
            zdata = a.zrange(k,1,-1,withscores=True)
            d = dict()
            for each in zdata:
                d[each[0]] = each[1];
                redis_store.zadd(k,d);
        elif a.type(k)=='string':
            a_data = a.get(k)
            redis_store.set(k,a_data)
        redis_store.expire(k,ttl_time)

# #1 6
# # 10.138.20.101:6380   10.138.20.102:6380  10.138.20.103:6380
# r1 = redis.Redis(host='10.138.20.103',password='', port=6380, db=1)
# #r2 = redis.Redis(host='10.72.20.100',password='', port=6380, db=1)
#
# key = r1.keys()
# print(len(key))
# print(key)
#
#
# #构建所有的节点
# startup_nodes = [
#     {"host":"10.140.1.131", "port":6379},  # 主
#     {"host":"10.140.1.162", "port":6379},  # 从
#     {"host":"10.140.1.106", "port":6379},  # 主
#     {"host":"10.140.1.47", "port":6379},  # 从
#     {"host":"10.140.1.52", "port":6379},  # 从·
#     {"host":"10.140.1.53", "port":6379}   # 主
# ]
# #构建StrictRedisCluster对象
# redis_store= StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#
# maxnum = "-inf"
# minnum = "+inf"
#
# for k in key:
#     a_data = r1.get(k)
#     redis_store.set(k,a_data)
#
#
# # zdata = r1.zrangebyscore("prod_touch_1233512558_12",1,6)
# # print(zdata)
# # for k in key:
# #     a_data = r1.zrangebyscore(k,0,1)
# #     print(a_data)
#     # redis_store.zadd(k,dickey,val)
