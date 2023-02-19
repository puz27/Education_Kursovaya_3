from utils.utils import get_transaction_type


class ClientOperations:


    def __init__(self, transactions: list) -> None:
        self.__transactions = transactions
        self.__needed_transactions = []


    def get_need_transactions(self, transaction_status: str, amount_day: int) -> list:
        """
        get information about transactions for period with status we need
        :param transaction_status: status we need to find
        :param amount_day: count of days we need
        :return: list of sorted transactions
        """
        for transaction in self.__transactions:
            if get_transaction_type(transaction, transaction_status) is True:
                self.__needed_transactions.append(transaction)

        sorted_transactions = sorted(self.__needed_transactions, key=lambda transaction: transaction["date"], reverse=True)
        return sorted_transactions[0:amount_day]





