# Creta an empty list to store the tasks and their Status
todo_list = []

# Function to add a new task
def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status":"pending"})
    print("New Task Added Successfully!\n")
    
    
# Function to view All Tasks
def view_task():
    print("Your Todo List: ")
    if len(todo_list) == 0:
        print("No pending tasks!\n")
    else:
          for index, task in enumerate(todo_list, 1):
              print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")

# Function to Remove a Task
def remove_task():
    if len(todo_list) == 0:
        print("List is Empty!\n")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}\n")
            else:
                print("Invalid Task Number.\n")
        except ValueError:
            print("Please Enter a Valid Task Number.\n")
            
# Function to Mark a Task as Done
def mark_done():
    if len(todo_list) == 0:
        print("List is Empty!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to Mark as Complete: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"Task {todo_list[search_index]['Task']} has been marked as Done.\n")
            else:
                print("Invalid Task Number.\n")
        except ValueError:
            print("Please Enter a Valid Task Number.\n")
    
    

#Function to Display a Menu
def menu():
    while(True):
        print("**** To-Do list ****")
        print("1. Add a New Tasks")
        print("2. View All Tasks")
        print("3. Remove a Tasks")
        print("4. Mark a Task as Completed")
        print("5. Exit")
        
        
        Choice = input("Enter Your Choice : ")
        if Choice == "1":
            add_task()
        elif Choice == "2":
            view_task();
        elif Choice == "3":
            remove_task()
        elif Choice == "4":
            mark_done()
        elif Choice == "5":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice! Try Again!!!\n")
            
menu()