
# coding=utf-8
import unittest
from selenium import webdriver
import time
from ddt import data, unpack, ddt


# 使用ddt在类前
@ddt
class catTest(unittest.TestCase):
    # 类的初始化
    @classmethod
    def setUpClass(cls):
        print('setupclass')

    # 类的释放
    @classmethod
    def tearDownClass(cls):
        print('teardown')

    # 用例的初始化
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

    # 用例的环境释放
    def tearDown(self):
        self.driver.back()
        time.sleep(5)

        self.driver.quit()

    # ddt的数据添加循环使用
    @data(('软件测试', '自动化框架'), ('设置语言', '测试入门'))
    @unpack
    def test_cs1(self, cc, dd):
        self.driver.find_element_by_id('kw').send_keys(cc, dd)
        self.driver.find_element_by_id('su').click()
        self.driver.find_element_by_id('u').click()
        time.sleep(5)

        # self.driver.titlee
        # return self.driver.title
    # def test_cs2(self, ):
    #     self.driver.find_element_by_id('kw').send_keys('问题')
    #     self.driver.find_element_by_id('su').click()
    #
    # def test_cs3(self, ):
    #     self.driver.find_element_by_id('kw').send_keys('自动化')
    #     self.driver.find_element_by_id('su').click()
    #
    # def test_cs4(self, ):
    #     self.driver.find_element_by_id('kw').send_keys('测试')
    #     self.driver.find_element_by_id('su').click()
    # def test_cs2(self,cc):
    #     print(cc)
    # def test_cs3(self,dd):
    #     print(dd)


if __name__ == "__main__":
    unittest.main(verbosity=2)