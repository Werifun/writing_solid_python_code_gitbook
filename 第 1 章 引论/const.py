#coding:utf-8

class _const:
    class ConstError(TypeError):pass  # TyperError 指对类型无效的操作
    class ConstCaseError(ConstError):pass

    def __init__(self):
        
        _const.__setattr__ = _const._setattr_imp1

    def _setattr_imp1(self, name, value):
        raise self.ConstError("Can't bind const instance attribute {}".format(name))

    def __setattr__(self, key, value):  # 在对类的属性赋值的时候会自动调用
        if key in self.__dict__:  # object.__dict__以dict的方式存储object所有可读属性
            raise self.ConstError("Can't change const.%s" %key)
        if not key.isupper():
            raise self.ConstCaseError("const name %s is not all uppercase" %key)

        self.__dict__[key] = value

    def __getitem__(self,key):  # 了解一下__getitem__的功能，并且使用getitem可以像字典一样获取常量
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            raise self.ConstError("Can't return const.%s, No Existsing Key!"%key)

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const instance attribute {}".format(name))

        raise AttributeError("const instance has no attribute {}".format(name))


import sys
sys.modules[__name__] = _const()
# sys.modules保存有当前Python环境中已经导入的模块记录，这是一个全局字典，当Python启动后就加载在内存中。
# dict的key为文件名，value为模块对象。
# __name__就是标识模块的名字的一个系统变量。
# 如果模块被导入，__name__就是模块的名字
# 如果模块被直接执行，__name__的值是'__name__'

# sys.modules['const'] = _const()
# 即，让_const类作为模块的入口点，引入const.py等价于声明了一个_const类的实例。


