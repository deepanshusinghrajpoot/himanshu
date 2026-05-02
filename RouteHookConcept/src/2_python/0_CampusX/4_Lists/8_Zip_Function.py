# Zip
#=======

# lll Definition (Interview Simple & Spoken)
#-------------------------------------------
# zip() function is used to combine two or more iterables together.
# It takes elements from the same index of each iterable and pairs them.
# The result is returned as tuples.
# If iterables have different lengths, zip() stops at the shortest one.



# Ques: Write a program to add items of 2 lists indexwise
#--------------------------------------------------------

L1 = [1, 2, 3, 4]
L2 = [-1, -2, -3, -4]
S3 = {6, 7, 8, 9}

print(list(zip(L1, L2, S3)))  
# [(1, -1, 8), (2, -2, 9), (3, -3, 6), (4, -4, 7)]

print(zip(L1, L2))
# zip() returns a zip object (iterator)

print(list(zip(L1, L2)))
# [(1, -1), (2, -2), (3, -3), (4, -4)]

L = [i + j for i, j in zip(L1, L2)]
print(L)
# [0, 0, 0, 0]


# Note :- In Python everything is an object
#------------------------------------------

# In Python, all values are treated as objects.
# This includes numbers, functions, and classes.

# A list can store multiple types of objects together.

L = [1, 2, print, type, input]
print(L)
# [1, 2, <built-in function print>, <class 'type'>, <built-in function input>]
