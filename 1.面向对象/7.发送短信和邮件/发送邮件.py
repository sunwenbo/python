#__author:  Administrator
#date:  2020/2/8
#发邮件的插件
import smtplib
from email.mime.text import MIMEText

#SMTP服务器地址
SMTPserver = "smtp.163.com"
#发邮件的地址
Sender="swb956721830@163.com"
#发送者邮件的密码,授权密码
Passwd = "LRNWTQVGNKHDQEIV"
#设置发送的内容
Message = "sunwenbo is a good man"
msg = MIMEText(Message)
#主题
msg["Subject"] = "来自帅哥的问候"
#发送者
msg["From"] = Sender
print(msg)
#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPserver,25)
#登录邮箱
mailServer.login(Sender,Passwd)
#发送邮件
mailServer.sendmail(Sender,["swb956721830@163.com","956721830@qq.com"],msg.as_string())
#退出邮箱
mailServer.quit()