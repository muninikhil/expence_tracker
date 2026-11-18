def show_menu():
    print("\n======Expense Tracker======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. monthly Summary")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("add expense --coming soon")
        elif choice == '2':
            print("view expense --coming soon")
        elif choice == '3':
            print("edit expense --coming soon")     
        elif choice == '4':
            print("delete expense --coming soon")
        elif choice == '5':
            print("monthly summary --coming soon")
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
