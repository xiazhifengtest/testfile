import unittest

# message = 'hello world'
# print(message)
# message = '1'
# print(1)
#
# message = 'app'
# print(message)
# message = '10'
# print(message)
# newmessage = 1
# print(newmessage)
# newmessage = 10
# print(newmessage)
#
# 'this isstring'
# name = 'ada lovelace'
# # title方法用首字母大写展示
# print(name.title())
# # upper全大写
# # lower全小写
# print(name.upper())
# print(name.lower())
# first_name = 'ada'
# last_name = 'love'
# full_name = first_name + ' ' + last_name
# print(full_name)
# nmessage = 'hello' + ' ' + full_name
# print(nmessage)
# # \t制表符，\n换行
# print('\t111')
# print('\n11\n11\n11')
# print('\n\t111\n\t111\n\t222')
#
# username = 'kelaier'
# print('hello dear' + ' ' + username)
# youname = 'xia'
# print(youname.title())
# print(youname.upper())
# print(youname.lower())
# cc = "do you like me,because  i'm fine"
# cc1 = 'doyou1jdlkjsjkls "111"hdshkd'
# print(cc, '  ', cc1)
# print(4 + 2)
# print(4 ** 2)
# print(0.1 + 0.1)
# age = 23
# message = 'happy' + str \
#     (age) + 'rd b'
# print(message)
# # int()数据类型改为int，str（）数据类型改为字符串
# print(4 + 4)
# print(2 * 4)
# print(10 - 2)
# print(int(16 / 2))
# c = str(1)
# print('i like number=' + c)
# # 注释用#号
# '''注释'''
# import this

# '''列表'''
# cclist = ['trck', 'cannondale', 'redine', 'sepr']
# print(cclist)
# print(cclist[0])
# print(cclist[0].title())
# # 记住列表中的索引是从0开始的
# print(cclist[2])
# print(cclist[3])
# print(cclist[-1])
# bic=['trek','canner','readine','spcialized']
# message='My first bic was a'+bic[2].title()+'.'
# print(message)
#
# motocc=['xia','zhi','feng']
# print(motocc)
# motocc[0]='se'
# print(motocc)
# motocc.append('ccc')
# print(motocc)
# motocc=[]
# print(motocc)
# motocc.append('hong')
# motocc.append('ccc')
# motocc.append('kkk')#列表最后添加
# print(motocc)
# motocc.insert(0,'qqq')#列表插入
# print(motocc)
# del motocc[0]
# print(motocc)
# del motocc[2]#列表删除
# print(motocc)
# motocc=['xia','zhi','feng']
# print(motocc)
# poppend_motocc=motocc.pop()
# print(motocc)
# print(poppend_motocc)
# motocc=['xia','zhi','feng']
# last_owen=motocc.pop()
# print('the '+last_owen.title()+'.')
# motott=['xia','zhi','feng']
# first_ow=motott.pop(0)
# print('the '+first_ow.title()+'.')
# motoname=['xia','zhi','feng','de','cc']
# too_expensive='de'
# motoname.remove(too_expensive)
#
# print(motoname)
# print("\nA"+too_expensive.title()+"istoo me.")
#
# visiter_name=['xia','wu','sun']
# print(visiter_name)
# no_come='sun'
# visiter_name.remove(no_come)
# to_come='liu'
# visiter_name.append(to_come)
# print(visiter_name)
# print('welcome '+visiter_name[0]+' to')
# print('welcome '+visiter_name[1]+' to')
# print('welcome '+visiter_name[2]+' to')
# welcom_1='zhang'
# welcom_2='li'
# welcom_3='peng'
# visiter_name.insert(0,welcom_1)
# visiter_name.insert(2,welcom_2)
# visiter_name.append(welcom_3)
# print(visiter_name)
# print('welcome '+visiter_name[0]+' to')
# print('welcome '+visiter_name[1]+' to')
# print('welcome '+visiter_name[2]+' to')
# print('welcome '+visiter_name[3]+' to')
# print('welcome '+visiter_name[4]+' to')
# print('welcome '+visiter_name[5]+' to')
# cc=visiter_name.pop(0)
# print('sorry '+cc)
# cc=visiter_name.pop()
# print('sorry '+cc)
# cc=visiter_name.pop()
# print('sorry '+cc)
# cc=visiter_name.pop()
# print('sorry '+cc)
# print('hello '+visiter_name[0])
# print('hell0 '+visiter_name[1])
# print(visiter_name)
# del visiter_name[0]
# print(visiter_name)
# del visiter_name[0]
# print(visiter_name)
# cars=['bmw','toyota','audi','su']
# print(len(cars))
# print(cars.sort())
# print(cars.sort(reverse=True))
# print(sorted(cars))


