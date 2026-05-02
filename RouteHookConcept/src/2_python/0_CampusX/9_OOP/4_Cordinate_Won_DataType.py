

# Ques: Write OOP classes to handle the following scenarios
#==========================================================

# 1. A user can create and view 2D coordinates
# 2. A user can find out the distance between 2 coordinates
# 3. A user can find the distance of a coordinate from origin
# 4. A user can check if a point lies on a given line
# 5. A user can find the distance between a given 2D point and a given line


import math


class Point:

    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod, self.y_cod)

    def euclidean_distance(self, other):
        distance_two_point = ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
        return distance_two_point

    def distance_from_origin(self):
        # distance_origin = ((self.x_cod)**2 + (self.y_cod)**2)**0.5
        # return distance_origin
        # OR
        return self.euclidean_distance(Point(0,0))




class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    
    def __str__(self):
        return '{}x + {}y + {}'.format(self.A, self.B, self.C)
    
    def point_on_line(self, point):
        if self.A*point.x_cod + self.B*point.y_cod + self.C == 0:
            print("lies on line!")
        else:
            print("does not lie on line!")
    
    def sort_dist_line_point(self, point):
        sortest_distance = abs(self.A*point.x_cod + self.B*point.y_cod + self.C) / (point.x_cod**2 + point.y_cod**2)**0.5
        return sortest_distance




p1 = Point(2, 3)
p2 = Point(2, 2)
p3 = Point(-2, -2)

# ans 1
#.......
#<x,y>
print(p1) # <2,3>
print(p1) # <2,2>

# ans 2
#.......
print(p1.euclidean_distance(p2)) # 1.0


# ans 3
#.......
print(p2.distance_from_origin()) # 2.8284271247461903



# ans 4
#.......
l1 = Line(1, 1, 4)
l1.point_on_line(p1) # does not lie on line!
l1.point_on_line(p3) # lies on line!

# ans 5
#......

print(l1.sort_dist_line_point(p3)) # 0.0














# How objects access attributes
#==============================

class Person:

    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == "Ind":
            print("Namaste Bhai !")
        else:
            print("Hellow Bro !")



person1 = Person("Rohan", "Ind")
person2 = Person("Max well", "Aus")


# How to access attribute
print(person1.name) # Rohan

# How to access method
person1.greet() # Rohan bhai


# Note : Object allow to create attribute and method outside the class
#---------------------------------------------------------------------

person1.gender = "male"
print(person1.gender) # male
