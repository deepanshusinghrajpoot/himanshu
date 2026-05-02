




# Method Vs Functions
#=====================


#lll method :- When a function implemented inside the class called method
#lll function :- When a function not implemented inside the class called function


L = [1, 2, 3, 4]

len(L) # function
L.append(5) # method






# Magic Methods or A.k.a Dunder Methods 
#======================================

# magic methods has super power

# syntax :   __name__  
# eg:  __init__






# What is constructor
#======================


#lll Special method invoked automatically at time of object creation. Used for Initialization.
#    Sir, In python Constructor is creat using magic methods



# What is Benifit of constructor (v.v.imp)
#--------------------------------

#lll Constructor is use to write configuration related code

# Ques :- if god is the programmer
#         and earth is class 
#         then what in constructor
#         then what is object

# ans :- constructor contain death
#     :- human being are objects




# Type of Constructor
# -------------------

# There are three type of constructor

# 1. Parameterize constructor : 👉 A constructor which takes parameters is called a parameterized constructor.
#..............................

# 2. Non-parameterize constructor : 👉 A constructor which does not take any parameter is called a non-parameterized constructor.
#..................................

# 3. Copy Constructor : 👉 A constructor which creates a new object as a copy of an existing object is called a copy constructor.
#......................


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def copy(cls, other):
        return cls(other.name, other.age)


s1 = Student("Deepanshu", 21)
s2 = Student.copy(s1)

print(s2.name, s2.age)




# there are two type of copy constructor 
# 1. Shallow Copy
# 2. Deep Copy






# golden rule of object oriented programming
#===========================================

# In object oriented programming have two things 
# 1. class
# 2. object

# Inside class make rule which follow by object

# Rule
#------
# In rule we are add attribute or methods


# Golden Rule
#------------
# Only object can access all attribute and methods(every things)

# So, self inside the class is use to build communication between two methods of class 





# self
#======

# self is default parameter for all method
# self is point to the object
# self is use to build communication between two methods of class 


# example

class Atm:

    # non parameterized constructor
    def __init__(self):
        print("memory address of self inside the class : ",id(self))



obj = Atm()
print("memory address of object : ", id(obj))


# memory address of self inside the class :  1786876456144
# memory address of object :  1786876456144

# Here both point same memory. So, self is nothing it is point to the object


