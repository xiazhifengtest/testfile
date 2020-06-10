import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能否正确处理John philiph这类名'''
        formatted_name=get_formatted_name('xia','zhifeng')
        self.assertEqual(formatted_name,'Xiazhifeng')

    def test_first_last_middle(self):
        '''正确处理带中间名'''
        formatted_name=get_formatted_name(
            'xia','feng','zhi'
        )
        self.assertEqual(formatted_name,'Xiazhifeng')

if __name__=='__main__':
    unittest.main()


