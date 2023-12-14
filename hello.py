'''
Print Hello
'''


def main()
    name = input("What's your name? ").strip().title()
    hello()  

def hello(to="world")
    print("hello,", to)

main()

'''
# different variations to produce the same result and solve the problem
# desending from currently used practises to basic begginer code


def main()
    name = input("What's your name? ").strip().title()
    hello()  

def hello()
    print("hello,", name)

main()


def hello(to="world")
    print("hello,", to)

# calls hellow to the world
hello()  
name = input("What's your name? ").strip().title()
# calls hello personally
hello(name)


# by default it makes the word to = world, without having to use an argument
def hello(to="world")
    print("hello,", to)
    
name = input("What's your name? ").strip().title()
hello(name)


def hello()
    
    print("hello")
    
# ask user for their name
name = input("What's your name? ").strip().title()

hello()

# say hello
print(name)


# ask user for their name
name = input("What's your name? ").strip().title()

# say hello
print(f"hello, {name}")


# ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split("")

# say hello
print(f"hello, {first}")



# ask user for their name
name = input("What's your name? ").strip().title()

# say hello
print(f"hello, {name}")



# ask user for their name
name = input("What's your name? ")

# Remove whitespace from str and Capitalize 1st letter of each word of user's name
name = name.strip().title()

# say hello
print(f"hello, {name}")



# ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize 1st letter of each word of user's name
name = name.title()

# {} list bracket to surrand the number
# say hello
print(f"hello, {name}")



# ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize 1st letter of user's name
name = name.capitalize()

# say hello
print(f"hello, {name}")



# ask user for their name
name = input("What's your name? ")

# say hello
print(f"hello, {name}")



# ask user for their name
name = input("What's your name? ")

# say hello
print("hello,", sep="")
print(name)



# ask user for their name
name = input("What's your name? ")

# say hello
print("hello,", end="")
print(name)



# ask user for their name
name = input("What's your name? ")

# say hello
print("hello,", name)



# ask user for their name
name = input("What's your name? ")

# + adds an additional function to the call function
# additional spcing ("hello, ") after the comma (,)
print("hello, " + name)



# ask user for their name
name = input("What's your name? ")

# say hello to user
print("hello,")
print(name)



# sedo code - stuctured to-do-list, that sets out sort guide lines of whats needed to be coded (bit-sized tasks)
# ask user for their name
# say hello to user



name = input("What's your name? ")
print("hello, name")



name = input("What's your name? ")
print("hello, John")



# prints hello world to be interperated and made readable 
print("hello world")
'''