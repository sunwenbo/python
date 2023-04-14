#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import sys
import json
import argparse
import re
import time
import urllib
import urllib2
import MySQLdb


TOKEN = "db7a5ef934405db9632410bbea115020b319dc1e"
BASEURL = "http://axe.yidian-inc.com/api/v1"
TPL = "grafana.json"
UID = "app-sync-axe"
#MYSQL = "10.136.44.10"
#MYSQLUSER = "root"
#MYSQLPASS = "sync-axe"
#MYSQLDATABASE = "grafana"

MYSQL = "10.103.32.115"
MYSQLUSER = "pig"
MYSQLPASS = "graf@123"
MYSQLDATABASE = "grafana"

# redisre = re.compile("pub/(re|co)dis")
serhosts = {}

def genMap(title, i, host):
    mymap = {}
    if title == "redis处理命令数":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.instantaneous_ops_per_sec.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis读取操作数":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.cmd_*get*.1sec, 2, 3, 4, 5, 8, 9)"    }
    if title == "redis插入操作数":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.cmd_*set*.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis删除操作数":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.cmd_*del*.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "当前客户端连接数量":
        mymap[title] =  {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.connected_clients.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis命中率":
        mymap[title] =  {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.keyspace_hits_percent.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis输出缓冲区队列对象个数最大值":
        mymap[title] =  {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.client_longest_output_list.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis输入缓冲区占用最大值":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.client_biggest_input_buf.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis最大内存":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.memory_max_bytes.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis-rss使用内存":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.memory_used_rss_bytes.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis使用内存":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.memory_used_bytes.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis-rss内存碎片率":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.memory_fragmentation_ratio.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis-rdb进行数量":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.rdb_bgsave_in_progress_num.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis-rdb当前花费时间":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.rdb_current_bgsave_duration_sec.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis上一次rdb消耗时间":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.rdb_last_bgsave_duration_sec.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "当前阻塞客户端连接数量":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.blocked_clients.1sec, 2, 3, 4, 5, 8, 7, 9)"}
    if title == "redis-aof是否开启":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.aof_enabled.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis-aof当前是否在进行":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.aof_rewrite_in_progress.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis-aof当前花费时间":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.aof_current_rewrite_duration_sec.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis最近一次fork操作耗费时间":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.latest_fork_usec.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis拒绝连接数量":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(perSecond(Ydbot.host."+host+".app.redis.$port.rejected_connections_total.1sec), 2, 3, 4, 5, 8, 9)"}
    if title == "redis过期key数量":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(perSecond(Ydbot.host."+host+".app.redis.$port.expired_keys_total.1sec), 2, 3, 4, 5, 8, 9)"}
    if title == "redis与master节点连接情况":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.master_link_status.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis key数量":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.keyspace_keys.1sec, 2, 3, 4, 5, 8, 9)"}
    if title == "redis主进程用户态占用cpu":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(perSecond(Ydbot.host."+host+".app.redis.$port.used_cpu_user.1sec), 2, 3, 4, 5, 8, 9)"}
    if title == "redis子进程内核态占用cpu":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(perSecond(Ydbot.host."+host+".app.redis.$port.used_cpu_sys_children.1sec), 2, 3, 4, 5, 8, 9)"}
    if title == "redis子进程用户态占用cpu":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(perSecond(Ydbot.host."+host+".app.redis.$port.used_cpu_user_children.1sec), 2, 3, 4, 5, 8, 9)"}
    if title == "redis主进程内核态占用cpu":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(perSecond(Ydbot.host."+host+".app.redis.$port.used_cpu_sys.1sec), 2, 3, 4, 5, 8, 9)"}
    if title == "slowlog数目":
        mymap[title] = {"refCount": 0,"refId": "A"+str(i),"target": "aliasByNode(Ydbot.host."+host+".app.redis.$port.slowlog_count.1sec, 2, 3, 4, 5, 8, 9)"}
    return mymap[title]

def getServices(redisre):
    services = []
    data = {'token': TOKEN, 'node_type': 1}
    url = BASEURL + "/service/nodes/?" + urllib.urlencode(data)
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    res_data = json.loads(res.read())
    for i, v in enumerate(res_data["results"]):
        if redisre.search(v["path"]):
            services.append(v["path"]+":"+str(v["id"]))
    return services

def getServiceHost(service):
    path = service.split(":")[0].encode('utf-8')
    hosts = []
    data = {'path': path, 'token': TOKEN}
    url = BASEURL + "/service/resource/?" + urllib.urlencode(data)
    req = urllib2.Request(url)
    req.add_header("Accept", "application/json")
    try:
        res = urllib2.urlopen(req)
        res_data = json.loads(res.read())
        for i, v in enumerate(res_data["results"]):
            if v["host_name"].startswith("l-"):
                hosts.append(v["host_name"])
            else:
                for j, vv in enumerate(v["nics"]):
                    hosts.append(vv["ipv4"])
            serhosts[service] = hosts
    except:
        return

def genJson(key, value=[]):
    with open("redis-grafana.json", "r") as load_f:
        mydict = json.load(load_f, encoding='utf-8')
        assert isinstance(mydict, dict)
        for index in range(len(mydict["panels"])):
            for i, host in enumerate(value):
                mydict["panels"][index]["targets"].append(genMap(mydict["panels"][index]["title"], i, host))
        mydict["title"] = formatTitle(key)
        mydict["templating"]["list"][0]["query"] = "Ydbot.host."+value[len(value)-1]+".app.redis.*"
    return json.dumps(mydict, ensure_ascii=False, encoding="utf-8")

def formatTitle(key):
    path = key.split(":")[0]
    # path = path.replace("/","\\\\")
    #ks = path.split("/")
    #return "app" + "-" + ks[len(ks)-3] + "-" + ks[len(ks)-2] + "-" + ks[len(ks)-1]
    return "应用监控-" + path

def formatDash(key):
    path = key.split(":")[0]
    return "ying-yong-jian-kong-" + path + ":" + key.split(":")[1]

def inserTodb(dash={}):
    created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    db = MySQLdb.connect(MYSQL, MYSQLUSER, MYSQLPASS, MYSQLDATABASE, charset="utf8")
    cursor = db.cursor()
    # cursor.execute("delete from dashboard where uid like 'app-sync-axe%'")
    for k,v in dash.items():
        name = k.split(":")[0].replace("/","-")
        title = k.split(":")[0].replace("ying-yong-jian-kong-", "应用监控-")
        axeid = k.split(":")[1]
        dsql = "delete from dashboard where uid like 'app-sync-axe%%' and title='%s'" %(title)
        #cursor.execute("delete from dashboard where uid like 'app-sync-axe%' and title=name")
        cursor.execute(dsql)
        sql = "insert into dashboard (version, slug, title, data, org_id, created, updated, folder_id, is_folder, has_acl, uid) \
        values ('%d', '%s', '%s', '%s','%d', '%s', '%s', '%d', '%d', '%d', '%s')" %(100, name, title, v, 1, created, updated, 0, 0, 0, UID+axeid)
        print sql
        try:
            cursor.execute(sql)
        except Exception, e:
            print "insert %s failed!" %str(e)
    db.commit()
    cursor.close()
    db.close()

def parseArgs():
    parser = argparse.ArgumentParser("add grafana dashboard accrording to axe service tree")
    parser.add_argument("-p",  "--path", help="axe service tree path, like ./redis-grafana.py -p 'pub/redis/redis-3rd-click/prod'")
    args = parser.parse_args()
    if not args.path or not args.path.find("redis") or not args.path.find("codis"):
        print "must specify a axe path with redis or codis,\n please use -h for help,use -p specify axe path\n \
        like ./redis-grafana.py -p 'pub/redis/redis-3rd-click/prod'"
        sys.exit(1)
    else:
        return args.path


if __name__ == '__main__':
    path = parseArgs()
    mgore = re.compile(path)
    dash = {}
    ser = getServices(mgore)
    for i, v in enumerate(ser):
        getServiceHost(v)

    for k, v in serhosts.items():
        #k = yidian/superfe/open/dependent/rediscluster-for-cache/prod:2689458
        #v = [u'10.138.12.56', u'10.138.12.59',u'10.138.12.60', u'10.138.12.58',u'10.138.12.57', u'10.138.12.107',u'10.138.12.104', u'10.138.12.110',u'10.138.12.109', u'10.138.12.105',u'10.138.12.106', u'10.138.12.108']
        dash[formatDash(k)] = genJson(k, v)
    inserTodb(dash)