from datetime import datetime

class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description

    def to_list(self):
        return [self.amount, self.category, self.date, self.description]

    @staticmethod
    def from_list(data):
        return Expense(data[0], data[1], data[2], data[3])