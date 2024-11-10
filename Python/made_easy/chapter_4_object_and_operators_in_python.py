# %%
"""Note-taking for Chapter 4 'Object and Operators in Python' & exercises."""

import math

# # Chapter 4: Objects and Operators in Python
#
# ## 4.1. Variables
#
# - Variables in Python are pointers to objects
# - They don't have values themselves, but point to assigned objects
# - Python automatically determines the variable type
#
# Example:
# ```python
# x = 38
# y = "emailid@python.com"
# print(x)  # Outputs: 38
# print(y)  # Outputs: emailid@python.com
# ```
#
# ### 4.1.1. Assignment Operator
#
# - The "=" sign is used to assign values to variables
# - It doesn't mean "equals", but means "assign"
#
# Example:
# ```python
# x = 38  # x - variable name, = - assignment operator, 38 - assigned value
# ```
#
# ### 4.1.2. Variable Names
#
# - Can contain letters, numbers, underscores
# - Must not start with a number
# - Are case-sensitive
# - Cannot match keywords
#
# Example:
# ```python
# valid_name = 10
# Valid_name = 20  # This is a different variable
# # 5fingers = 5  # Not allowed, starts with a number
# # sales data = 100  # Not allowed, contains a space
# ```
#
# ## 4.2. Program Structure
#
# - Programs consist of modules
# - Modules contain expressions
# - Expressions contain operators
# - Operators create and process objects
#
# ## 4.3. Objects
#
# - In Python, all data are objects
# - Objects have a type, value, and associated operations
#
# ### 4.3.1. Object Classification
#
# - Built-in and user-defined
# - Mutable and immutable
#
# Example table from the book:
#
# | Object Type | Object Examples | Mutable or Immutable? |
# |-------------|-----------------|------------------------|
# | Numbers     | 1234, 3.1415, 3+4j | Immutable           |
# | Strings     | 'nilabh', "Bob's" | Immutable            |
# | Lists       | [1, [2, 'three'], 4.5] | Mutable         |
# | Dictionaries| {'food': 'spam', 'taste': 'yum'} | Mutable|
#
# ### 4.3.2. Advantages of Built-in Types
#
# - Simplify programming
# - More efficient than user-defined structures
# - Are a standard part of the language
#
# Example from the book:
# ```python
# # Calculating rectangle area
# Length = 5
# Width = 8
# Area = Length * Width
# print("Area of the Rectangle is", Area)
# print("Perimeter of the rectangle is", 2 * (Length + Width))
# ```
#
# ## 4.4. Standard Type Hierarchy
#
# ### 4.4.1. Built-in Constants
#
# - None: single value, equivalent to False
# - NotImplemented: used in numeric methods
# - Ellipsis: accessed via the ... literal or the Ellipsis name
#
# ### 4.4.2. Numeric Types
#
# - Integers (int): unlimited range
# - Boolean values (bool): subtype of integers, True and False
# - Floating-point numbers (float): double-precision floating-point numbers
# - Complex numbers (complex): pair of floating-point numbers
#
# Example:
# ```python
# x = 2
# y = 3.14
# z = 1 + 2j
# print(
#     type(x), type(y), type(z)
# )  # Outputs: <class 'int'> <class 'float'> <class 'complex'>
# ```
#
# ### 4.4.3. Sequences
#
# Divided into mutable and immutable:
#
# Immutable:
# - Strings (str)
# - Tuples (tuple)
# - Bytes (bytes)
#
# Mutable:
# - Lists (list)
# - Byte arrays (bytearray)
#
# Example:
# ```python
# s = "Hello"
# t = (1, 2, 3)
# l = [1, 2, 3]
# print(s[0], t[1], l[2])  # Outputs: H 2 3
# l[0] = 10  # Allowed for lists
# # s[0] = "h"  # Will raise an error for strings
# ```
#
# ### 4.4.4. Sets
#
# - set: mutable set
# - frozenset: immutable set
#
# Example:
# ```python
# s = {1, 2, 3}
# s.add(4)  # Allowed for set
# fs = frozenset([1, 2, 3])
# # fs.add(4)  # Will raise an error
# ```
#
# ### 4.4.5. Mappings
#
# - dict: dictionary, mutable key-value mapping
#
# Example:
# ```python
# d = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(d["brand"])  # Outputs: Ford
# ```
#
# ## 4.5. Operations with Python Objects
#
# Examples of simple operations:
# ```python
# 14 + 26  # Integer addition
# 1.5 * 4  # Floating-point multiplication
# 2**100  # 2 to the power of 100
# 4 / 2  # Division (always returns float)
# 5 > 4  # Logical expression
# ```
#
# ## 4.6. Operators
#
# ### 4.6.1. Arithmetic operators:
# +, -, *, /, %, //, **
#
# ### 4.6.2. Assignment operators:
# =, +=, -=, *=, /=, %=, //=, **=
#
# ### 4.6.3. Comparison operators:
# ==, !=, >, <, >=, <=
#
# ### 4.6.4. Logical operators:
# and, or, not
#
# ### 4.6.5. Identity and membership operators:
# is, is not, in, not in
#
# ## 4.7. Indentation
#
# - Used to define code blocks
# - Usually 4 spaces are used
#
# Example of correct indentation usage:
# ```python
# if True:
#     print("Hello")
# ```
# Example that raises an error:
# ```python
# if True:
#     print("Hello")  # IndentationError: expected an indented block
# ```
#
# ## 4.8. Comments in Python
#
# - Start with the # symbol
#
# Example:
# ```python
# # This is a comment
# print("Hello")  # This is also a comment
# ```
#
# ## 4.9. Order of Execution
#
# - Determined by operator precedence
# - Can be changed using parentheses
#
# Example of changing execution order with parentheses:
# ```python
# print((2 + 3) * 4)  # Will output 20
# print(2 + 3 * 4)  # Will output 14
# ```
#
# ## 4.10. Dynamic Typing
#
# - Variables can change type during program execution
#
# Example from the book:
# ```python
# six = 6
# print(six)  # Will output: 6
# six = "six"
# print(six)  # Will output: six
# ```
#
# ## 4.11. Strong Typing
#
# - Despite dynamic typing, Python strictly checks types during operations
#
# Example of a type error:
# ```python
# "day" + 1  # Will raise TypeError
# ```
# Correct version:
# ```python
# "day" + str(1)  # Will output: 'day1'
# ```
#
# ## 4.12. Logical and Physical Lines
#
# - Physical line: what is visible in the code
# - Logical line: what Python considers as a single expression
#
# Example with two physical and logical lines:
# ```python
# i = 5
# print(i)
# ```
# Example with one physical but two logical lines:
# ```python
# i = 5
# print(i)
# ```
#
# Additional example from the book (calculating rectangle area):
# ```python
# # calculating rectangle area
# Length = 5
# Width = 8
# Area = Length * Width
# print("Area of the Rectangle is", Area)
# print("Perimeter of the rectangle is", 2 * (Length + Width))
# ```
# Output:
# ```
# Area of the Rectangle is 40
# Perimeter of the rectangle is 26
# ```
#
# This example demonstrates the use of variables, arithmetic operations, and the print() function, and also shows how Python automatically adds spaces when outputting for better readability.

