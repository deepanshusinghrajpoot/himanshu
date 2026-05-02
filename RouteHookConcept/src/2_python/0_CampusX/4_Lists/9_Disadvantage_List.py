# Disadvantages of Python Lists
#===============================

# (i)   Slower compared to arrays for large data
# (ii)  Risky usage due to reference behavior
# (iii) Uses more memory than arrays





# (ii) Risky Usage Example
#--------------------------

a = [1, 2, 3]
b = a   # b references the same list as a

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

b.append(4)  

print(a)  # [1, 2, 3, 4]  -> a is also changed!
print(b)  # [1, 2, 3, 4]

# Why? Because a and b point to the same memory location





# Safe way using copy()
#-----------------------

a = [1, 2, 3]
b = a.copy()  # Create a shallow copy

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

b.append(4)  

print(a)  # [1, 2, 3]    -> original list remains safe
print(b)  # [1, 2, 3, 4] -> new list updated

# ✅ Lesson: Always use copy() if you want independent lists
