'''
Date: 2021-03-08 14:20:19
LastEditors: GC
LastEditTime: 2022-01-07 20:45:18
FilePath: \Mosh Course 1\1-Basics_and_String.py
'''

# name = 'John Smith'
# age = 20
# is_new_patient = True
# print(age)
# print(name)
# print(is_new_patient)

# name = input('What is your name? ')
# print('Hi ' + name)


# name01 = input('What's your name? ')
# colour = input('What's your favorite colour? ')
# print(name01 + ' likes ' + colour)


# birth_year = input('Birth_year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year)
# print(type(age))
# print(age)


# weight_lbs = input('Weight_lbs: ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)


# course01 = "Python course for beginners"
# course02 = 'Python for "beginners"'
# course03 = '''
# Hi John,
# Here is the first email to you,
# Thank you very much,
# The support team
# '''
# print(course01)
# print(course02)
# print(course03)





# 0 是第一个字符
# -1 是最后一个字符
# 0:3 表示从第一位字符一直到后面两位，共三位,不包含第三个
# 0: 表示Python会将所有字符返回到字符串的末尾
# 1: 表示Python会将所有字符从第二位开始(索引值为1)一直返回到字符串的末尾
# :5 表示Python会默认从零到后面第五个, it's like 0:5
# : 表示Python will copy or clone the strings
# course01 = "Python for beginners"
# another = course01[:]
# print(course01[2])
# print(course01[-1])
# print(course01[0:3])
# print(course01[0:])
# print(course01[1:])
# print(course01[:5])
# print(course01[:])
# print(another)





# Formatted Strings
# //
# first = "John"
# last = "Fish"
# message = first + " [" + last + "] " + "is a coder"
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)




# String Methods
# //
# len() 计算字符串中的字符数目
# find() 寻找某个字符, 返回索引(此方法需要区分大小写),如果无法找到，将会返回-1
# course.find("Beginners") 将会返回11， 因为这一串字符从索引为11出开始
# replace() 替换方法 (此方法同样区分大小写)
# in 检查一个字符或者一个字符串是否存在, 产生一个boolean值，即返回boolean值
# not in
# title() 将语句的首字母大写
# strip() these white spaces will be remote,
#         that is to say, the strip() method will remove all the white spaces from both the beginning and end of the string
# rstrip()
# lstrip()

# course0 = "python for beginners"
# print(course0.title())
# course00 = "   Python for beginners"
# print(course00.strip())
# course = "Python for Beginners"
# print(len(course))
# print(course.upper())
# print(course.find("y"))
# print(course.find("o"))
# print(course.find("Beginners"))
# print(course.replace("Beginners", "Absolute Beginners"))
# print(course.replace("P", "J"))
# print("Python" in course)
# print("Hello World" in course)


# Escape Sequences
# \'
# \"
# \n
# \\

# course1 = "Python \"Programming"
# course2 = "Python \'Programming"
# course3 = "Python \\Programming"
# course4 = "Python \nProgramming"

# print(course1)
# print(course2)
# print(course3)
# print(course4)





# Learn how to debug our program:
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start !")       
#     # --> press F5(Start the program in debug mode, we have to press f5), and press F10, F11, then press F10 all the time to debug
#     # --> If you will step into a function and you know that function works properly, you can immediately step out of the function with Shift+F11

# print(multiply(1, 2, 3))





# Some useful shortcuts with VScode in Windows:
# 1:从每一列代码的首部直接移到尾部：Fn + End键
# 2:从每一列代码的尾部直接移到首部：Fn + Home键
# 3:将一整行代码移动：先选中， Alt + 上键或下键
# 4:直接复制整行代码：先选中， Shift + Alt + 上键或下键
# 5:更改某个单词：F2





# Practice:
# def fizz_buzz(input):
#     # Not a clean code:
#     # if input % 3 == 0:
#     #     result = "Fizz"
#     # else:
#     #     result = "Buzz"
#     # return result
    
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
    
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input
# print(fizz_buzz(3))
# print(fizz_buzz(5))
# print(fizz_buzz(15))
# print(fizz_buzz(7))