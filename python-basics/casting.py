# ex 1: converting into a float number:
a = "3"
b = float(a)
print(a, b)

# ex 2: converting integer to a float number
a = 6
b = float(a)
print(a, b)

# ex 3: converting floating number to an integer
a = 99.97
b = int(a)
print(a, b)

# ex 4 (optional): converting str to a complex number
a = "1.9"
b = complex(a)
print(a, b)

# ex 5 (optional): converting complex to an integer:
try:
    a = 6 + 0j
    b = int(a)
    print(a, b)
except TypeError:
    print("You cannot convert complex number to an integer!\nAutomatically converted to a str.")
    b = str(a)
    print(a, b)
