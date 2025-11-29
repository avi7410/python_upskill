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

