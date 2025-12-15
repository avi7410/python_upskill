#Control Flow

# For loop
# Write a program that takes the input from the user and checks if a number is even or odd.
num = int(input("enter a number to check for odd/even : "))
ans = "even" if num % 2 == 0 else "odd"
print(ans)
# Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”
a = 'civic'
b = 'hello'
print(reversed(a) == b)
# Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
def fibonacci_sequence(n, a = 0, b = 1):
   if n <= 0:
       return;
   print(f"{a}, ")
   fibonacci_sequence(n-1, b, a+b)

n = int(input("Please enter a number to generate Fibonacci sequence : "))
fibonacci_sequence(n)
# From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.	#Expected output : [4, 5]
list = [1,2,3,4,5]
target = 9
for i in range (0, len(list)):
    for j in range(i+1, len(list)):
        if list[i] + list[j] == target:
            print(f"[{list[i]}, {list[j]}]")

# While loop
# Print all even numbers between 1 and 20 using a while loop.
limit = 20
num = 1
while num <= limit:
    if num % 2 == 0:
        print(f"{num}, ", end="")
    num += 1

# Break
# Find the first occurrence of a number in a list and stop further searching.
# numbers = [10, 20, 30, 40, 50]
# search_for = 30
numbers = [10, 20, 30, 40, 50]
search_for = 30
for num in numbers:
    if(num == search_for):
        print(f"\nfound : {num}")
        break
# Continue
# Using continue statement, print only the odd numbers from 1 to 10.
for i in range (1, 11):
    if(i % 2 == 0):
        continue
    else:
        print(i, end=', ')
# Pass
# What will be the output
# for i in range(5):
#     if i == 3:
#         pass
#     print(i)
"""
EXPECTED OUTPUT : 
0
1
2
3
4
"""
# Match
# Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.
day = input("\nenter a day to check : ")
day.lower()
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("weekday")
    case "saturday" | "sunday":
        print("weekend")
    case _:
        print("invalid entry")
#


# Data Structures
# Given a list of numbers, find and print the maximum and minimum values.
#               nums = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5]
print(max(nums))
print(min(nums))

# Given two lists below, merge the values from both lists to one and print
#              a = [1,2,3,4]      b = [5,6,7,8]
a = [1,2,3,4]
b = [5,6,7,8]
a.extend(b)
print(a)
# 3. From a list, print the number of times the value 3 appears in the list:
# 		a = [1,3,4,5,2,1,3,9,3]
a = [1,3,4,5,2,1,3,9,3]
print(a.count(3))
# 4. From below list, Sort the list and print
# 		a = [1,3,4,5,2,1,3,9,3]
a = [1,3,4,5,2,1,3,9,3]
a.sort()
print(a)
# 5. Given a set, add the element 6 to it and print the updated set.
#                numbers = {1, 2, 3, 4, 5}
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)
# 6. Given a set, remove the element 3 from it and print the updated set.
# 		numbers = {1, 2, 3, 4, 5}
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)
# 7. Given two sets, find and print their intersection.
# 		set1 = {1, 2, 3}    set2 = {3, 4, 5}
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)
# 8. Given a tuple, count and print the number of occurrences of the element 'apple'.
# 		fruits = ('apple', 'banana', 'apple', 'cherry')
fruits = ('apple', 'banana', 'apple', 'cherry')
print(fruits.count('apple'))
# 9. Given two tuples, concatenate them and print the result.
# 		tuple1 = (1, 2, 3)     tuple2 = (4, 5, 6)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)
tuple3 = *tuple1, *tuple2
print(tuple3)
# 10. Access and print the value associated with the key "age" from the dictionary.
# 		person = {"name": "Alice", "age": 30, "city": "New York"}
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person['age'])
# 11. Add new key,  gender to dictionary and assign “M” to it and print
# person = {"name": "Alice", "age": 30, "city": "New York"}
person = {"name": "Alice", "age": 30, "city": "New York"}
person['gender'] = 'M'
print(person)
# 12. Remove the key "city" from the above Dict and print
del person['city']
print(person)
# 13. Given two dictionaries, merge them into one
# dict1 = {"a": 1, "b": 2}    dict2 = {"c": 3, "d": 4}
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)