# # 4.14. Exercises
#
# ## 4.14.1. Answer the questions
#
# 1. **What is a variable in Python? How is it different from an object?**
#
#    A variable in Python is a name that refers to an object in memory. It's essentially a pointer or reference. An object, on the other hand, is a piece of data with a type and associated methods. The main difference is that variables are names pointing to objects, while objects are the actual data in memory.
#
# 2. **What are the rules for naming variables in Python? Write which names can be used and which cannot.**
#
#    Rules for variable names in Python:
#    - Can contain letters, numbers, and underscores
#    - Must start with a letter or underscore
#    - Are case-sensitive
#    - Cannot be Python keywords
#
#    Valid names: `my_var`, `_count`, `item1`, `camelCase`
#    Invalid names: `2ndVar`, `class`, `for`, `my-var`
#
# 3. **What are the advantages of built-in data types?**
#
#    Advantages of built-in data types:
#    - Simplify programming
#    - More efficient than user-defined structures
#    - Standard across all Python implementations
#    - Optimized for performance
#    - Provide a consistent interface for common operations
#
# 4. **What is an immutable object? Which objects in Python are immutable?**
#
#    An immutable object is one whose state cannot be modified after creation. Immutable objects in Python include:
#    - Numbers (int, float, complex)
#    - Strings
#    - Tuples
#    - Frozen sets
#    - Boolean values
#
# 5. **What is called an object identifier? How is it different from the type?**
#
#    An object identifier is a unique integer representing the object's memory address, obtained using `id()`. The type defines the kind of data the object represents and its available operations. An identifier is unique to each object instance, while many objects can share the same type.
#
# 6. **What do the functions chr() and ord() do? How are they related?**
#
#    `chr()` converts an integer to its corresponding Unicode character. `ord()` converts a Unicode character to its integer code point. They are inverse operations of each other.
#
# 7. **What is an operator? How many types of operators exist in Python? Name them all.**
#
#    An operator is a symbol that tells the interpreter to perform specific operations. Python has six main types of operators:
#    1. Arithmetic operators
#    2. Assignment operators
#    3. Comparison operators
#    4. Logical operators
#    5. Identity operators
#    6. Membership operators
#
# 8. **The operators / and // perform division. What's the difference between them?**
#
#    `/` performs float division, always returning a float result. `//` performs floor division, returning the largest integer not greater than the result (also known as integer division).
#
# 9. **What value do logical operators return?**
#
#    Logical operators return Boolean values: `True` or `False`.
#
# 10. **Why are indentations important in the Python programming language?**
#
#     Indentations in Python define code blocks and structure. They replace curly braces or keywords used in other languages to denote the beginning and end of code blocks.
#
# 11. **How do you write comments in Python? What are they needed for?**
#
#     Comments in Python start with `#`. They are used to explain code, make it more readable, and provide additional information. They are ignored by the Python interpreter.
#
# 12. **How can you change the order of execution of operators in Python?**
#
#     The order of execution in Python can be changed using parentheses, similar to mathematical expressions.
#
# 13. **What's the difference between a logical line and a physical line of code?**
#
#     A physical line is what you see in the code editor. A logical line is what Python interprets as a single statement. Multiple logical lines can be on one physical line using semicolons.
#
# ## 4.14.2. True or False
#
# 1. **Variables in Python receive the value assigned to them.**
#
#    False. Variables in Python refer to objects, they don't receive values directly.
#
# 2. **In Python, you need to define the type of a variable before creating it.**
#
#    False. Python uses dynamic typing, so you don't need to declare variable types.
#
# 3. **The expressions x = 38 and x == 38 do not mean the same thing.**
#
#    True. `x = 38` is an assignment, while `x == 38` is a comparison.
#
# 4. **In Python, we perform operations on objects.**
#
#    True. All data in Python are objects, and operations are performed on these objects.
#
# 5. **Python keywords can be used as variable names.**
#
#    False. Python keywords cannot be used as variable names.
#
# 6. **User-defined data types work more efficiently than built-in ones.**
#
#    False. Built-in data types are generally more efficient as they are optimized at a lower level.
#
# 7. **An object's identifier never changes after its creation.**
#
#    True. The identifier (memory address) of an object remains constant throughout its lifetime.
#
# 8. **Comments make the program more readable and easier to understand.**
#
#    True. Comments help explain code and improve readability.
#
# 9. **Indentations are just decorations and a way to make the program more beautiful and readable.**
#
#    False. In Python, indentations are crucial for defining code structure and blocks.
#
# 10. **The % operator returns the remainder of dividing two numbers.**
#
#     True. The `%` operator is the modulo operator, which returns the remainder of division.

