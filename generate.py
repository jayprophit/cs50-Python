'''
Generate
'''


import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)




import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)



import random

number = random.randint(1, 10)
print(number)



# allows you to import a a function from the module called random
from random import choice

coin = choice(["heads", "tails"])
print(coin)



# imports module called random which has been installed
import random

# variable, calls random, has to input options, square brackets for list, parenthesis 
coin = random.choice(["heads", "tails"])
print(coin)
'''