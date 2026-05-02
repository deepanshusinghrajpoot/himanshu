


# Reference Variables
#====================

# 1. Reference variable hold the objects
# 2. We can create objects without reference variable as well
# 3. An object can have multiple reference variables
# 4. Assigning a new reference variable to an existing object not create a new object


class Person:

    def __init__(self):
        self.name = "nitish"
        self.gender = 'male'


# ans 1
#.......

p = Person()


# ans 2
#......

print(Person()) # <__main__.Person object at 0x000001BB69934B50>


# ans 
#....

p1 = Person()
p2 = p1

print(id(p1)) # 2770203003728
print(id(p2)) # 2770203003728





# Pass by referece
#==================


class Car:

    def __init__(self, brand_name, model_name, model_car_price):
        self.brand = brand_name
        self.model = model_name
        self.price = model_car_price


def greet(car):
    print(id(car))
    print("Car brand name:", car.brand, "|Car model name:", car.model, "|Car model price:", car.price)
    return car


c1 = Car("mahindra", "SUV 500", "10 lakh")

print(id(c1))      # 2916404230096
c2 = greet(c1)     # 2916404230096
                   # Car brand name:mahindra |Car model name:SUV 500 |Car model price:10 lakh
print(id(c2))      # 2916404230096

# Memory address same So, Here object is pass by reference



# How deside argument is pass by referece or pass by value
#---------------------------------------------------------
# When we pass immutable object then they pass by value
# When we pass mutable object then they pass by reference

# So, we can say that all user define object are mutable







# What is instance variable
#---------------------------
# In upper give class :- brand , model, price are instance variable

# Note :- That vriable is qnique for every object
#      :- har ek object ke liye alag hota(conver into eglish as interview spoken)