# Here's the translation of the practical tasks into English, formatted in Markdown:
#
# ## 4.14.3. Practical Tasks

# 1. Peter receives a salary of 12,000 per month. Write code to calculate his savings by the end of the year if he saves 20% of his salary each month.

# +
# 1. Peter's savings calculation
monthly_salary = 12000
savings_rate = 0.20
months = 12

annual_savings = monthly_salary * savings_rate * months
print(f"Peter's annual savings: {annual_savings}")
# -

# 2. The distance between Mumbai and Delhi is 1,422 km. If Sundar drives a car at an average speed of 72 km/h, how long will it take him to cover this distance?

# +
# 2. Travel time calculation
distance = 1422  # km
speed = 72  # km/h

time = distance / speed
print(f"Travel time: {time} hours")


# -

# 3. Human body temperature ranges from 97 to 99°F. How would this range look in degrees Celsius?


# +
# 3. Temperature conversion
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


LOW_F, HIGH_F = 97, 99
low_c: float = fahrenheit_to_celsius(LOW_F)
high_c: float = fahrenheit_to_celsius(HIGH_F)
print(f"Temperature range in Celsius: {low_c:.2f}°C to {high_c:.2f}°C")
# -

# 4. Given a six-digit number, write a program to calculate the sum of all digits in this number.

