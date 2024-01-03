'''
Name
'''


import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# starts at element 1 and everything else and removes last entry
for arg in sys.argv[1:-1]:
    print("hello, my name is" , arg)



'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# starts at element 1 and everything else
for arg in sys.argv[1:]:
    print("hello, my name is" , arg)




import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# calls the argument arg
for arg in sys.argv:
    print("hello, my name is" , arg)




import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
   sys.exit("Too many arguments")

# print name tags
print("hello, my name is" , sys.argv[1])




import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
   sys.exit("Too many arguments")

# print name tags
print("hello, my name is" , sys.argv[1])




import sys

# check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

# print name tags
print("hello, my name is" , sys.argv[1])




import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is" , sys.argv[1])



import sys

if len(sys.argv) < 2:
    # an error made by the coder for not completing the code matrix of using two double quotes
    print("Too few arguments)
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is" , sys.argv[1])



import sys

try:
    print("hello, my name is" , sys.argv[1])
except IndexError:
    print("Too few arguments")



import sys

# print the argument, name of file, no prompt
print("hello, my name is" , sys.argv[0])


# imports function called system
import sys

# print the argument, name of file, prompt
print("hello, my name is" , sys.argv[1])
'''