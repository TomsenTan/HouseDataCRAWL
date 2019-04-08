# -*-coding:utf-8-*-
# @Author:Thomson
# @Date:2019-03-21

import re

class Filter:
    def __new__(cls, *args, **kwargs):         # 单例模式
        if not hasattr(cls, '_instance'):
            origin = super(Filter, cls)
            cls._instance = origin.__new__(cls)
        return cls._instance

    def __init__(self, string):
        self.string = string

    def filterInt(self):
        try:
            _rex = re.compile('\d+')
            numbers = re.findall(_rex, self.string)
            return numbers
        except Exception as e:
            return None

    def filterFloat(self):
        try:
            _rex = re.compile('\d+\.\d+')
            numbers = re.findall(_rex, self.string)
            return numbers
        except Exception as e:
            return None

    def filterDivision(self):
        try:
            _rex = re.compile('\d+\/\d+')
            division = re.search(_rex, self.string).group()
            return division
        except Exception as e:
            return None

    def __call__(self, *args, **kwargs):
        pass


def test():
    string1 = '12.890 ㎡'
    string2 = '1345abc'
    filterNums1 = Filter(string1).filterFloat()
    filterNums2 = Filter(string2).filterFloat()
    print(filterNums1)
    print(filterNums2)

# test()