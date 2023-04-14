import jenkins
import re,requests
import xmltodict,json
import dicttoxml
import xml.dom.minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element
from bs4 import BeautifulSoup


truely_guonei_url = "http://10.138.10.240:8080/"
truely_guowai_url = "http://jenkins.spatio-inc.com/"
git_guonei_url = "git.yidian-inc.com:8021/ops"

# create jenkins server,return the result
def create_jenkins_server(url, username, password):
    server = jenkins.Jenkins(url, username, password)
    return server


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



if __name__ == '__main__':
    url = truely_guowai_url
    username = 'jenkins_opssre'
    password = 'lKBk*e,yYTMG%cnq'

    update_k8sconfig_config_url = "http://center.devops.spatio-inc.com/api/v1/k8s/node/deployment/"
    #update_k8sconfig_config_url = "http://axe.yidian-inc.com/api/v1/k8s/node/deployment/"
    server = create_jenkins_server(url, username, password)
    info = server.get_info()
    jobs = info['jobs']
    for job in jobs:
        jobName = job['name']
        if "assemble" in jobName or 'commit' in jobName:
            continue
        if jobName == "ops-sre-ngconf2":
            # job_config = server.get_job_config(jobName)
            job_config = server.get_job_config(jobName)
            print(job_config)
            # soup = BeautifulSoup(job_config, 'xml')
            # res = request_axe(url=update_k8sconfig_config_url)
            # env = ""
            # for i in res:
            #     if i['name'] == jobName:
            #         print("$$$$")
            #         content = json.loads(i["content"])
            #         env = "<script>env_list=[\""+content["service"]["env"]+"\"]</script>"
            # permission_list = list(soup.find_all('permission'))
            # permission = ""
            # for i in permission_list:
            #     permission += "      " + str(i) + '\n'
            # permission = permission.rstrip()
            # job_name = str(soup.projectName)
            # job_name = job_name.split('<projectName>')[-1].split('<')[0]
            # git_url = str(soup.command)
            # user_emails = str(soup.recipients)
            # email_list= str(soup.find_all("defaultValue")[1])

