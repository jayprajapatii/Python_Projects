import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Employee Management System")
root.geometry("800x500")
root.resizable(False, False)

employees = []  # List to store employee records (can be replaced with DB later)

# ---------------- Employee Information Frame ----------------
frame_info = tk.LabelFrame(root, text="Employee Information", padx=20, pady=10)
frame_info.pack(fill="x", padx=20, pady=10)

# Labels and Entries
tk.Label(frame_info, text="Employee ID:").grid(row=0, column=0, sticky="w")
entry_id = tk.Entry(frame_info, width=25)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Name:").grid(row=0, column=2, sticky="w")
entry_name = tk.Entry(frame_info, width=25)
entry_name.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_info, text="Department:").grid(row=1, column=0, sticky="w")
entry_dept = tk.Entry(frame_info, width=25)
entry_dept.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Salary:").grid(row=1, column=2, sticky="w")
entry_salary = tk.Entry(frame_info, width=25)
entry_salary.grid(row=1, column=3, padx=5, pady=5)

tk.Label(frame_info, text="Email:").grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(frame_info, width=25)
entry_email.grid(row=2, column=1, padx=5, pady=5)


# ---------------- Functions ----------------
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dept.delete(0, tk.END)
    entry_salary.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def show_employees():
    text_display.delete(1.0, tk.END)
    if not employees:
        text_display.insert(tk.END, "No employees found. Add some employees to get started!")
    else:
        for emp in employees:
            record = f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['dept']} | Salary: {emp['salary']} | Email: {emp['email']}\n"
            text_display.insert(tk.END, record)

def add_employee():
    emp_id = entry_id.get()
    name = entry_name.get()
    dept = entry_dept.get()
    salary = entry_salary.get()
    email = entry_email.get()

    if not emp_id or not name:
        messagebox.showwarning("Input Error", "Employee ID and Name are required!")
        return

    for emp in employees:
        if emp['id'] == emp_id:
            messagebox.showerror("Duplicate ID", "Employee ID already exists!")
            return

    employees.append({'id': emp_id, 'name': name, 'dept': dept, 'salary': salary, 'email': email})
    messagebox.showinfo("Success", "Employee added successfully!")
    clear_fields()
    show_employees()

def update_employee():
    emp_id = entry_id.get()
    for emp in employees:
        if emp['id'] == emp_id:
            emp['name'] = entry_name.get()
            emp['dept'] = entry_dept.get()
            emp['salary'] = entry_salary.get()
            emp['email'] = entry_email.get()
            messagebox.showinfo("Success", "Employee updated successfully!")
            show_employees()
            return
    messagebox.showerror("Not Found", "Employee ID not found!")

def delete_employee():
    emp_id = entry_id.get()
    for emp in employees:
        if emp['id'] == emp_id:
            employees.remove(emp)
            messagebox.showinfo("Deleted", "Employee deleted successfully!")
            show_employees()
            return
    messagebox.showerror("Not Found", "Employee ID not found!")

def search_employee():
    keyword = entry_search.get().lower()
    text_display.delete(1.0, tk.END)
    found = [emp for emp in employees if keyword in emp['id'].lower() or keyword in emp['name'].lower()]
    if not found:
        text_display.insert(tk.END, "No matching employee found.")
    else:
        for emp in found:
            record = f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['dept']} | Salary: {emp['salary']} | Email: {emp['email']}\n"
            text_display.insert(tk.END, record)


# ---------------- Buttons ----------------
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Add Employee", width=15, command=add_employee).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update Employee", width=15, command=update_employee).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete Employee", width=15, command=delete_employee).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Clear Fields", width=15, command=clear_fields).grid(row=0, column=3, padx=5)


# ---------------- Search Frame ----------------
frame_search = tk.LabelFrame(root, text="Search", padx=20, pady=10)
frame_search.pack(fill="x", padx=20, pady=10)

tk.Label(frame_search, text="Search:").grid(row=0, column=0)
entry_search = tk.Entry(frame_search, width=30)
entry_search.grid(row=0, column=1, padx=5)

tk.Button(frame_search, text="Search", command=search_employee, width=10).grid(row=0, column=2, padx=5)
tk.Button(frame_search, text="Show All", command=show_employees, width=10).grid(row=0, column=3, padx=5)


# ---------------- Employee Records Display ----------------
frame_records = tk.LabelFrame(root, text="Employee Records", padx=10, pady=10)
frame_records.pack(fill="both", expand=True, padx=20, pady=10)

text_display = tk.Text(frame_records, height=10, width=90)
text_display.pack(fill="both", expand=True)
text_display.insert(tk.END, "No employees found. Add some employees to get started!")

# Run the main loop
root.mainloop()
