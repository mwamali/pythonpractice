# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to input an operation (+, -, *, /)
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation based on user input
if operation == '+':
    print("Result:", num1 + num2)  # Addition
elif operation == '-':
    print("Result:", num1 - num2)  # Subtraction
elif operation == '*':
    print("Result:", num1 * num2)  # Multiplication
elif operation == '/':
    if num2 != 0:
        print("Result:", num1 / num2)  # Division, checking if divisor is not zero
    else:
        print("Error: Division by zero is not allowed.")  # Handle division by zero
else:
    print("Invalid operation.")  # Handle unsupported operations
