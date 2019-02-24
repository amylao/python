# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:27:49 2019

@author: Inke1812122
"""

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa_2048 (2)')
# 创建SSH对象
ssh = paramiko.SSHClient()

# 把要连接得机器添加到known_hosts文件中
    
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    
ssh.connect(hostname='10.111.39.222', port=22, username='liuyiming', pkey=private_key,
            allow_agent=False, look_for_keys=False)

cmd = "ls"
stdin, stdout, stderr = ssh.exec_command(cmd)

result = stdout.readlines()
print(result)



# 访问linux上的文件

sftp_client = ssh.open_sftp()

#按路径访问txt文件
remote_file = sftp_client.open("apple.csv") #文件路径
try:
    for line in remote_file:
        print(line.strip())
finally:
    remote_file.close()



# 上传与下载linux上的文件
#下载文件 
sftp_client.get("/home/test.txt","./c.txt")
#上传文件 
sftp.put("/a.txt","/home/b.txt")
#或者直接连ftp服务器 
transport = paramiko.Transport((hostname, port)) transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)
#下载文件 
sftp.get("/home/test.txt","/a.txt")
#上传文件 
sftp.put("/a.txt","/home/b.txt")


# 在xshell上操作Python——通
cmd = "python"
stdin, stdout, stderr = ssh.exec_command(cmd)

# 没有运行通
cmd = "hive -e 'set hive.cli.print.header = true; select * from bi.cc_download_smid_reg_view_pay_rday where cc = "TG0001"'| sed -e 's/\t/,/g'>apple.csv"
stdin, stdout, stderr = ssh.exec_command(cmd)






