#Data Types
# Objective: Convert between different data types.
# Task: Convert the following values to the specified types and print the results
# Convert 3.75 to an integer and print the value
val = 3.75
print(int(val))
#
# Convert "123" to a float and print the value
val = 123
print(float(val))
#
# Convert 0 to a boolean and print the value
val = 0
print(bool(val))
#
# Convert False to a string and print the value
val = False
print(str(val))
print(type(str(val)))
# 2. Convert all characters in the string to uppercase. x = "hello"
x = "hello"
print(x.upper())
# 3. Given x = 5 and y = 3.14, calculate z = x + y and determine the data type of z. And convert it to integer.
x = 5
y = 3.14
z = x + y
print(z)
print(type(z))
z = int(z)
print(z)
print(type(z))
# 4. Given the string s = 'hello', perform the following operations:
# Convert the string to uppercase.
s = 'hello'
print(s.upper())
#
# Replace 'e' with 'a'.
print(s.replace('e', 'a'))
#
# Check if the string starts with 'he'.
print(s.startswith("he"))
#
# Check if the string ends with 'lo'.
print(s.endswith("lo"))

#Function
# Define a function calculate_area that calculates the area of a rectangle and return the result. If no width is provided, it defaults to 10.
#
def calculate_area(length, width = 10):
    return width * length

# 2.  Write a recursive function to compute the factorial of a non-negative integer.
def factorial(n):
    if n <= 1:
        return 1;
    return n * factorial(n-1)
# 3. Write a function that takes one parameter as a string and reverse it and return.
def reverse_string(str):
    return str[::-1]
# 4. Write a Python function that takes two parameters as lists and to sum all the numbers in a list.
# a = [8, 2, 3, 0, 7], b =  [3, -2, 5, 1] and return a value.

def list_sum(a, b):
    ans = 0;
    for num in a:
        ans += num
    for num in b:
        ans += num
    return ans

a = [8, 2, 3, 0, 7]
b =  [3, -2, 5, 1]

# 5. Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list. a = [4,1,2,3,3,1,3,4,5,1,7]
# Output = [1,2,3,4,5,7]
def distinct_sorted_list(a):
    return sorted(set(a))

#Input Print
# Objective: Ask the user for their name and greet them.
# Task: Write a program that asks the user for their name and then prints a greeting   message using their name.
name = input("please enter your name: ")
print(f"Hello {name}")
# Objective: Perform basic arithmetic operations based on user input.
# Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
print(f"sum :  {num1 + num2}")
print(f"multiplication: {num1 * num2}")
print(f"division : {num1 / num2}")
# Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
user_input = input("please enter names seperated by commas : ")
final_list = user_input.split(",")
print(final_list)
# Task: Ask the user to enter their age and check if they are eligible to vote based on their age.
age = int(input("enter your age to verify voting eligibility : "))
result = "you are eligible" if age >= 18 else "you are not eligible"
print(result)
# For value = 3.14159, Using f-string print output for only up to 2 decimal places.
# Output: 3.14
#
val = 3.14159
print(f"{val:.2f}")

#List Comprehension
# Given a list of numeric strings, convert them into integers. Using List Comprehensions
# strings = ["1", "2", "3", "4", "5"]
# #Expected output : [1, 2, 3, 4, 5]
#
strings = ["1", "2", "3", "4", "5"]
output = [int(s) for s in strings]
print(output)
# Extract all integers from a list that are greater than 10. Using List Comprehensions
# numbers = [1, 5, 13, 4, 16, 7]
# #Expected output :[13, 16]
numbers = [1, 5, 13, 4, 16, 7]
output = [n for n in numbers if n > 10]
print(output)
# Create a list of squares for numbers from 1 to 5. Using List Comprehensions
# #Expected output :[1, 4, 9, 16, 25]
print([n**2 for n in range(1, 6)])
# Convert a 2D list into a 1D list.Using List Comprehensions
# matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
# #Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
print([n for r in matrix for n in r])
# Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
# #Expected output : {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)
# Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
# 	#Expected output : {'Alice': 85, 'Charlie': 90}
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
d = {k: v for k, v in scores.items() if v > 80}
print(d)

