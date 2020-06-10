# file=open('a.yml,encoding=utf-8')
# res=yaml.load(file,load=yaml.FUlLodaer)
# print(res)
import unittest
from selenium import webdriver
import time
from ddt import ddt, data, unpack


# skip用法通过装饰器,无条件跳过
# @unittest.skip('无理由跳过')
# @unittest.skipif(1 < 2, '当满足条件时运行')
# @unittest.skipUnless(1 < 2, '当不满足条件运行')
# @unittest.expectedFailure#使用保存当该用例不存在
class forTestTest(unittest.TestCase):
    # @unittest.skip('无理由跳过')
    def test_1(self):
        print('1')
        self.assertAlmostEqual(4, 3, msg='返回错误')

    # @unittest.skipIf(1 < 2, '当满足条件时运行')
    def test_2(self):
        print('2')

    # @unittest.skipUnless(1 < 2, '当不满足条件运行')
    def test_3(self):
        print('3')

    # @unittest.expectedFailure#用例执行错误不计入
    def test_4(self):
        print('4')

if __name__=='__main__':
    unittest.main()


