# Q1: For Loop – Level 2 (Even-numbered theater seats)
for seat in range(2, 21, 2):
    print(f"Seat {seat} is available")
# Output:
# Seat 2 is available
# Seat 4 is available
# ...
# Seat 20 is available

# Q2: While Loop – Level 2 (ATM PIN simulation)
correct_pin = "1234"
attempts = 0
pin = ""
while pin != correct_pin and attempts < 3:
    pin = input("Enter PIN: ")
    attempts += 1
if pin == correct_pin:
    print("Access granted")
else:
    print("Account locked")
# Output Example:
# Enter PIN: 0000
# Enter PIN: 1111
# Enter PIN: 1234
# Access granted

# Q3: For Loop – Level 3 (Monthly savings calculation)
monthly_saving = [1000, 1200, 1100, 1300, 1250, 1500, 1600, 1400, 1350, 1450, 1550, 1650]
total = 0
for amount in monthly_saving:
    total += amount
print("Total savings in a year:", total)
# Output:
# Total savings in a year: 17350

# Q4: While Loop – Level 3 (Countdown timer)
seconds = 5
while seconds > 0:
    print(f"Timer: {seconds} seconds left")
    seconds -= 1
print("Time's up!")
# Output:
# Timer: 5 seconds left
# Timer: 4 seconds left
# ...
# Timer: 1 seconds left
# Time's up!
