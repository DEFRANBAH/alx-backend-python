#!/usr/bin/python3

class person:
    """represents a class called person"""

    #a class variable counting the number of the animals
    population = 0

    def __init__(self, name):
        self.name = name

        person.population += 1

    def popinc(self):
        print("animal pupulation initially {}".format(self.name))


    def add(self):
        print("population after adding is {}".format(person.population))
        person.population += 1

    
    def minus(self):
        
        print("after takeaway there are stiil {:d} animals remaining".format(person.population))


class empoloyed(person):
    def __init__(self, salary, position):

        person.__init__(self, name)
        self.salary = salary
        self.position = position


    def popinc(self): print('there is not much here')

person1 = person("nick") 
person1.popinc() 
person1.add() 
person1.minus()

person2 = empoloyed(20000, "manager")
person2.popinc
