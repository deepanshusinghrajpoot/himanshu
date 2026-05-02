# Set supports the following operations:
#---------------------------------------

# lll There are three main types of operations on a set:

# 1. Membership operations
#    👉 in, not in

# 2. Looping operations
#    👉 for loop

# 3. Set operations
#    1. union (|)                :- Returns all unique elements from both sets
#    2. intersection (&)         :- Returns common elements from both sets
#    3. difference (-)           :- Returns elements present in first set only
#    4. symmetric_difference (^) :- Returns elements not common to both sets







# Union (|)
#-----------
# Definition:
# Union returns a new set containing all unique elements
# from both sets.

# Example:
# s1 | s2



# Intersection (&)
#------------------
# Definition:
# Intersection returns a new set containing only
# the common elements present in both sets.

# Example:
# s1 & s2



# Difference (-)
#----------------
# Definition:
# Difference returns a new set containing elements
# that are present in the first set but NOT in the second set.

# Example:
# s1 - s2



# Symmetric Difference (^)
#-------------------------
# Definition:
# Symmetric Difference returns a new set containing elements
# that are present in either of the sets but NOT common in both.

# Example:
# s1 ^ s2



# Membership Test
#-----------------
# Definition:
# Used to check whether an element exists in a set.

# Operators:
# in, not in



# Iteration
#-----------
# Definition:
# Used to access each element of a set one by one
# using a loop.





s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}


# Union (|)
print(s1 | s2)      # {1, 2, 3, 4, 5, 6, 7, 8}


# Intersection (&)
print(s1 & s2)      # {4, 5}


# Difference (-)
print(s1 - s2)      # {1, 2, 3}


# Symmetric Difference (^)
print(s1 ^ s2)      # {1, 2, 3, 6, 7, 8}





# Membership operation
#======================

s = {1, 2, 3, 4}

print(1 in s)        # True
print(1 not in s)    # False
print(9 not in s)    # True





# Iteration operation
#=====================

s = {1, 2, 3, 4}

for i in s:
    print(i, end=" ")   # 1 2 3 4
