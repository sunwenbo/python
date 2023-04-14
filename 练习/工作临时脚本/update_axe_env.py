import requests
import json
import re

update_k8sconfig_config_url = "http://center.devops.spatio-inc.com/api/v1/k8s/node/deployment/"
#update_k8sconfig_config_url = "http://axe.yidian-inc.com/api/v1/k8s/node/deployment/"

def axe_auth():
    url = "http://axe.yidian-inc.com/api/v1/token-auth/"
    auth_info = {"username": "", "password": "password"}
    auth_info['username'] = "jenkins_opssre"
    auth_info['password'] = "lKBk*e,yYTMG%cnq"
    headers = {
        'Authorization': '',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = json.dumps(auth_info)
    response = requests.request("POST", url, headers=headers, data=payload)
    reqdate = response.json()
    return reqdate

def request_axe(url=None):
    axe_token = axe_auth()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': ''
    }
    headers['Authorization'] = "JWT " + axe_token['token']
    reqdate = requests.get(url, headers=headers).json()
    return reqdate

def updateConfig(url,payload):
    axe_token = axe_auth()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': ''
    }
    headers['Authorization'] = "JWT " + axe_token['token']
    response = requests.request("POST", url=url, headers=headers, data=json.dumps(payload))
    return response

def payload(name=None,content=None,cluster=None,axe_env=None,image_name=None,node_id=None):

    payload_name = {
        "name": name,
        "content": content,
        "cluster": cluster,
        "env": axe_env,
        "image": image_name,
        "node_id": node_id
    }
    return payload_name

if __name__ == '__main__':
    res = request_axe(url=update_k8sconfig_config_url)
    for i in res:
        env = re.findall("test|dev|prod|perf|pt",str(i["name"]))
        if env:
            content = json.loads(i["content"])
            content["service"]["env"] = env[-1]
            payload_res = payload(name=str(i["name"]), content=json.dumps(content),cluster=i["cluster"],axe_env=env[-1],image_name=i["image"],node_id=i["node_id"],)

            try:
                res = updateConfig(url=update_k8sconfig_config_url, payload=payload_res)
            except Exception as e:
                print(e)

            res2 = request_axe(url=update_k8sconfig_config_url)
            for j in res2:
                if j["name"] == i["name"]:
                    res3 = json.loads(j["content"])
                    updata_env = res3["service"]["env"]
                    print(i["name"],"=====",updata_env)
        else:
            content = json.loads(i["content"])
            content["service"]["env"] = "prod"
            payload_res = payload(name=str(i["name"]), content=json.dumps(content), cluster=i["cluster"],
                                  axe_env="prod", image_name=i["image"], node_id=i["node_id"], )
            try:
                res = updateConfig(url=update_k8sconfig_config_url, payload=payload)
            except Exception as e:
                print(e)




