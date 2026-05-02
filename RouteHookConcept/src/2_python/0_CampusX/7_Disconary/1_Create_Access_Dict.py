# Dictionary
#============

# Dictionary in Python is a collection of key-value pairs.
# It is used to store data like a map, unlike other data types which store only a single value.

# In other languages, it is known as map or associative array.

# Example:
# dict = {'name': 'Nitish', 'age':33, 'gender':'male'}


# Characteristics (V.V.V. Important)
#-----------------------------------

# Mutable
# No indexing (unordered)
# Keys must be unique
# Keys must be immutable




# How to create dictionary
#=========================

# lll There are two common ways to create a dictionary:
#     1. Using type conversion (dict())
#     2. Using curly braces {}



# How to create empty dictionary
#--------------------------------

d = {}
print(d) # {}


# 1D dictionary
#--------------

d = {
    'first_name':'Deepanshu',
    'last_name':'Singh',
    'age':22,
    'qualification':'B.Tech'
}

print(d)


# Dictionary with mixed keys
#----------------------------

d2 = {(1, 2, 3):1, "hellow":"World"}
print(d2)


# 2D dictionary -> JSON style
#-----------------------------

d = {
    'first_name':'Deepanshu',
    'last_name':'Singh',
    'age':22,
    'qualification':'B.Tech',
    'family_member':{
        'father':'Mr. Vijay Bahadur Singh',
        'mother':'Mis. Sanju Singh',
        'brother':'Himanshu Singh'
    }
}

print(d)


# Using dict sequence and dict() function
#----------------------------------------

d = dict([('name', 'Himanshu Singh'), ('age', 24)])
print(d)


# Duplicate keys
#----------------

d = {'name':'Deepanshu', 'name':'Singh'}
print(d)


# Mutable items as key not allowed
#---------------------------------

# d = {'name':'Deepanshu', [1, 2, 3]:4}
# print(d)  :- gives error 






# Accessing items
#=================

#lll There are two way to access element from a tuple:
#    1. using keys
#    2. using get()


# Using []
#----------

d = {'name':'Deepanshu', 'age':22}
print(d['name']) 


# Using get()
#------------

d = {'name':'Deepanshu', 'age':22}
print(d.get('name'))
