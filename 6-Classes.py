'''
Date: 2021-03-22 19:26:25
LastEditors: GC
LastEditTime: 2022-02-25 16:41:24
FilePath: \Mosh Course 1\6-Classes.py
'''
# 1: Classes:
#      --> We can use classes to define new types to model real concepts. These types can have methods that we define in the
#             body of class and they can also have attributes that we can set anywhere in our programs.
# The difference of class and object:
#      --> Class: blueprint for creating new objects
#      --> Object: instance of a class
# For example:
#    class: Human
#    object: John, Mary, Jack


# class Point:
#     def move(self):
#         print("move")


#     def draw(self):
#         print("draw")


# point1 = Point()
#     # --> Creating a Point object

# print(type(point1))
# print(isinstance(point1, Point))
# # isinstance() --> Sometimes we have an object and we wanna know if this object is an instance of a given class.
# #                     In this example, we wanna see if this "point1" object is an instance of "Point" class.

# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 300
# print(point2.x)


# 2: Constructors
#   --> A constructor is a function that gets called at the time of creating an object.
# from abc import ABC, abstractmethod


# class Point:
#     def __init__(self, x1, y1):
#         #  __init__()  --> It is a magic method, and this magic method is called a Constructor, and it is executed when we create a new Point object.
#         #  And from this line of code,  we can know that "x" and "y" are the additional parameters for initializing a point object.
#         #  "self" is a reference to the current Point object.
#         self.x = x1
#         self.y = y1
#         #  And we can use "self" to set the x & y attritutes. We can set it to some default value like 0,
#         #  or this x argument or y argument I have been received in this method.

#         # From these line of codes, we can know that we defined two attributes x1 & y1 for point1 object in the constructor
#         # of the Point class. So whenever we create a new Point object, this Point object will have these attributes by default.

#     def move(self):
#         print("move")

#     def draw(self):
#         print(f"Point ({self.x} {self.y})")
#         #  --> So using "self", we can read attributes of the current object. Or we can also call other methods in this object.


# point1 = Point(10, 20)
# point1.z = 10
# #   --> And we can also define an attribute after we creating a point object.
# #   --> because objects in Python are dynamic. so we don't need to define all the attributes in a constructor.
# #   --> We can define them later whenever we need them.

# point1.draw()
# #   --> From this line of code, we can notice that when calling this draw() method, we didn't have to supply a value
# #       for the "self" parameter, because Python does it by default. So technically, we can pass the point object as
# #       a reference for the current object, like this: point1.draw(point1), but this is really unnecessary,
# #       it just makes our code busy or noisy.
# print(point1.x)


# # Summary: The method that define a class should have at least one parameter which by convention is called "self".
# #          and this references the current Point object that you are working with.
# #          When calling methods of an object, we never have to supply a value for this parameter. Python interpreter does that
# #          for us.


# Practice1:

# class Person():
#     def __init__(self, name):
#          self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")
# John = Person("John Fish")
# John.talk()

# bob = Person("Bob Smith")
# bob.talk()


# Practice 2:

# class Student:
#     def __init__(self, name, age, grade) -> None:
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade


# class Course:
#     def __init__(self, name, max_students) -> None:
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()

#         return value / len(self.students)


# s1 = Student("Tim", 23, 97)
# s2 = Student("John", 22, 99)
# s3 = Student("Bill", 21, 56)

# course = Course("Python", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())
# print(course.students[1].age)
# print(course.students[0].name)
# print(course.add_student(s3))



# 3: Class VS Instance Attributes:
#   --> Most of time, we will be using instance attributes, but there are times that you might want to define a class level
#       attribute that is shared accross all objects at a giving type.

# class Point:
#     default_color = "red"
# #   -> We can also define a class attribute in the body of this class, and we can read this via a class reference on an object reference.

#     def __init__(self, x1, y1):
#         self.x = x1
#         self.y = y1

#     def move(self):
#         print("move")

