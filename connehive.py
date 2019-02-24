# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:41:03 2019

@author: Inke1812122
"""

### 连接hive
### 要求先 conda/pip install 以下安装包
### pip install sasl
### pip install thrift
### pip install thrift-sasl
### pip install PyHive 
### cloudera
    

from pyhive import hive
import pyhs2
import sys

#default_encoding = 'utf-8'  
#if sys.getdefaultencoding() != default_encoding:  
#    reload(sys)  
#    sys.setdefaultencoding(default_encoding)  

class HiveClient:  
    def __init__(self,db_host,user,password,database,port=10008,authMechanism="PLAIN"):  
        """ 
        create connection to hive server2 
        """  
        self.conn = pyhs2.connect(host=db_host,  
                                  port=port,  
                                  authMechanism=authMechanism,  
                                  user=user,  
                                  password=password,  
                                  database=database,)  

    def query(self, sql):  

        """ 
        query 
        """  
        with self.conn.cursor() as cursor:  
            cursor.execute(sql)  
            return cursor.fetch()  

    def close(self):  
        """ 
        close connection 
        """  
        self.conn.close()  

hive_client = HiveClient(db_host='10.10.0.58',port=10000,user='inke',
                         password =  '123456789',
                         database='default', authMechanism='PLAIN') 


conn = hive.Connection(host='10.10.0.58', port=10000, username='liuyiming', database='default')
cursor = conn.cursor()

cursor.execute('select * from testhive limit 10')

for result in cursor.fetchall():

    print( result)






from pyhive import hive

import pandas as pd

#import sys

#reloar(sys)

#sys.setdefaultencoding('utf8')  

def LinkHive(sql_select):

    connection = hive.Connection(host='10.10.0.58', port=10000, username='inke', database='default',
                                 password = '123456789',)
    hive.Connection

    cursor = connection.cursor()      

    cursor.execute(sql_select)

    columns = [col[0] for col in cursor.description]

    result = [dict(zip(columns, row)) for row in cursor.fetchall()]

    Main = pd.DataFrame(result)

    Main.columns = columns 

    return Main

sql = "select * from tg.day_cc_data limit 1;"

df  = LinkHive(sql)
