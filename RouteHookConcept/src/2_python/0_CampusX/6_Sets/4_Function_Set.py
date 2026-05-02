# Remaining Set Functions
#-------------------------


# Some functions are universal
#-----------------------------

# These functions work on most iterables, including set.

# len    -> returns total number of elements
# min    -> returns smallest element
# max    -> returns largest element
# sorted -> returns a new sorted list (always returns list)
# sum    -> returns total sum of elements


# Set Update Methods
#--------------------

# s1.update(s2) :- Adds all elements of s2 into s1 (union update)
# s1.intersection_update(s2) :-  Keeps only common elements in s1
# s1.difference_update(s2) :- Removes elements of s2 from s1
# s1.symmetric_difference_update(s2) :- Keeps elements that are not common in both sets







s = {1, 2, 7, 3, 6, 5, 4}

print(len(s))      # 7
print(min(s))      # 1
print(max(s))      # 7
print(sum(s))      # 28

print(sorted(s))                # [1, 2, 3, 4, 5, 6, 7]
print(sorted(s, reverse=True))  # [7, 6, 5, 4, 3, 2, 1]








# union
#-------
# Definition:
# Returns a new set containing all unique elements
# from both sets. Original sets remain unchanged.

# update
#--------
# Definition:
# Adds all elements of another set into the current set.
# It modifies the original set.



s1 = {1, 4, 4, 4, 5, 7}
s2 = {2, 8, 9, 0}

print(s1.union(s2))  # {0, 1, 2, 4, 5, 7, 8, 9}
print(s1 | s2)       # {0, 1, 2, 4, 5, 7, 8, 9}

s1.update(s2)
print(s1)  # {0, 1, 2, 4, 5, 7, 8, 9}
print(s2)  # {0, 2, 8, 9}






# intersection
#--------------
# Definition:
# Returns a new set containing only the common
# elements present in both sets.

# intersection_update
#---------------------
# Definition:
# Updates the current set by keeping only
# elements found in both sets.



s1 = {1, 4, 4, 4, 5, 7}
s2 = {2, 4, 5, 6, 9, 0}

print(s1.intersection(s2))  # {4, 5}
print(s1 & s2)              # {4, 5}

s1.intersection_update(s2)
print(s1)  # {4, 5}
print(s2)  # {0, 2, 4, 5, 6, 9}






# difference
#-------------
# Definition:
# Returns elements present in the first set
# but NOT present in the second set.

# difference_update
#-------------------
# Definition:
# Removes all elements of another set
# from the current set.



s1 = {1, 4, 4, 4, 5, 7}
s2 = {2, 4, 5, 6, 9, 0}

print(s1.difference(s2))  # {1, 7}
print(s1 - s2)            # {1, 7}

s1.difference_update(s2)
print(s1)  # {1, 7}
print(s2)  # {0, 2, 4, 5, 6, 9}







# symmetric_difference
#----------------------
# Definition:
# Returns elements that are present in either set
# but NOT common in both.

# symmetric_difference_update
#-----------------------------
# Definition:
# Updates the current set by keeping only
# non-common elements from both sets.



s1 = {1, 4, 4, 4, 5, 7}
s2 = {2, 4, 5, 5, 7, 6, 9, 0}

print(s1.symmetric_difference(s2))  # {0, 1, 2, 6, 9}
print(s1 ^ s2)                      # {0, 1, 2, 6, 9}

s1.symmetric_difference_update(s2)
print(s1)  # {0, 1, 2, 6, 9}
print(s2)  # {0, 2, 4, 5, 6, 7, 9}







# isdisjoint
#------------
# Definition:
# Returns True if both sets have NO common elements.

# Example:
# {1,2}.isdisjoint({3,4}) → True


# issubset
#----------
# Definition:
# Returns True if all elements of the set
# are present in another set.

# Example:
# {1,2}.issubset({1,2,3}) → True


# issuperset
#------------
# Definition:
# Returns True if the set contains all elements
# of another set.

# Example:
# {1,2,3}.issuperset({1,2}) → True



s1 = {1, 4, 4, 4, 5, 7}
s2 = {2, 4, 5, 5, 7, 6, 9, 0}

print(s1.isdisjoint(s2))  # False
print(s1.issubset(s2))    # False
print(s1.issuperset(s2))  # False





# copy
#-------
# Definition:
# Creates a shallow copy of the set.
# Changes in copied set do not affect original set.



s1 = {1, 2, 3, 4}
s2 = s1.copy()

print(s2)  # {1, 2, 3, 4}
