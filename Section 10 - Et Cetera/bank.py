'''
bank
'''

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code





balance = 0


def main():
    print("Balance", balance)
    deposite(100)
    withdraw(50)
    print("Balance", balance)

def deposite(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()





def main():
    balance = 0
    print("Balance", balance)
    deposite(100)
    withdraw(50)
    print("Balance", balance)

def deposite(n):
    balance += n

def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()




balance = 0


def main():
    print("Balance", balance)
    deposite(100)
    withdraw(50)
    print("Balance", balance)

def deposite(n):
    balance += n

def withdraw(n):
    balance -= n

if __name__ == "__main__"
    main()




balance = 0


def main():
    print("Balance", balance)


if __name__ == "__main__"
    main()

'''