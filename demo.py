# coding:utf-8
import requests
import unittest
import json


class catTest(unittest.TestCase):

    def test_1(self):
        self.url = 'http://www.baidu.com'
        # self.param = {'': '', '': ''}
        res = requests.get(url=self.url)
        print(type(res.text))
        con = json.loads(res.text)
        print(con['msg'])
