"""

==========
Python
==========


Lists
======

1. What is a List?
2. List vs Array
3. Characteristics of a List
4. How to create a List
5. Access items from a List
6. Edit items in a List
7. Delete items from a List
8. Operations on Lists
9. Functions on Lists


List 
====

lll A list in Python is an ordered, mutable collection of elements
    that can store multiple values of different data types.

# lll A list in Python is similar to a tuple,
#     but the main difference is:
#         👉 List is mutable (can be changed)
#         👉 Tuple is immutable (cannot be changed)
#
#     Therefore, we can perform adding, editing, deleting, and reading operations on a list.


# Characteristics of list
#--------------------------

# lll Ordered                 -> Items have a fixed position
# lll changeable              -> Can modify elements after creation
# lll Allows duplicate values





List vs Array 
--------------
               
Advantages
-----------

Array                                     List
-----                                     -----
Array has fixed size                      lll List has dynamic size
Array is homogeneous                      lll List is heterogeneous
(stores same data type)                   (stores different data types)



Disadvantages
--------------

Array                                     List
-----                                     -----
Array is faster                           List is comparatively slower
Array uses less memory                    List uses more memory




Example of List
----------------

L = [20, 'Jessa', 35.75, [30, 60, 90]]




How a List is stored in memory
==============================

L = [1, 2, 3]

print(id(L))

print(id(L[0]))   # same as id(1)
print(id(L[1]))   # same as id(2)
print(id(L[2]))   # same as id(3)



Visual Representation (Memory Diagram)
--------------------------------------

L  ──────►  [  ●   ●   ●  ]
             |   |   |
             |   |   |
             ▼   ▼   ▼
            1    2    3

id(L)        → address of list object
id(L[0])     → address of integer object 1
id(L[1])     → address of integer object 2
id(L[2])     → address of integer object 3


So,
- List stores references (addresses) to objects
- Elements are stored separately in memory
- This is why a list can store different data types

Hence,
List is heterogeneous.




Characteristics of a List
=========================

- Order is maintained in a list
- Lists are mutable (can be changed)
- Lists are heterogeneous
- Lists can contain duplicate elements
- Lists are dynamic in size
- Lists can be nested
- List items can be accessed using index
- Lists can store any type of Python object




Note
-----

We know that everything in Python is an object.










"""
