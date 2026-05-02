# Data Types in Python
#--------------------

# Python data types are mainly divided into two type:
# 1. Primitive
# 2. Non-Primitive


# ✅ Primitive Data Type
# .......................
# lll Primitive data types store a single, simple value and do not have an internal structure.

# Example: int, float, bool, str



# ✅ Non-Primitive Data Type
# ...........................
# lll Non-primitive data types store multiple values and have an internal structure.

# Example: list, tuple, set, dict



# 🎯 If Interviewer Asks “Which are most used?”
# 👉 list, dict, string, int, float



# (1). Integer (Primitive)
#------------------------

# Used to store whole numbers
# Example range: up to 1e308 (1 × 10^308)

print(8)   # 8




# (2). Float / Decimal (Primitive)
#--------------------------------

# Used to store decimal numbers
# Example range: up to 1.7e308 (1.7 × 10^308)

print(7.7)  # 7.7




# (3). Boolean (Primitive)
#------------------------

# Used to store True or False values

print(True)  # True




# (4). String (Primitive)
#-----------------------

# Used to store text or character data

print("Hello World")  # Hello World




# (5). Complex (Primitive)
#------------------------

# Used to store complex numbers (real + imaginary)

print(5 + 6j)  # 5+6j






# (6). List (Non-Primitive) -> Similar to Array in C
#---------------------------------------------------

# Used to store multiple values in a single variable

print([1, 2, 3, 4, 5])  # [1, 2, 3, 4, 5]




# (7). Tuple (Non-Primitive)
#---------------------------

# Similar to list but immutable (cannot be changed)

print((1, 2, 3, 4, 5))  # (1, 2, 3, 4, 5)




# (8). Set (Non-Primitive)
#------------------------

# Used to store unique values (no duplicates)
# Unordered collection

print({1, 2, 3, 4, 5})  # {1, 2, 3, 4, 5}




# (9). Dictionary (Non-Primitive)
#--------------------------------

# Stores data in key-value pairs

print({"name": "Deepanshu", "gender": "male", "weight": 70})
# {'name': 'Deepanshu', 'gender': 'male', 'weight': 70}






# Summary
#--------

# Primitive Data Types:
# int, float, boolean, string, complex

# Non-Primitive Data Types:
# list, tuple, dictionary




# How to find data type
#=====================

# type() function is used to find the data type of a variable

print(type(2))   # <class 'int'>
