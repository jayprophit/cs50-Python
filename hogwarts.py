'''
Hogwarts
'''



# data base - a list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"}
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep="")


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



# associates the key student with the name
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}


for student in students:
    print(student, students[student], sep=", ")




# associates the key
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}


for student in students:
    print(student, students[student])



# associates the key of the name
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}


for student in students:
    print(student)



# associates the Name of the student to the House they are placed in
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}


print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])



# list of 4 strings
students = ["Hermione", "Harry", "Ron"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]



# list of 4 strings
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])



# list of 4 strings
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i, students[i])



# list of 4 strings
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(students[i])



# list of 4 strings
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)



# list of 3 strings
students = ["Hermione", "Harry", "Ron"]

# prints the variable (students) in the location of list
print(students[0])
print(students[1])
print(students[2])
'''

'''
'''