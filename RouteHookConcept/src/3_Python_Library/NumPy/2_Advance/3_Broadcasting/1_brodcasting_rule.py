# Broadcasting Rules
# ==================

# There are two main broadcasting rules in NumPy.



# Rule (1): Make the two arrays have the same number of dimensions
# ---------------------------------------------------------------

# If the number of dimensions of the two arrays are different,
# NumPy adds new dimensions with size 1 to the beginning (head)
# of the array with fewer dimensions.


# Example 1
# ---------

# Matrix order
# 1st array (2D) : (3, 2)
# 2nd array (1D) : (3)

# The 2nd array has fewer dimensions,
# so NumPy converts it to:

# (1, 3)


# Example 2
# ---------

# Matrix order
# 1st array (3D) : (3, 3, 3)
# 2nd array (1D) : (3)

# The 2nd array has fewer dimensions,
# so NumPy converts it to:

# (1, 1, 3)



# Rule (2): Make each dimension the same size
# -------------------------------------------

# NumPy compares the shape of arrays from right to left.

# If the sizes of the dimensions are different,
# the dimension with size 1 is stretched to match
# the size of the other array.

# If both dimensions are different and neither is 1,
# broadcasting is not possible and NumPy raises an error.



# Example
# -------

# (2, 3)
# (1, 3)

# Result shape → (2, 3)


# Invalid Example
# ---------------

# (2, 3)
# (4, 3)

# Broadcasting is not possible because
# neither dimension is 1.