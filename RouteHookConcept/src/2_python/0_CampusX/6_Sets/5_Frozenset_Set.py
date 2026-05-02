# FrozenSet
#==========

# lll A frozenset in Python is an unordered, immutable collection of elements
#     that stores unique values of different data types.

# lll A frozenset in Python is similar to a set,
#     but the main difference is:
#         👉 set is mutable (can be changed)
#         👉 frozenset is immutable (cannot be changed)
#
#       👉 FrozenSet is unordered (no fixed position)
#       👉 FrozenSet does not allow duplicate values
#       👉 FrozenSet is immutable (cannot be changed)
#       👉 FrozenSet can contain only immutable (hashable) data types
#
#     Therefore, we cannot perform adding or deleting operations on a frozenset.
#     We can only perform read operations.


# Characteristics of FrozenSet
#------------------------------

# lll Unordered               -> Items do not have a fixed position
# lll Immutable               -> Elements cannot be added or removed
# lll Does not allow duplicates
# lll Stores only immutable (hashable) elements




# create frozenset
#-------------------

# What we can pass to frozenset():
#---------------------------------
# Any iterable:
# list, tuple, set, string, range, another frozenset

fs = frozenset([1, 2, 3, 4, 5])
print(fs)  
# frozenset({1, 2, 3, 4, 5})

fs = frozenset((1, 2, 3))
fs = frozenset("abc")
fs = frozenset(range(5))



# What works and what does not work
#----------------------------------

# works  -> all READ operations
# doesn't work -> all WRITE operations

# READ operations (allowed)
#---------------------------

fs1 = frozenset([1, 2, 3, 4, 5])
fs2 = frozenset((4, 5, 6, 7, 8))

print(fs1 | fs2)  # Union
# frozenset({1, 2, 3, 4, 5, 6, 7, 8})

print(fs1 & fs2)  # Intersection
# frozenset({4, 5})

print(fs1 - fs2)  # Difference
# frozenset({1, 2, 3})

print(fs1 ^ fs2)  # Symmetric Difference
# frozenset({1, 2, 3, 6, 7, 8})

print(3 in fs1)   # Membership → True
print(len(fs1))   # Length → 5



# WRITE operations (NOT allowed)
#--------------------------------

# fs1.add(10)        ❌ Error
# fs1.remove(2)     ❌ Error
# fs1.update(fs2)   ❌ Error
# fs1.clear()       ❌ Error



# 2D set (Nested Set)
#---------------------

# Normal set inside set → NOT allowed
# frozenset allows nesting because it is immutable

fs = frozenset([1, 2, frozenset([3, 4])])

print(fs)
# frozenset({frozenset({3, 4}), 1, 2})



# Why frozenset is important
#----------------------------

# Because:
# set      → mutable → cannot be used as key
# frozenset → immutable → can be used as dictionary key

d = {frozenset([1, 2]): "Allowed"}
print(d)
# {frozenset({1, 2}): 'Allowed'}
