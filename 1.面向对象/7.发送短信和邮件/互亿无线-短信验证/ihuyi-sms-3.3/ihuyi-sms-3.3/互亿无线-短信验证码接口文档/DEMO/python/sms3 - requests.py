#�ӿ����ͣ��������ߴ������Žӿڣ�֧�ַ�����֤����š�����֪ͨ���ŵȡ�
#�˻�ע�᣺��ͨ���õ�ַ��ͨ�˻�http://sms.ihuyi.com/register.html
#ע�����
#��1�������ڼ䣬����Ĭ�ϵ�ģ����в��ԣ�Ĭ��ģ������ӿ��ĵ���
#��2����ʹ��APIID���鿴APIID���¼�û�����->��֤�����->��Ʒ����->APIID���� APIkey�����ýӿڣ�
#��3���ô���������뻥�����߶��Žӿڲο�ʹ�ã��ͻ��ɸ���ʵ����Ҫ���б�д��

#coding:utf-8
import requests

url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"

#APIID
account = "�û���"
#APIkey
password = "����"

mobile = "133xxxxxxxx"
content = "������֤���ǣ�201981���벻Ҫ����֤��й¶�������ˡ�"
#���������ͷ��
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
#�������������
data = {
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}
#��������
response = requests.post(url,headers = headers,data=data)
    #url ����ĵ�ַ
    #headers ����ͷ��
    #data ���������

print(response.content.decode())