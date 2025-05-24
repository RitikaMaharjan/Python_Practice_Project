#String Slicing and Operation 
word = "Hello! How are you?"
print(word[0:6])        # Slices from index 0 to 5
# Output: Hello!
print(len(word))        # Total characters in the string
# Output: 19

animal = "Tiger"
print(len(animal))      # Length of the string
# Output: 5
print(animal[0:4])      # Index 0 to 3
# Output: Tige
print(animal[0:5])      # Index 0 to 4 (entire string)
# Output: Tiger
print(animal[1:3])      # Index 1 to 2
# Output: ig
print(animal[:])       # Start to index 4
# Output: Tiger
print(animal[0:-3])     # Index 0 to (len-3)
# Output: Ti
print(animal[:-3])      # Same as above
# Output: Ti
print(animal[-1:-4])    # Invalid backward range (empty string)
# Output: 
print(animal[-3:-1])    # From -3 to -2
# Output: ge

nm = "Harry"
print(nm[-4:-2])        # From index -4 to -3
# Output: ar
