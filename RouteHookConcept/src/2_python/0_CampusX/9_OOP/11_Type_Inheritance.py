

# Type of Inheritance
#--------------------

# Single Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Multiple Inheritance(Diamond Problem)
# Hybrid Inheritance








 # Single Level Inheritance
 # ------------------------

 # Single Level Inheritance → When a class (child) inherits directly from only one parent class. ✅
 
 # parent
 #  |
 #  |
 #  |
 # child


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
    pass
   


SmartPhone1(10000, "Apple", "13px").buy()
# Inside phone constructor1
# Buying from phone1!










# Multiple Level Inheritance
# --------------------------

# Person (name, age)
#    |
#    |
#    v
# Student (rollNo)
#    |
#    |
#    v
# GraduateStudent (researchArea)


# Multilevel Inheritance → When a class is derived from another derived class, forming a chain of inheritance. ✅


# Example

class Product2:
    def review(self):
        print("Product2 customer review!")


class Phone2(Product2):

    def __init__(self, price, brand, camera):
        print("Inside phone constructor2")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying from phone2!")



class SmartPhone2(Phone2):
    pass
   


s = SmartPhone2(10000, "Apple", "13px")

s.buy()
s.review()

# Inside phone constructor2
# Buying from phone2!
# Product2 customer review!










# Hierarchical Inheritance
# ------------------------


#                  parent
#                     |
#                     |
#                     |
#            ------------------
#            |                |
#            |                | 
#          child-1          child-2

          
# Hierarchical Inheritance → When multiple child classes inherit from a single parent class. ✅


# Example:

class Phone3:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor3")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying from phone3!")



class SmartPhone3(Phone3):
    pass
   

class FeaturePhone3(Phone3):
    pass


SmartPhone3(10000, "Apple", "13px").buy()
FeaturePhone3(20000, "sumsum", '24px').buy()


# Inside phone constructor3
# Buying from phone3!
# Inside phone constructor3
# Buying from phone3!









# Multiple Inheritance
# --------------------



# (name, rollno)                         (subject, salary)
# Student                                P.hD scholor
#  |                                       |
#  |                                       |
#  -----------------------------------------
#                          |
#                          |
#                 Teaching Assistant
                           

# Multiple Inheritance → When a child class inherits features from more than one parent class. ✅



# Example 1

class Phone4:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor4")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying from phone4!")



class Product4:
    def review(self):
        print("Customer review 4!")
   

class FeaturePhone4(Phone4, Product4):
    pass


s4 = FeaturePhone4(30000, "xomi", "20px")

s4.buy()
s4.review()

# Inside phone constructor4
# Buying from phone4!
# Customer review 4!



# Example 2

class Phone5:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor5")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying from phone5!")



class Product5:
    def buy(self):
        print("Buying from product5!")
   

# Method resolution order
class FeaturePhone5(Phone5, Product5):
    pass


s5 = FeaturePhone5(50000, "LAVA", "50px")

s5.buy()

# Inside phone constructor5
# Buying from phone5!




# Method resolution order :- first parent class method execute 
#........................




  

# Hybrid Inheritance
# ------------------

# Hybrid Inheritance → When more than one type of inheritance (single, multiple, multilevel, hierarchical) is combined in a program. ✅


#                person
#                  |
#                  |
#        -------------------------                
#        |                       |
#        |                       |
#     Student                   gradStudent
#        |                       |
#        -------------------------
#                    |
#                TeacherAssistant



