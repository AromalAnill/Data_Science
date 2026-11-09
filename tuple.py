
t = (10, "Apple", 20.5, True, "Mango", 30)

print("Tuple:", t)

print("Sliced tuple:", t[1:4])

print("Tuple elements:")
for i in t:
    print(i)

# Packing
t1 = (100, "Python", 50.5)

print("Packed tuple:", t1)

# Unpacking
a, b, c = t1

print("Unpacked elements:")
print(a)
print(b)
print(c)