'''A command-line calculator that performs basic
 arithmetic operations: addition, subtraction,
 multiplication, and division'''
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print(f"Result: {num1 + num2}")
    elif operator == '-':
        print(f"Result: {num1 - num2}")
    elif operator == '*':
        print(f"Result: {num1 * num2}")
    elif operator == '/':
        print(f"Result: {num1 / num2 if num2 != 0 else 'Error: Division by zero'}")
    else:
        print("Invalid operator.")


calculator()