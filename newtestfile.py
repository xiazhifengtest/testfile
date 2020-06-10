# import requests as r
#
#
# url='https://www.zigeer.com/'
# b=r.get(url=url,verify=False)
# b.encoding='utf-8'
# print(type(b))
# print(b.text)
# print(b.encoding)
# c=1
# print(c)
# print('c')
# message=' /1hello_ world'
# print(message)
# bicyles=['trke','can','read','specy']
# print(bicyles[0])
# print(bicyles[2])
# import unittest
# import requests
# import json
#
#
# class test_name(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def test_name(self):
#         self.url = 'http://122.51.222.42'
#         res = requests.get(url=self.url, verify=False)
#         print(type(res.text))
#         print(res.text)
#
#         # con = json.loads(res.text)
#         # print(con['msg'])
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

import requests


# res = requests.get('https://httpbin.org/get', params={'name': 'xia', 'age': '18'})
# print('状态码', res.status_code)
# print('相应文本', res.text)
# print('响应投', res.headers)
# print('相应文本转为字典',res.json())
# url = 'https://httpbin.org/get'
# url_params = {'name': 'xia', 'age': '18'}
# res = requests.get(url=url, params=url_params)
# try:
#     print('响应文本转为字典', res.json())
# except:
#     print('响应文本', res.text)
# import requests
# url = 'https://www.jianshu.com/shakespeare/v2/notes/9d3f991c901a/book'
# headers = {
#     'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
#     'referer': 'https://www.jianshu.com/p/9d3f991c901a',
# }
# cookies = {'Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068': '1579601795',
#  'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068': '1579573487,1579587460,1579591333,1579591335',
#  '__yadk_uid': 'ratDswBmN3Kzid42v2gKV2q8veUvOsEd',
#  '_m7e_session_core': 'd0065296a1834086d0279a548d932927',
#  'default_font': 'font2',
#  'locale': 'zh-CN',
#  'read_mode': 'day',
#  'remember_user_token': 'W1s3NTc1NzIxXSwiJDJhJDExJFRVVTNvMlV6NjJaVTlXZjF0YWFuZi4iLCIxNTc5NTczNDg1Ljk2MzgyODYiXQ%3D%3D--feb4c1d88427a88d7321791daf2d76f7b11ed4b3',
#  'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221697595f5777a9-0a3caa4a8cc382-36667905-1024000-1697595f578430%22%2C%22%24device_id%22%3A%221697595f5777a9-0a3caa4a8cc382-36667905-1024000-1697595f578430%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22weixin-friends%22%2C%22%24latest_utm_medium%22%3A%22reader_share%22%2C%22%24latest_utm_campaign%22%3A%22hugo%22%2C%22%24latest_utm_content%22%3A%22note%22%7D%2C%22first_id%22%3A%22%22%7D'
# }
#
# res = requests.get(url, headers=headers, cookies=cookies)
# print(res.text)
# for i in range(5):
#     print(i,end=' ')
#     if i ==1 :
#         continue
#     else:
#         print('end')


import httprunner
import locust
