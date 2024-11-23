'''
Print Hello 2
'''

def main():
    name = input("What's your name? ").strip().title()
    print(hello(name)) 

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code




def main():
    name = input("What's your name? ").strip().title()
    output  = hello(name)
    print(output)  



def main():
    name = input("What's your name? ").strip().title()
    hello(name) 



def hello(to="world"):
    print("hello,", to)
'''