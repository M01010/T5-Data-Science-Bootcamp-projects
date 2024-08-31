from enum import Enum, auto


class Category(Enum):
    Food = auto()
    Transportation = auto()
    Entertainment = auto()
    Salary = auto()
    Other = auto()

    @classmethod
    def get_map(cls):
        return {
            'food': Category.Food,
            'transportation': Category.Transportation,
            'entertainment': Category.Entertainment,
            'salary': Category.Salary,
            'other': Category.Other
        }


def get_category() -> Category:
    cat_map = Category.get_map()
    print(f'options: {list(cat_map.keys())}')
    t_category = input('Category: ')
    if t_category in cat_map:
        return cat_map[t_category]
    return Category.Other
