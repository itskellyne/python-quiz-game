#Object-oriented programming

"""
Programming structured around the idea of creating objects which have their own properties (variables/data) and methods (functions)
"""
# Classes

"""
Classes are the blueprint for objects
Instances are the objects created from the class
In Python, class names are capitalized
Methods are created by defining a function within the class
Every class should have a method defined called __init__()
itit is also called the constructor 
when we create a new instance of our class the init function sets that new object up
Function names with underscores like __init__ are called dunder methods
Dunder methods are methods with predefined names with certain behaviors
The first parameter of  __init__ is called "self" and refers to the new object
"self" is automatically supplied when the constructor is called
The other parameters of _init_ will be the initial values for the new object
"""

class Person:
    def __init__(self, first_name, last_name, age):
        #Instance variables are unique to each object
        #We'll create instance variables on our new object
        #Set their values to the data from oue parameters
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    # We use self 
    def print_greeting(self):
        #use f for dynamic values
        print(f"Hi! I'm {self.first_name} {self.last_name} and I'm {self.age} years old.")



# INSTANCES

# When we create an object from a class, we call it an "instance" of that class
# To create an instance (call our constructor), we write the class name
# followed by a set of parentheses, like this: MyClass()

# Create a Person and store it in a variable
test_person = Person("Alekai", "McAdam", 24)

# Access the test_person's variables and methods with dot notation
print(test_person.first_name)
test_person.print_greeting()


# Create a list of people and call print_greeting() on each one
people_list = [
  Person("John", "Doe", 44),
  Person("Joe", "Shmoe", 30),
  Person("Mary", "Sue", 31)
]

for p in people_list:
  p.print_greeting()


# F-strings (template strings) allow us to create complex messages easily

print(f"this is an f-string! {5+5} {test_person.last_name}")


# The input() function asks the user to type something in and returns the result
# input() always returns a string!!!!

input_result = input("Please type something")
print(f"you typed {input_result}")