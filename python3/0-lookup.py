#!/usr/bin/python3
"""code to show the remarkable o fthe classs attributes and methods"""

from new4 import Webber, Person
def lookup(obj):
    # Use dir() to get the list of attributes and methods
    attributes_and_methods = dir(obj)

    # Filter out names that start with '__' (internal attributes/methods)
    filtered_attributes_and_methods = [name for name in attributes_and_methods if not name.startswith('__')]

    return filtered_attributes_and_methods

# Example usage:
class ExampleClass:
    def __init__(self):
        self.attribute1 = "I am an attribute"
    
    def method1(self):
        return "I am a method"

# Create an instance of ExampleClass
example_object = ExampleClass()

example_object1 = Webber("Jackson")
example_object2 = Person("Jackson2", 1103, "Mayor")
# Call the lookup function on the object
result = lookup(example_object)
result1 = lookup(example_object1)
result3 = lookup(example_object2)
# Print the result
print(result)
print(result1)
print(result3)  # Should print ['attribute1', 'method1']
