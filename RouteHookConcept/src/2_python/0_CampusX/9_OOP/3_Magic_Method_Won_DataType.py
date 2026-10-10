
# Magic Method
#==============

# lll "Magic methods are special double-underscore methods that Python
#      automatically calls to perform built-in operations on objects."



# Create our won data type (Fraction)
#=====================================


class Fraction:
    
    # parameterized constructo
    def __init__(self, x, y):
        self.num = x
        self.den = y

    # Non parameterize constructor
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)


    def __add__(self, other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den

        return '{}/{}'.format(new_num, new_den)

    
    def __sub__(self, other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den

        return '{}/{}'.format(new_num, new_den)
    

    def __mul__(self, other):
        new_num = self.num*other.den * other.num*self.den
        new_den = self.den*other.den

        return '{}/{}'.format(new_num, new_den)
    
    def __truediv__(self, other):
        new_num = self.num*other.den
        new_den = self.den*other.num

        return '{}/{}'.format(new_num, new_den)





f1 = Fraction(3, 4)
f2 = Fraction(1, 2)


print("Add fraction : ", f1 + f2)   # 10/8
print("Sub fraction : ", f1 - f2)   # 2/8
print("Mul fraction : ", f1 * f2)   # 24/8
print("Divi fraction : ", f1 / f2)  # 6/4






# Magic Methods (Dunder Methods)
# ==============================


# Syntax:
# __method_name__()


# Examples:
# __init__ , __str__ , __add__ , __sub__ , __mul__ , __truediv__


# Interview One-Liner:
# Magic methods give special powers to objects by allowing them
# to work with Python's built-in operators and functions.



# 1. Constructor Method
# ---------------------
# Magic Method: __init__
#
# Purpose:
# Automatically called when an object is created.
#
# Interview Answer:
# __init__ is a constructor method used to initialize
# object attributes at the time of object creation.

# Example

def __init__(self, num, den):
    self.num = num
    self.den = den



# 2. Object String Representation
# -------------------------------
# Magic Method: __str__
#
# Purpose:
# Controls how an object is displayed when using print().
#
# Interview Answer:
# __str__ returns a human-readable string representation
# of an object.

# Example

def __str__(self):
    return "{}/{}".format(self.num, self.den)



# 3. Object Addition Operator Overloading
# ---------------------------------------
# Magic Method: __add__
#
# Purpose:
# Defines behavior of the '+' operator for objects.
#
# Interview Answer:
# __add__ is used to perform addition between two objects.

# Example

def __add__(self, other):
    new_num = self.num * other.den + other.num * self.den
    new_den = self.den * other.den
    return "{}/{}".format(new_num, new_den)



# 4. Object Subtraction Operator Overloading
# ------------------------------------------
# Magic Method: __sub__
#
# Purpose:
# Defines behavior of the '-' operator for objects.
#
# Interview Answer:
# __sub__ is used to perform subtraction between two objects.

# Example

def __sub__(self, other):
    new_num = self.num * other.den - other.num * self.den
    new_den = self.den * other.den
    return "{}/{}".format(new_num, new_den)



# 5. Object Multiplication Operator Overloading
# ---------------------------------------------
# Magic Method: __mul__
#
# Purpose:
# Defines behavior of the '*' operator for objects.
#
# Interview Answer:
# __mul__ is used to perform multiplication between two objects.

# Example

def __mul__(self, other):
    new_num = self.num * other.num
    new_den = self.den * other.den
    return "{}/{}".format(new_num, new_den)



# 6. Object Division Operator Overloading
# ---------------------------------------
# Magic Method: __truediv__
#
# Purpose:
# Defines behavior of the '/' operator for objects.
#
# Interview Answer:
# __truediv__ is used to perform division between two objects.

# Example

def __truediv__(self, other):
    new_num = self.num * other.den
    new_den = self.den * other.num
    return "{}/{}".format(new_num, new_den)



# Quick Interview Revision
# ========================
#
# __init__      -> Object Initialization (Constructor)
# __str__       -> Object String Representation
# __add__       -> '+' Operator Overloading
# __sub__       -> '-' Operator Overloading
# __mul__       -> '*' Operator Overloading
# __truediv__   -> '/' Operator Overloading
#
# Interview One-Liner:
# Magic methods allow custom objects to behave like
# built-in Python data types.