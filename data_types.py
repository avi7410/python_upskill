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