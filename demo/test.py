#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys

# 注释后面空一格，否则有警告
# --------------以下两行对 python2 适用 ----------------
reload(sys)
sys.setdefaultencoding('utf8')
# ==============End ===================================
sys.path.append(".")


import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
logging.debug('debug 信息')
logging.info('info 信息')
logging.warning('warning 信息')
logging.error('error 信息')
logging.critical('critial 信息')