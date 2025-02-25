#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

pattern = r'ab{2,3}'
string = input()
matches = re.findall(pattern, string)
print(matches)
