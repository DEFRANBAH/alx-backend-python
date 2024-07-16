def my_fct(*args, **kwargs) 
    print("{} - {}".format(args, kwargs))

a_dict = { 'name': "Best", 'age': 89 }

my_fct(a_dict) # ({'age': 89, 'name': 'Best'},) - {}
my_fct(*a_dict) # ('age', 'name') - {}
my_fct(**a_dict) # () - {'age': 89, 'name': 'Best'}

# a function to demonstrate the use of kwargs and args 

def illenium(*args, **kwargs):
    print("{}, {}".format(args, kwargs))

a_dict = {'said_the_sky' : 'onguard', 'dabin' : 'nightight'}

illenium(a_dict) #({'said_the_sky' : 'onguard', 'dabin' : 'nightight'}), {}
illenium(*a_dict) #('said_the_sky','dabin')- {}
illenium(**a_dict) #()-{'said_the_sky' : 'onguard', 'dabin' : 'nightight'}

