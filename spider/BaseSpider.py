# -*- coding: utf-8 -*-

'''
@File    :   BaseSpider.py
@Time    :   2022/12/05 16:29:01
@Author  :   eric_zhou 
@Version :   1.0
@Desc    :   代理ip爬虫通用方法
'''
import requests
from util.MysqlPool import pool
from fake_useragent import UserAgent
from settings.settings import HTTP_PROXY


ua = UserAgent(browsers=['edge', 'chrome'])

proxies = {
    'http': HTTP_PROXY,
    'https': HTTP_PROXY,
}

class BaseSpider(object):
    
    def getPage(self,usrls=[]):
        headers = {'user-agent': ua.random}
        for url in usrls:
            r = requests.get(url, headers=headers)
            yield r.text
            
    def handlePage(self):
        pass
    
    def saveProxies(self,proxies=[]):
        con=pool.get_connection()
        cursor=con.cursor()
        sql='insert ignore into proxies(ip,port,nick_type,protocal,speed,area,score,diable_domains) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.executemany(sql,proxies)
        con.commit()
        con.close()
    
    
   