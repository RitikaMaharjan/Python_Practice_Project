#if_ else 

# Check if a number is positive or not
number = int(input("Enter a number: "))  # user enters a number

if number > 0:  # condition to check if number is greater than 0
    print("The number is positive.")  # Output if condition is true
else:
    print("The number is not positive.")  # Output if condition is false
# Example input: 5 → Output: The number is positive.


# Check if user is adult or not
age = int(input("Enter your age: "))  # user enters their age

if age >= 18:  # checks if age is 18 or more
    print("You are an adult.")
else:
    print("You are not an adult.")
# Example input: 17 → Output: You are not an adult.


# Check if a number is even or odd
num = int(input("Enter a number to check even/odd: "))

if num % 2 == 0:  # remainder is 0 means even number
    print("The number is even.")
else:
    print("The number is odd.")
# Example input: 4 → Output: The number is even.


# Check if user entered yes or no
answer = input("Do you want to continue? (yes/no): ")  # takes input as string

if answer == "yes":  # checks if user typed "yes"
    print("You chose to continue.")
else:
    print("You chose not to continue.")
# Example input: no → Output: You chose not to continue.


# Check if temperature is hot or cold
temp = int(input("Enter temperature in Celsius: "))

if temp > 30:  # checks if temperature is above 30
    print("It is hot.")
else:
    print("It is not hot.")
# Example input: 25 → Output: It is not hot.
