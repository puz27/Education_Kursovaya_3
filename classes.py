from utils import *
class ClientOperations:

    def __init__(self, transactions: list) -> None:
        self.__transactions = transactions
        self.__needed_transactions = []


    def get_need_transactions(self, transaction_status: str, amount_day: int) -> list:
        self.needed_transactions = []
        for transaction in self.__transactions:
            if get_transaction_type(transaction, transaction_status) is True:
                self.needed_transactions.append(transaction)

        sorted_transactions = sorted(self.needed_transactions, key=lambda transaction: transaction["date"], reverse=True)
        return sorted_transactions[0:amount_day]

client = ClientOperations(data)
# print(my_client.get_need_transactions("EXECUTED", 3))

for transaction in client.get_need_transactions("EXECUTED", 5):
    if check_transaction_type(transaction) is True:
        print(convert_time(transaction["date"]), get_operationAmount(transaction["operationAmount"]),
              transaction["description"], convert_account_or_card_information(transaction["from"]), "-->",
              convert_account_or_card_information(transaction["to"]))
    else:
        print(convert_time(transaction["date"]), get_operationAmount(transaction["operationAmount"]),
              transaction["description"], convert_account_or_card_information(transaction["to"]))




