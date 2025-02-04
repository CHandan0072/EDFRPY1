print("2+3*4= ",2+3*4)
print("1-7**2= ",1-7**2)
print("1//2**3 = ",1//2**3)
print("(3+4)*5 = ",(3+4)*3)
print("(5%3)*4= ", (5%3)*4)
print("(-2)**(-2)= ", (-2)**(-2))
print("7//3= ", 7//3)
print("14%4= ", 14%4)
print("1+7%4= ", 1+7%4)
print("14//4*4= ", 14//4*4)
print("5//2+2= ", 5//2+2)
print("5%5*5= ", 5%5*5)

print("NewYear.sales is invalid because variable names cannot contain a period.")
print("room&color is invalid because the ampersand (&) character is not allowed.")
print("TOrF_1040 is valid because it uses letters, numbers, and underscores, and does not start with a number.")
print("311HotLine is invalid because variable names cannot begin with a digit.")
print("expense# is invalid because the hash (#) character is not allowed in variable names.")
print("INCOME 101 is invalid because variable names cannot contain spaces.")

# Example for cost = cost + 5
cost = 10
cost += 5
print("cost = cost + 5 results in:", cost)

# Example for sum = sum * rate
sum_value = 10
rate = 2
sum_value *= rate
print("sum = sum * rate results in:", sum_value)

# Example for product = product / 10
product = 100
product /= 10
print("product = product / 10 results in:", product)

# Example for cost = cost // num
cost = 20
num = 4
cost //= num
print("cost = cost // num results in:", cost)

# Example for total = total - cost
total = 50
cost = 20
total -= cost
print("total = total - cost results in:", total)

# Example for quotient = quotient % rate
quotient = 20
rate = 3
quotient %= rate
print("quotient = quotient % rate results in:", quotient)

a = 5
b = 3

print("int(-a / b)= ", int(-a / b))           # Converts -5/3 to an integer by truncation (results in -1)
print("round(a / b, 2)= ", round(a / b, 2))       # Rounds 5/3 to two decimal places (results in 1.67)
print("abs(b - a)= ", abs(b - a))                 # Absolute difference between b and a (results in 2)