'''
names
'''


names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

# opens the file reads it, sorts the data and returns it in reverse alphabetical descending order
for name in sorted(names, reverse=True):
    print(f"hello, {name}")


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())



# opens the file reads it, sorts the data and returns it in alphabetical ascending order
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")



with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())


with open("names.txt", "r") as file:
    lines = file.readlines() 

for line in lines:
    print("hello,", line.rstrip())



with open("names.txt", "r") as file:
    lines = file.readlines() 

for line in lines:
    print("hello,", line, end="")


# opens a file writes data and closes saves and closes the file
name = input("whats your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n") 



name = input("whats your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n") 
file.close()



# a - append, to add to the bottom
file = open("names.txt", "a")
file.write(name) 
file.close()



# opens a file or creates a file
file = open("names.txt", "w")
# writes data on the file
file.write(name)
# saves and closes the file 
file.close()



names = []

for _ in range(3):
    names.append(input("whats your name? "))
    
for name in sorted(names):
    print(f"hello, {name}")



for _ in range(3):
    name = input("whats your name? ")
    names.append(name)



name = input("whats your name? ")
print(f"hello, {name}")
'''