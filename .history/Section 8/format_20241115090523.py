'''
format
'''

import re

name = input("What's your name? ").strip()
match = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
last = matches.group(2)
print(f"hello, {name}")


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code





name = input("What's your name? ").strip()
match = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")



name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ?")
    name = f"{first} {last}"
print(f"hello, {name}")



if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
'''