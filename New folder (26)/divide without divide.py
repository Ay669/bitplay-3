print("let's do easy division")

a = int(input("Big number: "))
b = int(input("Small number: "))

if b == 0:
    print("Error: Division by zero is not allowed.")
else:
    count = 0
    while a >= b:
        a = a - b
        count = count + 1

print("Answer is:")
print("Times =", count)
print("left =", a)
