'''
unpack
'''

def total(galleons, sickles, knuts):
    return(galleons * 17 +sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "knuts")


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code





def total(galleons, sickles, knuts):
    return(galleons * 17 +sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins[galleons], coins[sickles], coins[knuts]), "knuts")




def total(galleons, sickles, knuts):
    return(galleons * 17 +sickles) * 29 + knuts

print(total(galleons=100, sickles=50, knuts=25), "knuts")




def total(galleons, sickles, knuts):
    return(galleons * 17 +sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "knuts")




#has faults
def total(galleons, sickles, knuts):
    return(galleons * 17 +sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "knuts")




def total(galleons, sickles, knuts):
    return(galleons * 17 +sicles) * 29 + knuts

print(total(100, 50, 25), "knuts")




first, last = input("what's your name? ").split(" ")
print(f"hello, {first}")
'''