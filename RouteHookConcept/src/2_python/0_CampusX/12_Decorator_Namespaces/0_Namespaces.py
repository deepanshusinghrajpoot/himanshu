# Namespaces
#===========

# lll A namespace is a dictionary
#     where names (identifiers) are keys
#     and their corresponding objects are values.


# lll There are four types of namespaces:
#----------------------------------------
# 1. Built-in Namespace
# 2. Global Namespace
# 3. Enclosing Namespace
# 4. Local Namespace


# Built-in Namespace :-
#---------------------
# Contains all built-in functions, exceptions, and keywords
# provided by Python (e.g., print, len, max, int).

# Global Namespace :-
#-------------------
# Contains names defined at the top level of a Python program
# or module.

# Enclosing Namespace :-
#----------------------
# Contains names from the outer function when a function
# is defined inside another function.

# Local Namespace :-
#-------------------
# Contains names defined inside a function and is accessible
# only within that function.



# Scope and LEGB (Local, Enclosing, Global, Built-in) Rule
#--------------------------------------------------------

# Scope defines where we can access specific variables or functions
# in the code.

# A scope is a textual region of a Python program where
# a namespace is directly accessible.



#lll LEBG Rule
#--------------
# In Python searches variable in namespace in the following order:
# Local → Enclosing → Global → Built-in.
# If the name is not persent in any of these scopes,
# Python raises a NameError exception.




# Local scope and Global scope
#=============================

a1 = 1

def temp1():
    print(a1)

temp1()

# 1



# local and global -> editing global
#----------------------------------
# A global variable can be read inside a local scope,
# but it cannot be modified without using the global keyword.

a2 = 2

def temp2():
#    a2 += 1
    print(a2)

temp2()
print(a2)

# Note :- In local scope, a global variable can be read
# but cannot be modified directly.



# local and global -> global created inside local
#-----------------------------------------------
# Using the global keyword inside a function allows
# creating or modifying a global variable.
# This is generally considered a bad practice.

a3 = 3

def temp3():
    global a3   # Good not practice
    a3 += 1
    print(a3)

temp3()
print(a3)

# 4
# 4


def temp4():
    global a4   # Good not practice
    a4 = 4
    print(a4)

temp4()
print(a4)

# 4



# Built-in scope
#================

# Python resolves names by first checking the Local scope,
# then the Global scope, and finally the Built-in scope.

import builtins

# print(dir(builtins))


# Example

L = [1, 2, 3]

print(max(L))  # 3

def max():
    print("hellow")

# print(max(L))

# This gives an error because max() is already found
# in the Global scope, so Python does not reach
# the Built-in scope for max.



# enclosing scope (nonlocal scope)
#================================

# Enclosing scope refers to the scope of an outer function
# that contains a nested inner function.

def outer():
    def inner():
        print("Local Scope!")
    inner()
    print("Enclosing Scope!")

outer()
print("Global Scope!")



# How to change Enclosing scope (nonlocal scope) variable in Local scope
#-----------------------------------------------------------------------

# The nonlocal keyword allows a variable from the enclosing
# scope to be modified inside a nested function.

def outer1():
    m = 1
    def inner1():
        nonlocal m
        m += 1
        print("Local Scope! ", m)
    inner1()
    print("Enclosing Scope! ", m)

outer1()
print("Global Scope!")
