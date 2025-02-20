# PE3_4.py

# Prompt the user to enter three integer numbers
num1 = int(input("Please enter the first integer: "))  # First integer
num2 = int(input("Please enter the second integer: "))  # Second integer
num3 = int(input("Please enter the third integer: "))  # Third integer

# Display the numbers before sorting
print(f"Before sorting: {num1} {num2} {num3}")

# Use the built-in min() and max() functions to sort the numbers
smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)
middle = num1 + num2 + num3 - smallest - largest

# Display the numbers after sorting
print(f"After sorting: {smallest} {middle} {largest}")