#             job_config_template = '''<?xml version='1.1' encoding='UTF-8'?>
# <project>
# <actions/>
# <description>新版k8s集群，单个服务目前只支持2个版本共存;新生成的k8s job请务必点击Configure按钮并执行保存（否则容器实例会看不到）</description>
# <keepDependencies>false</keepDependencies>
# <properties>
# <hudson.security.AuthorizationMatrixProperty>
#   <inheritanceStrategy class="org.jenkinsci.plugins.matrixauth.inheritance.InheritParentStrategy"/>
# {users_permissions}
# </hudson.security.AuthorizationMatrixProperty>
# <com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty plugin="gitlab-plugin@1.5.8">
#   <gitLabConnection></gitLabConnection>
# </com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty>
# <com.sonyericsson.rebuild.RebuildSettings plugin="rebuild@1.31">
#   <autoRebuild>false</autoRebuild>
#   <rebuildDisabled>false</rebuildDisabled>
# </com.sonyericsson.rebuild.RebuildSettings>
# <hudson.plugins.throttleconcurrents.ThrottleJobProperty plugin="throttle-concurrents@2.0.1">
#   <maxConcurrentPerNode>0</maxConcurrentPerNode>
#   <maxConcurrentTotal>0</maxConcurrentTotal>
#   <categories class="java.util.concurrent.CopyOnWriteArrayList"/>
#   <throttleEnabled>false</throttleEnabled>
#   <throttleOption>project</throttleOption>
#   <limitOneJobWithMatchingParams>false</limitOneJobWithMatchingParams>
#   <paramsToUseForLimit></paramsToUseForLimit>
# </hudson.plugins.throttleconcurrents.ThrottleJobProperty>
# <jenkins.model.BuildDiscarderProperty>
#   <strategy class="hudson.tasks.LogRotator">
#     <daysToKeep>-1</daysToKeep>
#     <numToKeep>100</numToKeep>
#     <artifactDaysToKeep>-1</artifactDaysToKeep>
#     <artifactNumToKeep>-1</artifactNumToKeep>
#   </strategy>
# </jenkins.model.BuildDiscarderProperty>
# <hudson.model.ParametersDefinitionProperty>
#   <parameterDefinitions>
#     <hudson.model.StringParameterDefinition>
#       <name>COMMIT_ID</name>
#       <description>如果是灰度发布：	1、新版本替换旧版本，与全量发布同理	2、如果没有旧版本，则只输入新版本</description>
#       <defaultValue>0</defaultValue>
#       <trim>false</trim>
#     </hudson.model.StringParameterDefinition>
#     <org.biouno.unochoice.ChoiceParameter plugin="uno-choice@2.1">
#       <name>TARGET_ENV</name>
#       <description></description>
#       <randomName>choice-parameter-1464647741325096</randomName>
#       <visibleItemCount>1</visibleItemCount>
#       <script class="org.biouno.unochoice.model.GroovyScript">
#         <secureScript plugin="script-security@1.71">
#           {env}
#           <sandbox>false</sandbox>
#         </secureScript>
#         <secureFallbackScript plugin="script-security@1.71">
#           <script></script>
#           <sandbox>false</sandbox>
#         </secureFallbackScript>
#       </script>
#       <projectName>{job_name}</projectName>
#       <choiceType>PT_SINGLE_SELECT</choiceType>
#       <filterable>false</filterable>
#       <filterLength>1</filterLength>
#     </org.biouno.unochoice.ChoiceParameter>
#     <org.biouno.unochoice.CascadeChoiceParameter plugin="uno-choice@2.1">
#       <name>CLUSTER</name>
#       <description></description>
#       <randomName>choice-parameter-16650525072247720</randomName>
#       <visibleItemCount>1</visibleItemCount>
#       <script class="org.biouno.unochoice.model.GroovyScript">
#         <secureScript plugin="script-security@1.71">
#           <script>evaluate(new File(&quot;/ssd/var/lib/jenkins/get_new_k8s_cluster_auto.groovy&quot;))</script>
#           <sandbox>false</sandbox>
#         </secureScript>
#         <secureFallbackScript plugin="script-security@1.71">
#           <script></script>
#           <sandbox>false</sandbox>
#         </secureFallbackScript>
#       </script>
#       <projectName>{job_name}</projectName>
#       <parameters class="linked-hash-map"/>
#       <referencedParameters>TARGET_ENV</referencedParameters>
#       <choiceType>PT_SINGLE_SELECT</choiceType>
#       <filterable>false</filterable>
#       <filterLength>1</filterLength>
#     </org.biouno.unochoice.CascadeChoiceParameter>
#     <org.biouno.unochoice.CascadeChoiceParameter plugin="uno-choice@2.1">
#       <name>CURRENT_VERSIONS</name>
#       <description></description>
#       <randomName>choice-parameter-1464647748216344</randomName>
#       <visibleItemCount>1</visibleItemCount>
#       <script class="org.biouno.unochoice.model.GroovyScript">
#         <secureScript plugin="script-security@1.71">
#           <script>evaluate(new File(&quot;/ssd/var/lib/jenkins/get_new_k8s_instances.groovy&quot;))</script>
#           <sandbox>false</sandbox>
#         </secureScript>
#         <secureFallbackScript plugin="script-security@1.71">
#           <script></script>
#           <sandbox>false</sandbox>
#         </secureFallbackScript>
#       </script>
#       <projectName>{job_name}</projectName>
#       <parameters class="linked-hash-map"/>
#       <referencedParameters>CLUSTER,TARGET_ENV</referencedParameters>
#       <choiceType>PT_SINGLE_SELECT</choiceType>
#       <filterable>false</filterable>
#       <filterLength>1</filterLength>
#     </org.biouno.unochoice.CascadeChoiceParameter>
#     <org.biouno.unochoice.ChoiceParameter plugin="uno-choice@2.1">
#       <name>DEPLOY_TYPE</name>
#       <description>&lt;title&gt;huidu&lt;/title&gt;发布类型</description>
#       <randomName>choice-parameter-1464647751401490</randomName>
#       <visibleItemCount>1</visibleItemCount>
#       <script class="org.biouno.unochoice.model.GroovyScript">
#         <secureScript plugin="script-security@1.71">
#           <script>DEPLOY_TYPES = evaluate(new File(&quot;/ssd/var/lib/jenkins/get_DEPLOY_TYPE.groovy&quot;));DEPLOY_TYPES = DEPLOY_TYPES - &quot;扩容/减容&quot;</script>
#           <sandbox>false</sandbox>
#         </secureScript>
#         <secureFallbackScript plugin="script-security@1.71">
#           <script></script>
#           <sandbox>false</sandbox>
#         </secureFallbackScript>
#       </script>
#       <projectName>{job_name}</projectName>
#       <choiceType>PT_SINGLE_SELECT</choiceType>
#       <filterable>false</filterable>
#       <filterLength>1</filterLength>
#     </org.biouno.unochoice.ChoiceParameter>
#     <hudson.model.StringParameterDefinition>
#       <name>EMAIL_RECEIVER</name>
#       <description>上线通知邮件列表</description>
#       {email_list}
#       <trim>false</trim>
#     </hudson.model.StringParameterDefinition>
#     <hudson.model.StringParameterDefinition>
#       <name>INSTANCE_NUMBER</name>
#       <description>instance_number对全量发布不起作用，全量发布发布的是跟线上一样多的instance个数</description>
#       <defaultValue>1</defaultValue>
#       <trim>false</trim>
#     </hudson.model.StringParameterDefinition>
#   </parameterDefinitions>
# </hudson.model.ParametersDefinitionProperty>
# </properties>
# <scm class="hudson.scm.NullSCM"/>
# <canRoam>true</canRoam>
# <disabled>false</disabled>
# <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
# <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
# <triggers/>
# <concurrentBuild>false</concurrentBuild>
# <customWorkspace>${{HOME}}/workspace/${{JOB_NAME}}</customWorkspace>
# <builders>
# <hudson.tasks.Shell>
#   {git_url}
# </hudson.tasks.Shell>
# </builders>
# <publishers>
# <hudson.plugins.descriptionsetter.DescriptionSetterPublisher plugin="description-setter@1.10">
#   <regexp>\[DESC\] (.*)</regexp>
#   <regexpForFailed></regexpForFailed>
#   <setForMatrix>false</setForMatrix>
# </hudson.plugins.descriptionsetter.DescriptionSetterPublisher>
# <hudson.tasks.Mailer plugin="mailer@1.24">
#   {user_emails}
#   <dontNotifyEveryUnstableBuild>false</dontNotifyEveryUnstableBuild>
#   <sendToIndividuals>false</sendToIndividuals>
# </hudson.tasks.Mailer>
# </publishers>
# <buildWrappers>
# <hudson.plugins.ws__cleanup.PreBuildCleanup plugin="ws-cleanup@0.34">
#   <deleteDirs>false</deleteDirs>
#   <cleanupParameter></cleanupParameter>
#   <externalDelete></externalDelete>
# </hudson.plugins.ws__cleanup.PreBuildCleanup>
# <hudson.plugins.build__timeout.BuildTimeoutWrapper plugin="build-timeout@1.18">
#   <strategy class="hudson.plugins.build_timeout.impl.NoActivityTimeOutStrategy">
#     <timeoutSecondsString>1800</timeoutSecondsString>
#   </strategy>
#   <operationList>
#     <hudson.plugins.build__timeout.operations.AbortOperation/>
#   </operationList>
# </hudson.plugins.build__timeout.BuildTimeoutWrapper>
# <org.jenkinsci.plugins.builduser.BuildUser plugin="build-user-vars-plugin@1.5"/>
# </buildWrappers>
# </project>'''.format(users_permissions=permission, env=env, job_name=job_name, email_list=email_list,
#                              git_url=git_url, user_emails=user_emails)
#             try:
#                 server.reconfig_job(jobName,job_config_template)
#                 print("执行")
#             except Exception as e:
#                 print(e)



            # with open(srcfilepath, 'w') as f:
            #     f.write(job_config)
            # job_json = xml_to_JSON(srcfilepath)

            # job_xml = JSON_to_xml(job_json)
            # with open(desfilepath, 'w') as f:
            #     f.writelines(job_xml)
            # dom = xml.dom.minidom.parse(desfilepath)
            # new_xml = dom.toprettyxml()
            # print(new_xml)
            # server.reconfig_job(jobName,new_xml)

            # with open(desfilepath,'r') as f:
            #     lines = f.read().splitlines()
            # for i in lines:
            #     print(i)
















