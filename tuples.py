# Creating a tuple
my_tuple = (10, 20, 30)

# Printing the tuple
print(my_tuple)            # Output: (10, 20, 30)

# Accessing elements using index
print(my_tuple[0])         # Output: 10
print(my_tuple[1])         # Output: 20

# Tuples can contain different data types
mixed = (1, "hello", 3.5)
print(mixed)               # Output: (1, 'hello', 3.5)

# Tuples are immutable (cannot be changed)
# mixed[0] = 100           # This will cause an error

# Length of a tuple
print(len(mixed))          # Output: 3

# Looping through a tuple
for item in my_tuple:
    print(item)            # Output: 10 20 30 (each on a new line)

# Creating a single-element tuple (note the comma)
single = (5,)
print(type(single))        # Output: <class 'tuple'>

# Tuple without parentheses (works too)
t = 1, 2, 3
print(t)                   # Output: (1, 2, 3)
