
#how to find the 
def matching_letters():
    str1=input("Enter frist string: ")
    str2=input("Enter second string: ")

    s1 = set(str1)
    s2 = set(str2)

    lst=s1&s2

    return print(lst)

matching_letters()

# Split the string into words
string = 'Hello Oscar, how are you doing today?'
words = string.split()
d = {}

for i in words:
    if i not in d.keys():
        d[i] = 0
    d[i] = d[i] + 1


list1 = ['agustin','jorge','oscar']
list2 = [25,31,32]

data = {
    'name':['agustin','jorge','oscar'],
    'age':[25,31,32],
    'location':['BTS','BTS','BTS'],
    'stocks': [11, 8, 19]}

df = pd.DataFrame(data)

n = 2
col = 'age'

def multiple(df,col,n):
    result = df[col] * n
    print(result)

multiple(df,col,n)

multiple_lambda = lambda df,col,n: print(df[col] * n)

multiple_lambda(df,col,n)

i = 00000.1

while i <= 1:  
    i = i + i * i
    print(i)

import json

people_string = """{
    "people": [
        {
            "name":"Agustin",
            "age":25,
            "location": "BTS",
            "stocks": 11
        },
                {
            "name":"Oscar",
            "age":32,
            "location": "BTS",
            "stocks": 23
        },
                {
            "name":"Jorge",
            "age":31,
            "location": "BTS",
            "stocks": 18
        }
    ]
}
"""


json_data=json.loads(people_string)
pd.json_normalize(json_data['people'])

x='1'
int(x)
bool(x)
tuple(x)
list(x)
str(x)
set(x)

import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params)

print(response.status_code)   # should be 200

data = response.json()
df = pd.DataFrame(data)





#Dunder variables:
# __name__: The name of the current module. If the module is being run as the main program, __name__ will be set to "__main__".
# __doc__: The docstring of the current module, which can be accessed using the __doc__ variable.

def add(a, b):
    """This function adds two numbers."""
    return a + b

if __name__ == "__main__":
    if add(1,2) == 3:
        print("The add function works correctly.")
    else:
        print("The add function does NOT work correctly.")

# Packages and Modules
# A module is a file containing Python code that defines functions, classes, and variables. 
# A package is a collection of modules organized in a directory hierarchy. It allows for better organization and modularization of code.

#./my_package/
#     __init__.py
#     module1.py
#     module2.py
# ./my_package/my_package2/
#     __init__.py
#     module3.py

import my_package.module1
from my_package import module2
from my_package.my_package2 import module3

# Class & Objects
# A class is a blueprint for creating objects in Python. 
# It defines a set of attributes and methods that the objects created from the class will have. 
# An object is an instance of a class, which means it is a concrete entity that has attributes and behaviors defined by its class.

class Product:
    def __init__(self, asin, name, price, quantity):
        self.asin = asin
        self.name = name
        self.price = price
        self.quantity = quantity

    # Method to sell units
    def sell(self, units):
        if units <= self.quantity:
            self.quantity -= units
            revenue = units * self.price
            return revenue
        else:
            print("Not enough stock")
            return 0

    # Method to restock units
    def restock(self, units):
        self.quantity += units

    # Method to calculate inventory value
    def inventory_value(self):
        return self.quantity * self.price


# Create object (instance of the class)
product = Product("B08XYZ123", "Wireless Mouse", 25.0, 100)

# Use methods
revenue = product.sell(3)
print("Revenue:", revenue)

product.restock(10)

value = product.inventory_value()
print("Inventory value:", value)

print("Remaining quantity:", product.quantity)


# xrange
# xrange is a function that returns an iterator object, which we can iterate over.
# It is similar to range(), but it is more memory efficient for large ranges.
# However, xrange is not available in Python 3, where range() behaves like xrange.

# Difference between list, tuple, set and dictionary:
# List: A list is an ordered, mutable collection of items. It allows duplicate elements.
# Tuple: A tuple is an ordered, immutable collection of items. It allows duplicate elements.
# Set: A set is an unordered, mutable collection of unique items. It does not allow duplicate elements.
# Dictionary: A dictionary is an unordered, mutable collection of key-value pairs. It allows duplicate values but not duplicate keys.

#            / List / Tuple / Set/
# Syntax     / []   / ()    / {}  /
# Mutability  / True / False / True /
# Ordered     / True / True  / False/
# Duplicates   / True / True  / False/

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
# Output: [1, 4, 9, 16, 25]

items = ["Apple","Banana","Cherry","Date","BlackBerry"]

b_items = [item for item in items if item.startswith('B')]
# Output: ['Banana', 'BlackBerry']

upper_items = [item.upper() for item in items]
# Output: ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'BLACKBERRY']

print([n**2 for n in range(10)])
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#What is a function?
#A function is a reusable block of code that performs a specific task. It takes input (called parameters), processes it, and returns an output. Functions help to organize code, improve readability, and allow for code reuse.

def process_data(df):
    # Perform some data processing
    df["price_with_tax"] = df["price"] * df["tax_rate"]
    return df


#What is a lambda function?
#A lambda function is an anonymous function defined using the lambda keyword.
# It can take any number of arguments but can only have one expression. 
# Lambda functions are often used for short, simple functions that are not reused elsewhere in the code.

numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, numbers))
print(squared)
# [1, 4, 9, 16]

filtered = list(filter(lambda x: x > 2, numbers))
print(filtered)
# [3, 4]

sorted = sorted(numbers, key=lambda x: -x)
print(sorted)
# [4, 3, 2, 1]


#What are decorators?
#Decorators are a way to modify or enhance functions or methods in Python.
# They allow you to wrap another function, adding functionality before or after the wrapped function runs,
# without permanently modifying it. Decorators are often used for logging, access control, caching, and other cross-cutting concerns.
import time

