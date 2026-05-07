'''An application that allows users to track their
expenses by categorizing them and displaying a summary'''

def expense_tracker():
    expenses = []
    while True:
        action = input("Enter 'add', 'view', or 'exit': ")
        if action == 'add':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            expenses.append({'category': category, 'amount': amount, 'description': description})
        elif action == 'view':
            total = sum(exp['amount'] for exp in expenses)
            print(f"Total Expenses: {total}")
            for exp in expenses:
                print(exp)
        elif action == 'exit':
            break
        else:
            print("Invalid input.")

expense_tracker()