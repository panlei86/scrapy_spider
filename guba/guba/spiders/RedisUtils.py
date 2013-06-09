#-*-coding:utf-8-*-
'''
Created on 2013-6-6
url集合：所有爬去过的url
job集合：所有需要爬取的url
@author: liuyouli
'''
import redis
class RedisUtils:
    #ip='114.212.82.39'
    ip='127.0.0.1'
    def __init__(self):
        #self.ip=ip
        print 'connect redis-server:'+self.ip
        
    '''
     判断一个url是否在集合中，如果在则返回Ture；如果不再则返回False  
    '''
    def isExist(self,url):
        pool = redis.ConnectionPool(host=self.ip, port=6379)  
        r = redis.Redis(connection_pool=pool)
        exist=r.sismember('url',url)
        if(exist==1):
            return True
        else:
            return False
    def saveUrl(self,url):
        pool = redis.ConnectionPool(host=self.ip, port=6379)  
        r = redis.Redis(connection_pool=pool)
        r.sadd('url',url)
        r.rpush('job',url)
    '''
     从job集合中取出一个url。如果job集合为空，返回None;否则返回job中一个url
    '''    
    def getUrl(self):
        pool = redis.ConnectionPool(host=self.ip, port=6379)  
        r = redis.Redis(connection_pool=pool)
        url=r.lpop('job')
        return  url

ru=RedisUtils()
print ru.getUrl()
'''
print ru.isExist('127.0.0.1', 1)
'''

    
    