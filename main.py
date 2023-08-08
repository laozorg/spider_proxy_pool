from util.Log import logger
# from util.MysqlClient import cursor
# from util.MysqlClient import close_mysql
# from util.MysqlClient import connect
from spider.ProxySpider import Kuaidaili



if __name__ == '__main__':
    # print(id(logger))
    # print(id(logger))
    # logger.info('test')
    
    # cou=connect.cursor()
    # print(type(cursor))
    # print(type(close_mysql))
    
    # cou.execute("use python;")
    # close_mysql
    # cursor.execute("user mysql;") 
    
    spider=Kuaidaili()
    spider.handlePage() 