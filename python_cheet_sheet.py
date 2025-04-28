#Python Cheet Sheet

# Basics
print("Hello, World!")    # Print output
x = 35                    # Variable Assignment
type(x)                   # Get the type of a variable 
input("Enter Value: ")    # Take user input 


# Data Types 
my_list = [1, 2, 3, 4]    # List
my_tuple = (1, 2, 3, 4)   # Tuple
my_set = {1, 2, 3, 4}     # Set
my_dict = {"key": "value"}# Dictionary

# Conditions
if x > 5:                       # If condition
    print("Greater Than 5!")
elif x == 5:                    # Else-if 
    print("Equals 5")
else:                           # Else
    print("Less Than 5!")

# Loops 
for i in range(5):              # For loop
    print(i)
while x > 0:                    # While loop
    x -= 1

# Functions
def greet(name):                # Define Class
    return f"Hello,{name}"

greet("Alice")                  # Call Functions

# Classes
class Person:                       # Define class
    def __init__(self, name):       # Constructor
        self.name = name

    def greet(self):                # Method
        return f"Hi, {self.name}"   

p = Person("Bob")                   #Create object
p.greet                             # Call method

# File Operatiors
with open("file.txt", "r") as f:    # Open a file
    content = f.read()              # Read file content

with open("file.txt", "w") as f:    # Write to a file
    f.write("Hello, File!")

# Error Handlings
try:                                # Try block
    1/0
except ZeroDivisionError:           # Handle exception
    print("Cannot divide by zero")
finally:                            # Always execute
    print("Done")