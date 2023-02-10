from utils import *
class ClientOperations:

    def __init__(self, transactions: list) -> None:
        self.transactions = transactions
        self.needed_transactions = []


    def get_all_transactions(self, transaction_type: str) -> list:
        self.needed_transactions = []
        for transaction in self.transactions:
            if get_transaction_type(transaction, transaction_type) is True:
                self.needed_transactions.append(transaction)
        return self.needed_transactions



my_client = ClientOperations(data)
print(my_client.get_all_transactions("CANCELED"))


