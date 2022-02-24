'''
Date: 2021-03-13 15:11:10
LastEditors: GC
LastEditTime: 2022-02-24 15:37:52
FilePath: \Mosh Course 1\3-List.py
'''

# name[2:] --> 将会获取从索引值为2的元素开始一直到最后的所有内容
# name[2:4] -- > 从2开始一直到4（但并不会返回索引值为4所代表的值）
# name[:] --> 返回所有值（默认从0开始，一直到列表最后的元素 -> From the beginning to the end of the list
# name[::2] -->  return every second elements in the original list
# name[::-1] --> It will return all the items in the original list but in reverse order
# 修改列表元素：name[0] = "ohn"
# //
# name = ["John", "Mosh", "Bob", "Marry", "Lihua"]
# print(name)
# print(name[1])
# print(name[:])
# print(name[1:])
# print(name[2:])
# print(name[::2])
# print(name[::-1])

# Practice: Write a Python program to find the max number of a list
# //
# numbers = [1, 4, 90, 787, 9999]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(number)


# 2D lists
# 返回第一个元素中的第二个索引值所对应的元素，即结果为3
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 6, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)
# print(matrix[1])
# print(matrix[2])
# print(matrix[1:])

# for row in matrix:
# print(row[1])
# print(row[2])
# print(row[::-1])


# List Methods:
# numbers.append(a) --> 在列表末尾插入元素
# numbers.insert(a, b) --> a代表所需要插入元素的索引值， b代表插入元素的值
# numbers.remove(a) --> 删除某一值(如果有两个相同的元素，删除第一个。If you wanna remove all the items in this list, you have to look over the list and remove all the items individually)
# numbers.clear() --> 清除列表里面所有的值（此方法括号里面不写任何值）
# numbers.pop() --> 删除列表的最后一个元素（此方法括号里面不写任何值）
# numbers.pop(a) --> 删除指定元素(括号里为指定索引值) --> Pop method will remove only one item by index.
# del numbers[0:3] --> 删除一个范围内的元素          --> With del method we can remove a range of items.

# enumerate(numbers) -->
# print(numbers.index(a)) --> 判断列表里面是否存在元素a，最后结果返回索引值. If you try to get the index of an object that doesn't exist, we will get ValuesError.
# print(900 in numbers) --> 判断元素900是否存在于列表中,最后结果返回boolean值（即最后的结果不会产生错误提示，只会出现True 或者 False）
# print(numbers.count(6)) --> 计算一个元素出现的次数, It will return the number of occurrences of the given item in the list.

# numbers.sort() --> 对列表进行升序排序，没有返回值（None） Inscending order
# numbers.reverse() --> 对列表进行降序排序，没有返回值（None） Descending order
# numbers.sort(reverse=True) --> 降序排列

# sorted(numbers) --> This method will not modify the origin of list, it will return a new sort of list.
# sorted(numbers, reverse=True) --> 降序排列
# numbers2 = numbers.copy() --> numbers2 is a copy list of numbers(the original list)，
#                           -->这两个列表是独立的，对numbers列表的操作不会影响numbers2列表的元素值

# list(range(20))  --> 生成一个列表，索引值从1到19，共20位

# //
# numbers = [1 ,5, 6, 34, 6, 2, 6, 688]
# numbers.append(20)
# numbers.insert(1, 200)
# numbers1 = list(range(20))
# chars = list("Hello World")
# print(chars)
# print(numbers1)
# print(numbers)
# print(numbers.index(5))
# letters = ["a", "s", "f", "d", "gg"]
# for letter in enumerate(letters):
#     print(letter[0], letter[1])


# Sorting Example:
# items = [
#     ("Product1", 10),
#     ("Product2", 12),
#     ("Product3", 34),
#     ("Product4", 13)
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# #  I am not calling this function, I am simply passing a reference to this function.
# print(items)


# Another cleaner way(With Lamdab Function):
# items = [
#     ("Product1", 10),
#     ("Product3", 34),
#     ("Product2", 12)
# ]


# items.sort(key=lambda item: item[0])
# print(items)


# Map function:
# If we only interested in the price of these items, so we wanna transform this list into a list of numbers that is a list of price.