#     def draw(self):
#         print(f"Point ({self.x} {self.y})")


# Point.default_color = "Yellow"
# #  --> Be careful, I am using a class reference, so i am not working with any points objects, i am just working with Point class.
# #  --> And from this line of code, we can know that we have changed the default color to Yellow.

# point1 = Point(10, 20)
# print(point1.default_color)
# #  --> We can use this object reference to get access to the default color attributes.

# print(Point.default_color)
# #  --> We can also use this Point object reference to get access to the default color attributes.

# #  --> Class attributes are shared across all instances of a class.
# point1.z = 10
# point1.draw()
# print(point1.x)

# another = Point(3, 4)
# #   --> Run this program, we can know that these (another and point1) are complitely independent of each other. Each point has its own attribute.
# #   --> Just like John and Mary can have different eye colors.

# another.draw()
# print(another.default_color)
# #  --> From the result, the default_color is changed at first, and we can know that the class level attributes are shared across all the instances of a class.
# #  --> If you change their value and the change is visible to all of the objects of that type.


# # From this example, we have to know that all the attributes we have defined so far, x, y and z.
# # these are instance attributes, in other words, they are attributes that belong to point1 instance or point object.
# # so every point objects can have different values for this attribute.






# 4: Class VS Instance Methods:
#   --> We also have the same concept around the methods that we define in a class, so we have instance method as well as class method.


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # How to define a method at the class level.
#     @classmethod
#     #  To make this method as a class method, this is what we call a decorator(I need some ways to explain the behavior of a method or a function),
#     def zero(cls):
#         # With the "cls" --> We can know that we are not working with a point object or point instance.
        
#         return cls(0, 0)
#         # This is exactly like calling --> Point(0, 0). Their difference is that at the runing-time, when we call the zero() method,
#         # Python interpreter automatically pass a reference to the Point class to the zero() method.
    
#     def draw(self):
#         print(f"Point ({self.x} {self.y})")

# #  --> In this example, all these matters that we have defined in this Point class are instance methods --> __init__() and draw().
# #  --> So we can call them using an instance of the point class, using an object, like point.draw()
# #  --> Generally speaking, use this instance method whenever we need an object reference.
# #  --> For example, when drawing a point, you are really need to work with a specific point object. That is why draw() method is defined as an instance method.
# #  --> But there are times that we don't really need an existing object, and that's when we use a class method.

# # point = Point(0, 0)
# point = Point.zero()
# #  --> I am using a class reference. In this case, zero() is a method that is defined at the class level, and when we call it,
# #  --> it will return a point object, initialize with these zero values.
# #  --> So in this example, refer to the zero() method as a factory method. Because it is like a factory, it creates a new object.
# #  -->
# point.draw()





# 5: Static Method:
# class Math:
#     @staticmethod
#     def plus(x):
#         return x + 4

# # They do something but they do not change anything, they don't have access to anything, so in the plus() we don't need to add
# # something like self and cls.

# print(Math.plus(3))







# 6: Magic Methods:
#   --> Two examples of magic method (__init__ and __str__). For more information about the magic methods, go to Google and search "Python 3 Magic Methods"

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self) -> str:
#         return f"({self.x}, {self.y})"


#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# print(point)
# print(point.draw())







# 7: Comparing Objects:
#    --> There are times we need to compare two objects.

# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __eq__(self, other) -> bool:
#         return self.x == other.x and self.y == other.y
 
#     def __gt__(self, other1) -> bool:
#         return self.x > other1.x and self.y > other1.y


# point = Point(1, 2)
# other = Point(1, 2)

# point1 = Point(3, 4)
# other1 = Point(1, 2)

# print(point == other)
# # Without the magic method, From the result, we will get the "false". Because by default, this equality operator compares the references or addresses
# # of these two objects in memory. In order to solve this problem, we can use the magic method.

# print(point1 > other1)






# 8: Supporting Arithmetic Operations:
#   --> We also have magic method for performing arithmetic operations between two objects

# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y


