#!/usr/bin/python3

class webber:

   
    def __init_(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    @classmethod
    def from_cls(cls, empl_str):
        first, last, pay = empl_str.split('-')
        return cls(first, last, pay)


    emp_str6 = 'class-jackson-70000'
    emp_str5 = 'coshion-masinde-50000'
    emp_str4 = 'zadock-obiwire-80000'
    emp_str3 = 'nyakundi-masike-230000'
    emp_str2 = 'zayuni-okire-6560000'
    
    mkazi1 = webber.from_cls(emp_str2)
    print(mkazi1.pay)




