import json
import os

test_dict = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}

def load_data(file_name: str) -> list:
    """
    load data from local file
    :param file_name: name of import file
    :return: list of dictionaries
    """
    path_file = os.path.join(os.getcwd(), "data", file_name)

    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data

def check_executed_transaction(transaction: dict) -> bool:
    if transaction.get("state") == "EXECUTED":
        return True
    return False

data = load_data("operations.json")


def get_all_executed_transactions(transactions: list) -> list:
    all_executed_transactions = []
    for transaction in transactions:
        if check_executed_transaction(transaction) is True:
            all_executed_transactions.append(transaction)
    return all_executed_transactions

data_executed = get_all_executed_transactions(data)


import re
# - Номер карты замаскирован и не отображаться целиком,
# в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом)
# - Номер счета замаскирован и не отображаться целиком, в формате  **XXXX
# (видны только последние 4 цифры номера счета)

card = "MasterCard 7158300734726758"
account = ("Счет 35383033474447895560".split())[1]

def convert_cart_number(card_info: str) -> tuple:
    card_name = (card_info.split())[0]
    card_number = (card_info.split())[1]
    pattern1, pattern2 = r"(^\d{4})(\d{2})(\d{2})(\d{4})(\d{4})", r"\1 \2** **** \5"
    converted_number = re.sub(pattern1, pattern2, card_number)
    return card_name, converted_number

def convert_account_number(account_number: str) -> str:
    pattern1, pattern2 = r"(^\d{14})(\d{2})(\d{4})", r"**\3"
    converted_account = re.sub(pattern1, pattern2, account_number)
    return converted_account

def convert_time(full_time: str) -> str:
    pattern1, pattern2 = r"(^\d{4})-(\d{2})-(\d{2})(T\S+)", r"\3.\2.\1"
    convert_time = re.sub(pattern1, pattern2, full_time)
    return convert_time



class Operation:

    def __init__(self, id: int, state: str, data: str, operation_amount: dict, description: str, from_whom: str,
                 to_who: str):
        self.id = id
        self.state = state
        self.data = data
        self.operational_amount = operation_amount
        self.description = description
        self.from_whom = from_whom
        self.to_who = to_who


    def get_state(self):
        return self.state

    def get_date(self):
        return self.data

    def get_direction(self):
        return self.from_whom, self.to_who

    def get_operationamount(self):
        return self.operational_amount










