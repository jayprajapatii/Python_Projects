'''A simple console application to manage a to-do list,
allowing users to add, view, and delete tasks'''
def todo_list():
    tasks = []
    while True:
        action = input("Enter 'add', 'view', 'delete', or 'exit': ")
        if action == 'add':
            task = input("Enter a task: ")
            tasks.append(task)
        elif action == 'view':
            print("Tasks:", tasks)
        elif action == 'delete':
            task = input("Enter a task to delete: ")
            tasks.remove(task) if task in tasks else print("Task not found.")
        elif action == 'exit':
            break
        else:
            print("Invalid input.")

todo_list()