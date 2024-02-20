'''
Students
'''



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




'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



.



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