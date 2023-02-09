from classes import *
import unittest
from unittest import TestCase

class Test(unittest.TestCase):

    def test_convert_time(self):
        test_case = "2019-08-26T10:50:58.294041"
        expected = "26.08.2019"
        self.assertEqual(convert_time(test_case), expected)
