

import numpy as np



"""



1️⃣ What is NumPy
*******************

lll NumPy (Numerical Python) is the fundamental Python library used for scientific computing.

lll It provides a powerful multidimensional array object called ndarray and many
    functions to perform fast numerical operations.

lll and this ndarray(N-dimensional array) stores homogeneous data (same data type) in a fixed-size and
    efficient structure.

lll we also know NumPy is written in C language but used with Python syntax.
    So we get:
          • It get Speed from C
          • and Simplicity from Python

lll And there are Many popular libraries are built on top of NumPy:

• Pandas      -> Data analysis
• Matplotlib  -> Data visualization
• Seaborn     -> Statistical visualization
• Scikit-learn -> Machine learning
• TensorFlow / PyTorch -> Deep learning
• NLTK / SpaCy -> Natural language processing

        



# ==========================================
# NumPy Important Functions (Interview Ready)
# ==========================================


🔹 1. NumPy Array Creation
===========================

array()     
arange()
linspace()
zeros()
ones()
empty()
full()
eye()
identity()
random.rand()
random.randint()




"""






# ==================================================
# NumPy Array Creation Methods (Interview Notes)                               
# ==================================================

# 1. np.array()
# -------------
# Definition:
# lll array is a NumPy Method used to creates a NumPy array from a list, tuple, or
#     other iterable object.

# Syntax:
# np.array(object, dtype=None)

#     Parameters has two parameter:
#           object -> Input data (list, tuple, etc.)
#           dtype  -> Data type of array elements (optional)

#     Important Points:
#           It Creates homogeneous arrays.
#           and Supports 1D, 2D, and ND arrays.

arr = np.array([10, 20, 30], dtype=float)

print(arr)
# [10. 20. 30.]





# 2. np.arange()
# --------------
# Definition:
# lll arange is a NumPy Method used to creates a NumPy array with evenly spaced values
#     within a given range.

# Syntax:
# np.arange([start], stop, [step], dtype=None)

# Parameters:
# start -> Starting value (default = 0)
# stop  -> Ending value (excluded)
# step  -> Difference between consecutive values
# dtype -> Data type (optional)

# Important Points:
#     Similar to Python range().
#     Stop value is excluded.


arr = np.arange(1, 11, 2)

print(arr)
# [1 3 5 7 9]





# 3. np.linspace()
# ----------------

# Definition:
# lll linspace is a NumPy method used to creates a NumPy array with a fixed number of evenly
#     spaced values between two endpoints.

# Syntax:
# np.linspace(start, stop, num=50,
#             endpoint=True, dtype=None)


#     It has Parameters:
#         start    -> Starting value
#         stop     -> Ending value
#         num      -> Number of values to generate
#         endpoint -> Include stop value or not
#         dtype    -> Data type (optional)


# Important Points:
# lll Stop value is included by default.
# lll Used in plotting and numerical computations.


arr = np.linspace(
    start=10,      # Starting value
    stop=20,       # Ending value
    num=5,         # Generate 5 values
    endpoint=True, # Include 20
    dtype=int      # Integer data type
)

print(arr)





# 4. np.zeros()
# -------------
# Definition:
# lll zeros is a NumPy method used to creates a NumPy array and filled with zeros.

# Syntax:
# np.zeros(shape, dtype=float)

# It has Parameters:
#        shape -> Array dimensions
#        dtype -> Data type (default=float)

# Important Points:
# lll Used for initialization.


arr = np.zeros(
    shape=(2, 3),  # 2 rows, 3 columns
    dtype=int      # Integer data type
)

print(arr)

"""
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
"""


# 5. np.ones()
# ------------
# Definition:
# lll ones is a NumPy method used to creates a NumPy array and filled with ones.

# Syntax:
# np.ones(shape, dtype=float)

#     It has Parameters:
#            shape -> Array dimensions
#            dtype -> Data type (default=float)

