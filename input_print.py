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