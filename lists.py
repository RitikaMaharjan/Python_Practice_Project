# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing items
print(fruits[0])  # Output: apple

# Changing item
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Adding item at the end
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']

# Inserting item at index 1
fruits.insert(1, "banana")
print(fruits)  # Output: ['apple', 'banana', 'orange', 'cherry', 'grape']

# Removing item by value
fruits.remove("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'grape']

# Length of list
print(len(fruits))  # Output: 4

# Looping through the list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
# grape

# Sorting the list
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'grape']
