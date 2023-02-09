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





