#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from function import multiply

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data_1 = 20
        data_2 = 30
        result = multiply(data1, data2)
        self.assertEqual(result, 6)
        
        data_3 = 1
        data_4 = 5
        result = multiply(data3, data4)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main() 
