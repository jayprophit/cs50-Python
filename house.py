'''
House
'''

name = input("What's our name? ").strip().title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # -: = who in case - match
    case _:
        print("Who?")

'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # -: = who in case - match
    case _:
        print("Who?")



name = input("What's our name? ").strip().title()

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")



name = input("What's our name? ").strip().title()

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
'''