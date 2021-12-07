'''
Date: 2021-08-17 21:39:10
LastEditors: GC
LastEditTime: 2021-10-19 20:40:37
FilePath: \Mosh Course 1\4-Generators.py
'''
# Generator VS Iterator:
#   --> Iterator is an object that enables a programmer to traverse a containter, particularly lists. It allows you to to loop
#       thought a sequence of numbers or some sequence of data, some sequence of something without having to store all of the
#       different items in that sequence in memory.
#
#   --> Generator is a routine that can be used to control the iteration behavior of a loop. A generator is really similar to
#       a function that returns an array. It allows you to create an iterator without having to go thought kind of a more tedious
#       and less elegant process.

# Example one:
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = map(lambda i: i ** 2, x)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# # This function gives us the next value in the iteration through an iterator.

# print("For loop starts !")
# for i in y:
#     print(i)


# Example two:
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = map(lambda i: i ** 2, x)

# for i in y:
#     print(i)

# while True:
#     try:
#         value = next(y)
#         print(value)
#     except StopIteration:
#         print("Done")
#         break

# From the result, we can know that the for loop and while loop are doing the same thing.


# Creating legacy iterators:
# import sys
# class Iter:
#     def __init__(self, n) -> None:
#         self.n = n


#     def __iter__(self):
#         self.current = -1
#         return self

#     def __next__(self):
#         self.current += 1
#         if self.current >= self.n:
#             raise StopIteration

#         return self.current

# x = Iter(5)
# for i in x:
#     print(i)


# Creating Generators:
import sys
def gen(n):
    for i in range(n):
        yield i
# As soon as i get the through the first iteration of this for loop(i == 0), so i yield zero, what that means that i immediately
# pause and stop all the information about this function is saved, so it is stored in the memory. And then i go to the second
# for loop and i print whatever the value is that I yield it, then what happens is the function or this for loop continues, so
# we go to the next value and call the next on the genetator that then has the for loop runs again, so that we get the value one,
# then we call next again, we get the value two and so on and so forth,

for i in gen(5):
    print(i)

# The way that generator works is when the yield keyword is hit, it pauses the execution of the function (it is not terminated,
# and then we return to it and continue running whenever we see the next keyword again or whenever we call the next method,
# or function on this generator) and returns this value(i) to whatever is iterating through this generator object(gen()).
# So in this case, for i in gen(5), So i am looping through my generator here, passing the value five to it, and inside my generator,
# we created a for loop, and in this for loop, i am looping up to five or up to end.
