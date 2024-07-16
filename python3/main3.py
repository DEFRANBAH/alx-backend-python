#!/usr/bin/python3

doug = __import__('init2').doug

class myClass1(object):
    pass

class myClass2(object):
    my_attribute = 3
    def my_meth(self):
        pass

print(doug(myClass1))
print(doug(myClass2))
print(doug(int))
