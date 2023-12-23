'''
Mario
'''


# print bricks in a row
def main():
    print_square(3)


def print_square(size):
        for i in range(size):  
            print_row(size)

def print_row(width):
    print("#" * width)

main()

'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



# print bricks in a row
def main():
    print_square(3)


def print_square(size):
        for i in range(size):  
            print("#" * size)

main()



# print bricks in a row
def main():
    print_square(3)


def print_square(size):
    
    #for each row in square
    for i in range(size):
        
        # for each brick in row
        for j in range(size):
            
            # print brick
            print("#", end="")
            
        # prints a new line (\n)   
        print()

main()



# print bricks in a row
def main():
    print_row(4)


def print_row(width):
    print("?" * width)

main()



# print bricks in a column
def main():
    print_column(3)
    
def print_column(height):
        print("#\n" * height,end="" )

main()



# print bricks
def main():
    print_column(3)
    
def print_column(height):
    for _ in range(height):
        print("#")

main()



# print bricks
for _ in range(3):
    print("#")



# print bricks
print("#")
print("#")
print("#")
'''