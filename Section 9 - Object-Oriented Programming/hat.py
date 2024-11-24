'''
hat
'''
import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Raveclaw", "Slythrin"]


    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Raveclaw", "Slythrin"]


    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")




class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Raveclaw", "Slythrin"]


    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")



class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Raveclaw", "Slythrin"]


    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", "some house")


hat = Hat()
hat.sort("Harry")



class Hat:
    def sort(self, name):
        print(name, "is in", "some house")


hat = Hat()
hat.sort("Harry")
'''
