# PE3_3.py

# Prompt the user to enter their height in cm and weight in kg
height_cm = float(input("Please enter the height (in cm): "))  # User input for height
weight_kg = float(input("Please enter the weight (in kg): "))  # User input for weight

# Convert height from cm to inches (since 1 inch = 2.54 cm)
height_inch = height_cm / 2.54

# Calculate BMI using the formula: BMI = (weight / (height^2)) * 703
bmi = (weight_kg / (height_inch ** 2)) * 703

# Print the BMI, formatted to 3 decimal places
print(f"BMI = {bmi:.3f}")
