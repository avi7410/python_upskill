# All Any
# Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
# Input : numbers = [1, 2, 3, 4, 5]
# #Expected Output : True
numbers = [1, 2, 3, 4, 5]
print(all(x > 0 for x in numbers))
# Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
# Input: numbers = [1, 3, 5, 7, 8]
# #Expected Output: True
numbers = [1, 3, 5, 7, 8]
print(any(x % 2 == 0 for x in numbers))
# Determine if any number in a list is divisible by 5 an print.
numbers = [1, 3, 5, 7, 8]
print(any(x % 5 == 0 for x in numbers))
print(next(x for x in numbers if x % 5 == 0))



#Class
#
# 1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
#
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

student = Person("avi", 21)
print(f"{student.name} - {student.age}")
# 2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name

    def deposit(self, credit):
        self.balance += credit
    def withdraw(self, debit):
        self.balance -= debit
    def check_balance(self):
        return self.balance
# 3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
#
#       book = Book.from_string("Python Programming, John Doe")
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    @classmethod
    def from_String(self, str):
        arr = str.split(", ")
        return self(arr[0], arr[1])
book = Book.from_String("Python Programming, John Doe")
print(f"{book.author} wrote {book.name}")
# 4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.
class Animal:
    def sound(self):
        return "some sound"
    def breathe(self):
        return "breathing"
class Dog(Animal):
    def sound(self):
        return "bark"
class Cat(Animal):
    def sound(self):
        return "meow"

a = Animal()
print(a.sound())
print(a.breathe())
d = Dog()
c = Cat()
print(d.sound())
print(d.breathe())
print(c.sound())
print(c.breathe())

# 5. Write a code to perform multiple inheritance.
#
class A:
    def write(self):
        print("a")
class B:
    def write(self):
        print("b")
class C(B,A):
    pass

c = C()
c.write()

#Decorator
# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time.
# Calculate the total time taken and print.
import time

from week_2.lamda_map_filter_reduce import result


def time_calculator(func):
    def wrapper(* args, ** kwargs):
        start = time.time()
        result = func(* args, ** kwargs)
        end = time.time()
        print(f"time taken : {end-start}")
        return result
    return wrapper
@time_calculator
def appender(x):
    ls = []
    ans = 0
    for i in range (x):
        ans += i
    return ans

print(appender(1000))
# 2. Create a parameterised decorator retry that retries a function a specified number of times.
#
def retry(x):
    def decorator(func):
        def wrapper(* args, ** kwargs):
            for i in range (x):
                func(*args, **kwargs)
        return wrapper
    return decorator

@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("Avi")
#
# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
#
def validate_positive(func):
    def wrapper(*args, **kwargs):
        result = 0;
        for x in list(args):
            if(x < 0):
                print("negative argument passed")
            else:
                result = func(*args,**kwargs)
        return result
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(1))
print(square_root(-1))

# 4. Create a decorator cache that caches the result of a function based on its arguments.
# Write a cache decorator for it to check if the calculation is already performed then return the result.

d = {}
def cache(func):
    def wrapper(* args, **kwargs):
        k = args[0]
        if k in d:
            return d[k]
        result = func(*args, **kwargs)
        d[k] = result
        return result
    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

print(expensive_computation(5))
print(expensive_computation(5))

# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.
#
def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            func(user, *args, **kwargs)
        else:
            print("Admin permission needed!!!")
    return wrapper

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}
delete_user(user1, user2)
delete_user(user3, user2)


#Enumerate
# Using below list and enumerate(), print index followed by value.
#
# Input: fruits = ["apple", "banana", "cherry"]
# Output:
# 0 apple
# 1 banana
# 2 cherry
fruits = ["apple", "banana", "cherry"]
for i, a in enumerate(fruits):
    print(f"{i} {a}")
# Using below dict and enumerate, print key followed by value
#
# Input: person = {"name": "Alice", "age": 30, "city": "New York"}
#
# Output:
# name: Alice
# age: 30
# city: New York

person = {"name": "Alice", "age": 30, "city": "New York"}
for k, v in person.items():
    print(f"{k}: {v}")
# Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit, but only for even indices.
#
#   Output:
#              [(2, 'banana'), (4, 'date')]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
ls = []
for i, x in enumerate(fruits):
    if i % 2 == 0:
        ls.append((i, x))
print(ls)


#Exception Handling
# Write a Python program that attempts to divide two numbers a = 10  b = 0
# and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error
#
a = 10
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("zero division error!!!")
else:
    print(c)
# Apply exception handling to below code and handle an exception if the index is out of range.

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("index out of bound")


# Correct this below code with appropriate exception handlings. And finally print “Execution completed”
def safe_divide(a,b):
      try:
          result = a / b
          print(f"Result: {result}")
      except ZeroDivisionError:
          print("Division by zero !!")
      except Exception:
          print("Invalid division")
      finally:
          print("Execution Completed")

safe_divide(1,0)
safe_divide(1,'a')


#File Handling
# 1 . Write a Python program to read the entire content of a file named sample.txt and display it.
# from os.path import split
#
# with open("/home/avi-vyas/Desktop/sample.txt") as f:
#     print(f.read())
import csv

