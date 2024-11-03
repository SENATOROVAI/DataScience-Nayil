"""Этот скрипт демонстрирует основные операции со списками в Python."""

# Create a list
example_list = [2, 2.5, "Python"]
print(f"Initial list: {example_list}")
print()

# Convert string to list
str_list = list("Help")
print(f"String to list: {str_list}")
for cell in str_list:
    print(cell)
print()

# Create new list with cubes of odd numbers from 0 to 19
cubes_of_odds = [x**3 for x in range(20) if x % 2 == 1]
print(f"Cubes of odd numbers: {cubes_of_odds}")
print()

# Length of list
print(f"Letght of cubes_of_odds: {len(cubes_of_odds)}")

for index, element in enumerate(cubes_of_odds, start=1):
    print(f"{index} - {element}")
print()

# Check if an element belongs to the list
print(f"Is 2  in example_list: {2 in example_list}")
print(f"Is 'Java' in example_list: {'Java' not in example_list}")
print()

# Concatenate lists
concatenated_list = example_list + str_list
print(f"Concatenated lists: {concatenated_list}")
print()

# Repeat list
repeated_list = example_list * 2
print(f"Repeated list: {repeated_list}")
print()

# Access elements by index
print(f"First element from 'example_list': {example_list[0]}")
print(f"Last element from 'example_list': {example_list[-1]}")
print()

# Slices
print(f"Slice of 'example_list': {example_list[0:2]}")
print(f"Slice with step: {example_list[2:]}")
print()

# Minimum and maximum elements
numeric_list = [2, 2.25, 1.14]
print(f"Minimum in 'numeric_list': {min(numeric_list)}")
print(f"Maximum in 'numeric_list': {max(numeric_list)}")
print()

# Replace an element
print(example_list)
example_list[1] = 3.14
print(example_list)
print()

# Replace a slice
print(example_list)
example_list[0:2] = [1, 1.5]
print(f"List after slice replacement: {example_list}")
print()

# Delete elements from a slice
print(example_list)
del example_list[0:2]
print(f"List after deleting slice: {example_list}")
print()
