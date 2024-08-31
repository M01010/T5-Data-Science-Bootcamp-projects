from io_functions import load_transactions, dump_transactions
from transaction import UserTransactions


def main():
    transactions = load_transactions()

    user = input('Username: ')
    if user not in transactions:
        transactions[user] = UserTransactions()

    user_transactions = transactions[user]
    user_transactions.main_loop()

    dump_transactions(transactions)


if __name__ == '__main__':
    main()
