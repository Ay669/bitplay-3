print("welcome to the swaping game")
print("let's swap two numbers")

# step 1: take input from the user
num1 = input("enter first number: ")
num2 = input("enter second number: ")

print(f"\nBefore swapping: num1 = {num1}, num2 = {num2}")
print("swapping the numbers...")

# step 2: swaping using a temporary variable
temp = num1
num1 = num2
num2 = temp

# step 3: print the swapped numbers
print(f"After swapping: num1 = {num1}, num2 = {num2}")
print("swapping completed")
