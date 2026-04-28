import csv
import os
from expense import Expense

FILE_NAME = "expenses.csv"

class FinanceManager:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(FILE_NAME):
            return
        try:
            with open(FILE_NAME, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        self.expenses.append(Expense.from_list(row))
        except Exception as e:
            print("Error loading file:", e)

    def save_expenses(self):
        try:
            with open(FILE_NAME, mode='w', newline='') as file:
                writer = csv.writer(file)
                for expense in self.expenses:
                    writer.writerow(expense.to_list())
        except Exception as e:
            print("Error saving file:", e)

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        for exp in self.expenses:
            print(f"{exp.date} | {exp.category} | ₹{exp.amount} | {exp.description}")

    def total_spent(self):
        return sum(exp.amount for exp in self.expenses)

    def category_summary(self):
        summary = {}
        for exp in self.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount
        return summary