import json
from datetime import datetime

FILE = "expenses.json"

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except:
            return []

    def save_expenses(self):
        with open(FILE, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, category, note):
        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("✅ Expense added")

    def show_expenses(self):
        for e in self.expenses:
            print(e)

    def category_summary(self):
        summary = {}
        for e in self.expenses:
            summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

        for cat, total in summary.items():
            print(f"{cat}: ₹{total}")

tracker = ExpenseTracker()

while True:
    print("\n1. Add Expenses:\n2. View Expenses:\n3. Category Summary:\n4. Exit :")
    choice = input("Choose: ")

    if choice == "1":
        amt = float(input("Amount: "))
        cat = input("Category: ")
        note = input("Note: ")
        tracker.add_expense(amt, cat, note)

    elif choice == "2":
        tracker.show_expenses()

    elif choice == "3":
        tracker.category_summary()

    elif choice == "4":
        break
