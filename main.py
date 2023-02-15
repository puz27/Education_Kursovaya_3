# if __name__ == '__main__':
#     print('PyCharm')
from classes import ClientOperations
from utils import *

# load data
data = load_data("operations.json")

# create instance with all clients transactions
client_transactions = ClientOperations(data)

# process clients transactions with needed status and counts
for transaction in client_transactions.get_need_transactions("EXECUTED", 5):
    # check type of transaction
    if check_transaction_type(transaction) is True:
        # process transaction: "Переводы"
        print(convert_time(transaction["date"]),
              transaction["description"],
              convert_account_or_card_information(transaction["from"]), "-->",
              convert_account_or_card_information(transaction["to"]),
              get_operationAmount(transaction["operationAmount"]))
    else:
        # process transaction: "Открытие вклада"
        print(convert_time(transaction["date"]),
              transaction["description"],
              convert_account_or_card_information(transaction["to"]))