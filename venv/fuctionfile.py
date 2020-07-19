# #创建一个类
# class test_ceshi(object):#集成object
#     pass
# class test_ceshi1():#不继承
#     pass
# print(type(test_ceshi))
#
# #构造函数
# # def __init__(self.)
#
# class progaramer(object):
#     def __init__(self,name,age,weight):
#         self.name=name
#         self._age=age#带一个下划线代表为私有属性，但是还是可以被访问
#         self.__weight=weight#带2个下划线表示私有属性不可被外部类访问
#
#     def get_weight(self):
#         return self.__weight
#
# if __name__=='__main__':
#     progaramer=progaramer('abc',25,80)
#     print(dir(progaramer))
#     print (progaramer.__dict__)
#     print(progaramer.get_weight())
#     print(progaramer._progaramer__weight)
#
# #函数是直接使用函数名使用的
# #方法必须有对象
# #类方法就是类属性
# @classmethod#调用的时候用类名不是属性
#
# @property#像访问属性一样调用方法
# class Test(object):
#     def test(self):
#         pass
# print(a=Test())
# Printa.test(1,2,3)
#
# @classmethod
# def get_hobby(cls):
#     return cls.hobby
#
#
# @property
# def get_weight(self):
#     return self.__weight
# #继承类在括号里面写上父类的名称，使用super方法调用父类方法
# class a(object):
#     def method(self,arg):
#         pass
#
# class b(a):
#     def method(self,arg):
#         super(b,self).method(arg)#新调用方法
#         a.method(arg)#旧的调用方法
# def self_introdection(self):
#     print(self.name,self._age)
#
# # if __name__=='__main__':
# #多继承
# # class Driverclassname(base1,base2,base3):
#
#
spam=1
text='111ceshi1'
