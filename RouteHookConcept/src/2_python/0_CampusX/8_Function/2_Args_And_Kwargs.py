

# We know that in python every things eventualy link with object

# print(print.__doc__)

"""
sep
    string inserted between values, default a space.
  end
    string appended after the last value, default a newline.
  file
    a file-like object (stream); defaults to the current sys.stdout. 
  flush
    whether to forcibly flush the stream.

"""


# print(type.__doc__)

"""

type(object) -> the object's type
type(name, bases, dict, **kwds) -> a new type

"""








# *args and **kwargs
#====================

# lll *args and **kwargs are special python keywords that are used to pass 
#      the variable number of arguments to a function.

# *args
#------

#lll *args allows us to pass a variable number of non-keyword arguments to a function.
#     It is aggregated into a tuple.


def multiply(*args):   

    print(args)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)

    product = 1

    for i in args:
        product *= i
    
    return product


print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9)) # 362880





# **kwargs
#----------
# lll *args allows us to pass a variable number of keyword arguments to a function.
#     It is aggregated into a dictionary.



def display(**kwargs):

    print(kwargs) # {'name': 'Deepanshu', 'age': 22, 'qualification': 'B.Tech'}

    for (key, value) in kwargs.items():
        print(key, "->", value)



display(name="Deepanshu", age=22, qualification="B.Tech")


# name -> Deepanshu
# age -> 22
# qualification -> B.Tech




# Note : Point to remember while using *args and **kwargs
#---------------------------------------------------------

# order of the arguments matter (normal -> *args -> **kwargs)

