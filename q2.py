# Ask the user to input a number
number = int(input("Enter a number: "))

# Check if the number is even or odd using the modulus operator
if number % 2 == 0:
    print("The number is even.")  # If remainder is 0, number is even
else:
    print("The number is odd.")   # Otherwise, number is odd
