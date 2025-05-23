#Taking user input in python
a = input("Enter your name:") # input() returns string
print("My name is " ,a )  # prints the user's name

#Output : My name is Rits

# Taking user input for two numbers
x = input("Enter the first number:") # returns string 
y = input("Enter the second number:") # returns string 

# we try to add two numbers but since x and y are strings,
# this will perform string concatenation, not numeric addition

print(x + y)    # x = 100, y = 100 --Output:100100 
                #To actually do the numeric operation we have to use typecasting

#o convert the inputs to integers 
x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

print(x + y) # If x = 100 and y = 100, Output: 200

# Convert to floats (for decimal numbers)
x = float(input("Enter the first number:"))  
y = float(input("Enter the second number:")) 
print(x + y)  # If x = 5.5 and y = 2.5, Output: 8.0

#Strings in Python

name = "Ritika"
address = 'Kathmandu'
introduction = ''' My name is Ritika. I love to eat pizza.''' # Multi-line string

print(introduction) #Output: My name is Ritika. I love to eat pizza.

#Concatenation
first = "Veg"
second = "Pizza"
print(first + " " + second)  # Output: Veg Pizza

#Repetition
greet = " Hello "
print(greet * 3) #Output: Hello  Hello  Hello

#Indexing
test = "Lavanya"
print(test[0])  # Output: L
print(test[1])  # Output: a
print(test[2])  # Output: v
print(test[3])  # Output: a
print(test[4])  # Output: n
print(test[5])  # Output: y
print(test[6])  # Output: a
print(test[-1]) # Output: a (last character)
print(test[-5]) # Output: v
#print(test[7]) Error because string length 7 doesnot exist --Index Error

# Safely printing characters in a loop
test2 = "The moon is beautiful tonight. Isn't it ?"
for character in test2:
    print(character)  # Prints each character in the string on a new line