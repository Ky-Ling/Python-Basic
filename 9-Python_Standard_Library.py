'''
Date: 2021-08-20 13:46:58
LastEditors: GC
LastEditTime: 2021-10-21 22:24:24
FilePath: \Mosh Course 1\9-Python_Standard_Library.py
'''
# Paths:
#   --> It is the fundation to work with files and directories.

# from pathlib import Path

# # Various ways to create a Path object
# Path(r"C:\Program Files\Microsoft")
# #  Create an absolute path in Windows
# Path("/user/local/bin")
# #  Create an absolute path in Mac and Linux
# Path()
# #  Create a Path object that represents the current folder.
# Path("ecommerce/__init__py")
# #  Use a related Path
# Path() / Path("ecommerce")
# #  We can also combine Path objects together
# Path() / "ecommmerce" / "__init__.py"
# #  Combine Path objects together with a String
# Path.home()
# #  Get the home directory of the current user


# from pathlib import Path
# path = Path("ecommerce/__init__.py")
# # Now we have created a path object, and this object has quite a few useful methods:
# path.exists()
# # See if this file or directory exists or not
# path.is_file()
# path.is_dir()
# # To check to see if this path represents a file or directory

# # Extract individual components in this path which is extremely useful:
# print(path.name)
# # This code returns only the file name of this path.
# print(path.stem)
# # It returns the filename with this extension.
# print(path.suffix)
# # To get the extension of this filename.
# print(path.parent)
# # It returns the parent of this path

# path = path.with_name("file.txt")
# print(path)
# # To create a new path object based on this existing path but only change the name and extension of the file
# print(path.absolute())
# # To get the absolute value of this path
# path = path.with_suffix(".txt")
# print(path)
# # To change this extension of a file


# Working with Directories:
# from pathlib import Path
# path = Path("ecommerce")
# path.exists()
# # It returns boolean
# path.mkdir()
# # To create the directory
# path.rmdir()
# # To remove the directory
# path.rename("ecommerce2")
# # To rename to a new name

# print(path.iterdir())
# # We can get the list of files and directories in this path, and run this code, we will get a generator object(A generator object
# # as the name implies returns a new value every time we iterate. So when we are working with a large list of items, instead of
# # storing all of these items in the memory, we use a generator object, we iterate it and get a new value every time is more efficient)
# for p in path.iterdir():
#     print(p)


# paths = [p for p in path.iterdir() if p.is_dir()]
# print(path)
# # If we are working with the directory that does not have a million files in it, we can convert a generator to a list using
# # a list comprehension expression.


# all_files = [p for p in path.glob("*.*")]
# print(all)
# # To search for all files
# py_files = [p for p in path.glob("*.py")]
# print(py_files)
# # To search for all .py files
# py_files0 = [p for p in path.rglob("*.py")]
# print(py_files0)
# # In order to search recursively.


# Working with Files:
# from pathlib import Path
# path = Path("ecommerce/__init__.py")
# # Here we have a path object that references a file
# path.is_file
# # We can check to see if this file exists
# path.rename("rename.txt")
# # Rename this file
# path.unlink()
# # Remove this file or link
# path.stat()
# # It returns information about this file

# # Reading data from the file:
# path.read_bytes()
# path.read_text()
# # Returns the content of the file as a string
# path.write_bytes()
# path.write_text("....")


# # How to copy a file?
# import shutil
# source = Path("ecommerce/__init__.py")
# target = Path() / "__init.py"
# # target.write_text(source.read_text())
# shutil.copy(source, target)


# Working with Zip Files:
# from pathlib import Path
# from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
# # Create this file in the current folder
#     for path in Path("ecommerce").rglod("*.*"):
#         zip.write(path)
# #Get all the files and this ecommerce directory and write them for this zip file.
# # Run this program, we will get the files.zip in our catalogue.


# from pathlib import Path
# from zipfile import ZipFile

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     # It returns the list of all the files in this zip file.
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")


