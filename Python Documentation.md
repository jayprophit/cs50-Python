# Python



# cs50 - Introduction to Programming with Python - Full University Course

## Course Context

functions -
variables - 
conditionals - true or false
loops - repeated again and again set number of times
exceptions - except errors
libraries - 3rd party code or code you have written to be reused as many times as desired
unit test - write test to test your own code
file I/O - input/ out
regular expression - validate data or extract data
object-oriented programming:- allows you to represent real world entities
procedural programming - write procedures top to bottom to solve problems step by step
functional programming - 
et cetera

## python website documentation library:
https://docs.python.org/3/library/

## Youtube video link:
https://www.youtube.com/watch?v=nLRL_NcnK-4&t=1405s

## online course:
[edx.org online cs50 python full university course](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python?index=product&queryID=d261282de44491e46e7817fb335660b7&position=2&results_level=first-level-results&term=cs50&objectID=course-2cc794d0-316d-42f7-bbfd-25c34e4cd5df&campaign=CS50%27s+Introduction+to+Programming+with+Python&source=edX&product_category=course&placement_url=https%3A%2F%2Fwww.edx.org%2Fsearch)




# --SECTION 1--


## Single Line Comment
at the beginning of the line before any text input, 'number sign, hash, or pound sign' (#) is a comment, which allows you to leave notes that are reminders that are ignored by the programme


## Paragraph Comment
Three apostrophe's 'punctuation marks' (''' ''') or three Quotation marks (""" """) before and after your text, 
allows comment of a section of information, 
to leave notes that are reminders that are ignored by the programme 


## Python
is a program otherwise known as an interpreter.  
It converts the file into readable binary code a computer can understand,
then it changes the programme into readable human language


## Create New File
Using the terminal and typing 
code name.py
in the place of name, is where you put your file name
this allows you to create a new file


## Run/ Execute Python Code
Using the terminal and typing
python name.py
in the place of name, is where you put your file name
this will run your programme

## using the up arrow
is a quick way to recall a request command printed on the terminal


## Functions
a function is like an action or a verb,
that lets you do something in the programme.
generally any language comes with some predetermined set of functions.
the can be very basic actions or verbs, 
that the language will already know how to use.
as a programmer you can use the functions to get the computer to do those things

some functions take multiple arguments, 
if you separate the arguments to the function with a comma, 
you can pass in 1 or more arguments

e.g.
print("hello", + name)
print("hello, ", )

when you pass multiple arguments to print,
it automatically inserts a space for you


## Arguments
is an input to a function that somehow influences its's behaviour 

## Parameters ()
what you pass your argument inside to get an output

## Parentheses
arguments inside of the parameters

e.g.
(1 + 2)


## print()
Print is a function that use's parentheses, 
as an ability to take in some input of string of text data, 
in English or any other human language.
that you want this function to print onto the screen

[official Python documentation](https://docs.python.org/3/library/functions.html#print)

official documentation for:

print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

print(
    *                   - pass in zero to specified number of strings
    object              - is the string
    ,                   - is the separator
    sep=''              - separator is how many spaces.  default value is a single blank space
    ,                   - is the separator
    end='\n'            - new line, line ending specification
    ,                   - is the separator
    file=sys.stdout     - 
    ,                   - is the separator
    flush=False
)

Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.

## Speech Text that is visible and readable to the user is placed inside comma's ('text') or quotation marks ("text"),
as python accepts both, just remember to keep consistent when using a specific set when coding, 
as to not break code or confuse your self or some one else who may need to edit the code in the future


## Corner Case
quotations marks in side comma's

e.g.
print('hello, "friend"')
print("hello, \"friend\"")

## f - (means format)
before the quotation mark make it a special string
inside the parameters
print(f"hello,", {name})

## \n
is an escape character, also means new line, line ending

# Side Effects
when a function is executed. 
The program gives back an action from the commands given.
it can be:-
visual
audio


# Bugs
are mistakes that coders and programmers make, 
that causes errors in the programme
and its the coders and programmers job to fix theses problems
before, during and after programme launch.
Theses are just seen as problems that need to be solved, edited, rewritten, modified or simplified


## Return values
a feature of some of one or more functions, 
that returns values.

output = return value

e.g.
'''question = what's your name?'''
input = what's your name?

'''answer = John'''
output = John


## Variables
can store a value of some number, text, image, video or more.
a variable is a container for some value, 
inside of a computer or inside a programme that can be used or reused at any time


## input()
expects what's called a string, 
it's expecting text which is going to prompt the user

= sign means assignment operator
this means the programmer wants to assign from right to left

e.g.
name = input("What's your name? ")

the "input("what's your name? ")" is now stored in the word "name"
meaning any time the word name is called upon as a function,
it will display:-

what's your name?

## Concatenation - concatenates
to join the thing on the left and the thing on the right

e.g.
("hello + world")


## String - str()
a sequence of text be it English or any other human language, 
this is classed as data in programmes

[Python string documentation](https://docs.python.org/3/library/functions.html#func-str)

[Python string documentation](<https://docs.python.org/3/library/stdtypes.html#str>)

## .strip()
is a string extension
it is a method to remove white space, 
if a user inputs to many spaces it will reduce it by default off 1, 
or if you set a specific number like 2, it will reduce it to 2 white spaces

e.g.
name = name.strip()

## {} list - part: 1
allows you to store multiple pieces of data into a list, be it int or variable, 
to be recalled on command


## int - Integer
it represents a number, 
but not a decimal number

- +   - addition
- -   - subtraction
- *   - multiplication
- /   - division
- %   - modulo operator, it allows you to take the remainder after dividing one number by another


## Interactive Mode
you can start writing python code and immediately execute each of those lines interactively,
allowing the coder to execute some lines of code and get back some answers

using the terminal without any files open

you can process some lines of code to execute the code to instantly get a result

e.g.
1 + 1
print("hello, world)


## TAB
is used to indent inside code instead of multiple spaces.

if used in terminal.  
if you start typing the request command e.g. "cal TAB" (cal for the file ive named calculator).  
It will auto complete the rest of the text input,
as its recalling request memory, as a file you've already created and stored, as long as your saved file is located in the same file directory folder

e.g.
c:\Users\Python> cal(TAB)

'''finished input'''
c:\Users\Python> .\calculator.py

'''result'''
c:\Users\Python\calculator>

location: C drive
folder name: Users
folder name: Python
file name: calculator


## Nesting functions
means the return value of the inner function, 
becomes the argument to outer function

'''un-nested'''
input("what's x?)

'''nested'''
int(input("what's x? ))

this means that the input "whats x?" now equals or is represented by the function int


## float
is a number with a decimal point,
also know as a floating point value.

# [] square brackets
means an optional choice


# round - Rounding
you can round the number to the ndigit (nearest digit "integer") after the decimal point 

https://docs.python.org/3/library/functions.html#round

official documentation for:

round(number[, ndigits=None])

round(
    number          - represents 1 number
    [               - optional choice
    ndigits=None    - specify the number of digits e.g. you want the number 3.589068 rounded to 2 decimal point that would equal 3.59, if you don't specify it rounds to the nearest integer (number)
    ]               - optional choice
)


# Number break - 0,000.00 
to break a number up, so it has a comma in mathematics e.g. 1000 is 1,000
using the format principle and a list bracket {}

e.g.
print(f"{:,}")


# .2f
allows you to specify how many digits you want to print, e.g. 3.566789 into 3.56

e.g.
print(f"{:.2f,}")


# def - Define
allows you to invent or define your own function, 
specifying how you want to manipulate the function, 
allows you to stop repeating yourself again and again,

e.g.
def hello():
    print("hello")

'''ask user for their name'''
name = input("What's your name? ").strip().title()
hello()
'''say hello''
print(name)

you can also define a default value to some worlds by using parenthesis

e.g.
def hello(to="world"):

by default it makes the word to = world, without needing to use an argument

def main():
    inset argument
main()

by defining main() and closing with main, main can be any customized word e.g. house, car,
you can have your argument inside and it will run like a function but to a customized argument


## Scope
refer's to a variable only existing in the context in which you defined it

e.g.
'''with scope'''
def main():
    name = input("What's your name? ").strip().title()
    hello()  

def hello(to="world"):
    print("hello,", to)

main()

'''without scope'''
def main():
    name = input("What's your name? ").strip().title()
    hello()  

def hello():
    print("hello,", name)

main()

name doesn't exist in the hello function so can't be called


## return
it calls the input function to return a value string that the user typed in

e.g.
def main():
    x = int(input("what's x? "))

print("x squared is", square(x))

def square(n):
    return n * n

main()

square has been returned as a value after being called, 
raise a number to the value of another

e.g.
n ** 2
pow(n, 2)

this means ive raised n by the value of 2, raising the left side by the value of the right side



# --SECTION 2--


## Conditionals

built in syntax
>   - greater than
>=  - greater than or equal to
<   - less than
<=  - less than or equal to
==  - equal equal to - equality
!=  - not equal to


## Flow chart
a diagram that represent's the direction of the function,
also known as the control flow.
go left if the answer is true or go right if the answer is false

e.g.
follow the stages from start to stop, notice how many steps it function has!


## if
is a statement that represents

(view in code)
e.g.
if the answer to this question is true go ahead and execute this code

e.g.
0                        (start)
                            |
1              ----------(x < y)--------
            (true)                      |
2    (x is less than y)              (false)
3              |----------(x > y)--------|
                            |
               -------------|-----------
            (true)                      |
4    (x is greater than y)           (false)
5             |----------(x == y)-------|
                            |
               -------------|-----------
            (true)                      |
6    (x is equal to y)               (false)
7             |----------(stop)---------|


## elif
its a statement that is a conjunction  of else and if,
allow to ask a question that takes into account whether or not a previous question had a true or false answer

(view in code)
e.g.
0                                    (start)
                                        |
1          --------------------------(x < y)------------
          |                                             |
          |                                          (false)
2         |                             -------------(x > y)-------------------
          |                             |                                      |
        (true)                       (true)                                 (false)
3         |                             |                        -----------(x == y)-------
          |                             |                     (true)                        |
4   (x is less than y)      (x is greater than y)       (x is equal to y)               (false)
          |                             |                       |                          |
5         |--------------------------(stop)---------------------|--------------------------|


## else
is a statement that if the answer to the question is not true then lets just assume because its false  for example:- that x is equal to y

(view in code)
e.g.
0                                    (start)
                                        |
1          --------------------------(x < y)------------
          |                                             |
          |                                          (false)
2         |                             -------------(x > y)----
          |                             |                       |
        (true)                       (true)                     |
          |                             |                       |
          |                             |                     (false)
3   (x is less than y)      (x is greater than y)       (x is equal to y)
          |                             |                       |
4         |--------------------------(stop)---------------------|


## or
is x equal to y or not or is it true or false

(view in code)
e.g.
0                 (start)
                     |
1          -------(x < y)------
          |                    |
          |                 (false)
2         |         --------(x > y)----
          |        |                   |
        (true)  (true)                 |
          |        |                   |
          |        |                (false)
3   (x is not equal to y)       (x is equal to y)
              |                        |
4             |---------(stop)---------|


## !=  - not equal to
means its not equal to so just print
e.g. x is not equal to y

(view in code)
e.g.
0                  (start)
                      |
1          --------(x != y)---------
          |                        |
          |                        |
          |                        |
          |                        |
        (true)                  (false)
          |                        |
          |                        |
2   (x is not equal to y)   (x is equal to y)
          |                        |
3         |---------(stop)---------|

## ==  - equal equal to
means its equal equal to so just print
e.g. x is equal to y

(view in code)
e.g.
0                   (start)
                       |
1          ---------(x == y)-------
          |                        |
          |                        |
          |                        |
          |                        |
        (true)                  (false)
          |                        |
          |                        |
2   (x is equal to y)   (x is not equal to y)
          |                        |
3         |---------(stop)---------|


## and
means to ask, one or two or more questions


## bool - Boolean
they can only be True or False,
(has to have a capital for code input - True/ False)


## match - (also know as switch in other languages)
it uses a case argument
in a case argument -: = who?



# --Section 3--


## Loops

(view in code)
e.g.
0   (start)
       |
1   (meow)
       |
2   (meow)
       |
3   (meow)
       |
4   (stop)


## while
allows a question to be asked as a loop, 
that repeats again and again, 
as many times as you want


## Break out of infinite loop 
if stuck by accident
ctrl c (cancel, interrupt) in terminal window
(May very depending ong system software)

(view in code)
e.g.
0                   (start)
                       |
1                   (i = 3)
                       |
2          -------- (i != 0)-------
          |            |           |
          |            |           |
          |            |           |
          |            |           |
3       (true)      (False)        |
          |            |           |
          |            |           |
4       ("meow")     (stop)         |
          |                        |
5         |-------(i = i - 1)------|


when counting generally most scientist or programmers start from zero

(view in code)
e.g.
0                   (start)
                       |
1                   (i = 0)
                       |
2          ---------(i < 0)--------
          |            |           |
          |            |           |
          |            |           |
          |            |           |
3       (true)      (False)        |
          |            |           |
          |            |           |
4       ("meow")     (stop)        |
          |                        |
5         |--------(i += 1)--------|


## for
it allows you to iterate over a list of items


## [] list - pt: 2
allows you to contain multiple values all in the same place, all in the same variable.
the 1st item in a list starts at location zero

e.g.

shopping list equals, item one: location zero, item two: location one, item three: location two
shopping list = ["item1", "item 2", "item 3"]

item one    [0]
item two    [1]
item three  [2]

in a list when using loops call the variable by its name and don't use a place holder


e.g.

students = ["Hemione", "Harry", "Ron"]

for student in students:
    print(student)


## range
it returns to you a range of values, from at least one or more arguments,
this is a selection of values up to a specified value, 
not through the specified value

## _
use as a place holder, if its a variable but you not concerned about its name


## end=""
allows you to set the amount of spaces to reduce from the end


## len - length
tells you the length of a list


## dict - dictionary
a data structure that allows you to associate one value with another

e.g.
words with their definitions


## sep=", "
adds a separator, a separation with a comma


## None
this means the absents of a value


## end=""
allows you to end the line 


## nesting (notes)
you can use i, j, k
advised not to use any more as these letters are assigned to a function in python



# --Section 4--


## Exceptions

## Syntax error
is a problem that you have to solve and want resolve itself

## Run time error
this happens when you code is running.
as good practice coders write additional codes defensively to detect when the errors happen.  This is to prepare for the different varieties of code that will be input by different users correctly or incorrectly

## ValueError
this is an error with one of the input values

## try
try to see if this is exceptional code

## except
excepts a code regardless of the error

## NameError
your specified variable name has an error

## Pass
allows you to ignore/ pass on doing anything with it - meaning (don't print data)

## raise
allows you to raise exceptions yourself



# --Section 5--


## Libraries
are files that other people have written that you can use in your own program, or code that you yourself have written that you can use in your own program

## modules
are files with one or more functions built into it.
its to encourage reusability of code, meaning shorter work time and and the ability to share work

## random
its a modulator with pre programmed functions

[official Python documentation](https://docs.python.org/3/library/random.html)

### random.choice(seq)
module = random, function = choice, sequence = a list/ list like of string data

### random.randint(a, b)
randint - means random integer
module = random, function = randint, thats between a and b inclusive

e.g.

1-10
you will get a number back between one and ten and the numbers one and ten included.
this gives a 10% probability for each choice

### random.shuffle(x)
takes in a list of values and shuffle up the data into random order
module = random, function = shuffle, x - is the list of values

## import
allows you to import the entire contents of a module

## from
allows you to import parts of a functions from a module

## Statistics
has functions that are more mathematical in nature.  calculating means, modules or other aspects of a data set you may want to analyze

[official Python documentation](https://docs.python.org/3/library/statistics.html)

## command-line arguments
it allows to provide arguments that inputs to the program just when your executing at the command-line

## sys -system
contains functionality that specific to the python system itself

[official Python documentation](https://docs.python.org/3/library/sys.html)

a variable called argument vector.
the 1st element is the first thing you type the second element will be the second thing that you type. etc

sys.argv