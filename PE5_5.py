# PE5_5.py
# a) Request an integer input range.
num_range = int(input("Enter the range of numbers: "))

# b) Implement a list of the numbers 1 to range inclusive.
numbers = list(range(1, num_range + 1))

# c) Request an integer input number.
mult_num = int(input("Enter a number to generate its multiplication table: "))

# d) Use a loop upon this list to compute and print the multiplication table of the input number.
for i in numbers:
    print(f"{mult_num} x {i} = {mult_num * i}")

Enter the range of numbers: 5
Enter a number to generate its multiplication table: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15

Enter the range of numbers: 4
Enter a number to generate its multiplication table: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
