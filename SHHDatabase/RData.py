# -*- coding:UTF-8 -*-

import redis
from datetime import datetime
from SHHLog.MLog import mlog as RLog



class RedisData(object):
    '''
    创建一个通用的连接Redis的类，
    :param
        -- tittle  name的标签，在初始化一个key的时候需要添加这个参数
    '''
    def __init__(self, title):
        self.conn = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
        self.title = title

    def _set(self, key, value):
        self.conn.set(key, value)

    def _get(self, key):
        value = self.conn.get(key)
        return value

    def _listput(self, key, value):
        self.conn.lpush(key, *value)

    def _listpop(self, key):
        value = self.conn.rpop(key)
        return value

    def _listlen(self, key):
        length = self.conn.llen(key)
        return length

    def _hexset(self, name, key, value):
        self.conn.hset(name, key, value)

    def _hexget(self, name, key):
        value = self.conn.hget(name, key)
        return value

    def _hexgetall(self, name):
        value = self.conn.hgetall(name)
        return value

    def SET(self, key, value):
        return self._set(key, value)

    def HSET(self, name, key, value):
        name = self.title + name
        if isinstance(value, dict):
            for _key, _value in value.items():
                self._hexset(name, _key, _value)
        else:
            self._hexset(name, key, value)

    def HGETALL(self, name):
        return self._hexgetall(name)



# redissample = RedisData('ensureCrawl:IP:')
#
# ensureMes = {
#     'website': 'zr',
#     'proxy': 1,
#     'timestamp': str(datetime.now())
# }

# redissample.HSET('127.0.0.1', '', ensureMes)
# value = redissample.HGETALL('ensureCrawl:IP:127.0.0.1')
# print(value)
