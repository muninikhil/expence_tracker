
from storage import save_data
from validation import get_amount, get_date, get_int


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

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"{'ID':<5} {'Amount':<10} {'Category':<15} {'Date':<12} {'Description'}")
    print("-" * 60)
    for e in  sorted(expenses, key=lambda x: x['date']):
        print(f"{e['id']:<5} {e['amount']:<10.2f} {e['category']:<15} {e['date']:<12} {e['description']}")
    total=sum(e['amount'] for e in expenses)
    print("-" * 60)
    print(f"{'Total':<33} {total:<10.2f}")

def find_expense(expenses, expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense
    return None

def delete_expense(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    view_expenses(expenses)
    expense_id=get_int("Enter the ID of the expense to delete:")
    expense=find_expense(expenses,expense_id)
    if expense is None:
        print(f"No expense found with ID {expense_id}.")
        return
    answer=input(f"Are you sure you want to delete the expense with ID {expense_id}? (y/n):").strip().lower()
    if answer=="y":
        expenses.remove(expense)
        save_data(expenses)
        print("Expense deleted successfully!")
    else:
        print("Deletion canceled.")


def edit_expense(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    view_expenses(expenses)
    expense=find_expense(expenses,get_int("Enter the ID of the expense to edit:"))
    if expense is None:
        print("Expense not found.")
        return
    print("press enter to keep the current value.")
    new_amount=input(f"Amount({expense['amount']})").strip()
    if new_amount:
        try:
            value=float(new_amount)
            if value>0:
                expense['amount']=round(value,2)
            else:
                print("Amount must be a positive number. Keeping the current value.")   
        except ValueError:
            print("Invalid amount. Keeping the current value.")

    print("choose a new category or press enter to keep the current value.")
    for number,name in enumerate(CATEGORIES,start=1):
        print(f"{number}. {name}")
    new_category=input(f"Category({expense['category']})").strip()
    if new_category:
        if new_category.isdigit() and 1 <= int(new_category) <= len(CATEGORIES):
            expense['category']=CATEGORIES[int(new_category) - 1] 
        else:
            print("Invalid category. Keeping the current value.")
    print("enter a new date in YYYY-MM-DD format or press enter to keep the current value.")
    new_date=get_date(f"Date({expense['date']})" ,allow_blank=True)
    if new_date:
        expense['date']=new_date    
    print("enter a new description or press enter to keep the current value.")
    new_description=input(f"Description({expense['description']})").strip()
    if new_description:
        expense['description']=new_description

        save_data(expenses)
        print("Expense updated successfully!")