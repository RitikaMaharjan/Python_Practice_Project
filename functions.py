#  Function Basics in Python 

# 1. Define a function
def greet():
    print("Hello!")

greet()  # Output: Hello!


# 2. Function with parameters
def greet_name(name):
    print("Hello, " + name)

greet_name("Alice")  # Output: Hello, Alice


# 3. Function with return value
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5


# 4. Default parameter
def greet(name="Guest"):
    print("Hello, " + name)

greet()         # Output: Hello, Guest
greet("Bob")    # Output: Hello, Bob


# 5. *args - multiple positional arguments
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3, 4)  # Output: 10


# 6. **kwargs - multiple keyword arguments
def show_info(**info):
    print(info)

show_info(name="Anna", age=25)  
# Output: {'name': 'Anna', 'age': 25}