# visited_1=['xiamen','yunan','beijing','xizang','lasa']
# print(len(visited_1))
# visited_1.sort()
# print(visited_1)
# visited_1.sort(reverse=True)
# print(visited_1)
# sorted(visited_1)
# print(visited_1)
# visited_1.reverse()
# print(visited_1)
# visited_1.reverse()
# print(visited_1)
# print(visited_1[100])
# magic1=['xia','zhi','feng']
# for i in magic1:
#     print(i.title()+' good'+'\n'+'nice')
# print('thank')
#
#
# anm=['pig','dog','cat']
# for kimi in anm:
#     print('kimi is a good '+kimi)
# print('she is pretty')


# for value in range(1,10):
#     print(value)
#
# number=list(range(1,11))
# print(number)
# number=list(range(1,20,2))
# print(number)
# squs=[]
# for val in range(1,11):
#     squ=val**2
#     squs.append(squ)
# print(squs)
# squs=[]
# for val in range(1,11):
#     squs.append(value**2)
# print(squs)
# li1=list(range(1,11))
# print(min(li1))
# print(max(li1))
# print(sum(li1))


# squares=[value**2 for value in range(1,11)]
# print(squares)
#
# li1=list(range(1,1000000))
# for i in li1:
#     print(i)
# 通过继承unittest.testcase
# class fortest(unittest.TestCase)

'''unittest
衍生出pytest
pytest可以完美衔接unittest
pytest——unittest——robotframework
环境：python直接加载了unittest框架不需安装
4大组件
1.testfixure，setup（前置条件）teardown（后置条件）用于初始化环境，和清理释放资源
2.test case 测试用例 unittest中通过继承uitntest.testcase来实现用例的继承,unittest中用例都是通过test来识别
def test_test1()
3.test suite
list =(case1,case2,case3)
4.test runner 运行器，通过runner调用suite执行用例
unittest 运行机制，






'''

'''class forTest(unittest.TestCase):

    def setUpClass(cls) -> None:
        print('setupc')

    def tearDownClass(cls) -> None:
        print('tec')

    def setup(self):
        print('setup')
    def teardown(self):
        print('teardown')
    def test_test1(self):
        print(1)
    def piue(self):
        print('11')
    def test_pui(self):
        print('1333')
    def test_c(self):
        self.piue()

if __name__=='__main__':
    unittest.main()
'''
import unittest
from selenium import webdriver
import time
from ddt import ddt, data, unpack



# def readfile():
#     #定义一个list
#     params=[]
#     file=open('pagece.txt','r',encoding='gbk')
#     for line in file.readlines():
#         params.append(line.strip('\n').split(','))
#     return params

# 导入ddt


# 在类前定义使用ddt装饰器，将要使用ddt
@ddt
class forTestTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    @data('软件测试', '张学友', '张国荣', "黄家驹")
    def test_1(self, cc):
        self.driver.find_element_by_id('kw').send_keys(cc)
        self.driver.find_element_by_id('su').click()

    # def test_2(self):
    #     self.driver.find_elemen_by_id('kw').send_key('cc')
    #     self.driver.find_elemen_by_id('su').click()
    # @data(('虚竹', 'cc'), ('测试', "ceshi1"))  # 基于实际使用的数据来使用数据,设定参数
    # @data(*readfile())
    # @unpack  # 解析参数
    # def test_2(self, txt, zuzhu):
    #     print(txt)
    #     print(zuzhu)
    #     print('******************')


if __name__ == '__main__':
    unittest.main(verbosity=2)
