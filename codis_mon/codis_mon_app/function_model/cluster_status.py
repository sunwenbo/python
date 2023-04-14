from kazoo.client import KazooClient
from codis_mon_app.models import Clusters
from django.core import serializers
import  json

class NodeExists(object):
    def checkPath(self,cname,zkaddr):
        try:
            timeout = 100
            zkc = KazooClient(hosts=zkaddr, timeout=timeout)
            zkc.start()
            codis_cname = "/codis3/" + cname
            if  zkc.exists(codis_cname):
                clusterinfo = Clusters.objects.filter(cname=cname, zkaddr=zkaddr)
                if  not clusterinfo:
                    prox_list,group_list, = zkc.get_children(codis_cname+"/proxy"), zkc.get_children(codis_cname+"/group")
                    group_num= len(group_list)
                    sentinel_data = json.loads(str(zkc.get(codis_cname + "/sentinel")[0],'utf-8'))
                    if "servers"  in sentinel_data:
                        sentinel_list = sentinel_data["servers"]
                    else:
                        sentinel_list = None
                    sent_sync = sentinel_data["out_of_sync"]
                    proxy_value = zkc.get(codis_cname + "/proxy/" + prox_list[0])
                    prox_json = json.loads(str(proxy_value[0],'utf-8'))
                    dashboardurl = prox_json["admin_addr"]
                    start_time = str(prox_json["start_time"]).split(".")[0]
                    clusters = Clusters.objects.create(cname=cname, start_time=start_time,zkaddr=zkaddr,dashboardurl=dashboardurl,proxy_list=prox_list, group_num=group_num, sentinel_list=sentinel_list,sent_sync=sent_sync)
                    clusterinfo = Clusters.objects.filter(cname=cname, zkaddr=zkaddr)
                    cluster_data = json.loads(serializers.serialize("json", clusterinfo))
                    clusters.save()
                    return cluster_data
                else:
                    cluster_data = json.loads(serializers.serialize("json", clusterinfo))
                    return cluster_data
            else:
                cluster_data = "The %s cluster does not exist" % cname
                return cluster_data
        except Exception as err:
            print(err)

