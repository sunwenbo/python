import redis
r1 = redis.Redis(host='192.168.10.174',password='123456', port=6379, db=0)
r2 = redis.Redis(host='192.168.10.174', password='123456', port=6379, db=1)

key = r1.keys()
for k in key:
    a_data = r1.get(k)
    r2.set(k,a_data)
