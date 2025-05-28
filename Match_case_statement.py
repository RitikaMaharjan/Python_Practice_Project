# Match case Statement

number = 2

match number:
    case 1:
        print("One")             # not matched
    case 2:
        print("Two")             # matched
    case 3:
        print("Three")
    case _:
        print("Other number")

# Output: Two

command = input("Enter command: ").lower()

match command:
    case "start":
        print("System starting...")      # matched if input is 'start'
    case "stop":
        print("System stopping...")
    case "restart":
        print("System restarting...")
    case _:
        print("Unknown command.")

# Example Input: start
# Output: System starting...

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week.")     # matched
    case "Friday":
        print("End of the work week.")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Just another day.")

# Output: Start of the work week.

color = "blue"

match color:
    case "red" | "green" | "blue":
        print(f"{color} is a primary color.")   # matched
    case _:
        print(f"{color} is not a primary color.")

# Output: blue is a primary color.

value = "hello"

match value:
    case 0:
        print("Zero")             # not matched
    case _:
        print("Something else")   # matched

# Output: Something else
