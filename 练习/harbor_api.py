from flask import Flask,jsonify,request
import commands
import requests,json
import logging
app = Flask(__name__)
logtxt="/var/log/harbor_api.log"
def console_out(logFilename,log):
    # Define a Handler and set a format which output to file
    logging.basicConfig(
        level=logging.DEBUG,  ## 定义输出到文件的log级别，大于此级别的都被输出
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        filename=logFilename,  # log文件名
        filemode='a')  # 写入模式“w”或“
    console = logging.StreamHacommandsndler()  # 定义console handler
    console.setLevel(logging.INFO)  # 定义该handler级别
    formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)  # 实例化添加handler
    logging.debug(log)

def get_project_id(name): #获取project_id
   # print name
    #status,result = commands.getstatusoutput('curl -sq -k -u "admin:Ops12345" -X GET -H "Content-Type: application/json" "https://harbor.int.yidian-inc.com/api/search?q=%s"' % name)
    #get_data = json.loads(result)

    project_id = 0
    status,result = commands.getstatusoutput('curl -sq -k -u "admin:Ops12345" -X GET -H "Content-Type: application/json" "https://harbor.int.yidian-inc.com/api/projects"')
    get_data = json.loads(result)
    for i in range(len(get_data)):
      if get_data[i]['name'] == name:
         project_id = get_data[i]['project_id']
    return project_id
@app.route('/api_ops/get_project_id',methods=['GET','POST'])
def get_projectid():  #获取项目id
    result=[]
    project_name = request.args.get("project_name")
    if project_name is None or project_name.strip()=='':
       url="https://harbor.int.yidian-inc.com/api/projects"
       r = requests.get(url,auth=('admin','Ops12345'),verify=False)
       get_data = r.json()
       for i in range(len(get_data)):
           result2 = {'name':get_data[i]['name'],'project_id':get_data[i]['project_id']}
           result.append(result2)
    else:
           project_id=get_project_id(project_name)
           result2={'name':project_name,'project_id':project_id}
           result.append(result2)
    return json.dumps(result)
@app.route('/api_ops/get_item',methods=['GET','POST'])
def get_item():  #获取项目
    project_name = request.args.get("project_name")
    project_name = request.args.get("project_name")
    if project_name is None:
         harbor_url =  "curl -sq -k -u \"admin:Ops12345\" -X GET -H \"Content-Type: application/json\" \"https://harbor.int.yidian-inc.com/api/projects?project_name=guest\""
    else:
         project_id=get_project_id(project_name)
         harbor_url = "curl -sq -k -u \"admin:Ops12345\" -X GET -H \"Content-Type: application/json\" \"https://harbor.int.yidian-inc.com/api/projects/%s\"" % project_id
    status,result = commands.getstatusoutput(harbor_url)
    #result = json.dumps(result)
    console_out(logtxt,result)
    return result


@app.route('/api_ops/add_item',methods=['GET','POST']) #增加项目
def add_item():
    project_name = request.args.get("project_name")
    public = request.args.get("public")
    harbor_url = "curl -sq -k -u \"admin:Ops12345\" -X POST -H \"Content-Type: application/json\" \"https://harbor.int.yidian-inc.com/api/projects\" -d '{\"project_name\": \"%s\",\"public\": %s}'" % (project_name,public)
    #add_user_url = "curl -sq -k -u \"admin:Ops12345\" -X POST -H \"Content-Type: application/json\" \"https://harbor.int.yidian-inc.com/api/projects/%s/members/\" -d '{\"role_id\": 1,\"member_user\": {\"username\": \"wanglei\"}}'" % project_id
    status,result = commands.getstatusoutput(harbor_url)
    console_out(logtxt,result)
    return result
@app.route('/api_ops/add_user',methods=['GET','POST']) #项目添加用户
def add_user():
    project_name = request.args.get("project_name")
    username = request.args.get("username")
    role_id = request.args.get("role_id")
    project_id=get_project_id(project_name)
    print project_id
    harbor_url = "curl -sq -k -u \"admin:Ops12345\" -X POST -H \"Content-Type: application/json\" \"https://harbor.int.yidian-inc.com/api/projects/%s/members/\" -d '{\"role_id\": %s,\"member_user\": {\"username\": \"%s\"}}'" % (project_id,role_id,username)
    status,result = commands.getstatusoutput(harbor_url)
    console_out(logtxt,result)
    return result

@app.route('/api_ops/del_item',methods=['GET','POST']) #按照项目名删除项目
def del_item():
    project_name = request.args.get("project_name")
    project_id=get_project_id(project_name)
    harbor_url = "curl -sq -k -u \"admin:Ops12345\" -X DELETE -H \"Content-Type: application/json\" \"https://harbor.int.yidian-inc.com/api/projects/%s\"" % project_id
    status,result = commands.getstatusoutput(harbor_url)
    return result

@app.route('/api_ops/get_images',methods=['GET','POST'])#查询项目下有哪些镜像和查询具体镜像
def get_images():
    project_name = request.args.get("project_name")
    images_name = request.args.get("images_name")
    project_id=get_project_id(project_name)
    if images_name is None:
       harbor_url = "curl -sq -k -u \"admin:Ops12345\" -X GET -H \"Content-Type: application/json\" \"https://harbor.int.yidian-inc.com/api/repositories?project_id=%s\"" % project_id
    else:
       harbor_url = "curl -sq -k -u \"admin:Ops12345\" -X GET -H \"Content-Type: application/json\" \"https://harbor.int.yidian-inc.com/api/repositories?project_id=%s&q=%s\"" % (project_id,images_name)
    status,result = commands.getstatusoutput(harbor_url)
    return result

if __name__ == '__main__':
    #app.run(host='10.126.156.27',port=12121,debug=True)
    app.run(host='0.0.0.0',port=12121,debug=True)
