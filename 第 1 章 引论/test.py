#coding:utf-8

from .constant import const


print(const.TEXTLINE)
print(const.TEXTBOX)
del const.TEXTLINE

def add(a,b):
    return a+b


print(add(1,2))
