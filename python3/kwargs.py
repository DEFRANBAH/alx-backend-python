#!/usr/bin/python3

def print_stuff(*args):
    for args in args:
        print(args)

def print_many(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

def main():
    many = print_many(name ="member", age=30)

    stuff = print_stuff(67, 87, 89, 90,)

    print(f"here is the thing{many} \n and its func include{stuff}")

main()