#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#         # return Point(self.x + other.y, self.y + other.x)

# point = Point(10, 30)
# other = Point(1, 3)
# combined = point + other
# print(combined.x)
# print(combined.y)
# print(point.x + other.x)
# print(point.y + other.y)
# # print(point.x + other.y)
# # print(point.y + other.x)








# 9: Creating Custom Containers:
#   --> There are times you wanna create your own custom container types.

# class TagCloud:
#     def __init__(self) -> None:
#         self.tags = {}


#     def add(self, tag):
#         self.tags[tag] = self.tags.get(tag, 0) + 1
#         # self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
#     #  If we don't have it, we are going to set its value to one, otherwise we are going to incremented by one.


#     # Read a count of a tag:
#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)

#     # Set the number of a giving tag:
#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count


#     def __len__(self):
#         return len(self.tags)


#     def __iter__(self):
#         return iter(self.tags)
#     #  An iterator object is an object that walks a containter and gets one item at a time.


# # Create the cloud object:
# cloud = TagCloud()
# cloud["Python"]
# len(cloud)
# cloud.add("Python")
# cloud.add("Python")
# cloud.add("Python")
# cloud.add("python")

# print(cloud.tags)
# print(len(cloud))


# 10: Private members:
#   --> How we can make certain attributes or certain methods in a class private. If a prefix with double underscores(__)
#   --> on their squares, they are considered private.

# class TagCloud:
#     def __init__(self) -> None:
#         self.__tags = {}


#     def add(self, tag):
#         self.__tags[tag] = self.__tags.get(tag, 0) + 1


#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)


#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count


#     def __len__(self):
#         return len(self.__tags)


#     def __iter__(self):
#         return iter(self.__tags)

# cloud = TagCloud()
# print(cloud.__tags)
# #  Change "tags" to "__tags", and run this program, from the result(AttributeError: 'TagCloud' object has no attribute '__tags'),
# #  we can know that they are considered private
# cloud.add("Python")
# cloud.add("Python")
# cloud.add("Python")
# cloud.add("python")

# print(cloud.__tags["PYTHON"])


# cloud1 = TagCloud()
# print(cloud1.__dict__)
# #  From the result( {'_TagCloud__tags': {}} ), we can know that when Python interpreter runs this code, it automatically rename
# #  this attribute, and prefix it with what the name of its class. But technically you can still access it.
# print(cloud1._TagCloud__tags)
# #  We get an empty dictionary.
# #  Using double underscores is more of a convention to prevent accidental access of this private members.





# 11: Properties:
#   --> There are times that you wanna have control over an attribute in a class.

# class Product:
#     def __init__(self, price) -> None:
#         self.set_price(price)
#         # self.__price = price
#         # Instead of directly sending the price attribute, we call self.set_price() and give it this initital value(price)


#     def get_price(self):
#         return self.__price


#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price can not be negative.")
#         self.__price = value


# product = Product(-40)
#  Although the Python interpreter won't give me error, but it is not good. How can we prevent this? How can we ensure that our
#  products don't have a negative price.
#    --> One simple way: we can make this filed (price) private (__price) and then define two methods for getting and setting the value
#    --> of this attribute.
#    --> Another advanced way: Property is an object that sit in front of an attribute, it allows us to get for set the value of that attribute.










# 12: The Solution with Property:

# class Product:
#     def __init__(self, price) -> None:
#         self.set_price(price)


#     def get_price(self):
#         return self.__price


#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price can not be negative.")
#         self.__price = value


#     price = property(get_price, set_price)
#     # There are four functions which are optional. Be careful, i am not calling these two method, i am simply passing a reference to them
#     # So when we call this built-in property function, with this arguments, this function will return a property object,
#     # that property object will use the get_price to read the value of the price attribute,

# product = Product(10)
# print(product.price)



# Use the property class decorator to make our program better, our implemention will be cleaner and it will be less noisy:

