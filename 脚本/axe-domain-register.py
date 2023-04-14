import requests
import json


def create_domain(domain, headers,department):
    d = {'access_type': 'Api',
         'comment': '',
         'company': 'yidian',
         'department': 'yidian/qa',
         'domain_name': '',
         'load_balancing': 'nginx',
         'migrate_status': u'使用中',
         'monitor_name': 'None',
         'product_line': 'yidian',
         'service_monitor': '[{"key":"","value":""}]',
         'service_type': 'internal'
         }
    d["domain_name"] = domain
    d["department"] = department
    response = requests.request("POST", url, headers=headers, data=json.dumps(d))
    r = response.json()
    return r["id"]


def create_owner(d):
    url = "http://axe.yidian-inc.com/api/v1/domain_management/domain_name/%s/owners/" % d
    data = {"owner": [2007]}

    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))

    print("create_owner:", d, response.status_code)


def get_nodeid(path):
    url = "http://axe.yidian-inc.com/api/v1/service/nodes/?limit=1&offset=0&node_type=1&path=%s" % path
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    r = response.json()
    return r["results"][0]["id"]


def ReadJson(path):
    with open(path, 'r') as f:
        domain = json.load(f, encoding='utf-8')
    return domain


def create_up(did, nodeid, headers, cluster_name):
    url = "http://axe.yidian-inc.com/api/v1/domain_management/upstreams/"
    d = {"domain_name": "", "upstream": "default", "cluster": "dev_cluster", "comment": "", "service_node": "",
         "tag_key": "", "tag_value": ""}
    d["domain_name"] = did
    d["service_node"] = nodeid
    d["cluster"] = cluster_name

    response = requests.request("POST", url, headers=headers, data=json.dumps(d))

    print("create_up", d, nodeid, response.status_code)


if __name__ == '__main__':
    path = "/脚本/domain.json"
    domain_list = ReadJson(path)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN1bndlbmJvIiwidXNlcl9pZCI6MTg5OSwiZW1haWwiOiJzdW53ZW5ib0B5aWRpYW4taW5jLmNvbSIsImV4cCI6MTY0NzM1MDUzOH0.WOzn5LgKtqhC-LkSNVYViBxG1U8qqLftA3j00USZx7I'
    }

    url = "http://axe.yidian-inc.com/api/v1/domain_management/domain_names/"
    reqdate = requests.get(url, headers=headers)
    reqdate = reqdate.json()["results"]

    for k, v in enumerate(domain_list):
        domain = v['domain']
        axe_path = v['axe_path']
        cluster_name = v['cluster_name']
        department = v['department']
        isd = True
        for i in reqdate:
            if i["domain_name"] != None and domain == i["domain_name"]:
                isd = False
        if isd:
            d = create_domain(domain, headers,department)
            create_owner(d)
            nodeid = get_nodeid(axe_path)
            create_up(d, nodeid, headers, cluster_name)
        else:
            print("%s已存在" %(domain))
            exit(-1)