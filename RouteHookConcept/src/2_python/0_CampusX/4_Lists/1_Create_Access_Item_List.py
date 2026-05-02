# How to create a List
#====================

#lll There are two ways to create a list:
#      1. Using type conversion
#      2. Using square brackets



# Create a list using type conversion
#------------------------------------

# list() can convert an iterable into a list

print(list('hellow'))
# ['h', 'e', 'l', 'l', 'o', 'w']

print(list((1, 2, 4))) # [1, 2, 4]



# How to create an empty list
#----------------------------

print([])
# []




# How to create a 1D list
#------------------------

# A single-level list containing elements

print([1, 2, 3, 4, 5, "Deepanshu"])
# [1, 2, 3, 4, 5, 'Deepanshu']




# How to create a 2D list
#------------------------

# A list containing another list

print([1, 2, 3, 4, 5, [2, 3, 4]])
# [1, 2, 3, 4, 5, [2, 3, 4]]




# How to create a 3D list
#------------------------

# A list containing nested lists at multiple levels

print([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]







# How to access elements from list
#==================================


#lll There are two way to access element from a list
# 1. using indexing
# 2. using slicing  [included:excluded:jump]


# 1. Indexing
#------------

# Indexing is used to access elements using their position

L = [1, [2, 3], ["Deepanshu", "Singh"]]

# (i) Positive indexing
#----------------------

print(L[0])       # 1
print(L[1][0])    # 2


# (ii) Negative indexing
#----------------------

# Negative indexing starts from the end

print(L[-1][-1])  # Singh
print(L[2][0])    # Deepanshu




# 2. Slicing
#-----------

# Slicing is used to access a range of elements

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L[:])       # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[0:3])     # [1, 2, 3]
print(L[0:])      # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# step -> jump count
print(L[0::2])    # [1, 3, 5, 7, 9]
print(L[0::1])    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(L[-4:])     # [6, 7, 8, 9]
print(L[-1:])     # [9]

# step -> jump count (reverse direction)
print(L[-1::-2])  # [9, 7, 5, 3, 1]

# reverse the list
print(L[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(L[-1:-4:-1]) # [9, 8, 7]









