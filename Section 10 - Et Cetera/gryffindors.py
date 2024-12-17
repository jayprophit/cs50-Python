'''
gryffindors
'''

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


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code


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