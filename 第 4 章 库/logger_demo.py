#coding:utf-8


import logging
import logging.handlers
'''
变量           格式     变量描述

asctime        %(asctime)s 将日志的时间构造成可读的形式，默认情况下是精确到毫秒，如 2018-10-13 23:24:57,832，可以额外指定 datefmt 参数来指定该变量的格式

name           %(name) 日志对象的名称

filename       %(filename)s 不包含路径的文件名

pathname       %(pathname)s 包含路径的文件名

funcName       %(funcName)s 日志记录所在的函数名

levelname      %(levelname)s 日志的级别名称

message        %(message)s 具体的日志信息

lineno         %(lineno)d 日志记录所在的行号

pathname       %(pathname)s 完整路径

process        %(process)d 当前进程ID

processName    %(processName)s 当前进程名称

thread         %(thread)d 当前线程ID

threadName     %threadName)s 当前线程名称

'''

# 创建一个logger
logger = logging.getLogger("logger")

handler1 = logging.StreamHandler()
handler2 = logging.FileHandler(filename="test.log")

logger.setLevel(logging.DEBUG)
handler1.setLevel(logging.WARNING)
handler2.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.addHandler(handler1)
logger.addHandler(handler2)

# 分别为 10、30、30
# print(handler1.level)
# print(handler2.level)
# print(logger.level)

logger.debug('This is a customer debug message')
logger.info('This is an customer info message')
logger.warning('This is a customer warning message')
logger.error('This is an customer error message')
logger.critical('This is a customer critical message')

