#coding:utf-8

'''
# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10
# NOTSET = 0

https://juejin.im/post/5bc2bd3a5188255c94465d31
'''

import logging

# 自定义错误级别
#logging.addLevelName(31, 'SERIOUS WARNING') 

#logger = logging.getLogger('log')
#logger.warning('warn info')
#logger.log(logging.getLevelName('SERIOUS_WARNING'),'serious warn')


# 直接使用默认配置
# logging.basicConfig()
'''
参数名称   参数描述

filename   日志输出到文件的文件名

filemode   文件模式，r[+]、w[+]、a[+]

format     日志输出的格式

datefat    日志附带日期时间的格式

style      格式占位符，默认为 "%" 和 “{}”

level      设置日志输出级别

stream     定义输出流，用来初始化 StreamHandler 对象，不能 filename 参数一起使用，否则会ValueError 异常

handles    定义处理器，用来创建 Handler 对象，不能和 filename 、stream 参数一起使用，否则也会抛出 ValueError 异常
'''
logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

a, b = 5, 0

# 当发生异常的时候使用exception方法
# 否则，需要设置exc_info参数为True

try:
    c=a/b
except Exception as e:
    # 下面三种方式三选一，推荐使用第一种
    logging.exception("Exception occurred")  
    logging.error("Exception occurred", exc_info=True)
    logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)


