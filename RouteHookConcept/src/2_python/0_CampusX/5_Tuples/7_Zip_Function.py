# Zip
#=======

# Definition (Interview Simple & Spoken)
#--------------------------------------
# The zip() function is used to combine two or more iterables together.
# It takes elements from the same index of each iterable and pairs them.
# The result is returned as tuples.
# If iterables have different lengths, zip() stops at the shortest one.


# Ques: Write a program to add items of 2 tuple indexwise
#-------------------------------------------------------

T1 = (1, 2, 3, 4)
T2 = (-1, -2, -3, -4)

print(zip(T1, T2))
# zip() returns a zip object (iterator)

print(tuple(zip(T1, T2)))
# ((1, -1), (2, -2), (3, -3), (4, -4))

T = tuple(i + j for i, j in zip(T1, T2))
print(T)
# (0, 0, 0, 0)



# Tuple Comprehension Examples
#=============================

# Example 1: Create a tuple of squares
#-------------------------------------

T = tuple(i * i for i in range(1, 6))
print(T)
# (1, 4, 9, 16, 25)


# Example 2: Create a tuple of even numbers from 1 to 10
#--------------------------------------------------------

T = tuple(i for i in range(1, 11) if i % 2 == 0)
print(T)
# (2, 4, 6, 8, 10)


# Example 3: Add two tuples indexwise
#------------------------------------

T1 = (1, 2, 3, 4)
T2 = (10, 20, 30, 40)

T = tuple(i + j for i, j in zip(T1, T2))
print(T)
# (11, 22, 33, 44)


# Example 4: Convert list into tuple
#-----------------------------------

L = [1, 2, 3, 4, 5]

T = tuple(i for i in L)
print(T)
# (1, 2, 3, 4, 5)


# Example 5: Create tuple from string characters
#-----------------------------------------------

T = tuple(ch for ch in "python")
print(T)
# ('p', 'y', 't', 'h', 'o', 'n')













# Note : Python does not support tuple comprehension.
#        Using () creates a generator, tuple() converts it into a tuple.
