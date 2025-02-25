#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

string = input()
new_string = re.sub(r'[ ,.]', ':', string)
print(new_string)
