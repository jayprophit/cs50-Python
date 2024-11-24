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

[Python string documentation](https://docs.python.org/3/library/functions.html#round)

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



# --SECTION 3--


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



# --SECTION 4--


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



# --SECTION 5--


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

when passing through a prompt, you can put it in double quotes at the terminal window to except the argument as long as the in the code the allows it

e.g.

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is" , sys.argv[1])

at the terminal window:
python name.py "Jonathan Powell"

exits the program at the specified location, then are there

sys.exit


## IndexError
this tells the user that your prompt (list selection) is to far out of range.  this means to far to the left or to far to the right in this object which is a list of some values.

## slices
takes a sub-set of a list (a slice of a list)

e.g.

Example 1
import sys

check for errors

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

starts at element 1 and everything else

for arg in sys.argv[1:]:
    print("hello, my name is" , arg)


Example 2
import sys

check for errors

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

starts at element 1 and everything else and removes last entry

for arg in sys.argv[1:-1]:
    print("hello, my name is" , arg)


## Packages
3rd party library which is a module implemented in a folder of functions that you yourself or other people have created

## PyPi
is the python package index website, that allows you to download and install a package on your computer or server or upload a package you create for others to use

[official Python package index](https://pypi.org)

## cowsay
is a package in python that allows a cow to say something on your screen

[official Python package index](https://pypi.org/project/cowsay)

## pip
is a package manager.  install packages into your Mac, PC, Linux, Cloud environment or IDE (integrated development environment)

e.g.

pip install cowsay

## ASCII - art
is olden styled textual way of using keys on the keyboard to print pictures of sort on a screen

## APIs
application programming interface.
third party services that anyone can talk to.

## requests
allows the user to make web requests, allowing the user to automate the requests of URL's that stat with http or https

pip install requests

[official Python package index](https://pypi.org/requests)


### Itunes Exercise

https://itunes.apple.com/search?entity=song&limit=1&term=weezer

https://itunes.apple.com - is the website

search? - is the request made on the website server

entity=song - so that its songs is not artists or albums or something like that

limit=1 - this is to get back information on one song

term=weezer - this is the band or the artist that is requested

this gives you will give you a text file

{
 "resultCount":1,
 "results": [
{"wrapperType":"track", "kind":"song", "artistId":115234, "collectionId":1440878798, "trackId":1440879325, "artistName":"Weezer", "collectionName":"Weezer", "trackName":"Buddy Holly", "collectionCensoredName":"Weezer", "trackCensoredName":"Buddy Holly", "artistViewUrl":"https://music.apple.com/us/artist/weezer/115234?uo=4", "collectionViewUrl":"https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4", "trackViewUrl":"https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4",
"previewUrl":"https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/f0/ba/a8/f0baa81a-7449-c490-f43a-b5c6e3609e3f/mzaf_3988310882581261442.plus.aac.p.m4a", "artworkUrl30":"https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/30x30bb.jpg", "artworkUrl60":"https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/60x60bb.jpg", "artworkUrl100":"https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/100x100bb.jpg", "collectionPrice":10.99, "trackPrice":1.29, "releaseDate":"1994-01-01T12:00:00Z", "collectionExplicitness":"notExplicit", "trackExplicitness":"notExplicit", "discCount":1, "discNumber":1, "trackCount":10, "trackNumber":4, "trackTimeMillis":159587, "country":"USA", "currency":"USD", "primaryGenreName":"Pop", "isStreamable":true}]
}

this text format is known as 'json'

## JSON
javaScript object notation.
known as a 'language agnostic format' for exchanging data between computers.  this isn't limit to python.  you can use any other language to read json or write it as well.
its completely text based format.  meaning if i visit a url in a browser, what gets downloaded is just a bunch of text, but that text is formatted in a standard way using curly braces and square brackets, using quotes and some colons, that contains all of the information on apple's data base on Weezer's song at the first one as the selection was limited to one in their database.
thats using an API, a mechanism where the user can access some data on someone else's server and then integrate it into the user's own program.
as the web browser is not something that is written by the user.  the user will need a code to interact with the text format provide,

[Python string documentation](https://docs.python.org/3/library/json.html)

json.dumps - dump string,
this means to pass that function that response.json return value

## indent=
indents the data by the specified number of spaces

## __name__
automatically set by python to be main when you run a file from the command line

e.g.

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__name__":
    main()

name - becomes main



# --SECTION 6--

## Unit Tests

## assert
allows you to claim (assert) that something is true, if its not true it will show an error

## AssertionError
shows that theres an error wile using the assert command

## pytest
is a 3rd party program  tool that will automate the testing of your code, as long as the coder/ programmer write's the test

note - there are other unit testing programs available on python

[official Pytest package index](https://pytest.org)


running pytest on multiple folders

in terminal:-

pytest test

## mkdir
makes a new folder

## __init__.py
tells python to treat the specified folder not as a module but as a package

## package
is a python module or multiple modules that are organized inside of a folder



# --SECTION 7--

# File I/O
is the input and output of files.

## {} list - part: 3
list are stored in the computers memory, so once the program exits even the contents of those disappear

## open
open a file, allows the user to read information from it or write information to it

[official Python library](https://docs.python.org/3/library/functions.html#open)

## rm
in terminal if you input
rm (name) it will delete the file

e.g.

rm names.txt

## with
with open allows you to write and close a file

e.g.

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


## line
allows you to read files, stores them in a variable called line and return them as a list

e.g.

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)


## .rstrip
allows you to strip of the end of an implement detail in the line

e.g.

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

## append
sorts the file in alphabetical ascending order

e.g.

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

[official Python library](https://docs.python.org/3/library/functions.html#sorted)


summary:-

sorted(iterable, /, *, key=None, reverse=False)

to have descending order

you change it to:-

sorted(iterable, /, *, key=None, reverse=True)


## csv
 stands for - comma separated value, which is a file format, that allows you to store multiple pieces of information that are related in the same file

 you can import your csv file into spreadsheet software
 like:-

 excel
 apple number
 google spreadsheet

 [official Python library](https://docs.python.org/3/library/csv.html)


 ## .split
 the split function will split the pice of information into 1 or more pieces of data

 ## row
 it allows you to look at lines as rows, each part separated by comma's as columns

 ## key
 tells sorted function how to sort the specified list of dictionary.  you can also pass an anonymous function, which is called lambda which can be seen in example 3.

 e.g. #1

 def get_name(student):
    return student["name"]

for student in sorted (students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

e.g. #2

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]


for student in sorted (students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")

e.g. #3

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]

for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

## reader
it can be used to iterate over files, meaning it sorts where the quotes, corner cases, etc and will automatically sort them for you, you can override certain defaults or functions

e.g.

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


## DictReader - dictionary reader
is a function for csv that allows you to iterate over the file, top to bottom, loading in each line of text not as a list of columns but as a dictionary of columns, this gives automatic access yto those columns names

## writer
allows you to open and write a file

e.g.

import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

## DictWriter

allows you to open and write a file as a dictionary, it needs an extra function called fieldname that helps to define which column belongs to which group

e.g.

import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


## fieldname
is a string name given to the column you intend to write to in that file.  it ensures that the library knows which column has been given its name or tiles respectively


## binary files
allows you to store multiple keys and multiple values.  binary files are just zero's and one's (0, 1) and can be laid out in any pattern you want. this is not just restricted to text information but iyt can be graphical, audio or video information as well

## PIL
it allows you to apply filters, animation.
[official pillow library](https://pillow.readthedocs.io)

the pillow library takes care of opening, the saving and closing by just calling save

e.g.

import sys

from PIL import image

images = []

for arg in sys.argv:
    image = Image.open(arg)
    images.append(image)

images[0].save

to animate in the terminal window you call the command

e.g.

python costumes.py costume1.gif costume2.gif

to get the final gif in the terminal window you type

e.g.

code costumes.gif


## animated gif
this can be memes, stickers.  it is an image file that has multiple layers inside it.  the computer shows the images one after another sometimes on an endless loop. as long as theres enough images it creates the illusion of animation, as the observer is only seeing 1 frame per second it looks like an animation.  it can be seen as a simplistic version of a video file


## scratch
a programming language from MIT that allows you to animate images and more



# --SECTION 8--

# Regular Expressions
also known as a regex's.  is just a pattern in a code

## re
which stands for regular expressions, is a library.  the library gives a lot of capabilities to define, check for and even replace patterns and extract data from these patterns.

[official Python library](https://docs.python.org/3/library/re.html)

re.search(pattern, string, flags=0)

there are certain symbols which you can use to define patterns

e.g.

.           any character except a newline
*           0 or more repetitions
+           1 or more repetitions
?           0 or 1 repetitions
{m}         m repetitions
{m,n}       m-n repetitions
^           matches the start of the string
$           matches the end of the string or just before the newline at the end of the string
[]          set of characters
[^]         complementing the set - (you cannot match any of these characters)

it searches and finds a result using a finite state machine or formally known as non-deterministic finite automaton

e.g. v1

".*@.*"

start--> q1 --@-- q2

q1: its starts in a so called start state is the condition in which it begins (in the 1st state which has a curved edge meaning a reflexive Edge and its labeled dot [because dot means any character] it will follow these transitions as follows from left to right through single characters using the prompt input [name])

q2: then it reads the users email address from left to right, then it decides whether or no to stay in this 1st stat or transition to the next state (then it will follow through to the 2nd state as theres an @ sign [@email.com] and read the following in character order.  it has double circles one inside the other meaning if the computer finds its self in that 2nd accept state after reading all the users prompt input.  it means its a valid address)

q1: if by some chance it ends up in the 1st circle which dose not have double circles which is not an accept state.  the computer will conclude this is an invalid email address

e.g. v2

".+@.+"

start--> q1 --.-- q2 --@-- q3 --.-- q4

q1: can consume any one character

q2: can consume more characters before the @ sign

q3: can consume at least one more character because recall Rex has dot plus this time

q4: then we can consume even more characters if we want

(one your at state 4 your at an accept state, [as it has 2 circles in total] so if the computer finds its self in the 4th state then it is a valid email address)

if it dose not make it to the 4th state then it means the email address is Invalid

you can use "\." to to match on a dot or period

### r

use r before te r".+@.+\.com" to define that the "\." is used as a dot or period

this is similar to python using f as a format string in a certain way plugging in variables between curly braces.
In this case r represents a raw string i want passed through exactly as is

# \w
represents a "word character", commonly known as an alpha numeric symbol or the underscore

here are some other examples of input using backslash

e.g.

\d          decimal digit
\D          not a decimal digit
\s          whitespace characters
\S          not a whitespace character
\w          word character ... as well as numbers and the underscore
\W          not a word character

A|B         either A or B
(...)       a group
(?:...)     non-capturing version

# flags

re.IGNORECASE
re.MULTILINE
re.DOTALL


regular expression use case:

^[a-zA-Z0-9.!#$%&'*+\/=?^_'{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

re.match(pattern, string, flags=0)

re.match automatically starts matching from the start of the string

re.fullmatch(pattern, string, flags=0)

re.fullmatch starts matching at the start and end of the string

# :=
also known as the walrus operator, it allows you to sign assign a value from right to left and ask a boolean question about it.

# ignoring conditions
you can ignore some statements if they meet the conditions.  by using these methods:-

.replace() - replaces the statement with the the defined condition

.removeprefix() - removes the part that is defined by the statement

# re.sub
re.sub(pattern, repl, string, count=0, flags=0)

is a way to substatue outcode or sections of imformation that would normally be required, that now ignores or skips past some information

# re.split
re.split(pattern, string, maxplit=0, flag=0)

allows the user to split a string by usings not a specific character or characters, comma or a space but multiple characters aswell

# re.findall
re.findall(pattern, string, flag=0)

allows the user to search for multiuple copys of the same pattern in different places in a string 



# --SECTION 9--

# Object-Oriented Programming
also known as OOP 

## tuple
is type of data that is a collection of values, it's similar to a list but its immutable, not mutable - meaning you can not change the value.  that means a list is something you can change the values of but a tuple returns multiple values just by using a comma.  it returnsmultiple values as 1 value which is a tuple, and inside of that values is multiple values

e.g.

e,y
(x,z)

to return data that has been modified you must put the condition inside a [] instead of a of nothing or ()

e.g.
["name"]

you index into list's and tuples usings numbers, but you index into dictionaries using strings

# classes
a class is a blueprint for pieces of data or objects.  its a mold that can be defined and given a name.  when you use the mold or blueprint, you get types of data designed exactly as you want.
classes allow you to invent you own type of data types and give them a name

[official Python library](https://docs.python.org/3/tutorial/classes.html)

# class
allows you to define custom containers with custom names for pieces of data

# objects
any time you use a class you're creating an object as in OOP - object oriented programming.  the object is the incarnation of or technically instantiation of.  another term for object is instance, yoyu have instances of classes aswell

# attributes
any thing that is created which is the properties of or the attributes of

e.g.
name
house

# instance variables
also another technical name for attributes

# methods
classes come with certain methods or functions inside of them that can be defiend and will behave in a special way.  these functions allow yoy to determine behavour in a standard way known as special methods

# __init__
also known as Dunder init method is specifically known as an instance method.
if you want to initialize the contents of an object  from a class you define this method

this is known as adding vairbles to objects

a constructor call is data that will contruct the data object using synoyms. meaning instantiate the data object for the user, by using the class as a template to mold, so that all the data is structured the same.

e.g. they have names and houses

due to being customizable from being a class it allows you to modify the contents of that object

# self
gives you access to the current object that was just created

e.g.

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

# __new__
creates a new function for you

# raise
allows you to raise value errors, or create exception of an error

# __str__
this is also a special method, this is used when another function wants to see your object as a string
this is generally ment for users of the program, to be user friendly

# repr
is ment for developers which gives access to more information, it will provides the data on what type of object it is

# properties
is an attribute that has even more defences mechanisms put into place.  a little more functionality to prevent programmers messing things up

@property

# decorators
is a term of art, they are functions that modify the behavour of other functions

# int
int is a class and can be passed back an object called int

class int(x, base=10)

# str
str is a class and can be passed back as an object

class str(object='')

this is a method
str.lower()

this is a class
str.strip([chars])

# list
list is a class and can be passed back as an object

class list([iterable])

this is a method
list.append(x)

# dict
dict is a class and can be passed back as an object

# class methods
an instances or an object of a class that dosent have a special function but function stays the same no matter its use case

@classmethod

# random.choice
gives ramdom sorting