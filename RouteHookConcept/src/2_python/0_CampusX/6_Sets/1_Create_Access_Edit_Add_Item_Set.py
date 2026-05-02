
# How to create set
#==================

# lll There are two ways to create a set:
#     1. Using type conversion (set())
#     2. Using curly braces {}
#
# lll Note:
#     👉 Empty set cannot be created using {}
#     👉 Use set() to create an empty set




# Empty Set
#----------

s1 = {}            # By default, this creates a dictionary
print(s1)          # {}
print(type(s1))    # <class 'dict'>


# Correct way to create empty set
#--------------------------------

s2 = set()
print(s2)          # set()
print(type(s2))    # <class 'set'>




# 1D Set
#--------

s3 = {1, 2, 3}
print(s3)          # {1, 2, 3}
print(type(s3))    # <class 'set'>




# Homogeneous Set
#-----------------

s4 = {1, 2, 3, 4, 5, 6}
print(s4)          # {1, 2, 3, 4, 5, 6}




# Heterogeneous Set
#-------------------

s5 = {2, 5, 7, True, "Rohan"}
print(s5)
# {True, 2, 5, 7, 'Rohan'}

s5 = {1, 2, 5, 7, True, "Rohan"}
print(s5)
# {1, 2, 5, 7, 'Rohan'}
# (True is treated as 1)

s5 = {1, 2, 5, 7, (8, 9, 10), "Rohan"}
print(s5)
# {1, 2, 5, 7, (8, 9, 10), 'Rohan'}




# Using Type Conversion
#----------------------

s6 = set('hello')
print(s6)
# {'h', 'e', 'l', 'o'}




# Duplicate Not Allowed
#-----------------------

s7 = {1, 2, 3, 3, 4, 4, 1, 2, 2}
print(s7)
# {1, 2, 3, 4}






# Access Items
#==============

# Not allowed because set is unordered





# Edit Items
#============

# Not allowed because items are immutable








# Adding Items
#==============

# lll There are two common ways to add elements to a set:
#-------------------------------------------------------
# 1. add()    :- Adds a single element to a set
# 2. update() :- Adds multiple elements to a set





# add() → add one item
#---------------------

a1 = {11, 22, 55, 66}

a1.add(33)
print(a1)
# {11, 22, 33, 55, 66}




# update() → add multiple items
#-------------------------------

a2 = {11, 22, 55, 66}

a2.update([77, 88, 99, 22, 33, 44, 55])
print(a2)
# {11, 22, 33, 44, 55, 66, 77, 88, 99}
