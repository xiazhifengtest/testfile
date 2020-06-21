# encoding=utf-8
import unittest
from fortest3 import *
from HTMLTestReportCN import HTMLTestRunner
import os

# 创建空的集合list
suite = unittest.TestSuite()

# 添加测试用例到测试套件
# suite.addTest(forTestTest('test_1'))
# suite.addTest(forTestTest('test_3'))
# suite.addTest(forTestTest('test_2'))
#
# case=[forTestTest('test_2'),forTestTest('test_1'),forTestTest('test_3')]
# suite.addTests(case)
# test_dir='./'
# discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='forte*.py')

# suite.addTests(unittest.TestLoader().loadTestsFromTestCase('fortest3.forTestTest'))
# suite.addTests(unittest.TestLoader().loadTestsFromName('fortest3.forTestTest'))


report_path = './report/'
report_file = report_path + 'report.html'
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
with open(report_file, 'wb')as report:
    suite.addTests(unittest.TestLoader().loadTestsFromName('fortest3.forTestTest'))
    suite.addTest(unittest.TestLoader().loadTestsFromName('fortest1.catTest'))

    runner = HTMLTestRunner(stream=report, title='测试报告', description='下旨封')
    runner.run(suite)
report.close()

# 套件通过调用Texttestrunner对象运行
# runner=unittest.TextTestRunner()
# runner.run(suite)
