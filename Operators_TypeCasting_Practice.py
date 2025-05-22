# Operators in Python
a = 5
b = 6

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division (float result)
print(a // b)  # Floor Division 
print(a % b)   # Modulus (remainder)
print(a ** b)  # Exponentiation (a raised to the power b)

# Create a Simple Calculator
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The sum is =", a + b)
print("The subtraction is =", a - b)
print("The multiplication is =", a * b)
print("The division is =", a / b)
print("The modulus is =", a % b)

# Type Casting in Python - Converting one data type into another

a = "1"  # str
b = "2"  # str
print(int(a) + int(b))  # Converts to int and adds -- Output: 3

# Explicit Typecasting - Manual conversion using built-in functions

a = "10"
b = int(a)
print(b + 5)  # Output: 15

# Implicit Typecasting - Automatic conversion by Python during operations

a = 5        # int
b = 2.0      # float
c = a + b    # a is implicitly converted to float
print(c)     # Output: 7.0

# Error example 
a = "5"
b = 2
# print(a + b)  #  can't concatenate str and int

#  to fix it
print(int(a) + b)  # Output: 7
