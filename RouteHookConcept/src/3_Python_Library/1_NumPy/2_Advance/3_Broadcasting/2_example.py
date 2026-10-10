import numpy as np


# Broadcasting Examples
# =====================


# Example 1
# ---------
# Shape of a → (4,3)
# Shape of b → (3,)
# Broadcasting is possible

a = np.arange(12).reshape(4, 3)
b = np.arange(3)

print(a + b)

# [[ 0  2  4]
#  [ 3  5  7]
#  [ 6  8 10]
#  [ 9 11 13]]



# Example 2
# ---------
# Shape of a → (3,4)
# Shape of b → (3,)
# Broadcasting is NOT possible

a = np.arange(12).reshape(3, 4)
b = np.arange(3)

# print(a + b)  # Error: shapes are not compatible



# Example 3
# ---------
# Shape of a → (1,3)
# Shape of b → (3,1)
# Broadcasting is possible

a = np.arange(3).reshape(1, 3)
b = np.arange(3).reshape(3, 1)

print(a + b)

# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]



# Example 4
# ---------
# Shape of a → (1,)
# Shape of b → (3,1)
# Broadcasting is possible

a = np.array([1])
b = np.arange(3).reshape(3, 1)

print(a + b)

# [[1]
#  [2]
#  [3]]



# Example 5
# ---------
# Shape of a → (3,4)
# Shape of b → (4,3)
# Broadcasting is NOT possible

a = np.arange(12).reshape(3, 4)
b = np.arange(12).reshape(4, 3)

# print(a + b)  # Error: shapes are incompatible



# Example 6
# ---------
# Shape of a → (4,4)
# Shape of b → (2,2)
# Broadcasting is NOT possible

a = np.arange(16).reshape(4, 4)
b = np.arange(4).reshape(2, 2)

# print(a + b)  # Error: shapes are incompatible