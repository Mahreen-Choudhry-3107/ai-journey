# from storage import save_expenses, load_expenses


# def add_expense(expenses):
#     # Add new expense
#     name = input("Enter expense name: ").strip()

#     if not name:
#         print("Expense name cannot be empty.")
#         return

#     try:
#         amount = float(input("Enter amount (Rs.): "))

#         if amount <= 0:
#             print("Amount must be greater than zero.")
#             return

#     except ValueError:
#         print("Invalid amount! Please enter a number.")
#         return

#     expense = {
#         "name": name,
#         "amount": amount
#     }

#     expenses.append(expense)
#     print("Expense added successfully!")
#     return True


# def show_expenses(expenses):
#     # Show all expenses
#     if not expenses:
#         print("No expenses recorded yet.")
#         return

#     print("Expenses:")

#     for index, expense in enumerate(expenses, start=1):
#         print(
#             f"{index}. {expense['name']} - "
#             f"Rs. {expense['amount']:.2f}"
#         )


# def calculate_total(expenses):
#     # Calculate total expenses
#     total = 0

#     for expense in expenses:
#         total += expense["amount"]

#     return total


# def show_highest_expense(expenses):
#     # Display the most expensive item
#     if not expenses:
#         print("No expenses recorded yet.")
#         return

#     highest_expense = expenses[0]

#     for expense in expenses:
#         if expense["amount"] > highest_expense["amount"]:
#             highest_expense = expense

#     print("HIGHEST EXPENSE:")
#     print(f"Name: {highest_expense['name']}")
#     print(f"Amount: Rs. {highest_expense['amount']:.2f}")


# def delete_expense(expenses):
#     # Delete an expense
#     if not expenses:
#         print("No expenses recorded yet.")
#         return False

#     show_expenses(expenses)

#     try:
#         number = int(input("Enter the number of the expense to delete: "))

#         if number < 1 or number > len(expenses):
#             print("Invalid number! Please select a valid expense.")
#             return False

#     except ValueError:
#         print("Invalid input! Please enter a valid number.")
#         return False

#     deleted_expense = expenses.pop(number - 1)

#     print(
#         f"Deleted expense: {deleted_expense['name']} - "
#         f"Rs. {deleted_expense['amount']:.2f}"
#     )

#     return True



# def edit_expense(expenses):
#     if not expenses:
#         print("No expenses to edit.")
#         return False

#     show_expenses(expenses)

#     try:
#         number = int(input("Enter expense number to edit: "))

#         if number < 1 or number > len(expenses):
#             print("Invalid expense number.")
#             return False

#     except ValueError:
#         print("Please enter a valid number.")
#         return False

#     expense = expenses[number - 1]

#     new_name = input(
#         f"Enter new name [{expense['name']}]: "
#     ).strip()

#     if new_name:
#         expense["name"] = new_name

#     new_amount = input(
#         f"Enter new amount [{expense['amount']}]: "
#     ).strip()

#     if new_amount:
#         try:
#             amount = float(new_amount)

#             if amount <= 0:
#                 print("Amount must be greater than zero.")
#                 return False

#             expense["amount"] = amount

#         except ValueError:
#             print("Invalid amount.")
#             return False

#     print("Expense updated successfully!")
#     return True

# def main():
#     expenses = load_expenses()

#     while True:
#         print("\nPersonal Expense Tracker")
#         print("1. Add Expense")
#         print("2. View Expenses")
#         print("3. Calculate Total Expenses")
#         print("4. Show Highest Expense")
#         print("5. Delete Expense")
#         print("6. Edit Expense")
#         print("7. Exit")

#         choice = input("Choose an option (1-7): ").strip()

#         if choice == "1":
#             if add_expense(expenses):
#                 save_expenses(expenses)

#         elif choice == "2":
#             show_expenses(expenses)

#         elif choice == "3":
#             total = calculate_total(expenses)
#             print(f"Total Expenses: Rs. {total:.2f}")

#         elif choice == "4":
#             show_highest_expense(expenses)

#         elif choice == "5":
#             if delete_expense(expenses):
#                 save_expenses(expenses)

#         elif choice == "6":
#             if edit_expense(expenses):
#                 save_expenses(expenses)

#         elif choice == "7":
#             print("Exiting the program. Goodbye!")
#             break

#         else:
#             print("Invalid choice! Please select a valid option.")


# if __name__ == "__main__":
#     main()
