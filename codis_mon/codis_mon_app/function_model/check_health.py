from kazoo.client import KazooClient
import  json
import requests

zk_list1 = ["10.136.41.29","10.103.33.40","10.103.32.222","10.136.134.35","10.136.13.10","10.126.150.3","10.120.38.7","10.120.14.43","10.136.136.16","10.136.13.28"]
#["10.126.154.173"] #["l-sre-codis-zk1.ops.prod.bj2.yidian-inc.com"]
zk_list = ["10.126.154.173"]
timeout = 100


def check_codis_health():
    stack=[]
    for i in zk_list:
        stack.append(i)
    while len(stack) != 0 :
        zk_ip = stack.pop()
        zkc = KazooClient(hosts=zk_ip, timeout=timeout)
        zkc.start()
        codis_name = zkc.get_children("/codis3")
        for i in codis_name:
            codis_info = zkc.get_children("/codis3/" + i)
            if not codis_info:
                print(i + "为空")
                #zkc.delete("/codis3/" + i )
            if "slots"  in codis_info:
                codis_info.remove('slots')
            codis_info.sort()
            if i != "codis-KNN":
                group_list = zkc.get_children("/codis3/" + i + "/" + codis_info[0])
                for a in group_list:
                    group_response = zkc.get("/codis3/" + i + "/" + codis_info[0] + "/" + a)[0]
                    group_data= json.loads(group_response.decode("utf-8"))
                    if not group_data["out_of_sync"] == False:
                        print("一点资讯codis告警【严重】zk地址:%s  %s codis集群第%d组 sync 异常" % (zk_ip,i,group_data["id"]))

            if i != "codis-KNN":
                proxy_list = zkc.get_children("/codis3/" + i + "/" + codis_info[1])
                for b in proxy_list:
                    proxy_response = zkc.get("/codis3/" + i + "/" + codis_info[1] + "/" + b)[0]
                    proxy_data = json.loads(proxy_response.decode("utf-8"))
                    admin_addr = proxy_data["admin_addr"]
                    try:
                        if admin_addr != "127.0.0.1":
                            response = requests.get("http://" + admin_addr,timeout=0.1)
                            response = json.loads(response.text)
                            proxy_status = response["stats"]["online"]
                            if not proxy_status == True:
                                print("一点资讯codis告警【严重】zk地址:%s  %s codis集群第%d proxy异常,请检查" % (zk_ip,i,proxy_data["id"]))
                    except:
                        pass

            if i != "codis-KNN":
                sentinel_response = zkc.get("/codis3/" + i + "/" + codis_info[2])[0]
                sentinel_data = json.loads(sentinel_response.decode("utf-8"))
                if "servers" not in sentinel_data:
                    print("一点资讯codis告警【严重】zk地址:%s  %s codis集群没有哨兵" % (zk_ip,i))
                else:
                    sentinel_node = sentinel_data["servers"]
                    if sentinel_data["out_of_sync"] != False:
                        print("一点资讯codis告警【严重】zk地址:%s  %s codis集群哨兵 %s 异常,请检查" % (zk_ip,i,sentinel_node))


check_codis_health()
