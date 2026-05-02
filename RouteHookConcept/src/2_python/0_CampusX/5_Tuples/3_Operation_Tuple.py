# Operations on Tuples
#=====================

# Tuples support the following operations:
#---------------------------------------
# There are three ways to perform operations on a tuple:

# 1. Arithmetic operations (+, *)
# 2. Membership operations (in, not in)
# 3. Looping operations






# 1. Arithmetic Operations
#-------------------------

# +  → used to combine two tuples
# *  → used to repeat a tuple multiple times

T1 = (1, 2, 3, 4)
T2 = (5, 6, 7, 8)

print(T1 + T2)
# (1, 2, 3, 4, 5, 6, 7, 8)

print(T1 * 3)
# (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)






# 2. Membership Operations
#-------------------------

# in       → checks whether an element exists in the tuple
# not in   → checks whether an element does not exist in the tuple

T1 = (11, 22, 33, 44)
T2 = (55, 66, (77, 88))

print(33 in T1)         # True
print(33 not in T1)     # False

print(77 in T2)         # False
print((77, 88) in T2)   # True






# 3. Looping on Tuple
#--------------------

# Used to access each element of the tuple one by one

T1 = (111, 222, 333, 444, 555, 666)

for i in T1:
    print(i, end=" ")
else:
    print()
    print("loop end!")


# 111 222 333 444 555 666
# loop end!
