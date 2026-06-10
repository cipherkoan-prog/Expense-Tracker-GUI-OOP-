
class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }