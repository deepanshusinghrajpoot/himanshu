

# raise Exception
#================

# In Python programming, exceptions are raised when error occur at runtime.




class Bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise Exception("amount can not be negative (-ve) !")
        elif self.balance < amount:
            raise Exception("You balance is less then this amount!")
        
        self.balance = self.balance - amount


obj = Bank(100000)

try:
    obj.withdraw(50000)

except Exception as e:
    print(e)

else:
    print(obj.balance)








# Create our won exception
# ========================

class MyException(Exception):
    def __init__(self, message):
        print(message)


class Bank1:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise MyException("amount can not be negative (-ve) !")
        elif self.balance < amount:
            raise MyException("You balance is less then this amount!")
        else:
            self.balance = self.balance - amount


obj1 = Bank1(100000)

try:
    obj1.withdraw(-50000)

except MyException as e:
    pass
else:
    print(obj1.balance)



# 50000
# amount can not be negative (-ve) !







# Simple Example
#---------------


class SecurityError(Exception):

    def __init__(self, message):
        print(message)

    def logout(self):
        print("logout")

class Google:

    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if self.device != device:
            raise SecurityError("Bhai teri lag gayi !")
        if email == self.email and password == self.password:
            print("Welcome ")
        else:
            print("login error")




obj = Google("Deepanshu Singh", "deepanshusingh234@gmail.com", "123456789", "android")

try:
    obj.login("deepanshusingh234@gmail.com", "123456789", "window")

except SecurityError as e:
    e.logout()

else:
    print(obj.name)

finally:
    print("Database connection closed!")


# Bhai teri lag gayi !
# logout
# Database connection closed!