# 4. Sum of digits in a six-digit number
number = 123456
digit_sum = sum(int(digit) for digit in str(number))
print(f"Sum of digits in {number}: {digit_sum}")

# 5. We have data on monthly sales of 5 bookstores in Brooklyn:
#    A = $6500, B = $8000, C = $12000, D = $4900, and E = $5600.
#    Assuming there are only 5 bookstores in Brooklyn, find out the market share of each store. Also, check what the sum of market shares of all stores will be. (Market share means the ratio of one participant to all others.)

# +
# 5. Market share calculation
sales = {"A": 6500, "B": 8000, "C": 12000, "D": 4900, "E": 5600}
total_sales = sum(sales.values())

market_shares = {store: sale / total_sales for store, sale in sales.items()}
for store, share in market_shares.items():
    print(f"Market share of store {store}: {share:.2%}")
print(f"Sum of market shares: {sum(market_shares.values()):.2f}")
# -

# 6. The average of three numbers is 45. The first number is greater than the average by the same amount that the second number is less than the average. Find the third number.

# 6. Finding the third number
average = 45
difference = 5  # Assumed difference, you might need to adjust this
num1 = average + difference
num2 = average - difference
num3 = 3 * average - num1 - num2
print(f"The third number is: {num3}")

# 7. John buys a mobile phone for 1800 in Calcutta and sells it in Mumbai at a 25% profit. If his overhead costs are 5% of the selling price, what is the selling price?

# +
# 7. Selling price calculation
cost_price = 1800
profit_rate = 0.25
overhead_rate = 0.05

selling_price = cost_price * (1 + profit_rate) / (1 - overhead_rate)
print(f"Selling price: {selling_price:.2f}")
# -

# 8. Find the volume and surface area of a cube with a diagonal of 5 m.
#    Hint: V = (d³) / (3√3), S = (2d²) / 3

# +
# 8. Cube volume and surface area
diagonal = 5
edge = diagonal / math.sqrt(3)
volume = edge**3
surface_area = 6 * edge**2

print(f"Cube volume: {volume:.2f} cubic meters")
print(f"Cube surface area: {surface_area:.2f} square meters")
# -

# 9. Three metal cubes with edge lengths of 3, 4, and 5 cm respectively are melted down into a single cube. Find the edge length of the new cube.

# 9. New cube edge length
volumes = [3**3, 4**3, 5**3]
total_volume = sum(volumes)
new_edge = total_volume ** (1 / 3)
print(f"New cube edge length: {new_edge:.2f} cm")

# 10. Given a six-digit number, write a program to obtain the number with the reversed order of digits.

# 10. Reversing a six-digit number
number = 123456
reversed_number = int(str(number)[::-1])
print(f"Reversed number: {reversed_number}")
