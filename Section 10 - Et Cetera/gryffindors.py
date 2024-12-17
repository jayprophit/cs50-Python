'''
gryffindors
'''

# sorted list
students = [
    {"name": "Harmione", "house": "Gryffindor"}
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "Ron", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor":

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lamba s: s["name"]):
    print(gryffindor["name"])

'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

# unsorted list
students = [
    {"name": "Harmione", "house": "Gryffindor"}
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "Ron", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor":

gryffindors = filter(is_gryffindor, students)

for gryffindor in gryffindors:
    print(gryffindor["name"])




students = [
    {"name": "Harmione", "house": "Gryffindor"}
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "Ron", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor":




students = [
    {"name": "Harmione", "house": "Gryffindor"}
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "Ron", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
]

def is_gryffindor(s):
    if s["house"] == "Gryffindor":
        return True
    else:
        return False



students = [
    {"name": "Harmione", "house": "Gryffindor"}
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "Ron", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
]

gryffindor = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)



# not complete
students = [
    {"name": "Harmione", "house": "Gryffindor"}
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "Ron", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
]

gryffindor = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]



students = [
    {"name": "Harmione", "house": "Gryffindor"}
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "Ron", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
]
'''