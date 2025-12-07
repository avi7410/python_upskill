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
