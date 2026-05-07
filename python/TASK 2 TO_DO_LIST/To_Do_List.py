# To-Do List Application

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added successfully!")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Task removed: {removed}")
                else:
                    print("❌ Invalid task number!")

        elif choice == "4":
            print("👋 Exiting To-Do List. Have a productive day!")
            break

        else:
            print("⚠️ Invalid choice! Please try again.")

# Run the program
main()
