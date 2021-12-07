'''
Date: 2021-03-08 18:47:58
LastEditors: GC
LastEditTime: 2021-10-17 21:09:57
FilePath: \Mosh Course 1\Arithmetic_operations.py
'''

# +, -, *, /(除), //(取整), %(返回除法的其余部分), **(幂)
# 优先级：括号 > 幂 > 乘，除 > 加，减
# Math Functions: -->Go to Google to search "Python 3 math module"
#   1. 四舍五入：round()
#   2. abs: 绝对值的缩写，最终结果都为正值
#   3. import math: 导入数学模块
# import math
# x = 2.9
# print(round(x))
# print(abs(-3.3))
# print(math.ceil(4.8)) //值的上限


# Type conversion:
# type() --> It will pass an argument as an argument and returns its type
# int()
# float()
# bool()
# str()


# Falsy Values:
# ""
# 0
# None
#    --> whenever we use these three values in a boolean context, we will get False, anything else will be true
# For Example:
# bool(0) --> False
# bool(1) --> True
# bool("") --> False
# bool("False") --> True
# bool(None) -- False


# Practice1:
# //
# is_hot = True
# is_cold = False
# if is_hot:
#     print("It's a hot day!")
#     print("Drink plenty water!")
# elif is_cold:
#     print("It's a cold day!")
#     print("Wear more warm clothes!")
# else:
#     print("It's a lovely day(not hot and cold)!")
# print("Hope you can enjoy your day!")


# Practice2:
# //
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down_payment: {down_payment}")


# Logical Operator:
# "and", "or" 和 "not"的用法:
# and: both the conditions are true
# or: at least one condition is true
# not: reverse the boolean condition
# //
# has_high_income = True
# has_good_credit = True
# has_criminal_record = False
# if has_good_credit and has_high_income:
#     print("You are eligible for loan!")
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan!")


# Comparison operations
# >, < , >=, <=, ==, !=

# print(10 == "10")  --> Why we get false? Because these values have different types, and they are stored differently in the computer's memory.
# //
# temperature = 30
# if temperature > 30:
#     print("It's a hot day!")
# elif temperature < 10:
#     print("It's a cold day!")
# else:
#     print("It's neither hot or cold!")
#


# //
# name = "Jo"
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("Your name is so good!")


# Project Practice:
# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos!")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds!")


# While loops:
# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done!!!")


# Project 1: Guessing game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("Congratulations! you won!!!")
#         break
# else:
#     print("Sorry, you failed, please try again!!!")


# Project 2: Car game
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("The car is already started...")
#         else:
#             started = True
#             print("To start the car...")
#     elif command == "stop":
#         if not started:
#             print("The car is already stopped...")
#         else:
#             started = False
#             print("To stop the car...")
#     elif command == "help":
#         print("""
# start - to start the car...
# stop - to stop the car...
# quit - to quit...
#             """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I can't understand what are you talking about....")


# for loops
# //
# for item in "Python":
#     print(item)
# //
# for item in ["Python", "courses", "for", "beginners"]:
#     print(item)
# //
# range(10), range(5, 10), range(5, 10, 2) --> 2 代表从第一位数字开始往后面走两步(go to two steps forward)

# for item in range(5, 10, 2):
#     print(item)
# //
# prices = [10, 49, 89, 900]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# Nested loops(嵌套循环)
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# Practice:
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += 'x'
#     print(output)


# Ternary Operator:
# age = 22
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# Cleaner Code:
# age = 22
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)


# Chaining Comparision Operator:
# age = 22
# if age >= 18 and age < 65:
#     # if 18 <= age < 65:
#     print("Eligible")
