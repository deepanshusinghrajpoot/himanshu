# Decorators
#============

#lll Definition (Interview Spoken):
#-------------------------------
# A decorator in Python is a function that takes another function as input,
# adds extra functionality to it without changing its original code,
# and then returns the modified function.

# Decorators work because Python functions are FIRST CLASS CITIZENS,
# meaning:
# 1. Functions can be assigned to variables
# 2. Functions can be passed as arguments
# 3. Functions can be returned from another function


# Types of Decorators
#===================

# lll There are two types of decorators in Python:
# 1. Built-in decorators
# 2. User-defined decorators



# 1. Built-in Decorators
#======================

# Definition (Interview Spoken):
#--------------------------------
#lll Built-in decorators are predefined decorators provided by Python

# to modify the behavior of methods and functions in a standard way.

# Common Built-in Decorators:
# ---------------------------
# @staticmethod     -> Method does not depend on class or object
# @classmethod      -> Method receives class as first argument (cls)
# @property         -> Used to access a method like an attribute
# @abstractmethod   -> Used in abstract base classes to enforce method implementation



# 2. User-defined Decorators
#==========================

# Definition (Interview Spoken):
#-------------------------------
#lll User-defined decorators are custom decorators created by programmers

# to add reusable functionality to multiple functions.



# Question: Create a decorator to decorate the output of another function
#=========================================================================

def my_decorator(fun):
    b = 1   # outer function variable

    def wrapper():
        print("******************")
        print(b)
        fun()
        print("******************")

    return wrapper


def hellow():
    print("Hellow Bhaiya!")


a = my_decorator(hellow)
a()

# Output:
# ******************
# 1
# Hellow Bhaiya!
# ******************



# Interview Explanation:
# ----------------------
# Even though my_decorator() has finished execution,
# wrapper() still remembers variable 'b'.
# This happens because of CLOSURE.





# Closure
#========

# Definition (Interview Spoken):
# A closure is formed when a function remembers variables
# from its outer enclosing scope even after that scope has finished execution.

# lll In Python, a function along with its lexical environment forms a closure.

# Important Line for Interview:
# "Decorators are based on the concept of closures."



# Better Syntax Using @decorator
#===============================

def my_decorator(fun):
    b = 1
    def wrapper():
        print("******************")
        print(b)
        fun()
        print("******************")
    return wrapper


@my_decorator
def hellow():
    print("Hellow Bhaiya!")

# Interview Line:
# "@my_decorator replaces hellow = my_decorator(hellow)"

hellow()

# Output:
# ******************
# 1
# Hellow Bhaiya!
# ******************



# Question: Create a decorator to calculate execution time of a function
#========================================================================

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print("time taken by", func.__name__, time.time() - start, "sec")
    return wrapper


@timer
def my_hellow():
    print("Hellow Paji Kaise ho! Tusi ki kar rahe ho!")
    time.sleep(2)

my_hellow()

# Output:
# Hellow Paji Kaise ho! Tusi ki kar rahe ho!
# time taken by my_hellow ~2 sec



@timer
def display_game():
    print("Game Start After Short Break!")
    time.sleep(4)

display_game()



@timer
def square(num):
    print(num ** 2)
    time.sleep(1)

square(8)

# Output:
# 64
# time taken by square ~1 sec



# Interview Concept:
# ------------------
# *args allows decorator to work with functions
# having different number of arguments.



# Question: Create a decorator to check data type of function argument
#=====================================================================

def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type:
                func(*args)
            else:
                raise TypeError("Ye sab nahi chalega!")
        return inner_wrapper
    return outer_wrapper


@sanity_check(int)
def cube(num):
    print(num ** 3)


@sanity_check(str)
def greet(name):
    print("Hellow", name)


greet("Deepanshu Singh!")

# Output:
# Hellow Deepanshu Singh!



# Final Interview One-Liners
#===========================

# 1. Decorator modifies a function without changing its source code.
# 2. Decorators work because functions are first-class citizens.
# 3. Decorators are implemented using closures.
# 4. @decorator is syntactic sugar for function reassignment.
# 5. *args and **kwargs make decorators reusable.
