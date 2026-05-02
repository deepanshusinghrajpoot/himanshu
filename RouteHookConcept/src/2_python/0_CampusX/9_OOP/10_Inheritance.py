
# Inheritance
# -----------

# lll When properties & member functions of base class are passed on to the derived class.

            
# class A (Parent, Base)
#     |
#     |
#     |
#     |
#     |      (inherit)
#     -----> class B (Child, Derived)


# Inheritance is use for code reusability



# Example
#---------


class User:

    def __init__(self):
        self.name = "nitish"
        self.gender = "male"

    def login(self):
        print("login")





class Student(User):

    def __init__(self, roll_number):
        self.roll_number = roll_number

    def enroll(self):
        print("enroll into the course!")



u = User()
s = Student(1000)
print(s.roll_number) # 1000

# print(s.name)  # give error


# Concept 1:  In inheritance parent class constructor is called when child class does not contain constructor.
# Concept 2:  In inheritance child class can not access private member of the parent class.


# gpt add inheritance class diagram
#----------------------------------






# What gets inherited?
#=====================

# Constructor
# Non Private Attributes
# Non Private Methods



# Example:


class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone!")



class SmartPhone(Phone):
     
     def show(self):
         print("From child class!")
   


sp1 = SmartPhone(1000000, 'Apple', 13)

print(sp1.price, sp1.brand, sp1.camera) 

# Inside phone constructor
# 1000000 Apple 13






# Method Overriding
# =================

# lll base class & derive class both contain the same function with different implementation.
#     The base class function is said to be overridden.



# Example 

class Phone1:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor1")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying from phone1!")



class SmartPhone1(Phone1):
     
     def buy(self):
         print("Buying from SmartPhone1!")
   

sp2 = SmartPhone1(20000, "sumsung", 24)

sp2.buy() 

# Inside phone constructor1
# Buying from SmartPhone1!




# Super Keyword
# =============

# Diffinition
# ...........
# gpt give diffinition

# point
#......
# Super keyword always call only inside class
# Super keyword use to access only method




# Example 1:
#...........

class Phone2:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor2")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying from phone2!")



class SmartPhone2(Phone2):
     
     def buy(self):
         print("Buying from SmartPhone2!")

         # syntax to call parent ka buy method
         super().buy()

   

sp3 = SmartPhone2(20000, "sumsung", 24)

sp3.buy() 

# Inside phone constructor2
# Buying from SmartPhone2!
# Buying from phone2!


# Example 2:
#...........

class Phone3:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor3")
        self.price = price
        self.brand = brand
        self.camera = camera



class SmartPhone3(Phone3):
     
     def __init__(self, price, brand, camera, os, rem):
         print("Inside smartphone constructor3")
         super().__init__(price, brand, camera)
         self.os = os
         self.rem = rem
         print("Inside smartphone constructor3")

   

sp4 = SmartPhone3(20000, "sumsung", 24, "Andriod", 2)

# Inside smartphone constructor3
# Inside phone constructor3
# Inside smartphone constructor3





# Inheritance in summary
#-----------------------

# A class can inherit from another class
# Inheritance improves code reusability
# Constructor, attributes, methods get inherited to the child class
# The parent has no access to the child class
# Private properties of parent are not accessible directly in child class
# child class can override the attributes or methods. This is called method overriding

# super() is an inbuilt function which is used to invoke the parent class methods and constructor