# class Product:
#     def __init__(self, price) -> None:
#         self.price = price
#         #  We can use our price property like a regular attribute.


#     @property
#     def price(self):
#         return self.__price


#     @price.setter
#     # The name of this decorator starts with the name of our property in this case.
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price can not be negative.")
#         self.__price = value

# product = Product(10)
# print(product.price)







# 13: Inheritance:
#   --> Inheritance is a mechanism that allows us to define the common behavior or common function in one class.
#   --> Inheritance is not limited to method, we can also inherit the attributes of a base class.


# Mammal: Parent, Base class
# Dog, Cat: Child, sub class

# class Mammal:
#     def __init__(self) -> None:
#         self.age = 1

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

# print(dog1.age)
# #  When we create a mammal object, our mammal objects will automatically have the age attribute initialized one.
# cat1 = Cat()
# cat1.walk()
# cat1.be_annoying()








# 14: The Object Class:
#  --> We have a class called Object, and that is the base class for all classes in Python, every class we have directly or indirectly
#      derived from the object class.

# class Mammal(object):
#     def __init__(self) -> None:
#         self.age = 1


#     def walk(self):
#         print("Walk!")


# class Dog(Mammal):
#     def dark(self):
#         print("Dark!")


# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying!")

# dog1 = Dog()

# cat1 = Cat()

# print(isinstance(dog1, Dog))
# print(isinstance(cat1, Mammal))
# print(isinstance(dog1, object))
# #  Dog inherits from Mammal which inherits from object.
# print(issubclass(Dog, Mammal))
# print(issubclass(Dog, object))





# 15: Method Overriding:
#  --> What if we want to add a new Constructor to the Dog object and initialize its weight?

# class Mammal(object):
#     def __init__(self) -> None:
#         self.age = 1


#     def walk(self):
#         print("Walk!")


# class Dog(Mammal):
#     def __init__(self) -> None:
#         self.weihgt = 2


#     def dark(self):
#         print("Dark!")


# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying!")

# dog1 = Dog()
# print(dog1.age)
# print(dog1.weihgt)

# Run this program, we will get an AttributeError. Why? the reason is that the construtcor in the Mammal class was not executed.
# In other word, the constructor that would defined in the Dog class replace the constructor in the base class.
# This is what we call method overriding. That is say you are overriding or replacing a method in the base class.





# But what if we still wanna execute the constructor in the Mammal class and initialize the age of an animal, what should we do?
# We can use the built-in super() function the get access to the super or base class.

# class Mammal(object):
#     def __init__(self) -> None:
#         print("Mammal Constructor")
#         self.age = 1


#     def walk(self):
#         print("Walk!")


# class Dog(Mammal):
#     # def __init__(self) -> None:
#     #     super().__init__()
#     #     print("Dog Constructor")

#     #     self.weihgt = 2


#     def __init__(self) -> None:
#         print("Dog Constructor")

#         self.weight = 2
#         super().__init__()
#     #  And we can call the Mammal class after we initialize the Dog object.

#     def dark(self):
#         print("Dark!")


# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying!")

# dog1 = Dog()
# print(dog1.age)
# print(dog1.weight)


# From these two example, we can know that Method Overriding means replacing or extending a method defined in the base class.





# 16: Multi-level Inheritance
#  --> We can significantly increase the complexity of our software. Here is an example:

# class Animal:
#     def eat(self):
#         print("eat")


# class Bird(Animal):
#     def fly(self):
#         print("fly")


# class Chicken(Bird):
#     pass

# # From the Chicken class, The chicken class inherits all the features of bird class, but the chicken can't fly. So this is an
# # example of inheritance abuse and we should avoid it all the time. If we wanna use inheritance, limited to one or two levels.


# Multiple Inheritance:
#  --> It is similar to Multi-level inheritance, it is a source of issues, if we don't use it properly, we are going to introduce
#       all sorts of bugs in our program.

# class Employee():
#     def greet(self):
#         print("Employee Greet")


# class Person():
#     def greet(self):
#         print("Person Greet")


