'''Write a code for console application to store and
manage contacts, including names and phone numbers'''

def contact_book():
    contacts = {}
    while True:
        action = input("Enter 'add', 'view', 'delete', or 'exit': ")
        if action == 'add':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
        elif action == 'view':
            print("Contacts:", contacts)
        elif action == 'delete':
            name = input("Enter contact name to delete: ")
            contacts.pop(name, "Contact not found.")
        elif action == 'exit':
            break
        else:
            print("Invalid input.")

contact_book()