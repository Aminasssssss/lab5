#Write a Python program to find the sequences of one upper case letter
# followed by lower case letters.

import re

pattern = r'[A-Z][a-z]+'
string = input()
matches = re.findall(pattern, string)
print(matches)