def my_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Function executed in {end_time - start_time} seconds.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


#What is a generator?
# A generator is a special type of iterator in Python that allows you to iterate over a sequence once at the time. Avoiding excessive memory usage thanks to lazy evaluation.
# Lazy evaluation means they generate values on the fly as needed, rather than storing the entire sequence in memory.
# The opposite is eager evaluation, where all values are computed and stored in memory at once like general functions.

def my_generator():
    yield 1
    yield 2
    yield 3

obj = my_generator()
print(next(obj))

for value in my_generator():
    print(value)


# What is a closure?
# A closure is a function that retains access to variables from its enclosing scope, even after the outer function has finished executing.
# Closures are often used to create functions with private variables or to implement decorators.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
closure = outer_function(10)
print(closure(5))  # Output: 15


#What are *args and **kwargs?
#*args and **kwargs are used in function definitions to allow for variable-length arguments.

# *args allows a function to accept any number of positional arguments, which are passed as a tuple.
# **kwargs allows a function to accept any number of keyword arguments, which are passed as a dictionary.
def update_detailpage(asin, vendor_code, *args, **kwargs):
    print(f"ASIN: {asin}")
    print(f"Vendor Code: {vendor_code}")
    
    if args:
        print("Additional positional arguments:")
        for arg in args:
            print(arg)
    
    if kwargs:
        print("Additional keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

update_detailpage("B08N5WRWNW", "CMPPA", 'Extra 1', 'Extra 2', title='Super ASIN', sku="12345", color="red", size="M")

asin = {"asin": "B08N5WRWNW", "vendor_code": "CMPPA","title": "Super ASIN", "sku": "12345", "color": "red", "size": "M"}
update_detailpage(**asin)


# What is a class?
# A class is a blueprint for creating objects in Python. It defines a set of attributes and methods that the objects created from the class will have. Classes allow for encapsulation, inheritance, and polymorphism, which are key principles of object-oriented programming.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product Name: {self.name}, Price: {self.price}")


# What is an object?
# An object is an instance of a class. It is a concrete entity that has attributes and behaviors defined by its class. Objects can interact with each other and can be manipulated using the methods defined in their class.

product1 = Product("Laptop", 1200)
product1.display_info()


# What is inheritance?
# Inheritance is a fundamental principle of object-oriented programming that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.


# What is self in Python?
# self is a reference to the current instance of a class. It is used to access attributes and methods of the class within its own methods. When you define a method in a class, you must include self as the first parameter, which allows you to refer to the instance that is calling the method.


# Error handling with try-except
def divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both arguments must be numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Common Error Types:
#SyntaxError: Raised when there is a syntax error in the code.
#NameError: Raised when a variable is not defined.
#TypeError: Raised when an operation is applied to an object of inappropriate type.
#ValueError: Raised when a function receives an argument of the right type but inappropriate value.
#DivisionByZeroError: Raised when attempting to divide by zero.
#Exception: The base class for all exceptions, can be used to catch any exception that is not caught by more specific except blocks.


# Native file handling in Python

items = "Apple\nBanana\nCherry\nDate\nElderberry"

file = open("file.txt", "w")  # Open a file for writing
contents = file.write(items) # Write the items to the file
file.close()  # Close the file
file = open("file.txt", "r")  # Open a file for reading
contents = file.read()  # Read the contents of the file
print(contents)  # Print the contents of the file
contents = contents.split('\n')  # Split the contents into lines
contents.sort()  # Sort the lines alphabetically

for item in contents:
    print(' - ', item)  # Print each line

file.close()  # Close the file

file = open("file.txt", "a")  # Open the file for appending
file.write("\nGrape")  # Append new items to the file
file.close()  # Close the file

# Context managers with the with statement
with open("file.txt", "r") as file:  # Open the file for reading
    contents = file.read()  # Read the contents of the file
    print(contents)  # Print the contents of the file

# f-strings
f_temp = 250000
print(f"The current temperature is {(f_temp - 32)/ 1.8:.2f} degrees Celsius.")
#The current temperature is 138888888871.11 degrees Celsius.

print(f"The current temperature is {(f_temp - 32)/ 1.8:,.2f} degrees Celsius.")
#The current temperature is 138,888,888,871.11 degrees Celsius.

print(f"The current temperature is {(f_temp - 32)/ 1.8:17,.2f} degrees Celsius.") # extra spaces for alignment
#The current temperature is 138,888,888,871.11 degrees Celsius.

print(f"The current temperature is {(f_temp - 32)/ 1.8:-^20,.2f} degrees Celsius.") #<,>,^ for left, right and center alignment.




pd.read_csv("file.csv", 
            engine='pyarrow', # select the engine to read the file. Pyarrow is the fastest engine.
# Pyarrow is columnar, vectorized, zero-copy processing library.
            chunksize=1000, # process the file in chunks of 1000 rows
            compression='infer', # automatically detect the compression type based on the file extension. If the file is not compressed, it will be read as a regular CSV.
#            converters={'date': pd.to_datetime},
            sep=',',
            index_col=0,
            header=0,
            usecols=['date', 'asin', 'vendor_code', 'title', 'sku', 'color', 'size'],
            parse_dates=['date'],
            date_format='%Y-%m-%d', 
            cache_dates=True,
            encoding='utf-8',
#            low_memory=False, # checks data types interally in chunks.
            memory_map=True, # allows to read large files without loading them entirely into memory.
#            storage_options={'key':xxxx, 'secret_key':...}, # To connect to cloud 
            dtype={'asin': str, 'vendor_code': str, 'title': str, 'sku': str, 'color': str, 'size': str})



total = 0
for chunk in pd.read_csv("sales.csv", chunksize=100000):
    total += chunk["revenue"].sum()
print(total)
