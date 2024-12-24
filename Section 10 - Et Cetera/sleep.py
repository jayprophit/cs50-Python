'''
sleep
'''


def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()

'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code


def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()



def main():
    n = int(input("what's n? "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return "🐑" * n

if __name__ == "__main__":
    main()



def main():
    n = int(input("what's n? "))
    for i in range(n):
        print("🐑" * i)

if __name__ == "__main__":
    main()



n = int(input("what's n? "))
for i in range(n):
    print("🐑" * i)
'''