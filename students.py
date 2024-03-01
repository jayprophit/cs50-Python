'''
Students
'''


import csv

name = input("what's your name? ")
home = input("where's your home? ")


with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})



'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



name = input("what's your name? ")
home = input("where's your home? ")


with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])



students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home""]})

for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)
        
# lambda is an anonymous order, x and y are extra lambda's
for student in sorted (students, key=lambda student,x, y: student["name"],x["house"],y["name"]):
    print(f"{student['name']} is in {student['house']}")



students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")



# house names in ascending order
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]

# descending order
for student in sorted (students, key=get_house):
    print(f"{student['name']} is in {student['house']}")




# sorted by house ind reverse order
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]

# descending order / reverse order
for student in sorted (students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")


student = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

# ascending order
for student in sorted (students, key=get_name):
    print(f"{student['name']} is in {student['house']}")



students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    #using double and single quotes so python distinguishes between the two
    print(f"{student['name']} is in {student['house']}")



# sort them by specified category
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = name
        students.append(student)

for student in students:
    #using double and single quotes so python distinguishes between the two
    print(f"{student['name']} is in {student['house']}")



# sort them by a sentence of words
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)



# sort them by category
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")



with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
'''