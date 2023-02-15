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
    """
    check status of one transaction
    :param transaction: dictionary with one client transaction
    :param transaction_type: status we need to find
    :return: True if transaction has status we neeed. False - if not.
    """
    if transaction.get("state") == transaction_type:
        return True
    return False


def get_all_transactions(transactions: list, transaction_type: str) -> list:
    """
    get all transactions with status we need
    :param transactions: all client transactions
    :param transaction_type: type of transactions we need
    :return: all transactions with status we need
    """
    needed_transactions = []
    for transaction in transactions:
        if get_transaction_type(transaction, transaction_type) is True:
            needed_transactions.append(transaction)
    return needed_transactions


def check_account_type(account_description: str) -> bool:
    """
    use in def convert_account_or_card_information. Check what type of transaction we process
    if we find "Счет" - it is mean that we work with account (not cards)
    :param account_description: full description of account
    :return:if we find "Счет" - return True, else - return False
    """
    if "Счет" in account_description:
        return True
    return False


def convert_cart_number(card_info: str) -> str:
    """
    use in def convert_account_or_card_information.Convert card number in needed format
    :param card_info: full card transaction information
    :return: converted card number
    """
    card_description = (card_info.split())[0:-1]
    card_number = (card_info.split())[-1]
    pattern1, pattern2 = r"(^\d{4})(\d{2})(\d{2})(\d{4})(\d{4})", r"\1 \2** **** \5"
    converted_number = re.sub(pattern1, pattern2, card_number)
    all_converted_information = " ".join(card_description), converted_number
    return " ".join(all_converted_information)


def convert_account_number(account_info: str) -> str:
    """
    use in def convert_account_or_card_information.Convert account number in needed format
    :param account_info: full account transaction information
    :return: converted account number
    """
    account_description = (account_info.split())[0:-1]
    account_number = (account_info.split())[-1]
    pattern1, pattern2 = r"(^\d{14})(\d{2})(\d{4})", r"**\3"
    converted_number = re.sub(pattern1, pattern2, account_number)
    all_converted_information = " ".join(account_description), converted_number
    return " ".join(all_converted_information)


def convert_account_or_card_information(full_transaction: str) -> str:
    """
    convert transaction accounts and cards information. if process account - use def convert_account_number,
    if process cards - use convert_cart_number
    :param full_transaction: cart/account full information
    :return: converted cart/account full information
    """
    if check_account_type(full_transaction) is True:
        # process accounts
        return convert_account_number(full_transaction)
    else:
        # process cards numbers
        return convert_cart_number(full_transaction)


def convert_time(full_time: str) -> str:
    """
    convert date to needed format
    :param full_time:
    :return: needed date format
    """
    pattern1, pattern2 = r"(^\d{4})-(\d{2})-(\d{2})(T\S+)", r"\3.\2.\1"
    convert_time = re.sub(pattern1, pattern2, full_time)
    return convert_time


def check_transaction_type(transaction: dict) -> bool:
    """
    check type of transaction
    :param transaction: sorted dictionary
    :return: if type of transaction is "Открытие вклада" return False, else - return True
    """
    if transaction["description"] != "Открытие вклада":
        return True
    return False


def get_operationAmount(transaction: dict) -> str:
    """
    get amount and currency type from dictionary "operationAmount"
    :param transaction: dictionary with all information "operationAmount"
    :return: amount and currency type
    """
    return str(transaction["amount"]) + " " + str(transaction["currency"]["name"])