# items = [
#     ("Product1", 10),
#     ("Product2", 12),
#     ("Product3", 34)
# ]

# x = map(lambda item: item[1], items)
# for item in x:
#     print(item)


# Filter function:
# IF we wanna filter this list and only get the items with price greater than or equal to 10,
# items = [
#     ("Product1", 2),
#     ("Product2", 12),
#     ("Product3", 34)
# ]
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)


# List Comprehension:
#    --> [expression for item in items]  --> Do this for loop，and then applying this expression on each item.
# items = [
#     ("Product1", 2),
#     ("Product2", 12),
#     ("Product3", 34)
# ]

# prices = list(map(lambda item: item[1], items))

# # If we wanna get the price of each item, we can write an expression like this:
# price1 = [item[1] for item in items]

# filters = list(filter(lambda item: item[1] >= 10, items))
# filter1 = [item for item in items if item[1] >= 10]

# print(price1)
# print(filter1)


# Zip Function:
# list1 = [1, 3, 5]
# list2 = [23, 44, 57]
# print(list(zip(list1, list2)))
# print(list(zip("abc", list1, list2)))


# //

# Practice: Write a program to remove the duplicates in a list
# numbers = [1, 3, 4, 5, 5, 3, 4, 6, 7, 999]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)


# Tuples(Read-only list):
#       --> Like List, but We can't mutate or change it, such as insert, remove, clear and so on.
# 方括号定义列表，圆括号定义元组(tuple)
# 只有两种常用的方法：count and index ,但是还有其他 Advanced method. Don't need to master them as a beginner now.
#  --> Let's say if you are dealing with a sequence of objects, and you'd better make sure you don't accidentally
#      modify the sequence, you don't accidentally add a new object to it or remove an existing objects,
#      so instead of list you can use the tuple to prevent these accidental errors.

# number1 = (1, 3, 5, 6)
# print(number1[1])
# print(number1[1:3])


# point = (1, 2)
# point1 = 1, 2
# point2 = 1,
# # --> 必须加上“,”
# point3 = (1, 3) + (4, 7)
# point4 = (5, 7) * 6
# point5 = tuple([1, 3])
# point6 = tuple("Hello World")

# print(point)
# print(point1)
# print(type(point2))
# print(point3)
# print(point4)
# print(point5)
# print(point6)


# Swapping Variables:
# Swap values of two variables:
# x = 10
# y = 11

# z = x
# x = y
# y = z
# # x ,y = y, x
# #  --> same with: x ,y = (11, 10)
# a, b = 1, 3
# #   --> we find a tuple, and then unpacking it on the left hand.
# print("X: ", x)
# print("Y: ", y)
#
#


# Arrays(Take less memory and perform a little bit faster, we will see the difference only if we are dealing with a large list of numbers):
#    --> Use array only if you are dealing with large sequence of numbers, and you encounter performance problems.
#    --> In other cases, use list or tuple by default.

# from array import array
# numbers = array("i", [1, 3, 4])
# numbers.append(6)
# numbers.pop()
# print(numbers)

#  ---> Some methods are like list, but unlike list, objects in array are typed, so here every object should be an integer,
#       if you try to put a floating-point number here or any other kind of objects, you will get an error.


# Sets:
#    --> Which is basically a collection with no duplicates. Set is an unordered collection(无序集合) of unique items,
#    --> we can't have duplicate and these objects are on order, they are not in sequence.
#    --> And we can't access them using an index.

# numbers = [1, 1, 1, 3, 5, 6]
# unique = set(numbers)

# second = {1, 3, 4}
# second.add(5)
# second.remove(3)
# print(len(second))
# print(second)
# print(unique)


# numbers1 = [1, 2, 3, 4, 3, 3, 7]
# first = set(numbers1)
# # 1, 2, 3, 4, 7

# second = {1, 6, 5, 9}

# print(first | second)
# #   --> The result includes all the items that are either in the first set or the second set.

# print(first & second)
# #   --> It will return a new set that includes all the items are in both first and second sets.

# print(first - second)
# #   --> The first set has this additionally numbers that we don't have in the second set.

# print(first ^ second)
# #   --> Symmetric difference. This will return the items that are either in the first ser or second set but not the both.

