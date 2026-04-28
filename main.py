from manager import FinanceManager
from expense import Expense
from datetime import datetime

def get_valid_amount():
    while True:
        try:
            return float(input("Enter amount: ₹"))
        except ValueError:
            print("Invalid amount. Try again.")

def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format.")

def main():
    manager = FinanceManager()

    while True:
        print("\n==== Personal Finance Manager ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            amount = get_valid_amount()
            category = input("Enter category: ")
            date = get_valid_date()
            description = input("Enter description: ")

            expense = Expense(amount, category, date, description)
            manager.add_expense(expense)
            print("Expense added successfully!")

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            print("Total spent: ₹", manager.total_spent())

        elif choice == "4":
            summary = manager.category_summary()
            for cat, amt in summary.items():
                print(f"{cat}: ₹{amt}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()