#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

pattern = r'ab*'
string = input()
matches = re.findall(pattern, string)
print(matches)

