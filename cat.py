'''
Cat
'''


def main ():
    number = get_number()
    meow(number)

# personalized function called number
def get_number():
    while True:
        n = int(input("What's n ? "))
        if n > 0:
            break
        return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
    
'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



def main ():
    number = get_number()
    meow(number)

# make your own function
def get_number():
    while True:
        n = int(input("What's n ? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()



def main ():
    meow(3)

def 

def meow(n):
    for _ in range(n):
        print("meow")

main()



while True:
    n = int(input("What's n ? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")



while True:
    n = int(input("What's n ? "))
    if n < 0:
        continue
    else:
        break



n = int(input("What's n? "))
if n < 0:
    n = int(input("What's n? "))
    if n < 0:
        n = int(input("What's n? "))


# eliminates the extra blank space
print("meow\n" * 3, end="")



print("meow\n" * 3)


# multiples meow by three, then prints to the screen
print("meow" * 3)



for _ in range(3):
    print("meow")


for i in range(3):
    print("meow")



for i in [0, 1, 2]:
    print("meow")



i = 0
# while i is less than
while i < 3:
    print("meow")
    # i equals i plus one 
    i += 1



i = 1
# while i is less than or equal to three
while i <= 3:
    print("meow")
    # i equals adds one greater/ increased by one (unit, character, input/ output, etc) every time it loops back around
    i = i + 1



i = 3
# while i dose not equal zero
while i != 0:
    print("meow")
    # i equals one less/ decreased by one (unit, character, input/ output, etc) every time it loops back around
    i = i - 1



print("meow")
print("meow")
print("meow")
'''