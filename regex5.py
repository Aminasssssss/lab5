#Write a Python program that matches a string that has an 'a' followed by anything, 
#ending in 'b'.
import re

pattern = r'a.*b$'
string = input()
matches = re.findall(pattern, string)
print(matches)
