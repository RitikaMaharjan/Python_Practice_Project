# String methods demonstration
# Strings are immutable in Python

a = "Ritika"
print(len(a))  # 6: Length of the string
print(a.upper())  # RITIKA: Converts to uppercase
print(a.lower())  # ritika: Converts to lowercase

b = "Ritika!!!!!!!!!!!"
c = "!!!!!!!Treesss!!!!!!!"
print(b)  # Ritika!!!!!!!!!!!
print(c)  # !!!!!!!Treesss!!!!!!!
print(b.rstrip("!"))  # Ritika: Removes trailing '!' characters
print(c.rstrip("!"))  # !!!!!!!Treesss: Removes trailing '!' characters

x = "Mango"
print(x)  # Mango
print(x.replace("Mango", "Apples"))  # Apples: Replaces 'Mango' with 'Apples'

y = "I love mangoes"
print(y.split(" "))  # ['I', 'love', 'mangoes']: Splits the string by spaces

blogHeading = "introduction to python"
print(blogHeading.capitalize())  # Introduction to python: Capitalizes the first letter

word = "This is the practice Python."
print(len(word))  # 29: Total number of characters
print(len(word.center(50)))  # 50: Length after centering the string
print(word.count("t"))  # 2: Number of occurrences of 't'

type = "I don't like potatoes."
print(type.endswith("."))  # True: Ends with '.'
print(type.endswith("p"))  # False: Does not end with 'p'
print(type.endswith("like", 5, 11))  # True: 'like' is between index 5 and 11

str = "He's name is Dan. He is an honest man"
print(str.find("is"))  # 11: Index of first occurrence of 'is'
print(str.find("ishh"))  # -1: 'ishh' not found

# Uncommenting the line below would raise an error because 'ishh' is not found
# print(str.index("ishh"))

str1 = "WelcomeToPracticePython3"
print(str1.isalnum())  # True: Contains only letters and digits

strr = "WelcomeToPracticePython"
print(strr.isalnum())  # True: Only alphabetic characters

str2 = "Ritika009"
print(str2.isalpha())  # False: Contains letters and digits

str3 = "Ritika"
print(str3.isalpha())  # True: Only letters

str4 = "ritika"
print(str4.islower())  # True: All letters are lowercase

str5 = "I don't like cats"
print(str5.isprintable())  # True: All characters are printable

str5 = "I don't like cats\n"
print(str5)
print(str5.isprintable())  # False: Contains a newline character which is not printable

s = "   "
print(s.isspace())  # True: Only whitespace

s = "  a  "
print(s.isspace())  # False: Contains a letter

s = "Hello World"
print(s.istitle())  # True: Each word starts with an uppercase letter

s = "hello world"
print(s.istitle())  # False: Not in title case

s = "PYTHON"
print(s.isupper())  # True: All characters are uppercase

s = "Python"
print(s.isupper())  # False: Only first letter is uppercase

s = "hello world"
print(s.startswith("hello"))  # True: Starts with 'hello'

print(s.startswith("world"))  # False: Does not start with 'world'

s = "Hello World"
print(s.swapcase())  # hELLO wORLD: Switches case of each letter

s = "hello world"
print(s.title())  # Hello World: Converts to title case
