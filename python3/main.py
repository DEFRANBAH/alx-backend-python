#!/usr/bin/python3

class webber:
    person = 'animal'
    communism = 'conservative'
    freedom = 75

    def __init__(self,name,gearboxtype,chasisNo):
        self.name = name
        self.gearboxtype = gearboxtype 
        self.chasisNo = chasisNo
        
        print("the car is {}and the gearbox type is {} and chasis no is {}".format(self.name, self.gearboxtype, self.chasisNo))

    def speak(self):
        print('my name is toyota')

    def details(self):
        print("my cars name is {}".format(self.name))

vag = webber("voice", "DSG_crank", "71888")
daimlerchrysler = webber("benz", "inline_complimentary", "79934")

daimlerchrysler.details()


