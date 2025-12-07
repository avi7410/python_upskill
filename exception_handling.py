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
