'''
Print Hello 2
'''

def main():
    name = input("What's your name? ").strip().title()
    hello()  

def hello(to="world"):
    print("hello,", to)

if __name__ == "__main__":
    main()


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

'''