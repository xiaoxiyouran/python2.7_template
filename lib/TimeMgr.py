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
import time,datetime
# =====================================================

class TimeMgr(object):
    def GetCurFormatTime(self, tFormat = '%Y-%m-%d:%H%M%S'):
        '''
        获取当前格式化字符串
        :param tFormat: 格式
        :return:
        '''
        return datetime.datetime.now().strftime(tFormat)
