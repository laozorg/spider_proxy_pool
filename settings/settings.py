import logging

#代理健康分数
MAX_SCORE = 50

#log
LOG_LEVEL = logging.INFO
LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
LOG_FILENAME = 'log.log'

#mysql config
MYSQL_URL = '192.168.8.121'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'zsh'
MYSQL_DB_NAME = 'proxy_pool'

#proxy 项目请求用
HTTP_PROXY = 'http://192.168.8.2:7890'

#代理超时时间
