#Write a Python program to insert spaces between words starting with capital letters.
import re

string = input()
formatted_string = re.sub(r'([A-Z])', r' \1', string).strip()
print(formatted_string)
