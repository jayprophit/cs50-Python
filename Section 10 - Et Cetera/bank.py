'''
bank
'''

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