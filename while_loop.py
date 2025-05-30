# Example 1: Count from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5



# Example 2: Ask for correct password
password = ""
while password != "secret":
    password = input("Enter the password: ")
print("Access granted.")

# Output:
# Enter the password: 123
# Enter the password: test
# Enter the password: secret
# Access granted.



# Example 3: Countdown from 5
timer = 5
while timer > 0:
    print(timer)
    timer -= 1
print("Time's up!")

# Output:
# 5
# 4
# 3
# 2
# 1
# Time's up!



# Example 4: Sum numbers until 0
total = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    number = int(input("Enter another number (0 to stop): "))
print("Total sum is:", total)

# Output:
# Enter a number (0 to stop): 3
# Enter another number (0 to stop): 7
# Enter another number (0 to stop): 0
# Total sum is: 10


# Example 5: Infinite loop with break
while True:
    text = input("Type 'exit' to quit: ")
    if text == "exit":
        break
print("Exited the loop.")

# Output:
# Type 'exit' to quit: hi
# Type 'exit' to quit: okay
# Type 'exit' to quit: exit
# Exited the loop.
