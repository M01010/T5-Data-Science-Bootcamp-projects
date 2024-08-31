import datetime
import os.path
import json

from category import Category
from transaction import Transaction, UserTransactions

JSON_PATH = os.path.abspath('data.json')


def load_transactions() -> dict[str, UserTransactions]:
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
            res = {k: user_transaction_from_json(v) for k, v in data.items()}
            return res
    return {}


def dump_transactions(data):
    dir_name = os.path.dirname(JSON_PATH)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(JSON_PATH, 'w') as f:
        json_data = {k: v.__json__() for k, v in data.items()}
        json.dump(json_data, f, indent=True)


def transaction_from_json(data) -> Transaction:
    t_id = data['id']
    t_amount = data['amount']
    t_category = data['category']
    t_category = Category.get_map()[t_category.lower()]
    t_date = data['date']
    t_date = datetime.date.fromisoformat(t_date)
    return Transaction(t_id, t_amount, t_category, t_date)


def user_transaction_from_json(data) -> UserTransactions:
    return UserTransactions({k: transaction_from_json(v) for k, v in data.items()})