# Important Points:
# Commonly used in matrix operations.

arr = np.ones(
    shape=(2, 3),  # 2 rows, 3 columns
    dtype=int      # Integer data type
)

print(arr)

"""
[[1 1 1]
 [1 1 1]]
"""




# 6. np.empty()
# -------------
# Definition:
# lll empty() is a NumPy method used to creates an uninitialized NumPy array.

# Syntax:
# np.empty(shape, dtype=float)

#     It has Parameters:
#            shape -> Array dimensions
#            dtype -> Data type

# Important Points:
#           Contains garbage values.
#           Faster than zeros() and ones().

arr = np.empty(
    shape=(2, 3),  # 2 rows, 3 columns
    dtype=float    # Float data type
)

print(arr)

# Garbage values (Output may vary)
# [[6.9e-310 6.9e-310 6.9e-310]
#  [6.9e-310 6.9e-310 6.9e-310]]





# 7. np.full()
# ------------
# Definition:
# lll full() is a NumPy method used to creates a NumPy array and filled with a specified value.

# Syntax:
# np.full(shape, fill_value, dtype=None)

#     It has Parameters:
#         shape      -> Array dimensions
#         fill_value -> Value to fill
#         dtype      -> Data type (optional)

# Important Points:
#          Useful when every element should have the same value.

arr = np.full(
    shape=(2, 3),   # 2 rows, 3 columns
    fill_value=99,  # Fill value
    dtype=int       # Integer data type
)

print(arr)

# [[99 99 99]
#  [99 99 99]]






# 8. np.eye()
# -----------
# Definition:
# lll eye() is a NumPy method used to creates a matrix with ones on the main diagonal
#     and zeros elsewhere.


# Syntax:

# np.eye(N, M=None, k=0, dtype=float)

#     It has Parameters:
#          N     -> Number of rows
#          M     -> Number of columns (default=N)
#          k     -> Diagonal index
#                   0  = main diagonal
#                   1  = upper diagonal
#                  -1  = lower diagonal
#          dtype -> Data type

# Important Points:
# Can create rectangular matrices.

arr = np.eye(
    N=3,        # Rows
    M=4,        # Columns
    k=1,        # Upper diagonal
    dtype=int   # Integer data type
)

print(arr)

# [[0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]]

np.eye(3, k=0)
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

np.eye(3, k=-1)
# [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]






# 9. np.identity()
# ----------------
# Definition:
# lll Identity() is a NumPy method used to creates a square identity matrix.

# Syntax:
# np.identity(n, dtype=None)

# Parameters:
# n     -> Number of rows and columns
# dtype -> Data type (optional)

# Important Points:
# lll Always creates a square matrix.  


arr = np.identity(
    n=4,         # 4 rows and 4 columns
    dtype=int    # Integer data type
)

print(arr)

# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]]






# 10. np.random.rand()
# --------------------
# Definition:
# lll random.rand() is a NumPy method used to creates a NumPy array of random floating-point
#     numbers between 0 and 1.

# Syntax:
# np.random.rand(d0, d1, ..., dn)

# Parameters:
# d0,d1,... -> Dimensions of the array

# Important Points:
# lll Range is [0, 1).
# lll Returns float values.

arr = np.random.rand(
    2, 3      # 2 rows, 3 columns
)

print(arr)
# [[0.23 0.87 0.41]
#  [0.15 0.69 0.92]]


np.random.rand(5)
# [0.25 0.67 0.91 0.14 0.56]


np.random.rand(2,3)
# [[0.12 0.54 0.78]
#  [0.23 0.89 0.34]]






# 11. np.random.randint()
# -----------------------
# Definition:
# lll random.randint() is a NumPy method used to creates a NumPy array of random integers
#     within a specified range.

# Syntax:
# np.random.randint(low, high=None,
#                   size=None, dtype=int)

# Parameters:
# low   -> Lowest value (included)
# high  -> Highest value (excluded)
# size  -> Shape of output array
# dtype -> Data type
 
