import json
import os
from logic.dates import current_year, current_month_day


class ExpenseLogic:
    def __init__(self, file_name="expenses.json"):
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)
        self.file_path = os.path.join(self.data_dir, file_name)

        self.expenses = {}
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.expenses = json.load(f)

    def save_expenses(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.expenses, f, ensure_ascii=False, indent=4)

    def ensure_path(self, year, expense_name, day_key, list_name):
        # שנה
        self.expenses.setdefault(year, {})
        # קטגוריה
        self.expenses[year].setdefault(expense_name, {})
        # תאריך
        self.expenses[year][expense_name].setdefault(day_key, {})
        # list_name
        self.expenses[year][expense_name][day_key].setdefault(
            list_name, {"money": {}, "card": {}}
        )

    def create_expense(self, expense_name, list_name):
        year = str(current_year())
        day_key = current_month_day()

        self.ensure_path(year, expense_name, day_key, list_name)
        self.save_expenses()
        return year, expense_name, day_key, list_name

    def add_item(self, expense_name, list_name, item, amount, payment_type="money"):
        year = str(current_year())
        day_key = current_month_day()

        self.ensure_path(year, expense_name, day_key, list_name)
        self.expenses[year][expense_name][day_key][list_name][payment_type][item] = amount
        self.save_expenses()
        return year, day_key
    
    def total_for_month(self, year, month):
        total = 0.0
        for expense in self.expenses.get(year, {}).values():
            for day, lists in expense.items():
                if day.startswith(f"{month:02d}-"):
                    for lst in lists.values():
                        for pay in ("money", "card"):
                            total += sum(map(float, lst[pay].values()))
        return total
