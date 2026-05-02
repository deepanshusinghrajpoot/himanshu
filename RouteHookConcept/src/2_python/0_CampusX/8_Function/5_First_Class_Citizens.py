


# Funtions are 1st class citizens
#=================================

# Because

# We can assign a function in a variable
# We can pass a function as argument to another function
# A function can hold another as argument or return another function






# type and id
#------------

def square(num):
    return num**2

print(type(square)) # <class 'function'>
print(id(square))   # 2602399368352


# Function assign in variable
#----------------------------
x = square
print(x(3)) # 9



# function as argument
#----------------------

def fun_a():                 
    print("inside fun_a!")


def fun_b(z):
    print("inside fun_b!")
    return z


fun_b(fun_a)()  

# inside fun_a!
# inside fun_b!




# Callback Function :- When a function pass as argument in other function called callback function.
#...................

# Higher Order Function :- When a function hold another function as argument called higher order function.
#......................





# storing
#------------

L = [1, 2, 3, 4, square]

print(L) # [1, 2, 3, 4, <function square at 0x000001E3E27904A0>]
print(L[-1](4)) # 16



# deleting a function
#---------------------

def g(x):
    print(x)

del g

# print(g) :- give error




# returning function
#---------------------

def f():
    print("Print f!")
    
    def g():
        print("Print g!")
    
    return g

f()()

# Print f!
# Print g!