# class Manager(Employee, Person):
#     pass
# # It seems inherits all the features of the Person and Employee classes.


# manager = Manager()
# manager.greet()
# Both of these two classes, we have greet method, but from the result, we got the "Employee Greet". What is the reason?
# In Python interpreter, if we try to execute this line of code, at first, it will look the manager class to see if it has a
# method called "greet" . If it does not, it will look the first base class, if the Employee does not have this method,
# it will look the Person class.


# But Multiple Inheritance is not always a bad thing. It is bad if we do not use it properly.
# If the classes here(Like Person, Employee), they are small classes and they have absolutely nothing in common, and
# if you wanna inherit their features in a separate class, it is perfect fine to use the multiple inheritance.
# Things start to get complicated when these classes have things in common, like greet mathod here.
# Here is a good example of multiple inheritance:

# class Flyer():
#     def fly(self):
#         pass


# class Swimmer():
#     def swim(self):
#         pass
# # We can know that these two classes are very small and abstract, they have nothing in common.


# class FlyingFish(Flyer, Swimmer):
#     pass


# A good example of inheritance:
#  --> We can read the stream of data from a file, from the network or from the memory. All these stream have a few things in common,
#      we can read them, close them, read data from them. But how we read data from the stream is dependent upon the type of the stream.
#      Because read the data from a file is different from reading it form a network.

# class InvaidOperationError(Exception):
#     pass


# class Stream:
#     def __init__(self) -> None:
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvaidOperationError("Stream is already opened. ")
#         # Be careful, in this example, we can create a custom exception called invaid operation error. But we do not have
#         # a built-in function in Python that represents this concept, so on the top, we have to create a another class which is
#         # derived from the base class called Exception.
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvaidOperationError("Stream is already closed. ")
#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Reading a data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading a data from a network")

# # So from these line if code, first of all, we don't have Multi-Inheritance, we only have one or two levels depending on
# # how you want to calculate. We have this Stream class on top of a hierarchy, and below that we have two subclasses(FileStream and NetworkStream).
# # It is okay if you want to add another level of inheritance here, but we shouldn't go beyond that. Also as you can see we
# # do not have Multiple Inheritance, so our subclasses do not have multiple packs.


# Abstract Base Classes:
#  --> Its purpose is to provide some common code

# Example one:
# class InvaidOperationError(Exception):
#     pass


# class Stream:
#     def __init__(self) -> None:
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvaidOperationError("Stream is already opened. ")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvaidOperationError("Stream is already closed. ")
#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Reading a data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading a data from a network")


# stream = Stream()
# stream.open()

# There are a couple of issues with this implementation.
# The first issue is that we can create a stream object and call the open method. Because the Stream class is an abstract concept,
# What does it mean to open a stream? are we working with the file stream or network stream? What kind of the stream?
# So we should be able to directly create an instance of the stream class, we should always subclass and then create an instance
# of the subclass. So we only create this stream class, as a base class to provide some code that you are going to reuse across
# different kind of streams.


# If you look at the implementation of FileStream and NetworkStream classes, we can see both of these classes how to read message.
# But if tomorrow we decide to create a different kind of stream, we should remember to implement this read method, if you call
# it read line or read str or read whatever, it is not going to be consistent with the other kind of streams that we have here.
# In other words, currently there is no way to enforce a common interface across different kind of streams, this is more of a
# convention we have used here. It would be nice to have a common constract or common interface across these different kind of
# streams. So how can we solve these problems? That is when we use the abstract base class.
# So here we wanna make this Stream class and Abstract Base Class.
#


# Example two:
# We are going to use the abstractmethod as a decorator.
# As we can see, the name of module is all lowercase and the name of class is all uppercase.


# from abc import ABC, abstractmethod
# class InvaidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self) -> None:
#         self.opened = False


#     def open(self):
#         if self.opened:
#             raise InvaidOperationError("Stream is already opened. ")
#         self.opened = True


