from utils.classes import ClientOperations
from utils.utils import *


def main():
    # load data
    data = load_data("operations.json")

    # create instance with all clients transactions
    client_transactions = ClientOperations(data)

    # process clients transactions with needed status and counts. and print
    process_transactions(client_transactions.get_need_transactions("EXECUTED", 5))


if __name__ == '__main__':
    main()
