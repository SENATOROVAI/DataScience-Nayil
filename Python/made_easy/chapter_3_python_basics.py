"""Note-taking for Chapter 3 'Python Basics' & exercises."""

# +
# # Date: 17/10/24
#
# ## Summary of Chapter 3 (Python Basics)
#
# In this chapter, we first became acquainted with Spyder IDE and Jupyter
# Notebook. Then, we began working with Python and learned how to use it as a
# calculator. We also performed several string manipulations.
#
# After that, we delved into the basic structure of Python code and explored
# expressions, operators, and variables. We wrote our first multi-line program
# and studied several coding principles in Python, such as multiple assignment,
# indentation, loops, and output.
#
# We also learned how the `print()` function works, which introduced us to two
# key concepts: arguments and keyword arguments.

print("Hello World!")

2 + 2

50 - 5 * 6

(50 - 5 * 6) / 4

8 / 4  # division always returns a floating point number

17 // 4  # floor division discards the fractional part

17 % 4  # % operator returns the remainder of the division

4 * 4 + 1  # result * divisor + remainder

5**2  # squared

2**8  # 2 to the power of 8

width = 20
height = 5 * 9

value_str_a = "python strings"
value_str_a

value_str_b = "doesn't"
value_str_b

print('"Isn\'t" they said.')

print("C:\\some\\name")  # note the \n before the quote

print(r"C:\some\name")  # note the r before the quote

# Concatenation and Repetition

"a" + "b"

"t" * 5

"no" * 3 + "dir"

"nil" + "abh"

text = "Join several strings within-" + "-to have them combined."

text

word = "Python"

word

word[0]

word[5]

word[-4]

word[0:2]  # characters from position 0 (included) to 2 (excluded)

word[2:5]

word[:2] + word[2:]

len(word)

variable_a = 45
print(variable_a)

variable_a = 3 + 2
print(variable_a)

2 + 3

15

variable_a

value_str = "Hello World"
value_str

print("Hello World")

variable_a = 0
variable_b = 1
while variable_a < 10:
    print(variable_a)
    variable_a, variable_b = variable_b, variable_a + variable_b

var_a, var_b = 0, 1
while var_a < 15:
    print(var_a)
    var_a, var_b = var_b, var_a + var_b

val_i = 256 * 256
print("The value of val_i is", val_i)

val_c, val_d = 0, 1
while val_c < 15:
    print(val_c, end=",")
    val_c, val_d = val_d, val_c + val_d

v_a, v_b, v_c = 5, 6, 5 * 6
print(f"when {v_a} is multiplied by {v_b}, the result is {v_c}")

name = "Nilabh"
lastname = "Nishchhal"
place = "Mumbai"
print(f"{name} {lastname} lives in {place}")

print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

# ## 3.8.1 Answer the questions
#
# 1. **What are the advantages of the Spyder IDE over a simple text editor?**
#    - Spyder provides an integrated environment for coding in Python
#    - Includes debugging tools, code completion
#    - Advanced features not available in simple text editors
#
# 2. **How are the operators written in Python?**
#    - Addition: `+`
#    - Subtraction: `-`
#    - Multiplication: `*`
#    - Division: `/`
#
# 3. **What is the difference between `*` and `**` operators in Python?**
#    - `*` is for multiplication
#    - `**` is for exponentiation
#
# 4. **What are expressions in Python, and why are they important?**
#    - Expressions are combinations of values, variables, and operators
#    - They form basic building blocks of Python programs
#    - Allow execution of operations
#
# 5. **What is a variable, and how can a value be assigned to it?**
#    - A variable is a storage location in memory with a name
#    - Assign using `=`, example: `x = 5`
#
# 6. **Can a variable be named `import` in Python?**
#    - No, `import` is a reserved keyword
#
# 7. **Are `math`, `Math`, and `MATH` equivalent in Python?**
#    - No, Python is case-sensitive
#    - These are treated as different identifiers
#
# 8. **How can expressions be grouped in Python?**
#    - Using parentheses `()`
#    - Controls order of operations
#
# 9. **Difference between syntactic and semantic error?**
#    - Syntactic: violates grammar rules
#    - Semantic: runs but produces incorrect results
#
# 10. **Default values of `sep` and `end` in `print()`?**
#     - `sep`: space `' '`
#     - `end`: newline `\\n`
# ## 3.8.2 True or False
#
# 1. **Division of even number by 2 returns int?**
#    False. Simple division always returns float.
#
# 2. **String index: positive from 0, negative from -1?**
#    True.
#
# 3. **Python strings are mutable?**
#    False. Strings are immutable.
#
# 4. **`Dream team` valid variable name?**
#    False. Cannot contain spaces.
#
# 5. **Can use `lambda` as variable name?**
#    False. Reserved keyword.
#
# 6. **Expressions end with period?**
#    False. No special end symbol needed.
#
# 7. **`a = 25` equals `a == 25`?**
#    False. Assignment vs comparison.
#
# 8. **`print()` output differs from expression evaluation?**
#    True. Print displays, evaluation computes.
#
# 9. **Semantic errors are syntax errors?**
#    False. Different types of errors.
#
# 10. **Division by zero raises runtime error?**
#     True. Causes ZeroDivisionError.

# ## 3.8.3 Practical Exercises

# 1. Join first and last name with space
first_name = "Nayil"
last_name = "SENATOROVAI"
print(first_name + " " + last_name)

# 2. Rectangle area calculation
length = 23  # Using 'length' instead of 'l'
height = 8
area = length * height
print("Area of the rectangle:", area)

# 3. Square of 32 and cube of 27
square_32 = 32**2
cube_27 = 27**3
print("Square of 32:", square_32)
print("Cube of 27:", cube_27)

# 4. Calculate equation
numeric_valuea_a = 5
numeric_valuea_b = 3
result_equation = (numeric_valuea_a + numeric_valuea_b) ** 2
print("Result of the equation:", result_equation)

# 5. Name length
name = "Nayil"
print("Length of name:", len(name))

# 6. Draw rectangle
print("******")
print("*    *")
print("*    *")
print("******")

# 7. Draw letter "R"
print("RRRR")
print("R   R")
print("RRRR")
print("R  R")
print("R   R")

# 8. Name and Age print
Name = "Nayil"
Age = 39
print(f"My name is {Name} and my age is {Age}")

# 9. Fix syntax: words loop
words = ["cat", "window", "defenestrate"]
for value_w in words:
    print(value_w, len(value_w))

# 10. Fix Fibonacci loop
value_a, value_b = 0, 1
while value_a < 15:
    print(value_a, end=", ")
    value_a, value_b = value_b, value_a + value_b