# print(first[1])
# #   --> 'set' object is not subscriptable. 'set' object does not support indexting.
# #   --> So if you want to access items by an index you need to use the list.

# if 1 in first:
#     print("Yes!")
# #   --> We can check for the existence of an item in a set.


# Unpacking
# 当Python解释器看到此语句时，它将获得该元组的第一项，并把它分配给第一个变量x； 之后它将获得该元组的第二项，并把它分配给第二个变量；同样地，我们将获得该元组的第三项并把它分配给第三个变量z
#    --> So we are unpacking this tuple into 3 variables (这个方法对列表也适用)

# dic = {"a": 1, "b": 2}
# coords = [4, 5]
# a, b = dic.values()
# c, d = dic.items()
# x, y = coords
# print(a, b)
# print(c, d)
# print(x, y)


# Example one:
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#     ----> 这三行代码等价于 x, y, z = coordinates

# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)
# print(x + y + z)


# Example two:
# numberss = [1, 3, 4, 5, 2, 5, 5, 6, 8]
# first, second, *other = numberss  # --> We only get the first and second items, and everything else will be stored in a separate list whose name is "other":
# print(first)
# #   --> unpacking
# print(second)
# #   --> unpacking
# print(other)
# #   --> packing


# Example three:
# numberssss = [1, 2, 4, 33, 44, 56, 77, 88, 890]
# first, *other, last = numberssss
# print(first)
# print(last)
# print(other)


# Example four:
# letters = ["a", "s", "f", "d", "gg"]
# items = (0, "a")
# index, letter = items
# for index, letter in enumerate(letters):
#     print(index, letter)


# Unpacking Operators:
#     --> We can use the unpacking operators to take out individual values in any iterable.

# Example one:
# numbers = [1, 3, 4]
# print(*numbers)
# print(1, 3, 4)


# Example Two:
# values = list(range(5))
# values = [*range(5), *"Hello World"]
# print(values)


# Example Three:
# first = [1, 4, 5]
# second = [6, 7, 8]
# values = [*first, "about", *second, *"Hello World"]
# print(values)


# Example four:
# first = {"x": 12, "y": 455}
# second = {"x": 67, "y": 808}
# combined = {**first, **second, "z": 567}
# print(combined)
# #   --> If you have multiple items with the same key, the last value will be used


# Dictionaries:(Key-Value pairs, unordered, mutable)
#     We use dictionaries in situations where we want to store information that comes as key value pairs

# Example:
#     Name: John Fish
#     Email: John@gmail.com
#     Phone: 12345
#         ---> the key: Name, Email, Phone
#              the values: John Fish, John@gmail.com, 12345
#           Each key is associated with a value, so this is where we use a dictionary. With dictionary, we can store a bunch of key value pairs.
#           Each key should be unique in a dictionary
# //
# print(customer.get("hello", "error")) --> If it can not find the value of this first "", then it will return the value of the second "".

# customer["age"] = 123
# print(customer["age"]) ---> The way to update the value
# customer["birthday"] = "Jan 1 1990"
# print(customer["birthday"])   ---> 添加新的键值对
#

# customer = {
#     "name" : "John Fish",
#     "age" : 22,
#     "is_verified" : True
# }

# print(customer["name"])
# #    --> One way to get the value of "name"

# print(customer.get("name"))
# #    --> The other way to get the value of "name", if the key doesn't exist, by default it will return None.

# print(customer.get("hello", "error"))

# customer["age"] = 123
# print(customer["age"])

# customer["birthday"] = "Jan 1 1990"
# print(customer["birthday"])


# point = dict(x=1, y=3)
# print(point)
# print(point["x"])

# # update
# point["y"] = 10

# # Add a new key
# point["z"] = 34

# # Delete an item --> We can use some methods: del; pop(); popitem()
# del point["z"]

# print(point)

# # Loop over the dictionary
# for key in point:
#     print(key, point[key])

# # Another way to iterate the dictionary
# for key, value in point.items():
#     print(key, value)


# //
# Practice:
# phone = input("Phone: ")
# digits_mapping = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four",
#     "5" : "Five"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "") + " "
# print(output)


# A funny project --> Emoji Converter :)
# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)" : "😀",
#     ":(" : "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


