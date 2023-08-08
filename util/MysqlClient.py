import mysql.connector
from mysql.connector import errorcode
from settings.settings import MYSQL_URL, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB_NAME

config = {
        'host': MYSQL_URL,
        'port': MYSQL_PORT,
        'user': MYSQL_USER,
        'password': MYSQL_PASSWD,
        'database': MYSQL_DB_NAME
    }


class MysqlClient(object):

    def __init__(self):
        try:
            self._connector=mysql.connector.connect(**config)   
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            exit(1)
        
    @property
    def close_client(self):
        self._connector.close()
    
    @property
    def con(self):
        return self._connector.cursor()
    
connect=MysqlClient().con

close_connect=MysqlClient().close_client
   
   
   
   
   
   
   



# import pymysql
# from dbutils.pooled_db import PooledDB

# db_config = {
#     'host': '192.168.246.129',
#     'port': 3306,
#     'user': 'testuser',
#     'passwd': 'testpass',
#     'db': 'testdb',
#     'charset': 'utf8mb4',
#     'maxconnections': 0,     # 连接池允许的最大连接数
#     'mincached': 4,          # 初始化时连接池中至少创建的空闲的连接，0表示不创建
#     'maxcached': 0,          # 连接池中最多闲置的连接，0表示不限制，连接使用完成后的空闲连接保留数。
#     'maxusage': 5,           # 每个连接最多被重复使用的次数，None表示不限制
#     'blocking': True         # 连接池中如果没有可用连接后是否阻塞等待，
#                              # True 等待，让用户等待，尽可能的成功； False 不等待然后报错，尽快告诉用户错误，例如抢购，不成功就提示。

# }

# spool = PooledDB(pymysql, **db_config)
# conn = spool.connection()
# cur = conn.cursor()
# SQL = 'select * from bookorm;'
# cur.execute(SQL)
# f = cur.fetchall()
# print(f)
# cur.close()
# conn.close()