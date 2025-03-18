# PE5_1.py
a = list(range(5))
print(a)

b = []
for i in range(5):
    b.append(i)
print(b)

x = list(range(-10, 10))
print(x)
print(min(x), max(x), sum(x))

even_num = list(range(2, 11, 2))
print(even_num[0], even_num[-1])

odd_num = list(range(1, 10, 2))
print(odd_num)

cubes = [i**3 for i in range(1, 11)]
for cube in cubes:
    print(cube)

print('|'.join(map(str, cubes)))
