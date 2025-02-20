# PE3_2.py

# Prompt the user for the bill amount and the tip percentage
bill_amount = float(input("Enter the amount of the bill: "))  # Amount of the bill (float)
tip_percentage = int(input("Enter the percentage of tip: "))  # Tip percentage (integer)

# Calculate the tip amount
tip_amount = (bill_amount * tip_percentage) / 100

# Print the tip amount, formatted to two decimal places
print(f"Tip: ${tip_amount:.2f}")
