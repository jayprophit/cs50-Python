'''
twitter (X)
'''
import re

url = input("URL: ").strip()

matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if mathces:
    print(f"Username:", matches.group(2))



'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")




re.sub(r"^http|https://twitter\.com/", "", url)
print(f"Username: {username}")




re.sub(r"^https://twitter\.com/", "", url)
print(f"Username: {username}")




username = url.removeprfix("https://twitter.com/", "")
print(f"Username: {username}")



username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")



url = input("URL: ").strip()
print()
'''