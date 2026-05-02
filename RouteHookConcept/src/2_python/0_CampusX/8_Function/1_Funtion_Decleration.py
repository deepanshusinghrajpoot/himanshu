

# Let's create a function to check number is odd or even(with docstring)


def is_even(a):
    '''
    This function use to find the number is odd or even
    Input - any valid integer
    Output - odd/even
    Created on - date
    '''
    if type(a) == 'int':
        if a%2 != 0:
            print(a, " is an odd number!")
        else:
            print(a, " is a even number!")
    else:
        print("Chek your data type!")


is_even(9) # 9  is an odd number!
is_even(10) # 10  is a even number!






# Parameter Vs Arguments
#========================

# paraneter :- is use by function
# argument :- is pass into function


# Type of Arguments
#-------------------

# Default Argument
# Positional Argument
# Keyword Argument


# Default Argument
#.................
def power(a=1, b=1):
    return a**b

print(power(2,2)) # 4




# Positional Argument
#....................

print(power(2,3)) # 8



# Keyword Argument
#.................

print(b=3, a=2) # 8