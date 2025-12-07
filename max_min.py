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
