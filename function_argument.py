# 1. Positional Arguments
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5


# 2. Keyword Arguments
def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Alice", message="Hello")  # Output: Hello, Alice!


# 3. Default Arguments
def greet_default(name, message="Hi"):
    print(f"{message}, {name}!")

greet_default("Bob")            # Output: Hi, Bob!
greet_default("Bob", "Welcome") # Output: Welcome, Bob!


# 4. Variable-length Positional Arguments (*args)
def total(*args):
    print(f"Args: {args}")
    return sum(args)

print(total(1, 2, 3))  # Output: Args: (1, 2, 3) => 6


# 5. Variable-length Keyword Arguments (**kwargs)
def show_info(**kwargs):
    print("Info:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_info(name="Eve", age=25)
# Output:
# Info:
# name = Eve
# age = 25


# 6. Argument Unpacking
def multiply(x, y):
    return x * y

tuple_args = (4, 5)
dict_args = {'x': 6, 'y': 7}

print(multiply(*tuple_args))   # Output: 20
print(multiply(**dict_args))   # Output: 42