# Working with CSV files:
#  --> CSV stands for comma separated values
# import csv
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 51])
#     # It will pass an array of values


# How to read a csv file?
# import csv
# with open("data.csv") as file:
#     reader = csv.reader(file)
#     print(list(reader))

#     for row in reader:
#         print(row)
# Run this two lines, we will get nothing. Why?
# This reader object has an index pr a position that is initially set to the beginning of the file. When we converted this
# reader to a list, that position goes to the end of the file, so when we iterated this row, we are already at the end of the file.
# So we have to comment this line of code(print(list(reader)))


# Working with JSON Files:
#  --> JSON stands for JavaScript object notation
# import json
# movies = [
#     { "id" : 1, "title" : "Terminator", "year" : 1989 },
#     { "id" : 2, "title" : "Kindergarten Cop" , "year" : 1999}
# ]
# data = json.dumps(movies)
# print(data)
# # It will get a string includes all movies data formatted as JSON


# How to write data to JSON files:
# import json
# from pathlib import Path
# movies = [
#     { "id" : 1, "title" : "Terminator", "year" : 1989 },
#     { "id" : 2, "title" : "Kindergarten Cop" , "year" : 1999}
# ]
# data = json.dumps(movies)
# Path("movies.json").write_text(data)
# # Run this program and we will get the "movies.json" in our catalogue.


# How to read data from other files?
# import json
# from pathlib import Path
# data = Path("movies.json").read_text()
# # Now this data is a string includes data formatted as JSON, so next we will pass this string into an array of objects/
# movies = json.loads(data)
# # It will return an array of dictionaries.
# print(movies)
# print(movies[0])
# print(movies[0]["title"])
# print(movies[0]["year"])
# print(movies[1])


# Working with a SQLite Database:
#  --> SQLite is a very lightweight database that we use for storing data of an application, it is often the technology of choice
#      for small applications like the apps that they run on phones or tablets. So it allows us easily to store data in structure
#      format that the table of rows and columns

# Read all the movies from the JSON movies and store them in our SQLite database.
# import sqlite3
# import json
# from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()
# At this point, all these changes will be written to the database. We only need this commit() when we are writing data to a database.

# But when we run this program, we will get an error(OperationalError: no such table: movies), Because we are dealing with
# an empty database, this database does not have any tables, so we need to create the movies table first(Go to search
# DB Browser for SQLite and finish the rest of operations......).


# How to read data from the database?
# import sqlite3
# import json
# from pathlib import Path

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM movies"
#     cursor = conn.execute(command)
#     # The cursor is an iterable object
#     for row in cursor:
#         print(row)
#     # movies = cursor.fetchall()
#     # print(movies)
#     # # It will return all the rows in this table.


# Working with Timestamps:
# import time
# # print(time.time())
# # # It returns the date time as a timestamp.

# def send_emails():
#     for i in range(10000):
#         pass

# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)
# # Calculate the execution time of some piece of code.


# Working with Datetimes:

# The ways to create datetime objects:
# from datetime import datetime
# dt = datetime(2021, 1, 1)

# from datetime import datetime


# dt = datetime.now()
# dt = datetime.strptime("2021/01/01", "%Y/%m/%d")
# Convert a string into a datetime object

# import datetime
# dt = datetime.datetime(2021, 1, 1)


# Convert a timestamp into a datetime object.
# from datetime import datetime
# import time

# dt = datetime.fromtimestamp(time.time())
# print(dt)
# print(f"{dt.year}/{dt.month}/{dt.day}")
# print(dt.strftime("%Y/%m/%d"))
# # Convert a datetime object into a string

# # We can also compare datetime objects:
# dt1 = datetime(2018, 1, 1)
# dt2 = datetime.now()
# print(dt1 > dt2)


# Working with Time Deltas:
# from datetime import datetime, timedelta

# dt1 = datetime(2018, 1, 1)
# dt2 = datetime.now()

# duration = dt2 - dt1
# print(duration)
# # When we subtract these two dates, we get a timedelta object.

