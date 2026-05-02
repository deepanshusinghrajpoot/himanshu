# How to create tuple
#=====================

# lll There are two ways to create a tuple:
#     1. Using type conversion
#     2. Using parentheses (for a single element, a comma is required)



# Empty tuple
#-------------

t1 = ()
print(t1)  # ()



# Creating tuple with single element (common mistake)
#-----------------------------------------------------

t2 = (2)
print(type(t2))   # <class 'int'>

# 👉 To create a single-element tuple, comma is mandatory

t2 = (2,)
print(type(t2))   # <class 'tuple'>



# Homogeneous tuple
#-------------------

t3 = (1, 2, 3, 4, 5, 6)
print(t3)  # (1, 2, 3, 4, 5, 6)



# Heterogeneous tuple
#---------------------

t4 = (2, 5, 7, True, "Rohan")
print(t4)  # (2, 5, 7, True, 'Rohan')



# 2D tuple (Nested tuple)
#-------------------------

t5 = (1, 2, 3, (4, 5, 6, 7, 8))
print(t5)  # (1, 2, 3, (4, 5, 6, 7, 8))



# Using type conversion
#-----------------------

t6 = tuple('hellow')
print(t6)  # ('h', 'e', 'l', 'l', 'o', 'w')





# How to access elements from a tuple
#====================================

#lll There are two way to access element from a tuple:
#    1. using indexing
#    2. using slicing  [included:excluded:jump]



# 1. Indexing
#-------------

# Indexing is used to access elements using their position

T = (1, (2, 3), ("Deepanshu", "Singh"))

# (i) Positive indexing
#-----------------------

print(T[0])        # 1
print(T[1][0])     # 2


# (ii) Negative indexing
#------------------------

# Negative indexing starts from the end

print(T[-1][-1])   # Singh
print(T[2][0])     # Deepanshu



# 2. Slicing
#------------

# Slicing is used to access a range of elements

T = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(T[:])        # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(T[0:3])      # (1, 2, 3)
print(T[0:])       # (1, 2, 3, 4, 5, 6, 7, 8, 9)

# step -> jump count
print(T[0::2])     # (1, 3, 5, 7, 9)
print(T[0::1])     # (1, 2, 3, 4, 5, 6, 7, 8, 9)


print(T[-4:])      # (6, 7, 8, 9)
print(T[-1:])      # (9,)

# step -> jump count (reverse direction)
print(T[-1::-2])   # (9, 7, 5, 3, 1)

# reverse the tuple
print(T[::-1])     # (9, 8, 7, 6, 5, 4, 3, 2, 1)
print(T[-1:-4:-1]) # (9, 8, 7)
