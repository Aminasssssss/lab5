#Write a Python program to split a string at uppercase letters.
import re

string = input()
split_string = re.split(r'(?=[A-Z])', string)
print(split_string)
