import json
import os
import re


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


def get_transaction_type(transaction: dict, transaction_type: str) -> bool:
    if transaction.get("state") == transaction_type:
        return True
    return False

data = load_data("operations.json")


def get_all_transactions(transactions: list, transaction_type: str) -> list:
    needed_transactions = []

    for transaction in transactions:
        if get_transaction_type(transaction, transaction_type) is True:
            needed_transactions.append(transaction)
    return needed_transactions


sorted_needed_transactions = (get_all_transactions(data, "EXECUTED"))


def get_last_transactions(transactions: list, amount_day: int):
    sorted_transactions = sorted(transactions, key=lambda transaction: transaction["date"], reverse=True)
    return sorted_transactions[0:amount_day]
#
#print(get_last_transactions(sorted_needed_transactions, 5))

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


