#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

pattern = r'\b[a-z]+_[a-z]+\b'
string = input()
matches = re.findall(pattern, string)
print(matches)
