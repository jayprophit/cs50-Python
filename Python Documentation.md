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

python documentation library: https://docs.python.org/3/library/



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
It will finish the rest of the text input,
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