# print("days", duration.days)
# print("seconds", duration.seconds)
# print("total_seconds", duration.total_seconds())
# #  Why do not we have year or month here? Because we can have a varying amount of time in a month or a year. That is why we
# #  only have days, seconds and total_seconds.


# We can add a timedelta object to a datetime object:
# from datetime import datetime, timedelta

# dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=10000)
# print(dt1)


# Generating Random Values:
# import random
# import string
# print(random.random())
# print(random.randint(1, 100))
# # To generate a random integer between two numbers.
# print(random.choice([1, 4, 2, 5, 6]))
# # It takes an array and randomly picks one of the items in this array.
# print(random.choices([1, 4, 2, 5, 6], k=3))
# # It selects multiple values from this array.
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))
# # print("".join(random.choices("asfgehtrrbasgehynhgds", k=4)))
# # To generate a random password.

# print(string.ascii_letters)
# # It returns a string that includes all the lowercase and uppercase letters.
# print(string.digits)


# import random
# numbers = [1, 4, 5, 7, 4, 89, 3456]
# random.shuffle(numbers)
# print(numbers)


# Opening the Browser:
# import webbrowser
# print("Deployment complicated")
# webbrowser.open("http://baidu.com")
# # Run this program, and a browser window is opened.


# Sending Emails:
#  ---> This is particularly useful if you have a database of customers, and you wanna send them various emails based on their interests.
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# import smtplib
# # Basically we have email package in Python Standard Library, and in this package we have a subpackage called mime(mime stands for
# # multi-purpose internet mail extensions), and this is a standard that defines the format for email messages.
# # With this MIMEMultipart object, we can send an email message that includes both HTML and plain text content.
# # So when the email client receiver received this email message, if it supports HTML, it will render HTML content,
# # otherwise it will render plain text content.

# # Set the header:
# message = MIMEMultipart()
# message["from"] = "Mosh"
# message["to"] = "testuser@codewithmosh.com"
# message["subject"] = "This is a test."

# # Set the body:
# message.attach(MIMEText("body"))
# # We have to pass payload, this payload can be text, image and other types supported by the mime protecol
# message.attach(MIMEImage(Path("gc.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.elhi()
#     # The communication between a client and SMTP Server should start with the hello message.
#     smtp.starttls()
#     # It puts the SMTP connection in TLS mode. TLS stands for transport layer security. With this all the commands we sent to
#     # the SMTP Server will be encrypted.

#     smtp.login("testuser@codewithmosh.com", "todayskyisblue1234")
#     smtp.send_message(message)
#     print("Sent ......")


# Working with Templates:
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from os import name
# from pathlib import Path
# from string import Template
# import smtplib

# template = Template(Path("template.html").read_text())


# message = MIMEMultipart()
# message["from"] = "Mosh"
# message["to"] = "testuser@codewithmosh.com"
# message["subject"] = "This is a test."

# body = template.substitute({"name" : "John"})
# # We can pass a dictionary that contains key value pairs for parameters in our template or we can pass keyword arguments.
# # body = template.substitute(name="John")
# message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("gc.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.elhi()
#     smtp.starttls()
#     smtp.login("testuser@codewithmosh.com", "todayskyisblue1234")
#     smtp.send_message(message)
#     print("Sent ......")


# Command-line Arguments:
# import sys
# if len(sys.argv) == 1:
#     print("USEAGE: python 3 app.py <password>")

# else:
#     password = sys.argv[1]
#     print("Password", password)


# Running External Programs:
#  --> How to run any of the operating system commands as well as external programs?
# import subprocess
# # With this module we can spawn a child process, a process is basically an instance of a running program. SO with this module
# # we can run other programs.
# complicated = subprocess.run(["ls", "-l"])
# # -l gives us a detailed view of the files and directories in the current directory.
# print("args", complicated.args)
# print("returncode", complicated.returncode)
# print("stderr", complicated.stderr)
