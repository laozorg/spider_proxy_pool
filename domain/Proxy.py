from settings.settings import MAX_SCORE


class Proxy(object):


    def __init__(self,ip,port,speed=0,area=None,protocal=-1,nick_type=-1,score=MAX_SCORE,diable_domains=[]):
        self.ip=ip
        self.port=port
        # 0 高匿 1 匿名 2 透明
        self.nick_type=nick_type
        # 0 http 1 https 2 http&https
        self.protocal=protocal
        self.speed=speed
        self.area=area
        self.score=score
        self.diable_domains=diable_domains
    
    def __str__(self) -> str:
        return str(self.__dict__)