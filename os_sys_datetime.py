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
