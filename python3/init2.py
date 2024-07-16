def doug(obj):
    ## this function utilizes the dir function. lists of attributes and methods
    object_doug = dir(obj)

    filtered_object_doug = [name for name in object_doug if not name.startswith('__')]

    return filtered_object_doug

#example usage 
class Example():
    def __init__(self):
        self.atribute1 = "a string boom"

    def method1(self):
        return "iam a method"

exampleClass = Example()
### nmae of your variable before assigning and utilizing the objectinstance

results = doug(exampleClass)

print(results)

