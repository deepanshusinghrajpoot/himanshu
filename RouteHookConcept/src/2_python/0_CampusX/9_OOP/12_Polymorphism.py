"""
Polymorphism in Python
---------------------

Polymorphism is the ability of objects to take on different forms or behave in different
ways depending on the context in which they are used.


In Python, polymorphism is implemented in three ways

1. Method overriding
2. Method overloading
3. Operator overloading


1. Method Overriding
====================

 lll Base class & derived class both contain the same method with different implementations.
     The base class method is said to be overridden.


2. Function Overloading (method overloading)
=============================================

  When two or more functions in the same class (or scope) have the same name but a different
  number or type of parameters, it is called function overloading.
  
  lll When a class has more than one method with the same name but different numbers of
      parameters, it is called method overloading.
  

Python doesn't support method overloading.
We achieve it using default arguments.

"""

# Example


class Shape:

    def area(self, a, b=0):
        if b == 0:
            return 3.14 * a * a
        else:
            return a * b
          

s = Shape()

print(s.area(2))      # 12.56
print(s.area(2, 3))   # 6





"""
# Operator Overloading
#=====================

# When an operator is used to perform different operations depending on the operands,
# it is called operator overloading.


# lll In Python, operator overloading is achieved using magic methods
#     such as __add__, __sub__, __mul__, __truediv__, etc. inside a class.


# These methods allow operators like +, -, *, / to work with user-defined objects.

"""

class Fraction:
    
    # parameterized constructor
    def __init__(self, x, y):
        self.num = x
        self.den = y

    # non-parameterized constructor
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)


    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

        return '{}/{}'.format(new_num, new_den)

    
    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den

        return '{}/{}'.format(new_num, new_den)
    

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        return '{}/{}'.format(new_num, new_den)
    
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        return '{}/{}'.format(new_num, new_den)





f1 = Fraction(3, 4)
f2 = Fraction(1, 2)


print("Add fraction : ", f1 + f2)    # 10/8
print("Sub fraction : ", f1 - f2)    # 2/8
print("Mul fraction : ", f1 * f2)    # 3/8
print("Div fraction : ", f1 / f2)    # 6/4





"""


1. Constructor Overriding
=========================

 lll Base class & derived class both contain constructors with different implementations.
     The base class constructor is said to be overridden.
"""
