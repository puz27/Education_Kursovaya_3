from utils import *
import unittest


class Test(unittest.TestCase):


    def test_get_transaction_type(self):
        test_case_1 = {"id": 801684332, "state": "EXECUTED"}
        test_case_2 = "EXECUTED"
        self.assertTrue(get_transaction_type(test_case_1, test_case_2))


    def test_get_all_transactions(self):
        test_case_1 = [
                        {"id": 154927927, "state": "EXECUTED", "date": "2019-11-19T09:22:25.899614"},
                        {"id": 743628025, "state": "CANCELED", "date": "2018-06-04T06:59:55.424356"}
                    ]
        test_case_2 = "CANCELED"
        expected = {"id": 743628025, "state": "CANCELED", "date": "2018-06-04T06:59:55.424356"}
        self.assertTrue(get_all_transactions(test_case_1, test_case_2), expected)


    def test_check_account_type(self):
        test_case = "Счет для тестирования"
        self.assertTrue(check_account_type(test_case))


    def test_convert_cart_number(self):
        test_case = "Visa Platinum 1813166339376336"
        expected = "Visa Platinum 1813 16** **** 6336"
        self.assertEqual(convert_cart_number(test_case), expected)


    def test_convert_account_number(self):
        test_case = "Счет 97848259954268659635"
        expected = "Счет **9635"
        self.assertEqual(convert_account_number(test_case), expected)


    def test_convert_account_or_card_information(self):
        test_case = "Visa Classic 4040551273087672"
        expected = "Visa Classic 4040 55** **** 7672"
        self.assertEqual(convert_account_or_card_information(test_case), expected)


    def test_convert_time(self):
        test_case = "2019-08-26T10:50:58.294041"
        expected = "26.08.2019"
        self.assertEqual(convert_time(test_case), expected)


    def test_check_transaction_type(self):
        test_case = {"id": 108066781, "state": "EXECUTED", "date": "2019-06-21T12:34:06.351022",
                     "operationAmount": {"amount": "25762.92", "currency": {"name": "руб.", "code": "RUB"}},
                     "description": "Открытие вклада", "to": "Счет 90817634362091276762"}
        self.assertFalse(check_transaction_type(test_case))


    def test_get_operationAmount(self):
        test_case = {"amount": "25762.92", "currency": {"name": "руб.", "code": "RUB"}}
        expected = "25762.92 руб."
        self.assertEqual(get_operationAmount(test_case), expected)
