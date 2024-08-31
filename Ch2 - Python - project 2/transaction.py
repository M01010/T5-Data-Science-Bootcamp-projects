from dataclasses import dataclass
import datetime
from typing import Callable
from category import Category, get_category


def get_date() -> datetime.date:
    t_date_str = input('date (mm/dd/yyyy): ')
    t_date_split = t_date_str.split('/')
    t_date_split = [int(x) for x in t_date_split]
    t_date = datetime.date(month=t_date_split[0], day=t_date_split[1], year=t_date_split[2])
    return t_date


@dataclass
class Transaction:
    id: str
    amount: float
    category: Category
    date: datetime.date

    def __json__(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category.name,
            'date': self.date.isoformat()
        }

    def __repr__(self):
        return f'id: {self.id}, amount: {self.amount}, category: {self.category.name}, date: {self.date}'


class UserTransactions:
    def __init__(self, transactions: dict[str, Transaction] = None):
        if transactions is None:
            self.transactions: dict[str, Transaction] = {}
        else:
            self.transactions = transactions

    def __json__(self):
        return {k: v.__json__() for k, v in self.transactions.items()}

    def view_transactions(self, sorted_by: Callable):
        temp_list = sorted(self.transactions.values(), key=sorted_by)
        for t in temp_list:
            print(t)

    def add_transaction(self):
        try:
            t_id = input('ID: ')
            if t_id in self.transactions:
                print('id already exists')
                return
            t_amount = float(input('amount: '))
            t_category = get_category()
            t_date = get_date()
            t = Transaction(t_id, t_amount, t_category, t_date)
            self.transactions[t_id] = t
        except Exception as e:
            print(e)

    def update_transaction(self):
        try:
            t_id = input('ID: ')
            if t_id not in self.transactions:
                print('no transaction found')
                return
            transaction = self.transactions[t_id]
            print(transaction)
            print('options = [amount, category, date]')
            choice = input('choice: ')
            match choice:
                case 'amount':
                    amount = float(input('amount: '))
                    transaction.amount = amount
                case 'category':
                    category = get_category()
                    transaction.category = category
                case 'date':
                    date = get_date()
                    transaction.date = date
                case _:
                    print('unknown option')
        except Exception as e:
            print(e)

    def delete_transaction(self):
        t_id = input('ID: ')
        if t_id in self.transactions:
            self.transactions.pop(t_id)
            print('transaction deleted')
        else:
            print('no transaction found')

    def view_reports(self):
        print('options: [expense, income, total category, average category]')
        choice = input('choice: ')
        match choice:
            case 'expense':
                expenses = [x.amount for x in self.transactions.values() if x.category != Category.Salary]
                print(f'Total expenses: {sum(expenses)}')
            case 'income':
                salaries = [x.amount for x in self.transactions.values() if x.category == Category.Salary]
                print(f'Total income: {sum(salaries)}')
            case 'total category':
                for key, c in Category.get_map().items():
                    filtered = [x.amount for x in self.transactions.values() if x.category == c]
                    print(f'Total expenses for {key}: {sum(filtered)}')
            case 'average category':
                for key, c in Category.get_map().items():
                    filtered = [x.amount for x in self.transactions.values() if x.category == c]
                    total = sum(filtered)
                    n = len(filtered)
                    if n == 0:
                        avg = 0
                    else:
                        avg = total / n
                    print(f'Average expenses for {key}: {avg}')
            case _:
                print('unknown option')

    def main_loop(self):
        while True:
            print('Options: [add, view date, view category, update, delete, report, exit]')
            choice = input('Choice: ')
            match choice:
                case 'add':
                    self.add_transaction()
                case 'view date':
                    self.view_transactions(lambda x: x.date)
                case 'view category':
                    self.view_transactions(lambda x: x.category.value)
                case 'update':
                    self.update_transaction()
                case 'delete':
                    self.delete_transaction()
                case 'report':
                    self.view_reports()
                case 'exit':
                    break
                case _:
                    print('incorrect input')
