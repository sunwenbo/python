import json,requests,time,subprocess
import logging,datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from logging import handlers
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)


def get_project_id(name): #获取project_id
    project_id = 0
    status,result = subprocess.getstatusoutput('curl -sq -k -u "admin:Ops12345" -X GET -H "Content-Type: application/json" "https://harbor.int.yidian-inc.com/api/projects"')
    get_data = json.loads(result)
    for i in range(len(get_data)):
      if get_data[i]['name'] == name:
         project_id = get_data[i]['project_id']
    return project_id

def get_project(url): #获取有哪些项目
    harbor_result = requests.get(url)
    result =  harbor_result.json()
    project = []
    for i in range(len(result)):
        project.append(result[i]['name'])
    return project

def add_replication(*diff_project): #增加复制规则
    for name in diff_project:
        #console_out(logtxt,name)
        replication_name = name
        project_name = name
        project_id = get_project_id(name)

        url = "https://harbor.int.yidian-inc.com/api/policies/replication"

        payload = {
            "name": "content-process-cpp-component-server",
            "description": "",
            "trigger": {
                "kind": "Immediate"
            },
            "replicate_existing_image_now": True,
            "replicate_deletion": True,
            "filters": [],
            "projects": [
                {
                    "project_id": 27,
                    "owner_id": 1,
                    "name": "content-process-cpp-component-server",
                    "creation_time": "2022-12-02T03:16:38Z",
                    "update_time": "2022-12-02T03:16:38Z",
                    "deleted": False,
                    "owner_name": "",
                    "togglable": False,
                    "current_user_role_id": 0,
                    "repo_count": 0,
                    "chart_count": 0,
                    "metadata": {
                        "auto_scan": "false",
                        "enable_content_trust": "false",
                        "prevent_vul": "false",
                        "public": "true",
                        "severity": "low"
                    }
                }
            ],
            "targets": [
                {
                    "id": 2,
                    "endpoint": "https://harbor2.int.yidian-inc.com",
                    "name": "harbor2.int.yidian-inc.com",
                    "username": "admin",
                    "password": "",
                    "type": 0,
                    "insecure": True,
                    "creation_time": "2022-12-01T02:26:31.923545Z",
                    "update_time": "2022-12-02T16:43:21.755517Z"
                }
            ]
        }
        now_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        payload["name"] = project_name
        payload["projects"][0]["project_id"] = project_id
        payload["projects"][0]["name"]  = replication_name
        payload["projects"][0]["name"] = replication_name
        payload["projects"][0]["creation_time"] = now_time
        payload["projects"][0]["update_time"] = now_time

        payload = json.dumps(payload)
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Content-Type-Options': 'nosniff',
            'Authorization': 'Basic YWRtaW46T3BzMTIzNDU=',
            'Cookie': 'sid=b111caf0872f37009a9e0d36439581ef'
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        if response.status_code == 201:
            log.logger.info("%s project add replication successful. status_code: %d"  % (project_name,response.status_code))
            time.sleep(5)
        elif  response.status_code == 409:
            log.logger.warning("%s The mirror repository is empty. status_code: %d"  % (project_name,response.status_code))
        else:
            log.logger.error("%s project add replication failure. status_code: %d"  % (project_name,response.status_code))


harbor1_url = "http://10.126.156.27:12121/api_ops/get_item"
harbor2_url = "http://10.126.156.2:12121/api_ops/get_item"
harbor1_project = get_project(harbor1_url)
harbor2_project = get_project(harbor2_url)
log = Logger('./harbor_replication.log', level='debug')
# harbor1_project中有而harbor2_project中没有的，
diff_project = tuple(set(harbor2_project).difference(set(harbor1_project)))
print(diff_project)
#add_replication(*diff_project)