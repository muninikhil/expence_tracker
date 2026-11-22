from storage import save_data
from validation import get_amount, get_date

CATEGORIES = ["Food", "Transportation", "Rent", "Shopping", "Bills", "Health", "Entertainment","Other"]

def get_id(expences):
    if not expences:
        return 1
    return max(e["id"] for e in expences)+1

def choose_category():
    print("choose a category:\n")
    for number,name in enumerate(CATEGORIES,start=1):
        print(f"{number}. {name}")
    while True:
        try:
            choice = input("enter the number of the category:").strip()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice. Please select a valid category number.")

def add_expense(expenses):
    amount=get_amount()
    category=choose_category()
    date=get_date()
    description=input("enter a description(optional):").strip()

    expense={
        "id":get_id(expenses),
        "amount":amount,
        "category":category,
        "date":date,
        "description":description
    }
    expenses.append(expense)
    save_data(expenses)
    print("Expense added successfully!")