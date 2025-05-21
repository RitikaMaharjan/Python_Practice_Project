
#Python Numbers

#Getting a datatype
x = 2
print(type(x))

#Numeric Types in Python
x = 10 #1. Integer --Whole numbers (no decimals)
y = -0.001 #2. Float --with decimal numbers
z = 2 + 3j #3. Complex --Has a real and an imaginary part

print(type(x))
print(type(y))
print(type(z))

#Type Conversion

a = 2.3
b = 10
c = 1j

#converting float into int

x = int(a)
y = complex(b) # converting int into complex
z = float(1)  #Converting complex into float

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# Random Numbers
 #Common Functions in random 

import random
print(random.random()) #Returns a random float 
print(random.randint(1, 10))  #Returns a random integer --Random.randiant
print(random.uniform(1, 5)) #Returns a random float

colors = ['red', 'green', 'blue'] 
print(random.choice(colors)) #Randomly picks one item from a list, tuple, string, etc.

nums = [1, 2, 3, 4, 5]
random.shuffle(nums) #Shuffles the elements of a list in place
print(nums)

# Roll a dice

import random

dice = random.randint(1, 6)
print("You rolled:", dice)

#Random Greeting
import random

greetings = ["Hello!", "Hi", "Namaste!", "Goodbye!"]
print(random.choice(greetings))

# Number guessing game

import random

number = random.randint(1,10)

#let the user select pick their number
guess = int(input("Please select a number between 1 to 10:"))

if guess == number:
    print("Congratulations! You won:")
else:
    print(f'("Sorry you lost. The correct number was {number}:")')



