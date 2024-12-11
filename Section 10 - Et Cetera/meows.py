'''
meows
'''

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = cat()
cat.meow()

'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

MEOWS = 3


for _ in range(MEOWS):
    print("meow")




for i in range(3):
    print("meow")
'''