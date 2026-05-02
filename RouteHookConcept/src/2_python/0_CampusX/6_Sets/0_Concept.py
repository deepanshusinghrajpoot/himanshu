
# Sets
#======

# lll A set in Python is an unordered, mutable collection of elements
#     that stores unique values of different data types.

# lll A set in Python is different from a list and tuple,
#     because:
#       👉 Set is unordered (no fixed position)
#       👉 Set does not allow duplicate values
#       👉 Set is mutable (can be changed)
#       👉 Set can contain only immutable (hashable) data types

#     Therefore, we can perform adding and deleting operations on a set,
#     but we cannot access elements using index positions.




# Characteristics of Set
#------------------------

# lll Unordered                             -> Items do not have a fixed position
# lll Mutable                               -> Elements can be added or removed
# lll Does not allow duplicates
# lll Stores only immutable (hashable) elements



# A set is an unordered collection of items.
# Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# However, a set itself is mutable. We can add or remove items from it.

# Set can also be used to perform mathematical set operations
# like union, intersection, difference, symmetric difference, etc.




# Cannot contain mutable data types
#----------------------------------

# Ques: Set inside set -> Not possible

# Example (Invalid)
#------------------

# S = {1, 2, {3, 4}}   # ❌ Error (set is mutable)


# Example (Valid)
#----------------

S = {1, 2, (3, 4)}    # ✅ tuple is immutable
print(S)



# Duplicate values are automatically removed
#--------------------------------------------

S = {1, 2, 2, 3, 3, 4}
print(S)
# {1, 2, 3, 4}
