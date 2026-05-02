# change only important words for Python

'''

✅ Final Correct Interview-Style Answer:

lll Scope in Python
Scope defines where we can access specific variables or functions in code.

lll Lexical Environment
Created whenever an Execution Context is created

It consists of:
Lexical Environment = Local Memory + Reference to Parent Lexical Environment


lll Simple Definition:
"Lexical Environment means the local memory along with a reference to the parent Lexical Environment."
"Lexical Context means where the function is physically present inside the code."


✅ Example with Execution Context, Lexical Environment, and Scope Chain:

def a():
    def c():
        print(b)   # NameError: name 'b' is not defined
    c()

a()


Memory Creation Breakdown:
✔ a() is defined inside the Global Scope, so a is lexically inside Global.
✔ c() is defined inside a(), so c is lexically inside a.


Scope Chain Working:
c() tries to access b.
First, it looks in its own Local Memory → b not found.
Then, it follows the parent Lexical Environment, which is a()'s scope → b not found.
Finally, it checks the Global Scope → b not found.
Global Lexical Environment’s outer reference is None, so a NameError is raised.


lll ✅ Scope Chain Definition:
"The process of searching variables from the current Local Memory,
moving outward to parent Lexical Environments, is called the Scope Chain."


Call Stack and Execution Flow Example:

def a():
    def c():
        print("Inside c")
    c()

a()


✔ Call Stack:

1. GEC pushed → Global Execution Context
2. a() called → new Execution Context for a
3. Inside a(), c() called → new Execution Context for c
4. c() finishes → pop c() Execution Context
5. a() finishes → pop a() Execution Context
6. Global finishes


✅ Final Conclusion (Interview Version):
Python uses Lexical Scoping, meaning scope is determined by where
functions and variables are physically written, not where they are called.
Lexical Environment + Scope Chain ensures variable lookup follows
a structured, outward search mechanism.
If a variable isn't found in the entire chain, Python raises a NameError.


'''



# Function without return statement
#==================================

# then function return default :- None

def is_even(a):

    if a%2 != 0:
        print("odd")
    else:
        print("even")


print(is_even(4))

# even
# None


L = [1, 2, 3]

print(L.append(4)) # None
print(L)           # [1, 2, 3, 4]







# vriable Scope
#---------------

# There are two type of scope

# 1. Global Scope
# 2. Local Scope

# Impure function :- When function output depend on external state called impure function

def g(y):
    print(x) # 5
    print(x+1) # 6
x = 5
g(x)
print(x) # 5


# Scope chaining :- The process of searching variable from current local memory and moving outword to parent enviornment
#                   called scope chaining.



# Pure function :- When function output does not depend on external state called pure function


def p(y):
    print(y) # 7
    print(y+1) # 8

p(7)



# function can't change global variable
#----------------------------------------

def r(y):
#    m = 2   :- give error
    i=1

m = 10
r(7)
