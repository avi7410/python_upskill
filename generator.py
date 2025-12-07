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