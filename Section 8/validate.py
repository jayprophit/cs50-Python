'''
validate
'''

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|co.uk|edu|net|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code


if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.(com|co.uk|edu|net|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|co.uk|edu|net|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



if re.search(r"^\w+@(\w+\.)?\w+\.(com|co.uk|edu|net|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



if re.search(r"^[a-zA-Z0-9_ ]+@[a-zA-Z0-9_ ]+\.com$", email):
    print("Valid")
else:
    print("Invalid")



if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")
else:
    print("Invalid")



if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")



if re.search(r".+@.+\.com", email):
    print("Valid")
else:
    print("Invalid")



if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invalid")



if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")



if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")



if re.search("@", email):
    print("Valid")
else:
    print("Invalid")



email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")



if username and "." in domain:
    print("Valid")
else:
    print("Invalid")



if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")



if "@" in email:
    print("Valid")
else:
    print("Invalid")
'''