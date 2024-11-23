'''
Print Hello
'''


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt)
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



def main():
    x = get_int()
    print(f"x is {x}")

def get_int()
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main()



def main():
    x = get_int()
    print(f"x is {x}")

def get_int()
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()



def main():
    x = get_int()
    print(f"x is {x}")

def get_int()
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer")

main()



def main():
    x = get_int()
    print(f"x is {x}")

def get_int()
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main()



# while loops forever
while True:
    try:
        x = int(input("What's x? "))
        #breaks loop
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")



# while loops forever
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        #breaks loop
        break

print(f"x is {x}")



try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")



try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")



# tries a code
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
# accepts - over looks specified error 
except ValueError:
    print("x is not an integer")



x = int(input("What's x? "))
    print(f"x is {x}")
'''