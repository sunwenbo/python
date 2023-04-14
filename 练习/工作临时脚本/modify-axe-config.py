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
        if "ops" not in i["name"]:
            if i["name"]:
                content = json.loads(i["content"])
                content["service"]["logPath"] = "/home/services/logs"
                content["service"]["port"] = 9000
                old_start_command = content["service"]["start_command"]
                old_start_command_list = eval(old_start_command)
                if old_start_command_list[0] == 'sh' or old_start_command_list[1] != "-c":
                    old_start_command_list[0] = "bash"
                    old_start_command_list.insert(1,"-c")

                list2 = old_start_command_list.pop(-1).split(" ")
                if i["name"] == "spatio-kratos-rtm-manager-dev":
                    continue
                else:
                    if len(list2) <= 1:
                        continue
                    else:
                        list2[1] = "/home/services/start.sh"
                        old_start_command_list.append(" ".join(list2))
                    new_start_command = str(old_start_command_list).replace("\'","\"")
                    content["service"]["start_command"] = new_start_command

                    if not content["readinessProbe"]["type"] == "command":
                        content["readinessProbe"]["tcpSocket"]["port"] = 9000
                        content["readinessProbe"]["value"]= 9000
                    if not content["livenessProbe"]["type"] == "command":
                        content["livenessProbe"]["tcpSocket"]["port"] = 9000
                        content["livenessProbe"]["value"]= 9000
                    if not content["startupProbe"]["type"] == "command":
                        content["startupProbe"]["tcpSocket"]["port"] = 9000
                        content["startupProbe"]["value"]= 9000

                    env = content["service"]["env"]
                    payload_res = payload(name=str(i["name"]), content=json.dumps(content),cluster=i["cluster"],axe_env=env,image_name=i["image"],node_id=i["node_id"],)

                    try:
                        res = updateConfig(url=update_k8sconfig_config_url, payload=payload_res)
                        print(i["name"],"修改完成")
                    except Exception as e:
                        print(e)

