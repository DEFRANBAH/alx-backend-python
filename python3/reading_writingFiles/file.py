import os 

with open('main3.py', mode='w', encoding='utf-8') as myFile:
    myFile.write('some more random texts \nmore random texts\nAnd some')


with open('main3.py', encoding='utf-8') as myFile:

words = myFile.readline()

print('the words are:' words)
