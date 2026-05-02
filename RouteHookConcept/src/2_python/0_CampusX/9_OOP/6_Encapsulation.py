# How To Make Private Member in Python
#====================================

# In Python, we make a private member using double underscore:  __

# Note:
# Python internally creates a private member as:
# _ClassName__variableName
# Because of this, the private variable can still be accessed or modified.

#*****************************************
# lll In Python, nothing is truly private
#*****************************************
# Because Python is a programming language made for adults.



# How to access private members in the right way
#-----------------------------------------------

# Using getter and setter methods
#................................

# Getter : Used to access (get) the private member
# Setter : Used to modify (set) the private member






# Encapsulation
# -------------

#lll Encapsulation is wrapping up data and the two member functions
#    (getter and setter) into a single unit called encapsulation.
#    Technically :- for every attribute, we create one getter and one setter.

#           ------------------------------------------------------
#          |  data / properties / attributes   |  getter & setter |
#           ------------------------------------------------------

# Encapsulation is used for data hiding.










# example :- 

class Atm:
    
    # constructor 
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        #self.__menu()
    
    def get_balance(self):
        return self.__balance


    def set_balance(self, new_balance):
        if type(new_balance) == int:
            return self.__balance
        else:
            print("Enter valid value!")

    
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
        

 



obj = Atm()

obj.__balance = "hahaa"
# here our private member variable not change because the variable store as : _Atm__balance


print(obj.get_balance()) # 0
obj.set_balance("hahaa")


print(obj._Atm__balance) # 0

