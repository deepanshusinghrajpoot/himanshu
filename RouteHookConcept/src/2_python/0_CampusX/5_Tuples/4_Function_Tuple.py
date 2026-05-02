# Remaining Tuple Functions
#---------------------------

# Some functions are universal
#-----------------------------

# These functions work on most iterables, including tuples.

# len    → returns total number of elements
# min    → returns smallest element
# max    → returns largest element
# sorted → returns a new sorted list (tuple remains unchanged)
# sum    → returns total sum of elements


T = (1, 2, 7, 3, 6, 5, 4)

print(len(T))      # 7
print(min(T))      # 1
print(max(T))      # 7
print(sum(T))      # 28

print(sorted(T))                # [1, 2, 3, 4, 5, 6, 7]
print(sorted(T, reverse=True))  # [7, 6, 5, 4, 3, 2, 1]





# count() → used to find frequency of an element
#-----------------------------------------------

T = (1, 4, 4, 4, 5, 7)

print(T.count(4))  # 3
print(T.count(7))  # 1





# index() → used to find index of an element
#-------------------------------------------

# Returns the index of the first occurrence

T = (11, 22, 55, 33, 44, 33)

print(T.index(33))  # 3
print(T.index(44))  # 4
