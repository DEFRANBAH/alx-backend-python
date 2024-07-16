#!/usr/bin/python3

class Webber:
    population = 0

    def __init__(self, name):
        self.name = name
        Webber.population += 1
        print(f"The name of the thing is {self.name}. Current population is {Webber.population}")

    def speak(self):
        print("Into my room and the current population is {}".format(Webber.population))

class Person(Webber):
    def __init__(self, name, salary, position):
        self.salary = salary
        self.position = position
        super().__init__(name)
        Webber.population += 1
        print(f"{name}, {salary}, {position}, this is where iam currrently")
    def local(self):
        print("My name is not the legal name {}".format(self.name))

    def add(self):
        Webber.population += 1
        print("Now the population increament. Current population is {}".format(Webber.population))

    def minus(self):
        Webber.population -= 1
        print("Now the population decrement. Current population is {}".format(Webber.population))

webber_obj = Webber("Jackson")
webber_obj.speak()
person_obj = Person("Jackson2", 1103, "Mayor")
person_obj.local()
person_obj.add()
person_obj.minus()
