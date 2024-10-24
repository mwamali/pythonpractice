# Ask the user to enter a number between 1 and 7
day_number = int(input("Enter a number (1-7): "))

# Determine the corresponding day of the week
if day_number == 1:
    print("Day: Monday")
elif day_number == 2:
    print("Day: Tuesday")
elif day_number == 3:
    print("Day: Wednesday")
elif day_number == 4:
    print("Day: Thursday")
elif day_number == 5:
    print("Day: Friday")
elif day_number == 6:
    print("Day: Saturday")
elif day_number == 7:
    print("Day: Sunday")
else:
    print("Invalid input.")  # Handle numbers outside the 1-7 range
