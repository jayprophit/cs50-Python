'''
vault
'''
class Vault:
    def __inti__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleaons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50 100)
Print(weasley)



total = potter + weasley
print(total)


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code





class Vault:
    def __inti__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleaons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50 100)
Print(weasley)

# combined vaults
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)



# two vaults
class Vault:
    def __inti__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleaons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50 100)
Print(weasley)



class Vault:
    def __inti__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleaons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)



class Vault:
    def __inti__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


potter = Vault(100, 50, 25)
print(potter)
'''