# 2. Write a Python program to count the number of words in a file named words.txt
with open("/home/avi-vyas/Desktop/words.txt") as f:
    print(len(f.read().split()))
# 3.Create a program to write the string “Hello, Python!” into a file named output.txt.
with open("/home/avi-vyas/Desktop/output.txt", mode='w') as f:
    f.write("Hello, Python!")
# 4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries
#
data = [
["Name", "Roll Number", "Marks"],
["Alice", "101", "85"],
["Bob", "102", "90"],
["Charlie", "103", "88"]
]
with open("/home/avi-vyas/Desktop/students.csv", mode='w') as f:
    writer = csv.writer(f, delimiter=',')
    for row in data:
        writer.writerow(row)

# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.
#
def reader(path):
    with open(path) as f:
        for line in f:
            yield line

for i in reader("/home/avi-vyas/Desktop/words.txt"):
    print(i, end="")


#Generator
# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
# Of 10  numbers
#
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
#

def fibonacci_numbers():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

gen = fibonacci_numbers()
for i in range(10):
    print(next(gen))
# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.
#
#   Input n=3
#
# Output:
# 3
# 6
# 9
# 12
# 15
# …
def infinite_multiples(n):
    x = 1
    while True:
        yield n * x
        x += 1

gen = infinite_multiples(3)
for i in range(10):
    print(next(gen))
# 3. Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.
#
# word = “hello”
# times = 5
#
def repeat_word(word, times):
    for i in range(times):
        yield word

gen  = repeat_word("hello", 5)
for i in range(10):
    print(next(gen))

#Lamda Map Filter Reduce
# Given a list let's see how to double each element of the given list. Using map()
# a = [1, 2, 3, 4]
# #Expected Output: [2, 4, 6, 8]
from functools import reduce

a = [1, 2, 3, 4]
b = list((map(lambda x: x * 2, a)))
print(b)
# Use filter() and lambda to extract all even numbers from a list of integers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #Expected Output: [2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x : x%2 == 0, numbers))
print(result)
#
# Use reduce() and lambda to find the longest word in a list of strings.
# from functools import reduce
# words = ["apple", "banana", "cherry", "date"]
# #Expected Output: 'banana'
words = ["apple", "banana", "cherry", "date"]
longest = reduce(lambda a, b: a if len(a) >= len(b) else b, words)
print(longest)
# Use map() to square each number in the list and round the result to one decimal place.
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# #Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]
#
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
output = map(lambda x : round(x**2, 1), my_floats)
print(list(output))
# Use filter() to select names with 7 or fewer characters from the list.
# 	#Expected Output: ['olumide', 'josiah', 'omoseun']
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print(list(filter(lambda x : len(x) <= 7, my_names)))
# Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]
#
ls = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, ls))


##Max_Min

# Find the Maximum and Minimum Values in a List
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print(max(numbers))
print(min(numbers))
# Given a set of numbers, find the maximum and minimum values.
setn = {5, 10, 3, 15, 2, 20}
print(max(setn))
print(min(setn))
# Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order.
# If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.
#
# Input: words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
# Output: ('kiwi', 'grapefruit')
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
print((min(words, key=len), max(words, key=len)))


#OS Sys Datetime

import os
from datetime import datetime, timedelta, date
from time import process_time_ns

# Using datetime, add a week and 12 hours to a date.
# Given date: March 22, 2020, at 10:00 AM. print original date time and new date time
dt = datetime(2020, 3, 22)
print(dt)
dt += timedelta(days=7, hours=12)
print(dt)
# Code to get the dates of yesterday, today, and tomorrow.
print(date.today())
print(date.today()-timedelta(days=1))
print(date.today()+timedelta(days=1))

# Write a code snippet using os module, to get the current working directory and
# print and create a folder “test”. List all the files and folders in the current working directory
# and remove the directory “test” that was created.
cwd = os.getcwd()
print(cwd)
os.makedirs(cwd+"/test")
print(os.listdir())
os.rmdir(cwd+"/test")
print(os.listdir())
# Write a Python program to rename a file from old_name.txt to new_name.txt.
# os.rename("/home/avi-vyas/Desktop/old_name.txt", "/home/avi-vyas/Desktop/new_name.txt")


# Create a file and Write a Python program to get the size of a file named example.txt
with open("/home/avi-vyas/Desktop/example.txt", "w") as f:
    pass
stats = os.stat("/home/avi-vyas/Desktop/example.txt")
print(stats.st_size)
# Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
# O/P: 2020-02-25 16:20:00
str = "Feb 25 2020 4:20PM"
print(datetime.strptime(str,"%b %d %Y %I:%M%p"))

# Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18
str = "2025-02-25"
dt = datetime.strptime(str, "%Y-%M-%d").date()
dt -= timedelta(days=7)
print(dt)
# Format the date 2020-02-25 as "Tuesday 25 February 2020"
#
str = "2020-02-25"
dt = datetime.strptime(str, "%Y-%M-%d").date()
print(dt.strftime("%A %d %B %Y"))
