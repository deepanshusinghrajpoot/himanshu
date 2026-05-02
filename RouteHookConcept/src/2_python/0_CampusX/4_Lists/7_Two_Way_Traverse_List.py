# 2 ways to traverse a list
#-------------------------

# A list can be traversed in two common ways:
# 1. itemwise
# 2. indexwise


# 1. itemwise
#------------

# In itemwise traversal, we directly access each element of the list.

L = [11, 22, 33, 44, 55]

for i in L:
    print(i, end=" ")   # 11 22 33 44 55
print()


# 2. indexwise
#-------------

# In indexwise traversal, we access elements using their index values.

L = [11, 22, 33, 44, 55]

for i in range(0, len(L)):
    print(i, end=" ")   # 0 1 2 3 4
