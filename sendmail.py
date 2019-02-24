# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:41:51 2019

@author: Inke1812122
"""

### 使用第三方邮箱服务器发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'liuyiming@inke.cn'
receivers = ['luobin@inke.cn',]
mail_pass = '*******使用邮箱服务器的授权码不是登录密码'

message = MIMEText('Python mail test','plain', 'utf-8')
message['From'] = '刘一鸣'
message['To'] = '罗斌'

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    server = smtplib.SMTP()
    server.login(sender,mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('无法发送邮件')
    
    
    
## 在服务器上发送邮件没有什么差异
import smtplib

from email.mime.text import MIMEText

def sendEmail(toEmail,toUser,subject,content):

	msg=MIMEText(content,'plain','utf-8')

	msg['From']='xxx'

	msg['To']=toUser

	msg['Subject']=subject

	server='smtp.exmail.qq.com'

	server=smtplib.SMTP(server,25)

	server.set_debuglevel(1)

	server.login('xxx@xx.com','xxx')

	server.sendmail('xxx@xx.com',toEmail,msg.as_string())

	server.quit()