# Important Points:
# If high is omitted, range becomes [0, low).
# Returns integer values only.

arr = np.random.randint(
    low=10,       # Included
    high=50,      # Excluded
    size=(2, 3),  # Shape
    dtype=int     # Data type
)

print(arr)
# [[34 15 48]
#  [27 42 19]]




"""

for Data Inspection in NumPy array
===================================

ndim
shape
size
dtype
itemsize

bytes


"""

a1 = np.arange(10, dtype=np.int32)
print(a1)
# [0 1 2 3 4 5 6 7 8 9]


# ndim      → ndim is a NumPy attribute returns the number of dimensions of the NumPy array.
print(a1.ndim)   # 1

# shape     → shape is a NumPy attribute returns the structure of the NumPy array in the form (rows, columns, depth).
print(a1.shape)
# (10,)

# size      → size is a NumPy attribute returns the total number of elements in the NumPy array.
print(a1.size)
# 10

# itemsize  → itemsize is a NumPy attribute returns the size (in bytes) of each element in the NumPy array. 
print(a1.itemsize)
# 4 bytes (int32)

# dtype     → dtype is NumPy attribute show the data type of value store in the NumPy array. 
print(a1.dtype)
# int32






"""

 for NumPy Array Conversion 
============================

astype()
tolist()
copy()
view()


1️⃣ astype()
------------

lll astype() is a NumPy method used to change the data type of elements in a NumPy array.
    It creates a new NumPy array.

"""

# Example
# -------
a = np.arange(10)

print(a)
# [0 1 2 3 4 5 6 7 8 9]

print(a.dtype)
# int64



# Convert Data Type
# -----------------
b = a.astype(np.int32)

print(b.dtype)
# int32


"""
  tolist()
  --------
  lll tolist() is a NumPy method used to convert a NumPy array
      into a Python list.

      Parameters:
           No parameters
"""

arr = np.array(
    object=[[10, 20, 30],
            [40, 50, 60]]
)

result = arr.tolist()

print(result)

# [[10, 20, 30],
#  [40, 50, 60]]


"""

  copy()
  ------
  lll copy() is a NumPy method used to create a completely
      independent copy of a NumPy array.

  Parameters:
      No parameters

"""

arr = np.array(
    object=[10, 20, 30]
)

copied_arr = arr.copy()

copied_arr[0] = 100

print("Original Array:")
print(arr)

print("Copied Array:")
print(copied_arr)

# Original Array:
# [10 20 30]

# Copied Array:
# [100  20  30]


"""


 view()
 ------
       view() is NumPy method use to create NumPy array that shares the same memory as the original NumPy array. It doesn't create a new copy, 
       so changing the view also changes the original NumPy array. 



"""

# arr = np.array([10, 20, 30])

# view = arr.view()

# view[0] = 100

# print(arr)  :- [100 20 30]







"""

 for NumPy Array Manipulation
==============================

reshape()
resize()
flatten()
ravel()
transpose()


swapaxes()

"""

# 1. reshape()
# -------------
# Definition:
# lll reshape() is a NumPy method used to change the shape
#     of a NumPy array without changing its data.

#  We know:
#      lll Total number of elements must remain the same.
#      lll It Returns a new reshaped array.
#      lll -1 can be used to automatically calculate one dimension.


# Syntax:
# array.reshape(shape)

# Parameters:
# shape -> New dimensions of the array


arr = np.array(
    object=[1, 2, 3, 4, 5, 6]
)

result = arr.reshape(
    shape=(2, 3)
)

print(result)

# [[1 2 3]
#  [4 5 6]]



# 2. resize()
# ------------
# Definition:
# lll resize() is a NumPy method used to change the shape
#     of an existing NumPy array.

# Important Points:
#     lll It Modifies the original NumPy array.
#     lll If new size is larger, extra elements are filled with 0.
#     lll If new size is smaller, elements are removed.


