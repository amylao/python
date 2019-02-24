# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:14:28 2019

@author: Inke1812122
"""
########################################

### 需求 
### 使用 Python 连接 linux 读取 linux 中的表格
### 通过 Python 抓取表格内容，转换成数据框分析，得出异常波动的渠道和指标
### 本地调用 outlook 将邮件发送给对应的运营同学

########################################


### 第一步：连接 linux ——注意秘钥文件要与此py文件在同一文件夹内， 可封装为函数，返回数据框

import paramiko
from pandas.core.frame import DataFrame

private_key = paramiko.RSAKey.from_private_key_file('id_rsa_2048 (2)')
# 创建SSH对象
ssh = paramiko.SSHClient()

# 把要连接得机器添加到known_hosts文件中
    
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    
ssh.connect(hostname='10.111.39.222', port=22, username='liuyiming', pkey=private_key,
            allow_agent=False, look_for_keys=False)

cmd = "cd ~/inke/temp; cat duplicated_smid.txt"    # 更改为记录指标的预警表及其地址

# 读取数据，转化为数据框
stdin, stdout, stderr = ssh.exec_command(cmd)      
result = stdout.readlines()
for i in range(len(result)):
    result[i] = result[i].strip('\n').split(',')
print(result[0])
df = DataFrame(result,columns = result[0]).iloc[1:,] 
  


### 第二步：分析返回的表格，计算是否存在异动情况










### 第三步：调用本地的 outlook写邮件——邮件内容简单易操作
import win32com.client as win32
import warnings
import pythoncom
#sys.setdefaultencoding('utf8')

warnings.filterwarnings('ignore')

pythoncom.CoInitialize()

def sendmail():

    sub = 'Python调用本地outlook写邮件'

    body = '测试内容：\r 不打开ouklook，保存密码的情况下能发送成功'

    outlook = win32.Dispatch('outlook.application')

    receivers = ['liuyiming@inke.cn']

    mail = outlook.CreateItem(0)

    mail.To = receivers[0]

    mail.Subject = sub

    mail.Body = body

    #mail.Attachments.Add('C:\Users\xxx\Desktop\git_auto_pull_new.py')

    mail.Send()


sendmail()















    















