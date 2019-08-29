#coding:utf-8

import configparser
#coding:utf-8
import os

'''
-read(filename)               直接读取文件内容
-sections()                      得到所有的section，并以列表的形式返回
-options(section)            得到该section的所有option
-items(section)                得到该section的所有键值对
-get(section,option)        得到section中option的值，返回为string类型
-getint(section,option)    得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数
'''

cf = configparser.ConfigParser()

cf.read("test.ini")
#cf.read("test.conf")

#return all section
secs = cf.sections()
print('sections:', secs, type(secs))
opts = cf.options("db")
print('options:', opts, type(opts))
kvs = cf.items("db")
print('db:', kvs)

#read by type
db_host = cf.get("db", "db_host")
db_port = cf.getint("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_pass")

#read int
threads = cf.getint("concurrent", "thread")
processors = cf.getint("concurrent", "processor")
print("db_host:", db_host)
print("db_port:", db_port)
print("db_user:", db_user)
print("db_pass:", db_pass)
print("thread:", threads)
print("processor:", processors)

