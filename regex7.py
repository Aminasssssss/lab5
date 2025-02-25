#Write a python program to convert snake case string to camel case string.
import re

string = input()
camel_case = ''.join(word.capitalize() for word in string.split('_'))
print(camel_case)
