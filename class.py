#
# 1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
#
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

student = Person("avi", 21)
print(f"{student.name} - {student.age}")
# 2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name

    def deposit(self, credit):
        self.balance += credit
    def withdraw(self, debit):
        self.balance -= debit
    def check_balance(self):
        return self.balance
# 3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
#
#       book = Book.from_string("Python Programming, John Doe")
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    @classmethod
    def from_String(self, str):
        arr = str.split(", ")
        return self(arr[0], arr[1])
book = Book.from_String("Python Programming, John Doe")
print(f"{book.author} wrote {book.name}")
# 4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.
class Animal:
    def sound(self):
        return "some sound"
    def breathe(self):
        return "breathing"
class Dog(Animal):
    def sound(self):
        return "bark"
class Cat(Animal):
    def sound(self):
        return "meow"

a = Animal()
print(a.sound())
print(a.breathe())
d = Dog()
c = Cat()
print(d.sound())
print(d.breathe())
print(c.sound())
print(c.breathe())

# 5. Write a code to perform multiple inheritance.
#
class A:
    def write(self):
        print("a")
class B:
    def write(self):
        print("b")
class C(B,A):
    pass

c = C()
c.write()