#     def close(self):
#         if not self.opened:
#             raise InvaidOperationError("Stream is already closed. ")
#         self.opened = False

#     # we need to decorate this method.
#     @abstractmethod
#     def read(self):
#         pass
#     # This method has no implementation here.
# class FileStream(Stream):
#     def read(self):
#         print("Reading a data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading a data from a network")
# stream = Stream()
# stream.open()

# First: we should derive the Stream class from the ABC class.
# Second: Find a common interface for all streams, we want all streams to have the read method and potentially a right method in the future.
# Then if we run this program, we will get an error:
# (TypeError: Can't instantiate abstract class Stream with abstract methods read). --> With abstract methods instantiated.
# That is mean one class as an abstract method, it is considered as an abstract class and we cannot instantiate them which
# means we cannot create an instance of them.


# Example three:
# from abc import ABC, abstractmethod


# class InvaidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self) -> None:
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvaidOperationError("Stream is already opened. ")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvaidOperationError("Stream is already closed. ")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading a data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading a data from a network")


# class MemoryStream(Stream):
#     pass
#     # def read(self):
#     #     print("Reading data from a memory stream")


# stream = MemoryStream()
# stream.open()

# We created a new class called MemoryStream(We do not have any implementation, use "pass"), and we create a stream object, similarly we will get an error. Why?
# In the Stream class we defined an abstract method called read. If a class derived from to Stream class, it has to implement
# this method, otherwise this class will also be considered abstract. So if we wanna to make this a concrete class so we can instantiated.
# we have to implement the read method. After implementing the read method, our MemoryStream is an concrete class, we can
# instantiate it, and it also follow the constract or the interface of the Stream class. So all the streams now have a read method.


# Polymorphism:
# from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")


# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()


# ddl = DropDownList()
# print(isinstance(ddl, UIControl))
# # From the result we know that the DropDownLis object is an instance of UIControl, and that means whatever we expect a UIControl
# # object, we can pass any derivatives like a TextBox or DropDownList.
# textbox = TextBox()
# draw([ddl, textbox])
# # What is interesting here? The draw function does not know what kind of control it's working with, this is determined at runtime.
# # it is simply iterate over the list of controls and calls to draw method of each control object. This is what we call polymorphism.
# # In this example, our draw method is taking many different forms and this is determined at runtime.
# # We could be calling the draw method in a textbox or a dropdownlist or radio button and so on.


# Duck Typing:
# --> Depending on the type of control object that they are working with at runtime, this draw method takes a different forms.
#     It might be the draw method in a textbox or dropdownlist or radio button and so on. So this is how polymorphism works.
#     But because Python is a dynamically typed language, we do not necessarily need this UIControl as the base class.
#     Here is the changes:


# from abc import ABC, abstractmethod


# class TextBox():
#     def draw(self):
#         print("TextBox")


# class DropDownList():
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()

# With these line of code without base class which is UIControl, we can still achieve polymorphism behavior.
# Look at the "controls" parameter, nowhere here you have specified the type of this parameter, this is purity and label(a name),
# we can pass any kind of objects to destory the function. As long as that object is iterable, Python will be happy.
# Because here you are looping over that object, so that object has to be iterable. So technically we can pass a
# string, a list, a tuple, dictionary, anything that is iterable here. By the same token, that iterable object(controls) --> its individual
# parts should have a draw method. The Python does not care if these objects to write from the UIControl class.
# As long as these objects have a draw method, Python will be happy. This is why we call Duck Typing, that is how Python works,
# Because Python is a dynamically typed language and it does not check the type of object. It only looks for the existence of
# certain methods in their objects. In other words, in this case, it only looks for the existence of draw method,
# so this object has a draw method. It's exactly like saying, if it walks like a duck, and quacks like a duck, it is a duck.
# So ratchet polymorphism behavior, we don't necessarily need a base class like UIControl, because Python supports Duck Typing.
# Having said that, have a UIControl as an abstract base class is a good practice. because it enforces a common interface or
# common contract across all distributive. With this will make sure that every kind of UIControl will have the draw method.


