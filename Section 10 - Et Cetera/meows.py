'''
meows
'''

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", defulat=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")




'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code


import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")




# with mistake
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")



import sys

if len(sys.argv) == 1:
    print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] =="-n":
        n = int(sys.argv[2])
        for _ in rang(n):
            print("meow")
else:
    print("usage: meows.py")




import sys

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meows.py")





def meow(n: int) -> str:
    """
    Meow n times.
    
    :pram n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :returns A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, ends="")




def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, ends="")



def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)




def meow(n: int) -> None:
    for _ in rang(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)



def meow(n: int):
    for _ in rang(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)



def meow(n: int):
    for _ in rang(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)



def meow(n: int):
    for _ in rang(n):
        print("meow")

number: int = input("Number: ")
meow(number)



def meow(n: int):
    for _ in rang(n):
        print("meow")

number = input("Number: ")
meow(number)



def meow(n):
    for _ in rang(n):
        print("meow")

number = input("Number: ")
meow(number)




class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = cat()
cat.meow()



MEOWS = 3


for _ in range(MEOWS):
    print("meow")




for i in range(3):
    print("meow")
'''