# Syntax:
# array.resize(new_shape)

# Parameters:
# new_shape -> New dimensions of the array


import numpy as np

arr = np.array(
    object=[1, 2, 3, 4]
)

arr.resize(
    new_shape=(2, 3)
)

print(arr)

# [[1 2 3]
#  [4 0 0]]




"""

3. flatten() & ravel()
----------------------

ravel() and flatten() are NumPy methods used to convert a multi-dimensional NumPy array into a one-dimensional (1D) NumPy array. 
The main difference is that ravel() uses the same memory as the original NumPy array (whenever possible), 
while flatten() creates a new copy of the NumPy array.

Even Simpler
   ravel() → Same memory → Changes may affect the original array.
   flatten() → New memory → Changes do not affect the original array.

   
"""

# Example :- reshape()
# --------------------

a = np.arange(12).reshape(4,3)
print(a)

# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

b = np.ravel(a)
print(b)

# [ 0  1  2  3  4  5  6  7  8  9 10 11]



# Example :- flatten()
# --------------------

arr = np.array([[1, 2],
                [3, 4]])

f = arr.flatten()

f[0] = 100

print(arr)
print(f)






"""

4. Transpose Function
---------------------

Transpose is NumPy method use to convert converts **rows into columns**
and **columns into rows**.

In simple terms, it flips the matrix over its diagonal.

"""

# Create Array
# ------------

a = np.arange(12).reshape(3,4)
print(a)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



# Using np.transpose()
# --------------------

a = np.transpose(a)
print(a)

# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]


"""


🔹 6. for combining data NumPy Arrays
======================================

concatenate()
stack()
hstack()
vstack()
dstack()


column_stack()
row_stack()



"""



"""

concatenate()
-------------

concatenate()
-------------

np.concatenate() is a NumPy method used to combine two or more NumPy arrays into a single array.

It has an axis parameter:

• axis = 0 → Joins NumPy arrays row-wise (vertical). (Default)
• axis = 1 → Joins NumPy arrays column-wise (horizontal).

We know that
    The NumPy arrays must have compatible shapes.
         - For axis = 0, the number of columns must be the same.
         - For axis = 1, the number of rows must be the same.


Example 1 
..........

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5],
                 [6]])

np.concatenate((arr1, arr2), axis=1)      

[[1 2 5]
 [3 4 6]]

 
Example 2
.........

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5],
                 [6],
                 [7]])

np.concatenate((arr1, arr2), axis=1)

The rows don't match, so NumPy raises an error.


"""




"""

lll stack()
-----------

np.stack() is a NumPy method used to combine two or more NumPy arrays by creating a new axis (new dimension).

It has an axis parameter:

• axis = 0 → Stacks NumPy arrays row-wise (Default).
• axis = 1 → Stacks NumPy arrays column-wise.

We know that
   The NumPy arrays must have the same shape.
   If the shapes are different, NumPy raises an error.

Example 1
.........

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

np.stack((arr1, arr2))

Output

[[1 2 3]
 [4 5 6]]

Explanation

Two 1D arrays are stacked together to form a new 2D array.


Example 2
.........

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

np.stack((arr1, arr2), axis=1)

Output

[[1 4]
 [2 5]
 [3 6]]

Explanation

axis = 1 stacks the arrays column-wise.


Example 3
.........

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5])

np.stack((arr1, arr2))

The arrays have different shapes, so NumPy raises an error.


Difference between stack() and concatenate()
............................................

stack()
- Creates a new axis (new dimension).
- All arrays must have the same shape.

concatenate()
- Joins arrays along an existing axis.
- Arrays must have compatible shapes.


"""

