import redis
import kazoo

class redisDB:
    """
    https://www.runoob.com/w3cnote/python-redis-intro.html
    """
    def __init__(self, connect_dict):
        self.r = redis.StrictRedis(**connect_dict)

    def set(self, k, v):
        self.r.set(k, v)

    def get(self, k):
        return self.r.get(k).decode('utf-8')

    def hmget(self, k, *filed):
        return [i.decode('utf-8') if i is not None else i for i in self.r.hmget(k, *filed)]

    def hmset(self, k, f_dict):
        for field, v in f_dict.items():
            self.r.hset(k, field, v)


class zkCodis:
    def __init__(self, zk_codis_config: dict):
        """
        params zk_codis_config: {
            "name": "codis-name",
            "passwd": "codis-passwad",
            "zkServer": "host:port;host:port",
            "timeout": 5*60
            }
        """
        self.zk_codis_config = zk_codis_config
        self.zk = KazooClient(zk_codis_config['zkServer'], randomize_hosts=True, timeout=zk_codis_config['timeout'])
        self.zk.start()
        self.proxy_url = self.__get_codis_proxy_url()
        self.codis_connect_config = None

    def __get_codis_proxy_url(self):
        codis_children = [i for i in self.zk.get_children('/') if 'codis' in i][0]
        uri = codis_children + '/' + self.zk_codis_config['name'] + '/proxy'
        proxy_list = self.zk.get_children(uri)
        proxy_url = uri + '/' + random.choice(proxy_list)
        return proxy_url

    def _get_codis_config(self):
        return json.loads(self.zk.get(self.proxy_url)[0].decode('utf-8'))

    def connect_codis(self):
        # 通过zk获取proxy
        self.proxy_url = self.__get_codis_proxy_url()
        # 通过get方法获取代理 host:port
        codis_info = self._get_codis_config()
        host_c, port_c = codis_info['proxy_addr'].split(':')
        username_c = self.zk_codis_config['name']
        password_c = self.zk_codis_config['passwd']
        codis_connect_config = dict(
            host=host_c, port=int(port_c), username=username_c, password=password_c
        )
        self.codis_connect_config = codis_connect_config
        # 连接并返回redis实例
        rds = redisDB(codis_connect_config)
        addr_ = codis_info['proxy_addr']
        name_ = self.zk_codis_config['name']
        print(f"Connect To {addr_} Codis-{name_}")
        return rds

# 示例
zk_codis = zkCodis(zk_codis_config=codis_config)
rds = zk_codis.connect_codis()
