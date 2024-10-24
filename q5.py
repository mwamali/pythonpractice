# Ask the user to input their age
age = int(input("Enter your age: "))

# Determine the age category based on user input
if age < 18:
    print("You are a minor.")  # Age is less than 18
elif 18 <= age <= 65:
    print("You are an adult.")  # Age is between 18 and 65
else:
    print("You are a senior.")  # Age is greater than 65
