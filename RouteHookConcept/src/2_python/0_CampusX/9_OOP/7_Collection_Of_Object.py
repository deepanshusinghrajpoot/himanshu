



# Collection of object
#=====================

class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


p1 = Person("deepanshu", "male")
p2 = Person("himanshu", "male")
p3 = Person("ankita", "female")

L = [p1, p2, p3]

for i in L:
    print(i.name, i.gender)

# deepanshu male
# himanshu male
# ankita female