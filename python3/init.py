#!/usr/bin/python3

class Bird:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("{} too are flying birds".format(self.name))

    def flight(self):
        print("all bird have wings but {} can fly".format(self.name))

    def wings(self):
        print("not all {} birds can fly".format(self.name))

class Ostritch(Bird):
    def __init__(self, name, wingtype, weight):
        self.wingtype = wingtype
        self.weight = weight
        self.name = name
        super().__init__(name)
    
    
    def flight(self):
        print("have not wings")

    def wings(self):
        print("have not wings")

    def display(self):
        print("this is {} ostritch".format(self.name))

Ostritchy_obj = Ostritch('danny','long', 120)
Ostritchy_obj.flight()
Ostritchy_obj.wings()
Ostritchy_obj.wings()
Ostritchy_obj.display()
O


        
