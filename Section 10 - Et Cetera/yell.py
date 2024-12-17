'''
yell
'''

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercase)
    
if __name__ == "__main__":
    main()



'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code


def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercase)
    
if __name__ == "__main__":
    main()



def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercase = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercase)
    
if __name__ == "__main__":
    main()



def main():
    yell("This", "is", "CS50")

def yell(*args):
    uppercase = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercase)
    
if __name__ == "__main__":
    main()



# not complete
def main():
    yell(["This", "is" "CS50"])

def yell(words):
    uppercase =[]
    for word in words:
        uppercased.append(word.upper())
        print(uppercase)
    
if __name__ == "__main__":
    main()



# not complete
def main():
    yell(["This", "is" "CS50"])

def yell(words):
    uppercase = list()
    for word in words:
        uppercased.append(word.upper())
    print(uppercase)
    
if __name__ == "__main__":
    main()



# not complete
def main():
    yell(["This", "is" "CS50"])

def yell(words):
    for word in words:
        print(word, end="")
    
if __name__ == "__main__":
    main()



def main():
    yell("This is CS50)")

def yell(phrase):
    print(phrase.upper())
    
if __name__ == "__main__":
    main()
'''