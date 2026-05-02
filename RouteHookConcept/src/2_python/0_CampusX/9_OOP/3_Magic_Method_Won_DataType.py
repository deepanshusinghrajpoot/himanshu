
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







# Magic Methods or A.k.a Dunder Methods 
#======================================

# magic methods has super power

# syntax :   __name__  
# eg:  __init__



# constructor magic method(gpt choose relavent name)
#--------------------------

# __init__

# example

# def __init__(self, x, y):
#       self.num = x
#       self.dev = y




# use to show the object(gpt choose relavent name) 
#-----------------------

#  __str__

# example

# def __str__(self):
#     return '{}/{}'.format(self.num, seft.den)




# use to add the object(gpt choose relavent name) 
#-----------------------

#  __add__

# example

# def __add__(self, other):
#     new_num = self.num*other.den + other.num*self.den
#     new_den = self.den*other.den
#     return '{}/{}'.format(new_num, new_den)



# use to sub the object(gpt choose relavent name) 
#-----------------------

#  __sub__

# example

# def __sub__(self, other):
#     new_num = self.num*other.den - other.num*self.den
#     new_den = self.den*other.den
#     return '{}/{}'.format(new_num, new_den)



# use to mul the object(gpt choose relavent name) 
#-----------------------

#  __mul__

# example

# def __mul__(self, other):
#     new_num = self.num*other.den * other.num*self.den
#     new_den = self.den*other.den
#     return '{}/{}'.format(new_num, new_den)



# use to truediv the object(gpt choose relavent name) 
#-----------------------

#  __truediv__

# example

# def __truediv__(self, other):
#     new_num = self.num*other.den
#     new_den = self.den*other.num
#     return '{}/{}'.format(new_num, new_den)
