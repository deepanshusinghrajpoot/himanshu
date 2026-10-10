# Static Variable Vs Instance Variable
# ====================================

# Instance Variable
# -----------------
#


# Definition:
# lll An instance variable is a variable whose value is unique
#     to each object of a class.


# Key Points:
# 1. Belongs to an object.
# 2. Created using the self keyword.
# 3. Every object maintains its own separate copy.
# 4. Values can differ from object to object.
#
# Examples:
# name
# balance
# age
# salary



# Static Variable (Class Variable)
# --------------------------------
#
# Definition:
# lll A static variable is a variable whose value is shared
#     among all objects of a class.
#
# Key Points:
# 1. Belongs to the class, not an object.
# 2. Only one copy exists in memory.
# 3. Shared by all objects.
# 4. Declared directly inside the class and outside methods.
#
# Examples:
# IFSC Code
# Bank Name
# Company Name
# College Name



# Banking System Example
# ----------------------
#
# name       -> Instance Variable
# balance    -> Instance Variable
# account_no -> Instance Variable
# IFSC Code  -> Static Variable
#
# Reason:
# Every customer has a different name, balance,
# and account number.
#
# But the IFSC code remains the same for all
# accounts of the same bank branch.



# Interview One-Liner
# -------------------
#
#  lll Instance Variable:
#      "Each object has its own separate copy."
#
#  lll Static Variable:
#      "One copy is shared among all objects of the class."



# ==========================================================
# Static Method Vs Normal Method
# ==========================================================

# Normal Method
# -------------
#
# lll Definition:
#     A normal method belongs to an object.
#
# Key Points:
# 1. First parameter is self.
# 2. Can access instance variables.
# 3. Can access static variables.
# 4. Called using an object.
#
# Example:
#
# obj.method()



# Static Method
# -------------
#
# lll Definition:
#     A static method belongs to the class rather than
#     an object.
#
# Key Points:
# 1.     lll It create by using @staticmethod decorator.
# 2. Does not require self.
# 3. Cannot directly access instance variables.
# 4. Mainly used for utility/helper methods.
# 5. Can be called using the class name.
#
# Example:
#
# ClassName.method()



# What is a Utility Method?
# -------------------------
#
# A utility method performs a common task and does not
# depend on object-specific data.
#
# Examples:
# - Calculate Interest
# - Validate Email
# - Convert Temperature
# - Generate OTP
# - Calculate Tax



# ATM Example
# -----------

class Atm:

    # Static Variable
    counter = 1

    def __init__(self):

        # Instance Variables
        self.pin = ""
        self.__balance = 0

        self.cid = Atm.counter
        Atm.counter += 1


    # Static Method
    @staticmethod
    def get_counter():
        return Atm.counter


    # Normal Method
    def show_customer_id(self):
        print(self.cid)



# Object Creation

c1 = Atm()
print(c1.cid)      # 1

c2 = Atm()
print(c2.cid)      # 2

c3 = Atm()
print(c3.cid)      # 3

print(Atm.counter) # 4



# Quick Interview Comparison
# ==========================

# Normal Method
# -------------
# Belongs To     -> Object
# First Argument -> self
# Access Instance Variables -> Yes
# Access Static Variables   -> Yes
# Call Using     -> Object


# Static Method
# -------------
# Belongs To     -> Class
# First Argument -> No self
# Access Instance Variables -> No
# Access Static Variables   -> Yes
# Call Using     -> Class Name



# Most Asked Interview Question
# -----------------------------
#
# Q. When should we use a static method?
#
# Answer:
# We use a static method when the method does not need
# any object-specific data and performs a common utility task.



# 30-Second Interview Summary
# ---------------------------
#
# Instance Variable -> Unique for every object.
#
# Static Variable -> Shared among all objects.
#
# Normal Method -> Works with object data and uses self.
#
# Static Method -> Utility/helper method that belongs
#                  to the class and uses @staticmethod.