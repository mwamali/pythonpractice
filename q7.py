# Ask the user to input the lengths of three sides of a triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Determine the type of triangle based on the side lengths
if side1 == side2 == side3:
    print("The triangle is equilateral.")  # All three sides are equal
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")  # Two sides are equal
else:
    print("The triangle is scalene.")  # All three sides are different
