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

