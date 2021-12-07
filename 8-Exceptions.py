'''
Date: 2021-03-14 19:58:46
LastEditors: GC
LastEditTime: 2021-10-21 22:18:40
FilePath: \Mosh Course 1\8-Exceptions.py
'''
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
#     print(risk)
# except ZeroDivisionError:
#     print("Age can't be 0")
# except ValueError:
#     print("Invalid value")


# Handling Exceptions:
# try:
#     age = int(input("Age: "))

# except ValueError as ex:
#     print("You didn't enter a valid age.")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown.")
# print("Execution continues.")


# Handling Different Exceptions:
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except ValueError:
#     print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     print("Age can't be 0")
# else:
#     print("No exceptions were thrown")


# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")


# Cleaning UP:

# try:
#     file = open("Exceptions.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
#     # 如果中间的两行代码抛出异常，则无法执行最后文件关闭(file.close())的代码。我们可以把这行代码移至第70行代码后面，但是这行代码只有抛出异常之后才能执行，故这个方法行不通。
#     # 所以我们可以通过finally clause 来解决。
#     #    -->The finally clause is always executed whether we have an exception or not.
#     # file.close()
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")
# finally:
#     file.close()


# The With Statement:
# try:
#     with open("Exceptions.py") as file:
#         print("File opened.")
#     #  --> In this block of code, we can work with this file object, for example we can read something from this file or write to it and so on.
#     #  --> This is the file object that the open function returns.
#     #  --> Use the with statement, Python will automatically call the finally clause whether we have a finally clause or not.
#     #  --> In other words, the with statement is used to automatically release external resources。

#     with open("Exceptions.py") as file, open("Python.txt") as target:
#         print("File opened!")
#     #   --> We might be working with multiple external resources.
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")


# Raising Exceptions:
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age can't be 0 or less !")
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)


# Cost of raising exceptions:
#     -->Instead of raising an exception and handing try-exception functions, it could take a another different approach,
#     -->that would result in better performance.

from timeit import timeit
#    --> With this function, we can calculate the execution time of some Python code.
# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age can't be 0 or less !")
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     pass
# """


# code2 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         return None
#     return 10 / age


# xfactor = calculate_xfactor(-1)

# if xfactor == None:
#     pass

# """
# print("First code=", timeit(code1, number=10000))
# print("Second code=", timeit(code2, number=10000))
#   --> This function returns the execution time of this piece of code after 10000 repetitions.


#   --> From the result, we can know that if you are building a simple application for a few users,
#   --> raising exceptions in your function is not going to have the bat impact on the performance of your application.
#   --> But if you are building an application where performance and scalability is important, then it is better to raise
#   --> exceptions when you really have to.
#   --> See if you can handle the situation with a simple if statement, whether there is a performance difference or not,
#   --> your code end up bing a little bit cleaner.


# Some practice:
# 求1 到 100 之间的所有偶数之和
# sum = 0
# for i in range(2, 101, 2):
#     sum += i
# print(sum)


# 求1 到 100 之间的所有奇数之和
# sum = 0
# for i in range(1, 101, 2):
#     sum += i
# print(sum)


# 求阶乘
# num = int(input("Please input a number: "))
# res = 1
# for i in range(1, num + 1):
#     res *= i
# print("%d的阶乘是: %d" %(num, res))
