#Write a Python program to convert a given camel case string to snake case.
import re

string = input()
snake_case = re.sub(r'([A-Z])', r'_\1', string).lower().strip('_')
print(snake_case)
