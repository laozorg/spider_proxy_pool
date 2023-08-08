from spider.BaseSpider import BaseSpider
import time
from util.Log import logger
from bs4 import BeautifulSoup

class Kuaidaili(BaseSpider):
    urls = ['https://www.kuaidaili.com/free/inha/{}'.format(i) for i in range(1,100)]

    def handlePage(self):
        spider=Kuaidaili()
        for item in spider.getPage(spider.urls):
            proxies=[]
            bs=BeautifulSoup(item)
            trs=bs.find('table').find_all('tr')
            for item in trs: 
                if(item.select('td[data-title="IP"]') and item.select('td[data-title="PORT"]')):
                    proxy=(item.select('td[data-title="IP"]')[0].text 
                           ,item.select('td[data-title="PORT"]')[0].text 
                           ,'0','0','0'
                           ,item.select('td[data-title="位置"]')[0].text
                           ,'50'
                           ,''
                    )
                    logger.info(proxy)
                    proxies.append(proxy)
            spider.saveProxies(proxies)
            time.sleep(3)

        



