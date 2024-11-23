'''
twitter (X)
'''
import re

url = input("URL: ").strip()

username = url.removeprfix("https://twitter.com/", "")
print(f"Username: {username}")


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code


username = url.removeprfix("https://twitter.com/", "")
print(f"Username: {username}")



username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")



url = input("URL: ").strip()
print()
'''