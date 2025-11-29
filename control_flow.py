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
