# PE5_6.py

# A: Fixing the syntax error
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

# B: Fixing concatenation error
for i in range(1, 4):
    print(str(i) + '\t' + str(2**i))

# C: Fixing the range issue
for j in range(5, 0, -1):
    print(j)

# D: Displaying elements in uppercase
letters = ['a', 'b', 'c']
for i in range(len(letters)):
    letters[i] = letters[i].upper()
print(letters)

# E: Modifying the tuple
fruits = ('apple', 'banana', 'cherry')
print(fruits)
# Convert to a list to modify
fruits = list(fruits)
fruits[0] = 'orange'
fruits.append('pineapple')
print(fruits)
