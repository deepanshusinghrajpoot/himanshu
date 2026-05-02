

# Static Variable Vs Instance Variable
#=====================================

# Instance Variable
#------------------

# Definition
#...........
# Instance variable is unique for every object
# Instance variable belongs to an object


# Static Variable
#----------------

# Definition
#...........
# Static variable is the same for every object
# Static variable belongs to the class



# Example: We are designing a banking system
#-------------------------------------------

# What is instance or static?
# name        -> Instance
# balance     -> Instance
# IFSC code   -> Static


# Some important points about static variables
#---------------------------------------------
# Static variables are declared outside the constructor




# Static Method Vs Normal Method
#===============================

# Normal Method
#--------------

# Definition
#...........
# lll Normal method is a method of an object
# It can access both instance and static variables


# Static Method
#--------------

# Definition
#...........
# lll Static method is a method of a class
# Static method is used to create utility methods (small/common tasks)

# lll Static method is indicated by: @staticmethod



class Atm:

    counter = 1
    
    # constructor 
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.cid = Atm.counter
        Atm.counter = Atm.counter + 1
        #self.__menu()
    





    # utility method
    @staticmethod
    def get_balance():
        return Atm.__balance







    
    def __menu(self):
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
        else:
            exit()


    def create_pin(self):
        user_pin = input("enter your pin : ")
        self.pin = user_pin

        user_balance = input("enter balance : ")
        self.__balance = user_balance

        print("Pin created successfully!")

        self.__menu()


    def change_pin(self):

        old_pin = input("enter old pin : ")

        if old_pin == self.pin:
            # let him change the pin
            new_pin = input("enter new pin : ")
            self.pin = new_pin

            print("pin change successfully!")
        
        else:
            print("your pin is wrong!")
            self.__menu()


    def check_balance(self):
        
        user_pin = input("enter old pin : ")

        if user_pin == self.pin:
            print("you balance is : ", self.__balance)
        
        else:
            print("your pin is wrong!")
            self.menu()



    def withdraw(self):

        user_pin = input("enter the pin : ")

        if user_pin == self.pin:

            amount = input("enter the account balance : ")

            if type(amount) == int and amount == self.__balance:
                
                withdraw_amount = input("enter withraw amount : ")
                self.__balance = self.__balance - withdraw_amount

                print("Now your balance after withdraw : ", self.__balance)
            
            else:
                print("Enter valid value! OR  your account balance not correct!")
        else:
            print("your pin is wrong!")
        

 

c1 = Atm()
print(c1.cid) # 1

c2 = Atm()
print(c2.cid) # 2

c3 = Atm()
print(c3.cid) # 3


print(Atm.counter) # 4

