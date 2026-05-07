import tkinter as tk
from tkinter import messagebox, ttk

# ----------------- MAIN WINDOW -----------------
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("900x600")
root.resizable(False, False)

# ----------------- INVENTORY DATA -----------------
inventory = []  # List to store product data


# ----------------- FUNCTIONS -----------------
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_stock.delete(0, tk.END)


def show_products(data=None):
    text_display.delete(1.0, tk.END)
    if not inventory:
        text_display.insert(tk.END, "📦 No products found. Add some products to get started!")
    else:
        for product in (data if data else inventory):
            record = f"ID: {product['id']} | Name: {product['name']} | Category: {product['category']} | " \
                     f"Price: ${product['price']} | Stock: {product['stock']}\n"
            text_display.insert(tk.END, record)


def add_product():
    pid = entry_id.get()
    name = entry_name.get()
    category = entry_category.get()
    price = entry_price.get()
    stock = entry_stock.get()

    if not pid or not name:
        messagebox.showwarning("Input Error", "Product ID and Name are required!")
        return

    for p in inventory:
        if p['id'] == pid:
            messagebox.showerror("Duplicate ID", "Product ID already exists!")
            return

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for Price and Stock!")
        return

    inventory.append({'id': pid, 'name': name, 'category': category, 'price': price, 'stock': stock})
    messagebox.showinfo("Success", "Product added successfully!")
    clear_fields()
    update_category_filter()
    show_products()


def update_product():
    pid = entry_id.get()
    for p in inventory:
        if p['id'] == pid:
            try:
                p['name'] = entry_name.get()
                p['category'] = entry_category.get()
                p['price'] = float(entry_price.get())
                p['stock'] = int(entry_stock.get())
                messagebox.showinfo("Success", "Product updated successfully!")
                show_products()
                return
            except ValueError:
                messagebox.showerror("Invalid Input", "Enter valid numeric values for Price and Stock!")
                return
    messagebox.showerror("Not Found", "Product ID not found!")


def delete_product():
    pid = entry_id.get()
    for p in inventory:
        if p['id'] == pid:
            inventory.remove(p)
            messagebox.showinfo("Deleted", "Product deleted successfully!")
            update_category_filter()
            show_products()
            return
    messagebox.showerror("Not Found", "Product ID not found!")


def update_stock():
    pid = entry_id.get()
    for p in inventory:
        if p['id'] == pid:
            try:
                new_stock = int(entry_stock.get())
                p['stock'] = new_stock
                messagebox.showinfo("Updated", "Stock updated successfully!")
                show_products()
                return
            except ValueError:
                messagebox.showerror("Invalid Input", "Stock must be an integer!")
                return
    messagebox.showerror("Not Found", "Product ID not found!")


def search_product():
    keyword = entry_search.get().lower()
    results = [p for p in inventory if keyword in p['id'].lower() or keyword in p['name'].lower()]
    if results:
        show_products(results)
    else:
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, "🔍 No matching product found.")


def filter_by_category():
    selected_category = combo_category.get()
    if selected_category == "All":
        show_products()
    else:
        results = [p for p in inventory if p['category'].lower() == selected_category.lower()]
        show_products(results)


def update_category_filter():
    categories = sorted(set([p['category'] for p in inventory if p['category']]))
    combo_category['values'] = ["All"] + categories
    combo_category.set("All")


# ----- Inventory Statistics -----
def low_stock_alert():
    low_stock_items = [p for p in inventory if p['stock'] <= 5]
    if not low_stock_items:
        messagebox.showinfo("Low Stock Alert", "All products have sufficient stock.")
    else:
        msg = "\n".join([f"{p['name']} (Stock: {p['stock']})" for p in low_stock_items])
        messagebox.showwarning("Low Stock Alert", f"Low stock items:\n{msg}")


def category_summary():
    summary = {}
    for p in inventory:
        summary[p['category']] = summary.get(p['category'], 0) + p['stock']
    if summary:
        msg = "\n".join([f"{cat}: {qty} items" for cat, qty in summary.items()])
        messagebox.showinfo("Category Summary", msg)
    else:
        messagebox.showinfo("Category Summary", "No products in inventory.")


def inventory_value():
    total_value = sum(p['price'] * p['stock'] for p in inventory)
    messagebox.showinfo("Inventory Value", f"Total Inventory Value: ${total_value:.2f}")


# ----------------- PRODUCT INFORMATION FRAME -----------------
frame_info = tk.LabelFrame(root, text="Product Information", padx=20, pady=10)
frame_info.pack(fill="x", padx=20, pady=10)

tk.Label(frame_info, text="Product ID:").grid(row=0, column=0)
entry_id = tk.Entry(frame_info, width=20)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Product Name:").grid(row=0, column=2)
entry_name = tk.Entry(frame_info, width=20)
entry_name.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_info, text="Category:").grid(row=1, column=0)
entry_category = tk.Entry(frame_info, width=20)
entry_category.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Price ($):").grid(row=1, column=2)
entry_price = tk.Entry(frame_info, width=20)
entry_price.grid(row=1, column=3, padx=5, pady=5)

tk.Label(frame_info, text="Stock Quantity:").grid(row=2, column=0)
entry_stock = tk.Entry(frame_info, width=20)
entry_stock.grid(row=2, column=1, padx=5, pady=5)


# ----------------- BUTTONS -----------------
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Add Product", width=15, command=add_product).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update Product", width=15, command=update_product).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete Product", width=15, command=delete_product).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Update Stock", width=15, command=update_stock).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Clear Fields", width=15, command=clear_fields).grid(row=0, column=4, padx=5)


# ----------------- SEARCH & FILTER -----------------
frame_search = tk.LabelFrame(root, text="Search & Filter", padx=20, pady=10)
frame_search.pack(fill="x", padx=20, pady=10)

tk.Label(frame_search, text="Search:").grid(row=0, column=0)
entry_search = tk.Entry(frame_search, width=25)
entry_search.grid(row=0, column=1, padx=5)

tk.Button(frame_search, text="Search", width=10, command=search_product).grid(row=0, column=2, padx=5)

tk.Label(frame_search, text="Filter by Category:").grid(row=0, column=3, padx=10)
combo_category = ttk.Combobox(frame_search, width=18, state="readonly")
combo_category.grid(row=0, column=4, padx=5)
combo_category.set("All")

tk.Button(frame_search, text="Filter", width=10, command=filter_by_category).grid(row=0, column=5, padx=5)
tk.Button(frame_search, text="Show All", width=10, command=show_products).grid(row=0, column=6, padx=5)


# ----------------- INVENTORY STATISTICS -----------------
frame_stats = tk.LabelFrame(root, text="Inventory Statistics", padx=10, pady=10)
frame_stats.pack(fill="x", padx=20, pady=10)

tk.Button(frame_stats, text="Low Stock Alert", width=18, command=low_stock_alert).grid(row=0, column=0, padx=5)
tk.Button(frame_stats, text="Category Summary", width=18, command=category_summary).grid(row=0, column=1, padx=5)
tk.Button(frame_stats, text="Inventory Value", width=18, command=inventory_value).grid(row=0, column=2, padx=5)


# ----------------- INVENTORY RECORDS -----------------
frame_records = tk.LabelFrame(root, text="Inventory Records", padx=10, pady=10)
frame_records.pack(fill="both", expand=True, padx=20, pady=10)

text_display = tk.Text(frame_records, height=10, width=100)
text_display.pack(fill="both", expand=True)
text_display.insert(tk.END, "📦 No products found. Add some products to get started!")

# Run
root.mainloop()
