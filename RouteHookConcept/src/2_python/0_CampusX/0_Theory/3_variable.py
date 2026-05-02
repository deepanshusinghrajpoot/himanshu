

#lll ✔ Python is dynamically typed language,

# meaning:
#    Variables are not bound to a specific data type
#    We can assign different types of values at different times
#    The data type is determined at runtime
   











# Compiler and Interpreter
#-------------------------

# Compiler:
# - Translates the entire code at once
# - If error occurs, program will not run
# - Example: C, C++, Java

# Interpreter:
# - Translates code line by line
# - Executes code step by step
# - Stops where error occurs
# - Example: Python, JavaScript






# Static Typing vs Dynamic Typing
#--------------------------------

# Static Typing:
# - Variable is bound to a fixed data type
# - Data type must be declared in advance
# - Example: C, C++, Java

# Dynamic Typing:
# - Variable is NOT bound to a fixed data type
# - Data type is decided at runtime
# - Example: Python


a = 5
print(a)   # 5






# Static Binding vs Dynamic Binding
#----------------------------------

# Static Binding:
# - Variable cannot change its data type
# - Example: C, C++

# Dynamic Binding:
# - Variable can change its data type at runtime
# - Example: Python

b = 5
print(b)                   # 5

b = "Deepanshu Singh"
print(b)                   # Deepanshu Singh






# Stylish Declaration Techniques
#--------------------------------

# Multiple variable assignment in one line

p, q, r = 1, 2, 3
print(p + q + r)   # 6






# Keywords and Identifiers
#=========================


# Keywords
#----------

# Keywords are reserved words in Python
# They have predefined meaning
# Python has 32 keywords (version dependent)
# Example: if, else, for, while, True, False, None






# Identifiers
#-------------

# Identifiers are names of variables, functions, classes

# Rules:
# - Cannot start with a digit
# - Can start with a letter or underscore (_)
# - Cannot use special characters except underscore (_)
# - Cannot be a keyword

# Valid: name, _age, total_sum
# Invalid: 1name, @age, if






# Input in Python
#================

# input() always returns data in STRING format

a = input("Enter the number a: ")
b = input("Enter the number b: ")

print("a + b =", a + b)
# Output example:
# a = 7 , b = 3
# a + b = 73   (String Concatenation)






# To perform addition, type conversion is required

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

print("a + b =", a + b)
# Output: 10
