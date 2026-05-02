

# lll ✅ Interview-Ready: Python Execution Context & Call Stack
#=============================================================

# 🧠 "When any Python code runs, the Python interpreter first creates
# a Global Execution Context (GEC).
# This GEC is then pushed onto the Call Stack."

# ✨ "The Global Execution Context has two main phases:

# Memory Creation Phase –
# All variables and function names are created in memory
# (variables are name references, functions get full definitions).

# Code Execution Phase –
# The code is executed line-by-line,
# and values are assigned or computed."



# 🔁 "Every time a function is invoked, a new Execution Context is created for that function and pushed onto the Call Stack. When the function finishes execution, its context is popped off the stack, 
#     returning control to the previous context."





# Example
#--------

def fun1():
    print("Inside fun1")

def fun2():
    print("Inside fun2")
    fun1()
    print("Back to fun2")

fun2()

# Call Stack Flow:
# ----------------
# Global Execution Context
# -> fun2 Execution Context
# -> fun1 Execution Context
# <- fun1 popped
# <- fun2 popped




# Lexical Environment
#====================

# Interview Spoken Definition:
# A Lexical Environment is created whenever an Execution Context is created.

# It consists of two parts:
# --------------------------
# 1. Local Memory (variables and function declarations)
# 2. Reference to the Parent Lexical Environment

# Formula:
# --------
# Lexical Environment = Local Memory + Parent Lexical Environment Reference


# Simple Definition:
# ------------------
# "Lexical Environment means the local memory along with a reference
# to the parent lexical environment."



# Example
#--------

x = 10   # Global Lexical Environment

def outer():
    y = 20   # Outer Lexical Environment

    def inner():
        z = 30   # Inner Lexical Environment
        print(x, y, z)

    inner()

outer()

# Explanation:
# ------------
# inner() first looks for variables in its own local memory.
# If not found, it checks the parent lexical environment.
# This process continues until the global scope.



# Closure
#========

# Interview Spoken Definition:
# A closure is formed when a function remembers variables
# from its outer enclosing scope even after that outer function
# has finished execution.

# Important Line:
# ---------------
# lll "In Python, a function along with its lexical environment forms a closure."



# Example
#--------

def outer_func():
    a = 100   # Outer variable

    def inner_func():
        print(a)   # Remembering outer variable

    return inner_func


f = outer_func()   # outer_func execution ends
f()                # inner_func still remembers 'a'

# Output:
# 100



# Interview Explanation:
# ----------------------
# Even though outer_func() has finished execution,
# inner_func() still has access to variable 'a'.
# This happens because the lexical environment is preserved.



# Relation Between Concepts
#==========================

# Execution Context -> creates Lexical Environment
# Lexical Environment -> enables variable lookup
# Closure -> preserves Lexical Environment even after execution



# Very Important Interview Line:
# ------------------------------
# "Decorators are based on the concept of closures."



# One-Frame Interview Summary
#============================

# Execution Context:
# - Created on function call
# - Pushed to Call Stack
# - Destroyed after execution

# Lexical Environment:
# - Created with execution context
# - Contains local memory + parent reference

# Closure:
# - Function + preserved lexical environment
# - Remembers outer variables after execution
