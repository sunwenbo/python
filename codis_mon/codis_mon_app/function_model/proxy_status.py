from kazoo.client import KazooClient
from codis_mon_app.models import Proxys
from django.core import serializers
import  json
import requests


class CodisProxyinfo(object):
    def SelectProxy(self,cname,zkaddr):
        codis_cname = "/codis3/" + cname
        try:
            timeout = 100
            zkc = KazooClient(hosts=zkaddr, timeout=timeout)
            zkc.start()
            proxy_list = zkc.get_children(codis_cname + "/proxy")
            proxy_req=[]
            for i in proxy_list:
                proxy_response = zkc.get(codis_cname + "/proxy/" + i)[0]
                proxy_data = json.loads(proxy_response.decode("utf-8"))
                pname = "proxy-" + proxy_data["token"]
                start_time = proxy_data["start_time"].split(".")[0]
                proxy_addr = proxy_data["proxy_addr"]
                admin_addr = proxy_data["admin_addr"]
                response = requests.get("http://" + admin_addr)
                response = json.loads(response.text)
                proxy_max_clients = response["config"]["proxy_max_clients"]
                proxy_status = response["stats"]["online"]
                product_name = proxy_data["product_name"]
                proxydata_info = Proxys.objects.filter(pname=pname, proxy_addr=proxy_addr)
                if  not proxydata_info:
                    Proxys.objects.create(pname=pname,start_time=start_time,proxy_max_clients=proxy_max_clients,proxy_addr=proxy_addr,admin_addr=admin_addr,product_name=product_name,proxy_status=proxy_status)
                proxydata_info = Proxys.objects.filter(pname=pname, proxy_addr=proxy_addr)
                proxyinfo = json.loads(serializers.serialize("json", proxydata_info))
                proxy_req=proxy_req+proxyinfo
            return proxy_req
        except Exception as err:
            print(err)
