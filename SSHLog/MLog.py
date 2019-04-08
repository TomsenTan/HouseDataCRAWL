# -*-coding:utf-8-*-
# @Author:Thomson
# @Date:2019-04-04

'''
此模块调用python系统的日志来对程序写日志
作用：
1. 建立统一的日志规范，避免多人开发过程中日志格式的不一样（例如写文件记录日志）
2. 在多进程并发写日志的时候可以节省掉加减锁的繁琐问题
'''

import logging
import traceback
# import stackless  # 第三方模块
import sys

class SHlog:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            origin = super(SHlog, cls)
            cls._instance = origin.__new__(cls)
        return cls._instance

    def __init__(self, objname):
        # 创建日志实例
        self.objname = objname
        self.logger = logging.Logger(self.objname)
        # 日志格式
        self.formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        # 创建处理器
        self.setHandler()

    def _setHandlerFormat(self):
        # 创建日志：文件日志/终端日志
        # 自动创建文件日志
        self.fileName = self.objname + '.log'
        self.file_handler = logging.FileHandler(self.fileName)
        self.file_handler.setFormatter(self.formatter)

        # 终端日志
        self.consle_handler = logging.StreamHandler(sys.stdout)
        self.consle_handler.setFormatter(self.formatter)

    def _setLevel(self):
        # 设置默认级别，发布的时候使用INFO级别
        self.logger.setLevel(logging.DEBUG)

    def _addHandler(self):
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.consle_handler)

    def setHandler(self):
        self._setHandlerFormat()
        self._setLevel()
        self._addHandler()

    def _log(self, msg, *args, **kwargs):  # 格式化msg, *args, **kwargs
        if not isinstance(*args, str):
            msg = msg + str(*args)
            return msg
        else:
            return msg

    def CRITICAL(self, msg, *args, **kwargs):
        self.logger.critical(msg *args, **kwargs)

    def ERROR(self, msg, *args, **kwargs):
        try:
            # etype, value, tb = sys.exc_info()
            Recmsg = "E" + "| ************************************************************"
            self.logger.error(Recmsg)
            msg = self._log(msg, *args, **kwargs)
            Recmsg = msg
            self.logger.error(Recmsg)
            # if tb:
            #     traceback.print_tb(tb)
            # traceback.print_exception(etype, value, tb, None, None)
        finally:
            etype = value = tb = None
            Recmsg = "E" + '| ------------------------ Call Stack ------------------------'
            self.logger.error(Recmsg)
            self.logger.error(traceback.format_exc(limit=1))
            Recmsg = "E" + "| ************************************************************"
            self.logger.error(Recmsg)

    def WARNNING(self, msg, *args, **kwargs):
        msg = self._log(msg, *args, **kwargs)
        self.logger.warning(msg)

    def INFO(self, msg, *args, **kwargs):
        msg = self._log(msg, *args, **kwargs)
        self.logger.info(msg)

    def DEBUG(self, msg, *args, **kwargs):
        msg = self._log(msg, *args, **kwargs)
        self.logger.debug(msg)

    def removeHandler(self):
        # 当不使用日志时要remove，否则会重复写
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.consle_handler)

    def __del__(self):
        self.removeHandler()

mlog = SHlog('mlog')


