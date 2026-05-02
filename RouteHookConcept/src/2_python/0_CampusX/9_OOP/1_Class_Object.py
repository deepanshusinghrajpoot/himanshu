



# What is class?
#===============

# lll Diffinition : Class is a blueprint/template that defines properties (data) 
#                   and behaviors (functions).



# class has two part
#--------------------
# 1. Data or property
# 2. Function or behavior


# Type of class
#---------------

# There are two type of class
# 1. builden class
# 2. user define class


# What is object?
#=================

#lll Diffinition : Object is an instance of a class, representing a real-world entity.



# syntax to create an object
#---------------------------

# obj_name = class_name()

L = list()










# We are write ATM machine code
#==============================


# Constructor : Special method invoked automatically at time of object creation. Used for Initialization.


class Atm:
    
    # constructor 
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    
    def menu(self):
        user_input = input("""
                
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exist  

        """)

        if user_input == '1':
            # create pin
            self.create_pin()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw()
            pass
        else:
            exit()


    def create_pin(self):
        user_pin = input("enter your pin : ")
        self.pin = user_pin

        user_balance = int(input("enter balance : "))
        self.balance = user_balance

        print("Pin created successfully!")

        self.menu()


    def change_pin(self):

        old_pin = input("enter old pin : ")

        if old_pin == self.pin:
            # let him change the pin
            new_pin = input("enter new pin : ")
            self.pin = new_pin

            print("pin change successfully!")
        
        else:
            print("your pin is wrong!")
            self.menu()


    def check_balance(self):
        
        user_pin = input("enter old pin : ")

        if user_pin == self.pin:
            print("you balance is : ", self.balance)
        
        else:
            print("your pin is wrong!")
            self.menu()



    def withdraw(self):

        user_pin = input("enter the pin : ")

        if user_pin == self.pin:

            amount = int(input("enter the account balance : "))

            if amount == self.balance:
                withdraw_amount = int(input("enter withraw amount : "))
                self.balance = self.balance - withdraw_amount

                print("Now your balance after withdraw : ", self.balance)
            
            else:
                print("you account balance not correct!")

        else:
            print("your pin is wrong!")

        self.withdraw()   








obj = Atm()

print(type(obj))  # <class '__main__.Atm'>
    







# class diagram
#---------------


# gpt add class diagram 

