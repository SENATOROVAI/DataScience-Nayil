# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---
"""Note-taking for Chapter 3 'Python Basics' & exercises."""

# # Date: 17/10/24
#
# ## Summary of Chapter 3 (Python Basics)
#
# In this chapter, we first became acquainted with Spyder IDE and Jupyter Notebook. Then, we began working with Python and learned how to use it as a calculator. We also performed several string manipulations. After that, we delved into the basic structure of Python code and explored expressions, operators, and variables.
#
# We wrote our first multi-line program and studied several coding principles in Python, such as multiple assignment, indentation, loops, and output. We also learned how the `print()` function works, which introduced us to two key concepts: arguments and keyword arguments.

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

print("C:\\some\name")  # note the \n before the quote

print(r"C:\some\name")  # note the r before the quote

# Concatenation and Repetition
"a" + "b"
"t" * 5
"no" * 3 + "dir"

# "nil" "abh"
"nil" + "abh"

# +
# text = "Join several strings within-" "-to have them combined."

text = "Join several strings within-" + "-to have them combined."
# -

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

# +
variable_a = 45

print(variable_a)

# +
variable_a = 3 + 2

print(variable_a)
# -

2 + 3

15

variable_a

# +
# "Hello World"

value_str = "Hello World"

value_str
# -

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

# +
v_a, v_b, v_c = 5, 6, 5 * 6

# print("when {} is multiplied by {}, the result is {}".format(v_a, v_b, v_c))

print(f"when {v_a} is multiplied by {v_b}, the result is {v_c}")

# +
name = "Nilabh"
lastname = "Nishchhal"
place = "Mumbai"

# print("{} {} lives in {}".format(name, lastname, place))

print(f"{name} {lastname} lives in {place}")
# -

print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

# ## 3.8.1 Answer the questions
#
# 1. **What are the advantages of the Spyder IDE over a simple text editor?**
#    - Spyder provides an integrated environment for coding in Python, with debugging tools, code completion, and other advanced features, unlike a simple text editor.
#
# 2. **How are the operators for addition, subtraction, multiplication, and division written in Python?**
#    - Addition: `+`, Subtraction: `-`, Multiplication: `*`, Division: `/`
#
# 3. **What is the difference between the `*` and `**` operators in Python?**
#    - `*` is used for multiplication, while `**` is used for exponentiation.
#
# 4. **What are expressions in Python, and why are they important?**
#    - Expressions are combinations of values, variables, and operators. They are crucial because they form the basic building blocks of Python programs, allowing the execution of operations.
#
# 5. **What is a variable, and how can a value be assigned to it in Python?**
#    - A variable is a storage location in memory with a name. You assign a value using the assignment operator `=`, for example, `x = 5`.
#
# 6. **Can a variable be named `import` in Python? Justify your answer.**
#    - No, `import` is a reserved keyword in Python and cannot be used as a variable name.
#
# 7. **Are the names `math`, `Math`, and `MATH` equivalent in Python? Justify your answer.**
#    - No, Python is case-sensitive, so `math`, `Math`, and `MATH` are treated as different identifiers.
#
# 8. **How can expressions be grouped in Python?**
#    - Expressions can be grouped using parentheses `()` to control the order of operations.
#
# 9. **What is the difference between a syntactic error and a semantic error?**
#    - A syntactic error occurs when the code violates the grammar rules of Python, while a semantic error happens when the code runs but produces incorrect results.
#
# 10. **What are the default values of the keyword arguments `sep` and `end` in the syntax of the `print()` function?**
#    - The default value of `sep` is a space `' '`, and the default value of `end` is a newline character `\n`.

# ## 3.8.2 True or False
#
# 1. **Simple division of an even number by 2 returns an object of type int (integer).**
#    False. Simple division (using `/`) in Python always returns a float, even if dividing even numbers.
#
# 2. **A positive string index starts from 0, and a negative index starts from -1.**
#    True.
#
# 3. **Python strings can be modified, or in other words, they are mutable.**
#    False. Strings in Python are immutable, meaning they cannot be changed once created.
#
# 4. **`Dream team` is a valid variable name in Python.**
#    False. Variable names in Python cannot contain spaces.
#
# 5. **In Python, you can give a variable the name `lambda`.**
#    False. `lambda` is a reserved keyword in Python and cannot be used as a variable name.
#
# 6. **Expressions in Python end with a period (`.`).**
#    False. Python statements do not end with any special symbol (unlike some other languages like JavaScript or C).
#
# 7. **The expressions `a = 25` and `a == 25` in Python are equivalent.**
#    False. `a = 25` is an assignment, while `a == 25` is a comparison.
#
# 8. **The output of an expression using the `print()` function is not the same as the evaluation of that expression.**
#    True. The `print()` function only displays the result, while the actual evaluation occurs when the expression is executed.
#
# 9. **Semantic errors are a subtype of syntax errors.**
#    False. Semantic errors relate to the logic of the program, while syntax errors occur when the code does not conform to Python's grammar.
#
# 10. **Division by zero raises a runtime error.**
#     True. Division by zero is undefined and causes a `ZeroDivisionError` at runtime.

# ## 3.8.3 Practical Exercises
#
# 1. **Write a program that joins your first and last name with a space between them.**
#

# 1. Join first and last name with a space between them
first_name = "Nayil"
last_name = "SENATOROVAI"
print(first_name + " " + last_name)

# 2. **A rectangle has a length `l` and height `h`. Write code to compute the area of a rectangle with a height of 8 and a length of 23.**

# 2. Compute the area of a rectangle with a height of 8 and a length of 23
length = 23  # Renamed 'l' to 'length' to avoid confusion with the number 1
height = 8
area = length * height
print("Area of the rectangle:", area)

# 3. **What is the square of 32 and the cube of 27? Write an operator to answer this question.**

# 3. Square of 32 and cube of 27
square_32 = 32**2
cube_27 = 27**3
print("Square of 32:", square_32)
print("Cube of 27:", cube_27)

# 4. **Write the following equation in Python. Assign numeric values to the variables and compute the result.**

# 4. Equation (a + b)^2 = a^2 + b^2 + 2ab
numeric_valuea_a = 5
numeric_valuea_b = 3
result_equation = (numeric_valuea_a + numeric_valuea_b) ** 2
print("Result of the equation:", result_equation)

# 5. **Find the length of your name using a single line of Python code.**

# 5. Find the length of your name
name = "Nayil"
print("Length of name:", len(name))

# 6. **Draw a rectangle using the `print()` function.**

# 6. Draw a rectangle using the print function
print("******")
print("*    *")
print("*    *")
print("******")

# 7. **Draw the letter "R" using simple geometry and the `print()` function.**

# 7. Draw the letter "R" using simple geometry and print function
print("RRRR")
print("R   R")
print("RRRR")
print("R  R")
print("R   R")

# 8. **Create a variable `Name` with your name and a variable `Age` with your age. Write a `print()` statement that outputs "My name is Name and my age is Age".**

# 8. Create a variable Name with your name and Age, and print the output
Name = "Nayil"
Age = 39
print(f"My name is {Name} and my age is {Age}")

# 9. **Fix the syntax error in the following code:**

# 9. Fix the syntax error in the following code
words = ["cat", "window", "defenestrate"]
for value_w in words:
    print(value_w, len(value_w))

# 10. **Fix the syntax error in the following code:**

# 10. Fix the syntax error in the Fibonacci loop code
value_a, value_b = 0, 1
while value_a < 15:
    print(value_a, end=", ")
    value_a, value_b = value_b, value_a + value_b
