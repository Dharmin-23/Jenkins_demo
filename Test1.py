#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from function import multiply

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data1 = 20
        data2 = 30
        result = multiply(data1, data2)
        self.assertEqual(result, 600)
        
        data3 = 1
        data4 = 5
        result = multiply(data3, data4)
        self.assertEqual(result, 5)
        
        data5 = 19
        data6 = 10
        result = multiply(data5, data6)
        self.assertEqual(result, 190)

if __name__ == '__main__':
    unittest.main() 
