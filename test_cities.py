import unittest
from city_function import get_cityname

class NameTestCase(unittest.TestCase):
    def test_city_country(self):
        coun_name=get_cityname('beijing','china')
        self.assertEqual(coun_name,'Beijingchina')

if __name__=='__main__':
    unittest.main()