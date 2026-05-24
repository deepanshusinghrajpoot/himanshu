# Operations on Lists
#===================

# Lists support the following operations:

#lll There are three way to perform operation on the list
#--------------------------------------------------------
# Arithmetic operations (+, *)
# Membership operations (in, not in)
# Looping operations




# 1. Arithmetic Operations
#------------------------

# +  is used to combine two lists
# *  is used to repeat a list multiple times

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print(L1 + L2)
# [1, 2, 3, 4, 5, 6, 7, 8]

print(L1 * 3)
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]




# 2. Membership Operations
#-------------------------

# in       -> checks whether an element exists in the list
# not in   -> checks whether an element does not exist in the list

L1 = [11, 22, 33, 44]
L2 = [55, 66, [77, 88]]

print(33 in L1)        # True
print(33 not in L1)    # False

print(77 in L2)        # False
print([77, 88] in L2)  # True




# 3. Looping on List
#------------------

# Used to access each element of the list one by one

L1 = [111, 222, 333, 444, 555, 666]

for i in L1:
    print(i, sep=" ", end="")
else:
    print()
    print("loop end!")


# 111222333444555666
# loop end!