# Extending Built-in Types:
#  --> In Python we can also use inheritance with the built-in types,

# Example one:
# class Text(str):
#     # We defined a Text class which inherits from the built-in str class, with this our Text class will inherit all the features
#     # of Python string, but we can also add additional features to it, for example, we can add the ability to summarize it,
#     # or duplicate it and so on.
#     def duplicate(self):
#         return self + self
#     # "self" represents the current object which is an instance of a string class in this case.


# text = Text("Python")
# print(text.lower())
# print(text.duplicate())


# Example two:
# class Text(str):
#     def duplicate(self):
#         return self + self


# class TrackableList(list):
#       def append(self, object):
#           print("Append Called")
#           super().append(object)

# list = TrackableList()
# list.append("1")

# From these two examples, as we can see, extending built-in types in Python is really easy.


# Data Classes:
#  --> We may come across classes that do not have any behaviors, they do not have any methods, they only have data.
# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y


#     # def __eq__(self, other) -> bool:
#     #     return self.x == other.x and self.y == other.y
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)

# # Run this program, we will get False. Because these two objects are stores in different locations in memory. So by default,
# # Python compares objects based on where they are stored in memory. If two variables are referencing the same object in memory,
# # they are considered equal. In this example, our two Point objects are in two different location, even though they have the
# # same attributes.

# print(id(p1))
# print(id(p2))
# # From the result of these two lines, we can see where these two objects are in two different locations in memory.
# # The solution of comparing two objects, we should go to Point class and implement a magic method(__eq__)


# But writing these codes is a little bit tedious, if you are dealing with classes that have no bahavoir, no method, it only
# has data, you can use a namedtuple instance.

# from collections import namedtuple
# Point = namedtuple("Point", ["x", "y"])
# # The first argument with a specified the name for this new type you want to create, as the second argument, array, it wants
# # our Point objects to have two attributes -- x and y. So this return the namedtuple that we can store.

# p1 = Point(x=1, y=2)
# # Instead of passing the arbitrary value here, we should pass keyword arguments.
# # The first improvement here is that our code is more clear and less ambiguous. We don't have to wonder what are these values.
# # The second benifit is that we don't have to explicitly implement a magic method to compare two objects.
# print(p1.x)

# p2 = Point(x=1, y=2)
# p2.x = 10
# print(p2)
# # And we have to notice that these namedtuples are immutable which means once
# # we create them we can not modify them, we can not mutate them. That is to say, we can not set an attribute of a namedtuple
# # after the initializer. So if you really need to modify one of these values, you need to create a new Point object.
# # p2 = Point(x=10, y=2)

# print(p1 == p2)

# # So if you are working with classes that has only data without methods, you might want to use the namedtuple instead, you will
# # write less code, and this namedtuple is better than regular tuple. Because it will have attributes in this Point object, just
# # like the attributes we have in our classes.


# Generating Random Values:
# Practice1:
# import random
# for i in range(3):
#     print(random.random())
#     print(random.randint(10, 20))

# Practice2:
# import random
# numbers2 = ["John", "Mary", "Bob", "Mosh"]
# leader = random.choice(numbers2)
# print(leader)

# Practice3: 掷骰子
# import random
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second


# dice = Dice()
# print(dice.roll())


# Files and Directories:
# Absolute path: We start from the root of our hard disk.
#                       --> For example: C:\ Program Files\Microsoft
# Relative path:

# from pathlib import Path
# path = Path("ecommerce")
# print(path.exists())
# # 创建新文件目录 --> mkdir()
# # 删除已经创建好的文件目录 --> rmdir()
# path1 = Path("emails")
# print(path1.rmdir())

# We can use the glob method to search for files using a pattern, we can also get all the files and directories in the current path(only use "*").
# from pathlib import Path
# path = Path()
# for file in path.glob("*"):
#     print(file)