"""

lll hstack()
------------

np.hstack() is a NumPy method used to combine two or more NumPy arrays horizontally (side by side).

We know that
         The NumPy arrays must have the same number of rows.

Example 1
.........

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5],
                 [6]])

np.hstack((arr1, arr2))

Output

[[1 2 5]
 [3 4 6]]

Explanation

The arrays are joined horizontally (column-wise).


Example 2
.........

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5],
                 [6],
                 [7]])

np.hstack((arr1, arr2))

The number of rows is different, so NumPy raises an error.


"""


"""

lll vstack()
------------

np.vstack() is a NumPy method used to combine two or more NumPy arrays vertically (one below another).

We know that
      The NumPy arrays must have the same number of columns.

Example 1
.........

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6]])

np.vstack((arr1, arr2))

Output

[[1 2]
 [3 4]
 [5 6]]

Explanation

The arrays are joined vertically (row-wise).


Example 2
.........

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6, 7]])

np.vstack((arr1, arr2))

The number of columns is different, so NumPy raises an error.


"""



"""

lll dstack()
------------

np.dstack() is a NumPy method used to combine two or more NumPy arrays along the third dimension (depth).

We know that
      The NumPy arrays must have the same number of rows and columns.

Example 1
.........

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

np.dstack((arr1, arr2))

Output

[[[1 5]
  [2 6]]

 [[3 7]
  [4 8]]]

Explanation

The arrays are stacked along the third dimension (depth).


Example 2
.........

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6, 7],
                 [8, 9, 10]])

np.dstack((arr1, arr2))

The number of rows or columns is different, so NumPy raises an error.


"""






"""

🔹 5. Broadcasting
====================

Array + Scalar
Array * Scalar
Array + Array
Broadcasting Rules

"""

# Broadcasting
# ============

# lll  Broadcasting describes how NumPy performs arithmetic
#      operations on NumPy arrays with different shapes.


# Broadcasting Rules
# ------------------

# lll There are two main broadcasting rules in NumPy.



# lll Rule (1): Make the two NumPy arrays have the same number of dimensions
# ---------------------------------------------------------------------------

#     If the number of dimensions of the two NumPy arrays are different,
#     NumPy adds new dimensions with size 1 to the beginning (head)
#     of the NumPy array with fewer dimensions.


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

# NumPy compares the shape of NumPy arrays from right to left.

# If the sizes of the dimensions are different,
# the dimension with size 1 is stretched to match
# the size of the other NumPy array.

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



import numpy as np

# 2D array (3×3)
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 1D array (3,)
B = np.array([1, 2, 3])

print("Array A:")
print(A)

print("\nArray B:")
print(B)

# Broadcasting Examples
print("\nAddition (+)")
print(A + B)

print("\nSubtraction (-)")
print(A - B)

print("\nMultiplication (*)")
print(A * B)

print("\nDivision (/)")
print(A / B)

print("\nFloor Division (//)")
print(A // B)

print("\nModulus (%)")
print(A % B)

print("\nPower (**)")
print(A ** B)



"""

🔹 NumPy Operations
===================

lll There are two main types of operations in NumPy:

1️⃣ Scalar Operations
2️⃣ Vector Operations



Scalar Operations
-----------------
lll Scalar operations are performed between a NumPy array
    and a single numeric value (scalar).

lll The same value is applied to every element of the NumPy array.

Example:
Array + 10
Array * 2
Array / 5



Vector Operations
-----------------
lll Vector operations are performed between two NumPy arrays.

lll Both NumPy arrays must have the same shape or a compatible shape,
    which means broadcasting should be possible.

Example:
Array1 + Array2
Array1 * Array2
Array1 > Array2



Types of Operations
-------------------
lll Both Scalar Operations and Vector Operations
    can be divided into two categories:

1️⃣ Arithmetic Operations
   - add (+)
   - subtract (-)
   - multiply (*)
   - divide (/)
   - power (**)
   - modulus (%)

2️⃣ Relational Operations
   - greater than (>)
   - less than (<)
   - greater than or equal to (>=)
   - less than or equal to (<=)
   - equal to (==)
   - not equal to (!=)

"""