# Dictionary Comprehensions:
#    --> [expression for item in items]

# values = []
# for x in range(5):
#     values.append(x * 2)
# # values = [x * 2 for x in range(5)]
# print(values)
#     # -- For list

# values = {x * 2 for x in range(5)}
# print(values)
# #   --> For set


# # {1, 3, 5, 6} --> Set
# # {1 : "a", 2 : "b", 3 : "c"} --> Dictionary
# values = {x : x * 2 for x in range(5)}
# print(values)
#     # --> For dictionary

# # All in all, we can use comprehensions with lists, sets, dictionaries. But we can't use it in tuple.



# Generators:
#    --> There are situations that might be working with a really large data set,
#    --> with these situations, it's more efficient to use a generator object, generate a new value in each iteration.

# values = (x * 3 for x in range(10))
# print(values)
# #    --> From the result we can see generator objects are iterable, we can iterate over them. In each iteration, they split out a new value.
# for x in values:
#     print(x)


# how to get the size of an object?
# from sys import getsizeof

# values = (x * 2 for x in range(1000))
# print("gen: ", getsizeof(values))

# values = [x * 2 for x in range(1000)]
# print("list: ", getsizeof(values))


# Functions
#     --> 定义完一个Function之后要空两行，为了代码规范(Whenever we defined a function, we need to add two lines to break after.)
#     --> 必须在定义functions之后才能调用它，如果在定义方法之前调用它，会出现错误
#     --> In programming we have two types of functions, 1- Perform a task(Which is printing something in the terminal); 2-Calculate and return a value.
# def greet_user():
#     print("Hello")
#     print("Welcome to my class")


# print("Start")
# greet_user()
# print("Finished")


# Parameters
#    --> We will learn how to pass your information to your functions
# //

# Parameters are the holes or placeholders that we define in our function for receiving information
# Arguments are the actual pieces of information that we supply to these functions, like positional arguments and key arguments

# def greet_user(name):
#     print(f"Hi {name}")
#     print("Welcome to my class")


# print("Let's start!")
# greet_user("John Fish")
# greet_user("Marry")
# print("It is finished!")


# Keyword Arguments
# --> In the last Python example of Parameters, we can learn that "John" is the Positional Arguments, "name" is the Parameters.
# --> The position of keyword Arguments is doesn't matter, and in order to improve the readability of the code, we always use the key arguments
# --> For the most of the part, please use the positional arguments, but if you are dealing with functions that take multiple numerical values,
#        see if you can improve the readability of your code by using keyword arguments
# --> These keyword arguments should always come after positional arguments. If you're mixing positional arguments and keyword arguments,
#        you should always use the positional arguments first and then the keyword arguments

# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome to my class")

# print("Let's start!")
# greet_user(last_name="Fish", first_name="John")
# greet_user("Mary", last_name="Bob")
# #    --> positional arguments(Mary) is the first, the key argument(last_name="Bob") is the second
# print("It is finished!")


# Return statement:

# def square(number):
#     return number * number


# result = square(3)
# print(result)
# print(square(5))


# Creating a Reusable Function
# //
# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#     ":)" : "😀",
#     ":(" : "😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# message = input(">")
# print(emoji_converter(message))


# *args
#    --> When we use the ‘*’. Python will get all these arbitrary arguments and unpack all of them into a list.

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#         # Result: 2 * 3 * 4 * 5 = 120
#     return total


# print(multiply(2, 3, 4, 5))


# **args
#    --> When we use ** in the function, we can pass multiple key-values pairs or multiple keyword arguments to the function,
#    --> and Python will automatically package them into a dictionary

# def save_user(**user):
#     print(user)
#     print(user["name"])
#     print(user["id"])


# save_user(id="1", name="John Fish", age="21")


# Exercise:
#    --> Please write a program to find the most repeated charactor in this text.
#    --> First we have to know how many times each charactor is repeated. Once we have that information, then we can find the most repeated charactor.
#    --> And we all know that a dictionary is a collection of key-value pairs, so here we can use the charactor as the keys and the repeation as the value
#    -->


# Normal Solution:
# sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# print(char_frequency)


# Another Solution:
# from pprint import pprint

# sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# print(char_frequency_sorted)
# print(char_frequency_sorted[0])
