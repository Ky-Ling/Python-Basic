'''
Date: 2021-03-22 19:26:25
LastEditors: GC
LastEditTime: 2021-07-19 09:31:37
FilePath: \Mosh Course 1\Classes copy.py
'''
# Classes
#      --> We can use classes to define new types to model real concepts. These types can have methods that we define in the 
#             body of class and they can also have attributes that we can set anywhere in our programs.
# class Point:
#     def move(self):
#         print("move")


#     def draw(self):
#         print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 300
# print(point2.x)


# Constructors
#   --> A constructor is a function that gets called at the time of creating an object.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")


#     def draw(self):
#         print("draw")

# point1 = Point(10, 20)
# print(point1.x)


# 
# Practice:
# class Person():
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")
# John = Person("John Fish")
# John.talk()

# bob = Person("Bob Smith")
# bob.talk()


# Inheritance
# class Mammal:
#     def walk(self):
#         print("Walk!")


# class Dog(Mammal):
#     def dark(self):
#         print("Dark!")
# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying!")

# dog1 = Dog()
# dog1.walk()
# dog1.dark()

# cat1 = Cat()
# cat1.walk()
# cat1.be_annoying()


# Modules
#     --> A modules in Python is basically a file with some python code, and we use modules to organize our code into files.
# Two ways to import module:
# 
# (1)
# import converters
# print(converters.kg_to_lbs(70))
# 
# (2)
# import converters
# from converters import kg_to_lbs
# print(kg_to_lbs(700))
# 
# 
# Practice:
# (1)
# import utils
# utils.find_max()
# numbers1 = [10, 30, 4, 56, 677]
# print(max1) 
# (2)
# import utils
# from utils import find_max
# numbers1 = [10, 30, 4, 56, 677]
# max1 = find_max(numbers1)
# print(max1)



# Packages
#    --> A packages is a container for multiple modules. In file system, a packages is a directory or folder.
# 
# Ways to use packages:

# (1)
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# (2)
# from ecommerce.shipping import calc_shipping
# calc_shipping()

# (3)
# from ecommerce import shipping
# shipping.calc_shipping()


# Generating Random Values:
