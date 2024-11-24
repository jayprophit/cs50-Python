'''
hat
'''

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Raveclaw", "Slythrin"]


    def sort(self, name):
        print(name, "is in", random.choice(self.house))


hat = Hat()
hat.sort("Harry")


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code





class Hat:
    def sort(self, name):
        print(name, "is in", "some house")


hat = Hat()
hat.sort("Harry")
'''
