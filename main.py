from expences import add_expense
from storage import load_data
from expences import view_expenses,delete_expense,edit_expense
from report import show_monthly_summary

def show_menu():
    print("\n======Expense Tracker======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Monthly Summary")
    print("6. Exit")


def main():
    expenses = load_data()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            edit_expense(expenses)    
        elif choice == '4':
            delete_expense(expenses)
        elif choice == '5':
            show_monthly_summary(expenses)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
