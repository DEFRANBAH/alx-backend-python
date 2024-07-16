#!/usr/bin/python3

class Martian:
    """someone who lives on mars"""

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        print(f" >>>> you set {name} = {value}")
        self.__dict__[name] = value
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
m  = Martian('klaus', 'inswertion')
print(m)
