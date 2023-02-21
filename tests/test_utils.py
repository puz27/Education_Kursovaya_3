from src.utils import *
import pytest


@pytest.fixture()
def card_visa():
    return "Visa Platinum 1813166339376336"


@pytest.fixture()
def account():
    return "Счет 97848259954268659635"


def test_get_transaction_type():
    test_case_1 = {"id": 801684332, "state": "EXECUTED"}
    test_case_2 = "EXECUTED"
    assert(get_transaction_type(test_case_1, test_case_2)) is True


def test_get_all_transactions():
    test_case_1 = [
        {"id": 154927927, "state": "EXECUTED", "date": "2019-11-19T09:22:25.899614"},
        {"id": 743628025, "state": "CANCELED", "date": "2018-06-04T06:59:55.424356"}
    ]
    test_case_2 = "CANCELED"
    expected = {"id": 743628025, "state": "CANCELED", "date": "2018-06-04T06:59:55.424356"}
    assert(get_all_transactions(test_case_1, test_case_2)) == [expected]


def test_check_account_type(account, card_visa):
    assert(check_account_type(account)) is True
    assert (check_account_type(card_visa)) is False


def test_convert_cart_number(card_visa):
    expected = "Visa Platinum 1813 16** **** 6336"
    assert(convert_cart_number(card_visa)) == expected


def test_convert_account_number(account):
    expected = "Счет **9635"
    assert(convert_account_number(account)) == expected


def test_convert_account_or_card_information(card_visa):
    expected = "Visa Platinum 1813 16** **** 6336"
    assert(convert_account_or_card_information(card_visa)) == expected


def test_convert_time():
    test_case = "2019-08-26T10:50:58.294041"
    expected = "26.08.2019"
    assert(convert_time(test_case)) == expected


def test_check_transaction_type():
    test_case = {"id": 108066781, "state": "EXECUTED", "date": "2019-06-21T12:34:06.351022",
                 "operationAmount": {"amount": "25762.92", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Открытие вклада", "to": "Счет 90817634362091276762"}
    assert(check_transaction_type(test_case)) is False


def test_get_operationAmount():
    test_case = {"amount": "25762.92", "currency": {"name": "руб.", "code": "RUB"}}
    expected = "25762.92 руб."
    assert(get_operationAmount(test_case)) == expected


def test_process_transactions(capsys):
    test_case = [{"id": 108066781, "state": "EXECUTED", "date": "2019-06-21T12:34:06.351022",
                  "operationAmount": {"amount": "25762.92", "currency": {"name": "руб.", "code": "RUB"}},
                  "description": "Открытие вклада", "to": "Счет 90817634362091276762"}]
    expected = "21.06.2019 Открытие вклада Счет **6762\n"
    process_transactions(test_case)
    captured = capsys.readouterr()
    assert captured.out == expected
