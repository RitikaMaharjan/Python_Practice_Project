# 1. Print numbers from 0 to 4
print("Example 1:")
for i in range(5):          # i goes from 0 to 4
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4


# 2. Print each fruit from a list
print("\nExample 2:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:       # Goes through each item in the list
    print(fruit)
# Output:
# apple
# banana
# cherry


# 3. Stop when fruit is banana
print("\nExample 3:")
for fruit in fruits:
    if fruit == "banana":  # If fruit is banana, stop the loop
        break
    print(fruit)
# Output:
# apple


# 4. Skip banana
print("\nExample 4:")
for fruit in fruits:
    if fruit == "banana":  # If fruit is banana, skip this loop
        continue
    print(fruit)
# Output:
# apple
# cherry


# 5. Loop with else
print("\nExample 5:")
for i in range(3):         # Prints 0 to 2
    print(i)
else:                      # Runs after loop ends normally
    print("Finished")
# Output:
# 0
# 1
# 2
# Finished


# 6. Nested loop (loop inside a loop)
print("\nExample 6:")
colors = ["red", "green"]
for color in colors:           # Outer loop
    for fruit in fruits:       # Inner loop
        print(color, fruit)
# Output:
# red apple
# red banana
# red cherry
# green apple
# green banana
# green cherry
