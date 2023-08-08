# -*- coding: utf-8 -*-

'''
@File    :   MysqlPool.py
@Time    :   2022/12/05 15:27:33
@Author  :   eric_zhou 
@Version :   1.0
@Desc    :   mysql 数据库连接池
'''

from mysql.connector.pooling import MySQLConnectionPool
from util.Log import logger
from settings.settings import MYSQL_URL, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB_NAME

config = {
    'host': MYSQL_URL,
    'port': MYSQL_PORT,
    'user': MYSQL_USER, 
    'password': MYSQL_PASSWD,
    'database': MYSQL_DB_NAME
}


class MysqlPool(object):

    def __init__(self):
        try:
            self._pool = MySQLConnectionPool(
                **config,
                pool_size=10
            )
            
        except Exception as e:
            logger.error('Mysql pool create error',e)
            exit(1)
            
    @property
    def pool(self):
        return self._pool
    
    
pool=MysqlPool().pool