#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
# 注释后面空一格，否则有警告
# --------------以下两行对 python2 适用 ----------------
reload(sys)
sys.setdefaultencoding('utf8')
# =====================================================
sys.path.append(".")

# -------------- 本文件用到的库 ----------------
import logging
from logging import handlers

from TimeMgr import *
# =====================================================


import logging
from logging import handlers


class LogMgr(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,  # info 级别的日志不会在屏幕打印
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }                                                            # 日志级别关系映射

    def __init__(self, _bIsErrorSplit = False):
        '''
        :param _bIsErrorSplit: 错误日志是否输出到另一个文件
        '''
        self._isErrorSplit = _bIsErrorSplit

        # 第一个 logger: 输出到 终端
        self._ConsoleLogger = self._GenConsole()

        # 第一个 logger: 能同时输出到 终端和文件
        gTimeMgr = TimeMgr()
        self._logFile = '..' + os.path.sep + 'Log/log_' + gTimeMgr.GetCurFormatTime('%Y-%m-%d') + ".log"
        self._ConsoleAndFileLogger = self._GenConsoleAndFile(self._logFile)


    def _GenConsole(self, level='debug', when='W', backCount=3, fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        logger = logging.getLogger('Console')
        format_str = logging.Formatter(fmt)  # 设置日志格式
        logger.setLevel(self.level_relations.get(level))  # 日志级别都设置为 最低级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        logger.addHandler(sh)  # 把对象加到logger里
        return logger

    def _GenConsoleAndFile(self, filename, level='debug', when='D', backCount=3, fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        '''
        创建同时输出屏幕和文件的 looger 对象
        :return: logger
        '''
        logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)                 # 设置日志格式
        logger.setLevel(self.level_relations.get(level))    # 日志级别都设置为 最低级别
        sh = logging.StreamHandler()                        # 往屏幕上输出
        sh.setFormatter(format_str)                         # 设置屏幕上显示的格式

        # 往文件里写入#指定间隔时间自动生成文件的处理器
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding='utf-8')
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        logger.addHandler(sh)  # 把对象加到logger里
        logger.addHandler(th)

        return logger

    def Console(self):
        '''
        在 Console 中输出
        :return:
        '''
        return self._ConsoleAndFileLogger

    def ConsoleAndFile(self):
        '''
        同时在 Console 和 文件中输出
        :return:
        '''
        return self._ConsoleAndFileLogger

if __name__ == '__main__':
    log = LogMgr()
    log.Console().debug('终端')
    log.ConsoleAndFile().debug('终端和文件中')

    # Logger('error.log', level='error').logger.error('error')