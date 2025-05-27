# 1. Check if the number is Even or Odd
number = int(input("Enter a number: "))  # Example input: 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output for input 7:
# Odd

# 2. Check Voting Eligibility
age = int(input("Enter your age: "))  # Example input: 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Output for input 16:
# Not eligible to vote

# 3. Find the Largest of Two Numbers
a = int(input("Enter first number: "))   # Example input: 25
b = int(input("Enter second number: "))  # Example input: 18

if a > b:
    print(f"{a} is larger")
elif b > a:
    print(f"{b} is larger")
else:
    print("Both are equal")

# Output for inputs 25 and 18:
# 25 is larger

# 4. Grade Checker
score = int(input("Enter exam score (0–100): "))  # Example input: 83

# Determine grade using if-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Output the grade
print(f"Grade: {grade}")

# Output for input 83:
# Grade: B
