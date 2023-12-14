Python



cs50 - Introduction to Programming with Python - Full University Course

Course Context

functions -
varaibes - 
conditionals - true or false
loops - repeated again and again set number of times
exceptions - except errors
libraries - 3rd party code or code you have writen to be reused as many times as desired
unit test - write test to test your own code
file i/o - input/ out
regular expression - validate data or extract data
object-oriented programming:- allows you to represent real world entities
procedural programming - write procedures top to bottom to solve problems step by step
functinal programming - 
et cetera

python website documentation library: https://docs.python.org/3/library/

Youtube video link: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=1405s

online course: https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python?index=product&queryID=d261282de44491e46e7817fb335660b7&position=2&results_level=first-level-results&term=cs50&objectID=course-2cc794d0-316d-42f7-bbfd-25c34e4cd5df&campaign=CS50%27s+Introduction+to+Programming+with+Python&source=edX&product_category=course&placement_url=https%3A%2F%2Fwww.edx.org%2Fsearch




SECTION 1

# Sinlgle Line Comment - 'number sign, hash, or pound sign' (#) is a comment, which allows you to leave notes that are reminders that are ignored by the programme


Paragraph Commnet
Three apostrophe's 'punctuation marks' (''' ''') or three Quotation marks (""" """) before and after your text, 
allows comment of a section of information, 
to leave notes that are reminders that are ignored by the programme 


Python is a program otherwise known as an interperator.  
It converts the file into readable binary code a computer can understand,
then it changes the programme into readable human language


Create New File
Using the terminal and typing 
code name.py
in the place of name, is where you put your file name
this allows you to create a new file


Run/ Exicute Python Code
Using the terminal and typing
python name.py
in the place of name, is where you put your file name
this will run your programme

using the up arrow
is a quick way to recall a request command printed on the terminal


Functions
a function is like an action or a verb,
that lets you do something in the programme.
generally any language comes with some predetermined set of functions.
the can be very basic actions or verbs, 
that the language will already know how to use.
as a programmer you can use the functions to get the computer to do those things

some functions take multiple arguments, 
if you seperate the arguments to the function with a comma, 
you can pass in 1 or more arguments

e.g.
print("hello", + name)
print("hello, ", )

when you pass multiple arguments to print,
it automatically inserts a space for you


Arguements
is an input to a function that somehow influences its's behavior 

Parameters ()
what you pass your argument inside to get an output

Parentheses
arguments inside of the parameters

e.g.
(1 + 2)


print()
Print is a function that use's parentheses, 
as an ability to take in some input of string of text data, 
in english or any other human language.
that you want this function to print onto the screen

https://docs.python.org/3/library/functions.html#print

official documentation for:

print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

print(
    *                   - pass in zero to specified number of strings
    object              - is the string
    ,                   - is the seperator
    sep=''              - seperator is how many spaces.  default value is a single blank space
    ,                   - is the seperator
    end='\n'            - new line, line ending specification
    ,                   - is the seperator
    file=sys.stdout     - 
    ,                   - is the seperator
    flush=False
)

Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.

Speech Text that is visible and reable to the user is placed inside comma's ('text') or quotation marks ("text"),
as python accepts both,
just remember to keep consistant when using a specific se when coding, 
as to not break code or confuse your self or some one else who may need to eidt the code in the future


Corner Case
quotations marks in side comma's

e.g.
print('hello, "friend"')
print("hello, \"friend\"")

f - (means format)
before the quotation mark make it a special string
inside the parameters
print(f"hello,", {name})

\n
is an escape character, also means new line

Side Effects
when a function is exicuterd. 
The program gives back an action from the commands given.
it can be:-

visual
audio


Bugs
are mistakes that coders and progammers make, 
that causes errors in the programme
and its the coders and progammers job to fix theses problems
before, during and after programme launch.
Theses are just seen as problems that need to be solved, edited, rewritten, modified or simplified


Retrun values
a feature of some of one or more funtions, 
that returns values.

output = return value

e.g.
# question = what's your name?
input = what's your name?

# answer = John
output = John


Variables
can store a value of some number, text, image, video or more.
a variable is a container for some value, 
inside of a computer or inside a programme that can be used or reused at any time


input()
exspects what's called a string, 
it's exspecting text which is going to prompt the user

= sign means assignment operator
this means the programmer wants to asign from right to left

e.g.
name = input("What's your name? ")

the "input("what's your name? ")" is now stored in the word "name"
meaning any time the word name is called upon as a function,
it will display:-

what's your name?

Concatenation - concatenates
to join the thing on the left and the thing on the right

e.g.
("hello + world")


String - str()
a sequence of text be it english or any other human language, 
this is classed as data in programmes

https://docs.python.org/3/library/functions.html#func-str

https://docs.python.org/3/library/stdtypes.html#str

.strip()
is a string extension
it is a method to remove white space, 
if a user inputs to many spaces it will reduce it by default off 1, 
or if you set a specific number like 2, it will reduce it to 2 whitespsaces

e.g.
name = name.strip()

{} list
allows you to store multiple pieces of data into a list, be int int or variable, 
to be recalled on command


int - Integer
it represents a number, 
but not a decimal number

+   - addition
-   - subtraction
*   - multiplication
/   - division
%   - modulo operator, it allows you to take the remainder after dividing one number by another


Interactive Mode
you can start writing python code and immediately execute each of those lines interactively,
allowing the coder to excute some lines of code and get back some answers

using the termianl without any files open

you can process some lines of code to excute the code to instatly get a result

e.g.
1 + 1
print("hello, world)


TAB
is used to indent inside code instead of multiple spaces.

if used in terminal.  
if you start typing the request command e.g. "cal TAB" (cal for the file ive named calculator).  
It will auto complete the rest of the text input,
as its recalling request memory, as a file you've already created and stored, as long as your saved file is located in the same file directory folder

e.g.
c:\Users\Python> cal(TAB)

# finished input
c:\Users\Python> .\calculator.py

# result
c:\Users\Python\calculator>

location: C drive
folder name: Users
folder name: Python
file name: calculator


Nesting functions
means the return value of the inner function, 
becomes the argument to outer function

# un-nested
input("what's x?)

# nested
int(input("what's x? ))

this means that the input "whats x?" now equals or is represented by the function int


float
is a number with a decimal point,
also know as a floating point value.

[] square brackets
means an optional choice


round - Rounding
you can round the number to the ndigit (nearest digit "integer") after the decimal point 

https://docs.python.org/3/library/functions.html#round

official documentation for:

round(number[, ndigits=None])

round(
    number          - represents 1 number
    [               - optional choice
    ndigits=None    - specify the number of digits e'g' you want the number 3.589068 rounded to 2 decimal point that would equal 3.59, if you dont specify it rounds to the nearest integer (number)
    ]               - optional choice
)


Number break - 0,000.00 
to break a number up, so it has a comma in mathmatics e.g. 1000 is 1,000
using the format principle and a list bracket {}

e.g.
print(f"{:,}")


.2f
allows you to specify how many digits you want to print, e.g. 3.566789 into 3.56

e.g.
print(f"{:.2f,}")


def - Define
allows you to invent or define your own function, 
specifying how you want to maniulate the function, 
allows you to stop repeating yourself again and again,

e.g.
def hello()    
    print("hello")

# ask user for their name
name = input("What's your name? ").strip().title()
hello()
# say hello
print(name)

you can also deine a default value to some worlds by using paranthaeses

e.g.
def hello(to="world")

by default it makes the word to = world, without needing to use an argument

def main()
    inset argument
main()

by defining main() and closing with main, main can be any customized word e.g. house, car,
you can have your argument inside and it will run like a function but to a customized argument


Scope
refer's to a variable only existing in the context in which you defined it

e.g.
# with scope
def main()
    name = input("What's your name? ").strip().title()
    hello()  

def hello(to="world")
    print("hello,", to)

main()

# without scope
def main()
    name = input("What's your name? ").strip().title()
    hello()  

def hello()
    print("hello,", name)

main()

name dosen't exsit in the hello function so can't be called


return
it calls the input function to return a value string that the user typed in

e.g.
def main()
    x = int(input("what's x? "))

print("x squared is", square(x))

def square(n):
    return n * n

main()

square has been returned as a value after being called


Raise a number to the value of another

e.g.
n ** 2
pow(n, 2)

this means ive raised n by the value of 2, raising the left side by the value of the right side



SECTION 2


