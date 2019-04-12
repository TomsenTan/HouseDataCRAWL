# -*- coding:UTF-8 -*-
import mongoengine
from SHHLog.MLog import mlog as MgLog


class MongoEngine(object):
    def __init__(self, Metaclass):
        self.Object = Metaclass.objects()
        super(MongoEngine, self).__init__()

    def __getAll(self):
        return self.Object.all()

    def __get(self, name, value):
        return self.Object.filter(__raw__={name: value})

    def __mget(self):
        pass

    def __save(self):
        pass

    def __msave(self):
        pass

    def __update(self, key1, key2,  action, value=None, upvalue=None):
        '''
        说明：调用接口为UPDATE,UPDATE函数内部调用__update
        eg：对匹配article_title的文档的article_views_count数值增加5
        MGeng(Article).UPDATE('article_title', 'article_views_count',
#                           'incr', kvalue=artilcTitle, upvalue=5)

        :param key1:  用于查询文档的key
               注意：若key1是id,则必须用 _id 形式，因数据库存储形式为 _id
        :param key2:  更新的key
        :param action:  更新操作
               --incr  增加
               --decr  减少
               --set   设置新值
               --unset 删除
        :param value:   用于查询文档的key对应的值
        :param upvalue: 更新字段的值
        :return:
        '''
        try:
            if action == 'incr':
                upaction = 'inc__' + key2
                self.Object(__raw__={key1: value}).update(**{upaction: upvalue})
            elif action == 'decr':
                upaction = 'dec__' + key2
                self.Object(__raw__={key1: value}).update(**{upaction: upvalue})
            elif action == 'set':
                upaction = 'set__' + key2
                self.Object(__raw__={key1: value}).update(**{upaction: upvalue})
            elif action == 'unset':
                upaction = 'unset__' + key2
                self.Object(__raw__={key1: value}).update(**{upaction: 1})
            else:
                pass
            MgLog.INFO('Update %s %s'%(action, key2))
        except Exception as e:
            MgLog.ERROR(e)

    def __updateOne(self, key1, key2,  action, value=None, upvalue=None):
        '''
        说明：此更新操作只更新符合匹配的第一个文档的值
        '''
        try:
            if action == 'incr':
                upaction = 'inc__' + key2
                self.Object(__raw__={key1: value}).update_one(**{upaction: upvalue})
            elif action == 'decr':
                upaction = 'dec__' + key2
                self.Object(__raw__={key1: value}).update_one(**{upaction: upvalue})
            elif action == 'set':
                upaction = 'set__' + key2
                self.Object(__raw__={key1: value}).update_one(**{upaction: upvalue})
            elif action == 'unset':
                upaction = 'unset__' + key2
                self.Object(__raw__={key1: value}).update_one(**{upaction: 1})
            elif action == 'push':
                lupaction = 'push__' + key2
                self.Object(__raw__={key1: value}).update_one(**{lupaction: upvalue})
            elif action == 'pushall':
                if isinstance(upvalue, list):
                    lupaction = 'push_all__' + key2
                    self.Object(__raw__={key1: value}).update_one(**{lupaction: upvalue})
                else:
                    return
            else:
                MgLog.INFO('Update None')
            MgLog.INFO('Update %s %s' % (action, key2))
        except Exception as e:
            MgLog.ERROR( e)

    def __updateList(self, key1, key2,  action, value=None, lupvalue=None):
        try:
            if action == 'push':
                lupaction = 'push__' + key2
                self.Object(__raw__={key1: value}).update(**{lupaction: lupvalue})
            elif action == 'pushall':
                if isinstance(lupvalue, list):
                    lupaction = 'push_all__' + key2
                    self.Object(__raw__={key1: value}).update(**{lupaction: lupvalue})
                else:
                    MgLog.ERROR('(PUSH_ALL)lupvalue must be list')
                    return
            elif action == 'pull':
                lupaction = 'pull__' + key2
                self.Object(__raw__={key1: value}).update(**{lupaction: lupvalue})
            elif action == 'pullall':
                if isinstance(lupvalue, list):
                    lupaction = 'pull_all__' + key2
                    self.Object(__raw__={key1: value}).update(**{lupaction: lupvalue})
                else:
                    MgLog.ERROR('(PULL_ALL)lupvalue must be list')
                    return
            else:
                pass
        except Exception as e:
            MgLog.ERROR(e)


    def __del(self, id):
        pass

    def __order(self, name, des=-1):
        if des == -1:
            name = '-' + name
            return self.Object.order_by(name)
        else:
            return self.Object.order_by(name)

    def __average(self, name):
        return self.Object.average(name)

    def GET(self, name, value):
        return self.__get(name, value)

    def GETAll(self):
        return self.__getAll()

    def MGET(self):
        return self.__mget()

    def SAVE(self):
        return self.__save()

    def MSAVE(self):
        return self.__msave()

    def UPDATE(self, key1, key2,  action, kvalue=None, upvalue=None):
        self.__update(key1, key2,  action, value=kvalue, upvalue=upvalue)

    def UPDATEONE(self, key1, key2,  action, kvalue=None, upvalue=None):
        self.__updateOne(key1, key2,  action, value=kvalue, upvalue=upvalue)

    def UPDATELIST(self, key1, key2,  action, kvalue=None, lkupvalue=None):
        return self.__updateList(key1, key2,  action, value=kvalue, lupvalue=lkupvalue)

    def DELETE(self, id):
        return self.__del(id)

    def ORDER(self, name, des=-1):
        return self.__order(name, des)

    def AVERAGE(self, name):
        return self.__average(name)

    def __call__(self):
        return self

class Mongo(object):
    def __init__(self):
        pass


    def MSAVE(self):
        pass