# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print("Initial Dictionary:", student)
# Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}

#  Accessing values
print("Name:", student["name"])
# Output: Alice

#  Using get() to access keys safely
print("Email:", student.get("email", "Not found"))
# Output: Not found

#  Adding a new key-value pair
student["grade"] = "A"
print("After Adding Grade:", student)
# Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'grade': 'A'}

#  Updating an existing key
student["age"] = 21
print("After Updating Age:", student)
# Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'grade': 'A'}

#  Deleting a key-value pair
del student["major"]
print("After Deleting Major:", student)
# Output: {'name': 'Alice', 'age': 21, 'grade': 'A'}

# Looping through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(f"{key} -> {value}")
# Output:
# name - Alice
# age - 21
# grade - A

#  Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
# Output:
# Keys: dict_keys(['name', 'age', 'grade'])
# Values: dict_values(['Alice', 21, 'A'])
# Items: dict_items([('name', 'Alice'), ('age', 21), ('grade', 'A')])
