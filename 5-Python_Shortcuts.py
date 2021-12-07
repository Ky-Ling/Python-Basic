'''
Date: 2021-08-03 18:35:09
LastEditors: GC
LastEditTime: 2021-10-19 20:57:56
FilePath: \Mosh Course 1\5-Python_Shortcuts.py
'''
# F strings:
# name = "John Fish"

# print(f"Hello {name}, 1 + 5, { name * 3}")


# Unpacking:
dic = {"a": 1, "b": 2}
# coords = [4, 5]
# a, b = dic.values()
# c, d = dic.items()
# x, y = coords
# print(a, b)
# print(c, d)
# print(x, y)


# Multiple Assignment(Swapping Variables:):
# width, height = 100, 300
# width, height = height, width
# print(width, height)


# Comprehensions:
#    --> A comprehension is a way to initialize or create some type of collection in Python in one line.
#    --> [expression for item in items]  --> Do this for loop and then applying this expression on each item.

# x = [0 for i in range(100)]
# y = [i for i in range(100) if i % 2 == 0]
# z = [i * j for i in range(100) if i % 2 == 0 for j in range(10)]

# print(x)
# print(y)
# print(z)


# sentence = "Hello, my name is John Fish"
# m = {char: sentence.count(sentence) for char in set(sentence)}
# print(m)


# Object Multiplication
# x = "Hello World" * 5
# y = [1, 3, 4] * 3
# z = (1, 3, 5) * 3
# m = [[1, 2, 4]] * 4
# print(x)
# print(y)
# print(z)
# print(m)


# Inline/Ternary Condition:
# if 2 > 3:
#     x = 1
# else:
#     x = 0


# x = 1 if 2 > 3 else 0
#    --> On the left hand side of the if statement and then what you want to happen, if this is not the case, after the else statement.

# print(x)


# Zip:
#    --> What the zip() will do is combine lists or collections together, so usually you can iterate through them at the same time.
# names = ["Tim", "John", "Mosh"]
# ages = [21, 22, 23]
# eyes_color = ["Blue", "Brown", "Green", "Red"]
# print(list(zip(names, ages, eyes_color)))
# print(list(zip(names, eyes_color)))

# for name, age, eyes_color in zip(names, ages, eyes_color):
#     if age > 22:
#         print(name)
#     print(age)
#     print(eyes_color)


# *args and **kwargs:


# for - else & while - else:
#    --> it allows us to determine if you broke out of a for loop or while loop without having to use a flag .
# search = [1, 2, 3, 4, 5, 6, 7]
# target = 7
# found = False

# for element in search:
#     if element == target:
#         print("I found it !")
#         found = True
#         break
# if not found:
#     print("I didn't find it ! ")


# search = [1, 2, 3, 4, 5, 6, 7]
# target = 8

# for element in search:
#     if element == target:
#         print("I found it !")
# else:
#     print("I didn't find it ! ")
# What the else statement will do? It will be triggered if we get through the entire for loop without breaking.


# search = [1, 2, 3, 4, 5, 6, 7]
# target = 8
# i = 0

# while i < len(search):
#     element = search[i]
#     if element == target:
#         print("I found it !")
#     i += 1
# else:
#     print("I didn't find it ! ")


# Sort by key:
# lst = [[-1, 1], [3, 2], [4, 2], [2, 5], [6, 7]]
# lst1 = [[-1, 1], [3, 2], [4, 2], [2, 5], [6, 7]]
# lst2 = [[-1, 1], [3, 2], [4, 2], [2, 5], [6, 7]]
# lst.sort()
# print(lst)
# #   --> It sorts it by the first element inside of the nested list,
# lst1.sort(key=lambda x: x[1])
# print(lst1)
# #   --> What you need to do after the "key=" is to pass a function that returns what it should sort by each element.
# #   --> In this example, after the function, it is going to sort by the second element.
# lst2.sort(key=lambda x: x[1] + x[0])
# print(lst2)


# Bonus - Itertools
#    --> This module allows you to do iteration related operations and can save a ton of time.
# import itertools
# lst = [1, 2, 3, 4, 5]
# sum_list = itertools.accumulate(lst)
# #    accumulate() is to accumulate the sums of the values in order or in sequence from this list.
# print(list(sum_list))


# lst1 = ["A", "B", "C", "D", "E"]
# chain_list = itertools.chain(lst, lst1)
# #    chain() is to combine the two lists that you have into one list without actually creating a new list, such that you can iterate through it.
# print(list(chain_list))
