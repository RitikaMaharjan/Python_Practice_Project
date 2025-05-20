#Variables
''' Variables are like a containeer which is used to store any data that can be manipulated later in your code.'''

a = 1        
b ="Ritika"   

print(a)
print(b)

# Declaring a variable and variable names


name = "Ritika"
_age = 35
Address1 = "Kathmandu"
address1 = "Sirutar" # Case Sensitive
course_sub = "Computer"

print(address1)

# Checking the types of variables

x = "Kathmandu"
y = 10 
z = 3.5
w = True
print(type(x))
print(type(y))
print(type(z))
print(type(w))

# Assigning Multiple Variables

q,r,s = "cow","dog","cat" #many values to multiple variables
print(q)
print(r)
print(s)

q=r=s="animals" # one value to multiple variables
print(q)
print(r)
print(s)

# Unpacking a variable
animals = ["cow", "dog", "cat"]
q, r, s = animals
print(x)
print(y)
print(z)

#Changing Values

tree = "green"
tree = "blue"#overwrites

print(tree)

#Output Variables-An output variable is just a variable that stores the result (output) of a function or an operation.
a = 5
b = 3
result = a + b   
print(result)    

first_name = "Ritika"
last_name = "Maharjan"
full_name = first_name +" "+ last_name   # output variable
print(full_name)   

# Global and Local variables
#Local variable
 #local variable is a variable that is created inside a function, and it can only be used inside that function.
def greet():
    name = "Sita"   # local variable
    print(name)

greet()

#Global Variable
#A global variable is a variable that is created outside of all functions, and you can use it anywhere, inside or outside functions.

name = "Ram"   # global variable

def say_hello():
    print(name)  # we can use global variable here

say_hello()     
print(name)     

# To change global variable inside a function - use global keyword

count = 1   # global variable

def increase():
    global count    # use global variable
    count = count + 5

increase()
print(count)    

# Deleting a variable
food = "Pizza"

 