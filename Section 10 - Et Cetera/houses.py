'''
house
'''

student = [
    {"name": "Hermione", "house", "Gryffindor"},
    {"name": "Harry", "house", "Gryffindor"},
    {"name": "Ron", "house", "Gryffindor"},
    {"name": "Draco", "house", "Slytherin"},
    {"name": "Padma", "house", "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])


for house in sorted(houses):
    print(house)


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

student = [
    {"name": "Hermione", "house", "Gryffindor"},
    {"name": "Harry", "house", "Gryffindor"},
    {"name": "Ron", "house", "Gryffindor"},
    {"name": "Draco", "house", "Slytherin"},
    {"name": "Padma", "house", "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])


for house in sorted(houses):
    print(house)



student = [
    {"name": "Hermione", "house", "Gryffindor"},
    {"name": "Harry", "house", "Gryffindor"},
    {"name": "Ron", "house", "Gryffindor"},
    {"name": "Draco", "house", "Slytherin"},
    {"name": "Padma", "house", "Ravenclaw"},
]

houses = list()
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])


for house in sorted(houses):
    print(house)




student = [
    {"name": "Hermione", "house", "Gryffindor"},
    {"name": "Harry", "house", "Gryffindor"},
    {"name": "Ron", "house", "Gryffindor"},
    {"name": "Draco", "house", "Slytherin"},
    {"name": "Padma", "house", "Ravenclaw"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])


for house in sorted(houses):
    print(house)

'''