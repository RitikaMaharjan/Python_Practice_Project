#  break examples 

# Example 1: stop the loop when i becomes 5
for i in range(1, 10):
    if i == 5:
        break  # exit the loop
    print(i)
# Output: 1 2 3 4

# Example 2: stop when we find "Charlie"
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    if name == "Charlie":
        print(name)  # print "Charlie"
        break        # stop the loop
# Output: Charlie

# Example 3: while loop that stops at 3
i = 1
while True:
    print(i)
    if i == 3:
        break  # exit the loop
    i += 1
# Output: 1 2 3

# continue examples 

# Example 4: skip number 3
for i in range(1, 6):
    if i == 3:
        continue  # skip this turn
    print(i)
# Output: 1 2 4 5

# Example 5: print even numbers only
for i in range(1, 11):
    if i % 2 != 0:
        continue  # skip odd numbers
    print(i)
# Output: 2 4 6 8 10

# Example 6: skip empty words
words = ["apple", "", "banana", "", "cherry"]
for word in words:
    if word == "":
        continue  # skip empty strings
    print(word)
# Output: apple banana cherry

# break and continue together

# Example 7: skip even numbers, stop at 9
for i in range(1, 11):
    if i % 2 == 0:
        continue  # skip even numbers
    if i == 9:
        break     # stop at 9
    print(i)
# Output: 1 3 5 7

# Example 8: while loop skips 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # skip 3
    print(i)
# Output: 1 2 4 5 6

# Example 9: skip empty inputs
inputs = ["yes", "", "no", "maybe", ""]
for item in inputs:
    if item == "":
        continue  # skip empty items
    print(item)
# Output: yes no maybe
