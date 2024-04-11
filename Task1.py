# Take input from user for arithmetic operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = num1 / num2

print("Arithmetic operations:")
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Division:", division_result)

# String manipulation
text = "Hello, World!"
uppercase_text = text.upper()
lowercase_text = text.lower()
reversed_text = text[::-1]

print("\nString manipulation:")
print("Uppercase:", uppercase_text)
print("Lowercase:", lowercase_text)
print("Reversed:", reversed_text)

# Conditional statements
number = 15
if number > 10:
    print("\nConditional statements:")
    print("Number is greater than 10")
else:
    print("Number is less than or equal to 10")

# Common data structures
# Lists
my_list = [1, 2, 3, 4, 5]
print("\nCommon data structures:")
print("List:", my_list)

# Operations with lists
# Append to list
my_list.append(6)
print("Appended list:", my_list)

# Remove from list
my_list.remove(3)
print("List after removing 3:", my_list)

# Access elements by index
print("Element at index 2:", my_list[2])

# Tuples
my_tuple = (1, 2, 3)
print("\nTuple:", my_tuple)

# Operations with tuples
# Access elements by index
print("Element at index 1:", my_tuple[1])

# Dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print("\nDictionary:", my_dict)

# Operations with dictionary
# Access value by key
print("Age:", my_dict['age'])

# Add new key-value pair
my_dict['occupation'] = 'Engineer'
print("Dictionary after adding occupation:", my_dict)

# Remove key-value pair
del my_dict['city']
print("Dictionary after removing city:", my_dict)
