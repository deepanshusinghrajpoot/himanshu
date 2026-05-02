"""



Abstraction
-----------

Hiding all unnecessary details & showing only the important parts.



Abstract Class
--------------

An abstract class is a class that contains 
at least one abstract method.




Abstract Method
---------------

An abstract method is a method that is declared 
but does not contain any implementation.


In Python, an abstract class is created in two steps:

1. Inherit from ABC (Abstract Base Class)
2. Use the @abstractmethod decorator




"""

from abc import ABC, abstractmethod


class BankApp(ABC):

    def database(self):
        print("Connected to database")

    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):

    def mobile_login(self):
        print("Mobile Login Security")

    def security(self):
        print("Mobile Security Implemented")


# If we do not implement the abstract method (security)
# inside MobileApp, Python will not allow object creation.


mob = MobileApp()
mob.database()
mob.security()


