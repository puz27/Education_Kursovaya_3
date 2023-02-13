from utils import *
import unittest


class Test(unittest.TestCase):


    def test_convert_time(self):
        test_case = "2019-08-26T10:50:58.294041"
        expected = "26.08.2019"
        self.assertEqual(convert_time(test_case), expected)


    def test_convert_cart_number(self):
        test_case = "Visa Platinum 1813166339376336"
        expected = "Visa Platinum 1813 16** **** 6336"
        self.assertEqual(convert_cart_number(test_case), expected)


    def test_convert_account_number(self):
        test_case = "Счет 97848259954268659635"
        expected = "Счет **9635"
        self.assertEqual(convert_account_number(test_case), expected)