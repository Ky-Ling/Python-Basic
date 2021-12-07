'''
Date: 2021-08-18 09:27:07
LastEditors: GC
LastEditTime: 2021-10-21 21:58:40
FilePath: \Mosh Course 1\7-Modules.py
'''


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


# How do we decide what functions or what classes we should put in what module?
# Module should contain highly related objects, these objects can be functions, classes, variables and so on.
# Here in an example:

# def calc_tax():
#     pass


# def calc_shipping():
#     pass

# These functions have no implementation, but they are highly related to the concept of sales. We have to calculate tax and
# calculate shipping.
# So now let us put these functions in a separate module called sales.

# First: create a new Python file called sales.py
# Then move all these code into the sales.py
# Now we need to import one or two functions from the sales.py, what should we do? We have different ways to do it.

# from sales import calc_shipping
# # from sales import calc_tax
# # from sales import calc_tax, calc_shipping

# calc_shipping()
# # calc_tax()


# There is also another way to import a module:
# import sales
# sales.calc_tax()


# Module Search Path:
# import sales
# # When Python see this line of code, it will look for a file called sales.py in the current directory, if it does not find this
# # file, it will look in a bunch of predefined directories that comes with Python installation.
# import sys
# print(sys.path)
# # It will return a list of diretories that Python will look at to find a module.
# # Run this program, we will get an array of strings.
# # So when Python see an import statement, it will search all the diretories to find this module, as soon as it find the module,
# # the search stops there.


# # How can we import a module from a subdirectory. It is about packages.


# Packages:
#    --> A packages is a container for multiple modules. In file system, a packages is a directory or folder.
#

# First of all, Move the "sales.py" into "ecommerce":

# import sales
# After we moving the "sales.py" into "ecommmerce", and from this line, there is something wrong. That is because Python
# can not find a sales module. To address this problem, we should add a new file called __init__.py in the commmerce.
# When we add this file here, Python will treat this ecommmerce folder as a package, so package is a container for one or two
# modules. In file system terms, a package is map to diretory, and a module is map to file. So change this line of code:

# import ecommerce.sales
# # So use any of the objects in the sales module, we should prefix that with the name of their package and module
# ecommerce.sales.calc_shipping()
# ecommerce.sales.calc_tax()
# # from these two lines of code, we know there are tedious, a better approach is to use the From statement.

# from ecommerce.sales import calc_tax
# calc_tax()

# What if we wanna use multiple objects in the sales module, we can use "from ecommerce.sales import calc_tax, calc_shipping",
# But it is noisy, not a good way, here is another better approach:
# from ecommerce import sales
# # Import this sales module as an object, and then we can use the "." operator to access all the members of this module:
# sales.calc_shipping()
# sales.calc_tax()


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


# Sub-packages:
#   --> Imagine that our ecommerce package has grown a lot, we have so many files and modules here, so we decide to break this
#       package into a few subpackages. So we create a new folder under the ecommerce package, and move the "sales.py" into
#       this new folder. So on the top we have the ecommerce package, and under that we have the shopping package. The currently
#       this shopping package is not a package, because in this folder we do not have the __init__ file. So under the shopping
#       package, we have to create a new file called __init__.py.

# from ecommerce.shopping import sales


# Intra-package References:
#  --> From the ecommerce package, we created a new subpackage called customer, and this package has two files, __init__.py and contact.py.
#      In the sales module of shopping package, if we wanna use the contact module in the customer package. What should we do?

# Go to the sales.py, and implement these lines of code:

# # The absolute import:
# from ecommerce.customer import contact
# # The Related import:
# # from ..customer import contact
# # "." represents the current package, ".." takes us one level up
# # But most of time we use the absolute import.
# contact.contact_customer()

# def calc_tax():
#     pass


# def calc_shipping():
#     pass


# The dir() function
#  --> With this function, we can get the list of attributes and methods to find in an object.
# from ecommerce.shopping import sales
# print(dir(sales))
# # Run this program, we get an array of strings, in this array, we have all the attributes and method defined in an object.
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)


# Executing Modules as Scripts:

# Go to the sales.py, and implement these lines of code:
# print("Sales initialized")

# def calc_tax():
#     pass

# def calc_shipping():
#     pass


# Currently we have these two functions, and we can also write any statements and these statements will be executed at the
# first time when this module is loaded. So if there are different modules in our program, Python will load this module only
# once and cash it in memory, so the statements that be written here will be executed once.

from ecommerce.shopping import sales

# Using the same technique, we can write the initialization code in for package, so go to the __init__.py of ecommmerce,
# write this line of code: print("Ecommerce initialized")
# And run this program.
