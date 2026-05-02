# Python Operators
#=================

# lll Python has different types of operators:
# (0). Membership Operators
# (1). Arithmetic Operators
# (2). Comparison Operators / Relationship
# (3). Logical Operators
# (4). Bitwise Operators
# (5). Assignment Operators





# (0). Membership Operators
#---------------------------

print("D" in "Delhi")         # True
print("D" not in "Delhi")     # False
print(1 in [2, 3, 4, 5, 6])   # False





# (1). Arithmetic Operators
#---------------------------

print(5 + 2)   # 7
print(5 - 1)   # 4
print(5 * 2)   # 10
print(5 / 2)   # 2.5    (float division)
print(5 // 2)  # 2      (floor division)
print(5 % 2)   # 1      (modulus)
print(5 ** 2)  # 25     (exponent)





# (2). Relational / Comparison Operators
#--------------------------------------

print(5 > 4)    # True
print(5 >= 4)   # True
print(5 < 4)    # False
print(5 <= 4)   # False
print(5 == 4)   # False
print(5 != 4)   # True





# (3). Logical Operators
#----------------------

print(1 and 0)  # 0
print(1 or 0)   # 1
print(not 1)    # False





# (4). Bitwise Operators
#----------------------

# Bitwise AND (&)
print(2 & 3)  # 2   (010 & 011 = 010)

# Bitwise OR (|)
print(2 | 3)  # 3   (010 | 011 = 011)

# Bitwise XOR (^)
print(2 ^ 3)  # 1   (010 ^ 011 = 001)

# Bitwise NOT (~)
print(~3)     # -4

# Bitwise right shift (>>)
print(4 >> 2)  # 1   (100 >> 2 = 001)

# Bitwise left shift (<<)
print(4 << 2)  # 16  (100 << 2 = 10000)





# (5). Assignment Operators
#--------------------------

a = 3
a += 5   # Equivalent to: a = a + 5
print(a)  # 8
