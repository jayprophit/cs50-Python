Here is the rewritten and formatted version of the provided section, designed for a coursework-oriented GitHub book:

---

# Python Programming Guide  

## CS50: Introduction to Programming with Python  
**Course Type**: Full University Course  

### Course Topics  
- **Functions**: Perform specific tasks within the program.  
- **Variables**: Store values for later use.  
- **Conditionals**: Execute code based on conditions (true or false).  
- **Loops**: Repeat actions for a set number of times.  
- **Exceptions**: Handle errors gracefully.  
- **Libraries**: Reusable code modules (third-party or custom).  
- **Unit Tests**: Validate code functionality through tests.  
- **File I/O**: Handle input/output operations on files.  
- **Regular Expressions**: Validate or extract data patterns.  
- **Object-Oriented Programming (OOP)**: Model real-world entities.  
- **Procedural Programming**: Solve problems step-by-step.  
- **Functional Programming**: Use functions as primary building blocks.  

### Resources  
- **Python Documentation**: [Official Python Library](https://docs.python.org/3/library/)  
- **YouTube Lecture**: [CS50 Python Course Video](https://www.youtube.com/watch?v=nLRL_NcnK-4&t=1405s)  
- **Online Course**: [CS50 Python on edX](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python)  

---

## --Section 1--: Basics of Python  

### Comments  
- **Single-Line Comments**: Use `#` at the beginning of a line to write notes ignored by the program.  
  Example:  
  ```python  
  # This is a single-line comment  
  ```  

- **Multi-Line Comments**: Use triple quotes (`'''` or `"""`) to write longer notes ignored by the program.  
  Example:  
  ```python  
  '''  
  This is a multi-line comment.  
  It spans multiple lines.  
  '''  
  ```  

### Python as an Interpreter  
Python is an interpreter that converts code into machine-readable binary and translates it into human-readable output.  

### File Operations  
- **Create a New File**: Use the terminal command:  
  ```bash  
  code name.py  
  ```  
  Replace `name` with your desired filename.  
- **Run/Execute Python Code**: Use the terminal command:  
  ```bash  
  python name.py  
  ```  
  Replace `name` with your filename.  

- **Quick Command Recall**: Use the up arrow in the terminal to quickly recall previous commands.  

---

### Functions  
A function is an action or verb that performs specific tasks. Functions can take arguments (inputs) and return outputs.  

- **Syntax**:  
  ```python  
  def function_name(parameters):  
      # code block  
      return output  
  ```  

- **Example**:  
  ```python  
  def greet(name):  
      print(f"Hello, {name}!")  
  greet("Alice")  
  ```  

- **Arguments and Parameters**:  
  - **Arguments**: Inputs passed to functions.  
  - **Parameters**: Variables inside the function that receive the arguments.  

---

### The `print()` Function  
The `print()` function displays output on the screen.  

- **Syntax**:  
  ```python  
  print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)  
  ```  
  - `sep`: Separator (default is a space).  
  - `end`: End of the printed line (default is a newline).  

- **Examples**:  
  ```python  
  print("Hello, World!")  
  print("Hello,", "World!", sep="-", end="!!\n")  
  ```  

### Strings  
- **Definition**: A sequence of text, such as `"Hello"` or `'World'`.  
- **Escape Characters**:  
  - `\n`: Newline.  
  - `\"`: Double quote inside a string.  
  - **Example**:  
    ```python  
    print("He said, \"Hello!\"")  
    ```  

- **Concatenation**: Join strings using `+`.  
  Example:  
  ```python  
  greeting = "Hello" + " " + "World"  
  print(greeting)  
  ```  

---

### Variables  
Variables store values like numbers, text, or other data.  

- **Syntax**:  
  ```python  
  variable_name = value  
  ```  
  Example:  
  ```python  
  name = "Alice"  
  age = 25  
  ```  

---

### Input and Output  
- **Input**: Use `input()` to get user input.  
  Example:  
  ```python  
  name = input("What's your name? ")  
  print(f"Hello, {name}!")  
  ```  

- **Return Values**: Functions can return values using the `return` keyword.  
  Example:  
  ```python  
  def square(x):  
      return x * x  
  result = square(5)  
  print(result)  
  ```  

---

### Numeric Operations  
- **Integers (`int`)**: Whole numbers.  
- **Floating Point Numbers (`float`)**: Numbers with decimals.  
- **Operators**:  
  - `+` (Addition)  
  - `-` (Subtraction)  
  - `*` (Multiplication)  
  - `/` (Division)  
  - `%` (Modulo)  

---

### Formatting Numbers  
- **Rounding**:  
  ```python  
  print(round(3.5678, 2))  # Output: 3.57  
  ```  

- **Comma Separator**:  
  ```python  
  print(f"{1000:,}")  # Output: 1,000  
  ```  

- **Decimal Precision**:  
  ```python  
  print(f"{3.5678:.2f}")  # Output: 3.57  
  ```  

---

### Defining Functions (`def`)  
- **Syntax**:  
  ```python  
  def function_name(parameters):  
      # Code block  
  ```  
- **Example**:  
  ```python  
  def greet(name="World"):  
      print(f"Hello, {name}!")  
  greet()  
  greet("Alice")  
  ```  

---




# --SECTION 2--: Conditionals  

## **Conditionals**  
### Built-in Syntax  
| Symbol | Description                     | Example               | Meaning                          |
|--------|---------------------------------|-----------------------|----------------------------------|
| `>`    | Greater than                   | `x > y`               | `x` is greater than `y`         |
| `>=`   | Greater than or equal to       | `x >= y`              | `x` is greater than or equal to `y` |
| `<`    | Less than                      | `x < y`               | `x` is less than `y`            |
| `<=`   | Less than or equal to          | `x <= y`              | `x` is less than or equal to `y` |
| `==`   | Equal to (equality)            | `x == y`              | `x` is equal to `y`             |
| `!=`   | Not equal to                   | `x != y`              | `x` is not equal to `y`         |

---

## **Flow Chart**  
A flow chart is a diagram that represents the direction or control flow of a function.  
- Follow steps from **start** to **stop** to understand how the function operates.  

### Example Flow:  
```plaintext
0 (Start)
  |
1 ----------(x < y)----------
   (True)                 (False)
   |                      |
2 (x is less than y)      ----------(x > y)----------
                          (True)                 (False)
                          |                      |
3               (x is greater than y)    (x is equal to y)
                          |                      |
4                       (Stop)                (Stop)
```

---

## **`if` Statement**  
The `if` statement allows the program to execute a block of code only if a specified condition is **true**.  

### Code Example:  
```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

---

## **`elif` Statement**  
The `elif` statement is a combination of `else` and `if`. It allows checking multiple conditions in sequence.  

### Example Flow:  
```plaintext
0 (Start)
  |
1 -------(x < y)---------
   |                    |
(True)              (False)
   |                    |
(x is less than y)   -------(x > y)-------
                       |                |
                    (True)           (False)
                      |                |
          (x is greater than y)   (x is equal to y)
                      |                |
                   (Stop)            (Stop)
```

---

## **`else` Statement**  
The `else` statement executes a block of code when all previous conditions are **false**.  

### Example Flow:  
```plaintext
0 (Start)
  |
1 -------(x < y)---------
   |                    |
(True)              (False)
   |                    |
(x is less than y)   -------(x > y)----
                       |             |
                    (True)        (False)
                      |             |
      (x is greater than y)  (x is equal to y)
                      |             |
                   (Stop)         (Stop)
```

---

## **Logical Operators**  
- **`or`**: At least one condition must be **true**.  
- **`and`**: All conditions must be **true**.  

### Example:  
```python
if x < y or x == y:
    print("Condition met")
if x > y and y > 0:
    print("Both conditions are true")
```

---

## **Boolean (bool)**  
A Boolean value can only be **True** or **False**.  
> **Note:** Always capitalize `True` and `False` in Python.  

### Example:  
```python
is_greater = x > y  # Returns True or False
```

---

## **`match` Statement**  
The `match` statement, also known as a `switch` in other languages, evaluates an expression and executes a case that matches the value.  

### Code Example:  
```python
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case _:
        print("x is something else")
```


# --SECTION 3--: Loops 

## **Loops**  
Loops allow you to repeat a block of code multiple times, either a fixed number of times or until a specific condition is met.  

### Example Flow:  
```plaintext
0   (Start)
    |
1   (Meow)
    |
2   (Meow)
    |
3   (Meow)
    |
4   (Stop)
```

---

## **`while` Loop**  
The `while` loop repeatedly executes a block of code as long as the given condition is **true**.  

### Code Example:  
```python
i = 3
while i != 0:
    print("Meow")
    i -= 1  # Decrement `i` to avoid an infinite loop
```

### Flow Diagram:  
```plaintext
0                   (Start)
                       |
1                   (i = 3)
                       |
2          -------- (i != 0)-------
          |            |           |
        (True)      (False)        |
          |            |           |
3       ("Meow")     (Stop)        |
          |                        |
4         |-------(i = i - 1)------|
```

> **Tip:**  
If you accidentally create an **infinite loop**, press **`Ctrl + C`** to interrupt it (may vary depending on your system).  

---

## **Counting with `while`**  
Counting typically starts at zero in programming.  

### Code Example:  
```python
i = 0
while i < 3:
    print("Meow")
    i += 1
```

### Flow Diagram:  
```plaintext
0                   (Start)
                       |
1                   (i = 0)
                       |
2          ---------(i < 3)--------
          |            |           |
        (True)      (False)        |
          |                        |
3       ("Meow")     (Stop)        |
          |                        |
4         |--------(i += 1)--------|
```

---

## **`for` Loop**  
The `for` loop iterates over a sequence (e.g., list, range, etc.).  

### Example with a List:  
```python
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)
```

---

## **Lists (`[]`)**  
A list allows you to store multiple values in a single variable.  
- The first item in a list is at index `0`.  

### Example:  
```python
shopping_list = ["item1", "item2", "item3"]
print(shopping_list[0])  # Output: item1
```

### Iterating through a List:  
```python
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)
```

---

## **`range`**  
The `range` function generates a sequence of numbers up to (but not including) a specified value.  

### Example:  
```python
for i in range(3):
    print(i)  # Output: 0, 1, 2
```

---

## **Placeholders (`_`)**  
Use `_` as a placeholder when the variable is not important.  

### Example:  
```python
for _ in range(3):
    print("Meow")
```

---

## **`end=""`**  
Controls how the print function ends its output.  

### Example:  
```python
for _ in range(3):
    print("Meow", end=" ")  # Output: Meow Meow Meow
```

---

## **`len` (Length)**  
The `len` function returns the number of items in a list.  

### Example:  
```python
students = ["Hermione", "Harry", "Ron"]
print(len(students))  # Output: 3
```

---

## **Dictionaries (`dict`)**  
A dictionary allows you to map keys to values.  

### Example:  
```python
words = {"cat": "a small domesticated animal", "dog": "a loyal companion"}
print(words["cat"])  # Output: a small domesticated animal
```

---

## **`sep` (Separator)**  
Adds a custom separator between printed values.  

### Example:  
```python
print("Hermione", "Harry", "Ron", sep=", ")  # Output: Hermione, Harry, Ron
```

---

## **`None`**  
Represents the absence of a value.  

### Example:  
```python
value = None
if value is None:
    print("No value assigned")
```

---

## **Nesting**  
You can nest loops or functions, but it’s common practice to use variables like `i`, `j`, and `k` for loop counters. Avoid nesting too deeply for clarity.  




# --SECTION 4--: Exceptions  

## **Exceptions**  
Exceptions are errors that occur during the execution of a program. They interrupt the normal flow of the program unless they are handled.  

---

## **Types of Errors**  

### **Syntax Error**  
- Occurs when the code is written incorrectly and doesn't follow Python's syntax rules.  
- **Example:**  
  ```python
  print("Hello World  # Missing closing quote
  ```
  **Error:** `SyntaxError: EOL while scanning string literal`

---

### **Runtime Error**  
- Occurs during the execution of the program.  
- These errors can vary based on user input or external factors.  
- **Good Practice:** Write defensive code to anticipate and handle these errors gracefully.  

---

### **ValueError**  
- Raised when a function receives an argument of the correct type but an inappropriate value.  
- **Example:**  
  ```python
  int("abc")  # Trying to convert a string to an integer
  ```
  **Error:** `ValueError: invalid literal for int() with base 10`

---

### **NameError**  
- Occurs when a variable or function is referenced before it is defined.  
- **Example:**  
  ```python
  print(x)  # Variable `x` is not defined
  ```
  **Error:** `NameError: name 'x' is not defined`

---

## **Handling Exceptions**  

### **`try` and `except`**  
Use `try` to test a block of code and `except` to handle exceptions if they occur.  

### Example:  
```python
try:
    x = int(input("Enter a number: "))
    print(f"The number is {x}")
except ValueError:
    print("That's not a valid number!")
```

---

### **`pass`**  
Use `pass` to ignore an error and continue execution.  

### Example:  
```python
try:
    x = int("abc")
except ValueError:
    pass  # Do nothing if an exception occurs
```

---

### **`raise`**  
Use `raise` to manually raise an exception.  

### Example:  
```python
x = -5
if x < 0:
    raise ValueError("Negative values are not allowed")
```

---



# --SECTION 5--: Libraries  

## **Libraries**  
Libraries are collections of pre-written code (functions, modules, or classes) that you can use in your programs. They save time and encourage reusability. Libraries can be written by you, or they can be third-party libraries shared with the community.

---

## **Modules**  
Modules are files containing Python code, including variables, functions, or classes. They promote modularity and reusability.  

### Example:  
```python
# math module example
import math
print(math.sqrt(16))  # Output: 4.0
```

---

## **Random Module**  
The `random` module provides functions to generate random numbers or perform random operations.  

### Key Functions:  

- **`random.choice(seq)`**: Selects a random element from a sequence (e.g., list, string).  
  ```python
  import random
  colors = ["red", "blue", "green"]
  print(random.choice(colors))  # Randomly selects one color
  ```

- **`random.randint(a, b)`**: Returns a random integer between `a` and `b` (inclusive).  
  ```python
  print(random.randint(1, 10))  # Random number between 1 and 10
  ```

- **`random.shuffle(x)`**: Shuffles the elements of a list in place.  
  ```python
  my_list = [1, 2, 3, 4, 5]
  random.shuffle(my_list)
  print(my_list)  # List shuffled randomly
  ```

---

## **Importing Modules**  

- **`import`**: Imports the entire module.  
  ```python
  import random
  ```

- **`from ... import ...`**: Imports specific functions or variables.  
  ```python
  from random import randint
  print(randint(1, 10))
  ```

---

## **Statistics Module**  
Provides mathematical functions to analyze data sets (e.g., mean, median).  

### Example:  
```python
import statistics
data = [1, 2, 3, 4, 5]
print(statistics.mean(data))  # Output: 3
```

---

## **Command-Line Arguments**  
Allows passing arguments to a Python script via the command line.  

- **`sys` Module**: Contains `sys.argv`, a list of command-line arguments.  
  ```python
  import sys
  print(sys.argv)  # List of command-line arguments
  ```

### Example:  
```python
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print(f"Hello, {sys.argv[1]}")
```

Run the script in the terminal:  
```bash
python script.py John
```

Output:  
```
Hello, John
```

---

## **Common Errors**  

- **`IndexError`**: Accessing a list element out of range.  
- **`ValueError`**: Invalid input value for a function.  

---

## **Slicing**  
Extracts a subset of a list.  

### Example:  
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4]
```

---

## **Packages**  
Packages are collections of modules organized in directories.  

### Example: Installing a package using `pip`:  
```bash
pip install cowsay
```

---

## **APIs**  
Application Programming Interfaces (APIs) allow interaction with external services or data.  

### Example: Using the `requests` library to fetch data:  
```python
import requests

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
print(response.json())
```

---

## **JSON**  
JavaScript Object Notation (JSON) is a text-based format for exchanging data.  

- **`json` Module**: Handles JSON data in Python.  

### Example:  
```python
import json

data = '{"name": "John", "age": 30}'
parsed_data = json.loads(data)  # Converts JSON string to Python dictionary
print(parsed_data["name"])  # Output: John
```

---

## **Special Variables**  

- **`__name__`**: A special variable set to `"__main__"` when a file is executed directly.  
  ```python
  if __name__ == "__main__":
      print("This script is running directly")
  ```



# --SECTION 6--: Unit Tests  

## **Unit Tests**  
Unit tests are used to verify that individual parts (units) of a program work as expected. They help ensure code reliability and correctness.  

---

## **`assert`**  
The `assert` statement checks if a condition is true. If it is not true, an `AssertionError` is raised.  

### Example:  
```python
def add(a, b):
    return a + b

# Test the function
assert add(2, 3) == 5  # Passes silently if true
assert add(2, 3) == 6  # Raises AssertionError if false
```

---

## **AssertionError**  
An error raised when an `assert` condition evaluates to `False`.  

### Example:  
```python
x = 10
assert x < 5  # Raises AssertionError because x is not less than 5
```

---

## **`pytest`**  
`pytest` is a third-party testing framework that simplifies writing and running unit tests in Python.  

### Installation:  
```bash
pip install pytest
```

### Running Tests:  
- To run tests in a folder:  
  ```bash
  pytest <folder_name>
  ```
- To run all tests in the current directory:  
  ```bash
  pytest
  ```

---

### Writing Tests with `pytest`:  
Save test files with names like `test_*.py` or `*_test.py` for `pytest` to detect them automatically.  

### Example:  
Create a file `test_math.py`:  
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

Run the tests:  
```bash
pytest test_math.py
```

---

## **Organizing Tests in Folders**  
To organize tests in folders:  

1. **Create a new folder for tests**:  
   ```bash
   mkdir tests
   ```

2. **Add `__init__.py`**:  
   Create an empty `__init__.py` file in the folder to treat it as a package.  

3. **Add test files**:  
   Add your test files (e.g., `test_example.py`) in the `tests` folder.  

4. **Run `pytest` on the folder**:  
   ```bash
   pytest tests
   ```

---

## **`__init__.py`**  
An `__init__.py` file marks a folder as a package. It can be empty or contain initialization code.  

### Example:  
Folder structure:  
```
mypackage/
    __init__.py
    module.py
tests/
    __init__.py
    test_module.py
```

---

## **Packages in Testing**  
A package is a folder containing one or more Python modules, often with an `__init__.py` file.  

### Example:  
```bash
mypackage/
    __init__.py
    math_utils.py
```

Code in `math_utils.py`:  
```python
def multiply(a, b):
    return a * b
```

Test file in `tests/test_math_utils.py`:  
```python
from mypackage.math_utils import multiply

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
```

Run the tests:  
```bash
pytest tests
```


# --SECTION 7--: File I/O  

## **File I/O**  
File I/O refers to reading data from files (input) and writing data to files (output).  

---

## **Lists and Memory**  
Lists are stored in memory and are not persistent; their contents disappear when the program ends. To store data permanently, use files.  

---

## **`open`**  
The `open()` function opens a file for reading or writing.  

### Modes:  
- `"r"`: Read (default)  
- `"w"`: Write (overwrites the file)  
- `"a"`: Append (adds to the end of the file)  

[Documentation: `open()`](https://docs.python.org/3/library/functions.html#open)

---

## **`rm`**  
The `rm` command in the terminal deletes a file.  
```bash
rm names.txt
```

---

## **`with` Statement**  
The `with` statement ensures the file is properly closed after its suite finishes execution.  

### Example: Writing to a File  
```python
with open("names.txt", "a") as file:
    file.write("John\n")
```

---

## **Reading Files**  
- **`readlines()`**: Reads all lines and returns them as a list.  
- **`.rstrip()`**: Removes trailing characters (like `\n`).  

### Example: Reading and Stripping Lines  
```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())
```

---

## **Sorting and Appending**  
- **`sorted()`**: Sorts an iterable (e.g., list).  

### Example: Alphabetical Sorting  
```python
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
```

- **Descending Order**: Use `reverse=True` in `sorted()`.  

---

## **CSV Files**  
- CSV (Comma-Separated Values) files store tabular data in plain text.  
- Easily opened in spreadsheet software like Excel, Google Sheets, etc.  

[Documentation: `csv`](https://docs.python.org/3/library/csv.html)

---

### **Splitting Data**  
- **`.split(",")`**: Splits a string into parts using a delimiter (e.g., a comma).  

### Example: Splitting CSV Rows  
```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```

---

## **Using `csv.reader`**  
Parses CSV files into rows.  

### Example: Reading CSV with `csv.reader`  
```python
import csv

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} is from {row[1]}")
```

---

## **Using `csv.DictReader`**  
Parses CSV files into dictionaries with column names as keys.  

### Example: Reading CSV with `DictReader`  
```python
import csv

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} is from {row['home']}")
```

---

## **Writing CSV Files**  
- **`csv.writer`**: Writes rows as lists.  
- **`csv.DictWriter`**: Writes rows as dictionaries.  

### Example: Writing with `DictWriter`  
```python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```

---

## **Binary Files**  
Binary files store data in binary format (e.g., images, audio, video).  

---

## **Pillow (PIL)**  
Pillow is a library for image processing in Python.  

[Documentation: Pillow](https://pillow.readthedocs.io)  

### Example: Creating Animated GIFs  
```python
from PIL import Image

images = []

for arg in ["image1.gif", "image2.gif"]:
    image = Image.open(arg)
    images.append(image)

images[0].save("output.gif", save_all=True, append_images=images[1:])
```

---

## **Animated GIFs**  
- GIFs consist of multiple image frames played in sequence.  
- Useful for creating simple animations or memes.  

---

## **Scratch**  
Scratch is a visual programming language from MIT designed for beginners, enabling animation and interactive projects.  




# --SECTION 8--: Regular Expressions  

## **Regular Expressions (Regex)**  
Regular expressions are patterns used to match, search, and manipulate strings.  

---

## **`re` Module**  
The `re` module in Python provides tools for working with regular expressions.  

### Common Functions:  
1. **`re.search(pattern, string, flags=0)`**: Searches for a match anywhere in the string.  
2. **`re.match(pattern, string, flags=0)`**: Matches the pattern only at the start of the string.  
3. **`re.fullmatch(pattern, string, flags=0)`**: Matches the pattern from the start to the end of the string.  
4. **`re.sub(pattern, repl, string, count=0, flags=0)`**: Substitutes matched parts of the string with a replacement.  
5. **`re.split(pattern, string, maxsplit=0, flags=0)`**: Splits the string by a regex pattern.  
6. **`re.findall(pattern, string, flags=0)`**: Finds all occurrences of the pattern in the string.  

[Documentation: `re`](https://docs.python.org/3/library/re.html)  

---

## **Regex Symbols and Patterns**  
### Quantifiers:  
- `.`: Matches any character except a newline.  
- `*`: Matches 0 or more repetitions.  
- `+`: Matches 1 or more repetitions.  
- `?`: Matches 0 or 1 repetition.  
- `{m}`: Matches exactly `m` repetitions.  
- `{m,n}`: Matches between `m` and `n` repetitions.  

### Anchors:  
- `^`: Matches the start of the string.  
- `$`: Matches the end of the string.  

### Character Sets:  
- `[abc]`: Matches any one of the characters `a`, `b`, or `c`.  
- `[^abc]`: Matches any character except `a`, `b`, or `c`.  

### Escape Sequences:  
- `\d`: Matches a digit.  
- `\D`: Matches a non-digit.  
- `\s`: Matches whitespace.  
- `\S`: Matches non-whitespace.  
- `\w`: Matches a word character (letters, digits, underscore).  
- `\W`: Matches a non-word character.  

---

## **Regex Examples**  

### Example 1: Email Validation  
Pattern: `r".+@.+\..+"`  
```python
import re

email = "user@example.com"
if re.fullmatch(r".+@.+\..+", email):
    print("Valid email address")
else:
    print("Invalid email address")
```

---

### Example 2: Matching Digits  
Pattern: `r"\d{3}-\d{2}-\d{4}"` (e.g., Social Security Number format)  
```python
text = "My SSN is 123-45-6789."
if re.search(r"\d{3}-\d{2}-\d{4}", text):
    print("SSN found!")
```

---

### Example 3: Replacing Text  
Using **`re.sub()`**:  
```python
text = "I love cats."
new_text = re.sub(r"cats", "dogs", text)
print(new_text)  # Output: I love dogs.
```

---

### Example 4: Splitting Text  
Using **`re.split()`**:  
```python
text = "apple, orange; banana|grape"
fruits = re.split(r"[,;|]", text)
print(fruits)  # Output: ['apple', 'orange', 'banana', 'grape']
```

---

### Example 5: Finding All Matches  
Using **`re.findall()`**:  
```python
text = "The numbers are 42, 17, and 68."
numbers = re.findall(r"\d+", text)
print(numbers)  # Output: ['42', '17', '68']
```

---

## **Flags in `re`**  
- `re.IGNORECASE`: Makes the pattern case-insensitive.  
- `re.MULTILINE`: Allows `^` and `$` to match at the start and end of each line.  
- `re.DOTALL`: Allows `.` to match newline characters.  

---

## **Walrus Operator (`:=`)**  
The walrus operator assigns a value and returns it in a single expression.  

### Example:  
```python
import re

if match := re.search(r"\d+", "The number is 42"):
    print(f"Found number: {match.group()}")
```

---

## **String Methods for Simplified Manipulation**  
1. **`.replace()`**: Replaces parts of a string.  
2. **`.removeprefix()`**: Removes a specified prefix.  
3. **`.removesuffix()`**: Removes a specified suffix.  

### Example:  
```python
text = "prefix_string_suffix"
text = text.removeprefix("prefix_").removesuffix("_suffix")
print(text)  # Output: string
```

---



# --SECTION 9-- Object-Oriented Programming (OOP)

## **Object-Oriented Programming (OOP)**  
OOP is a programming paradigm that structures software design around objects, which represent data and methods. The primary goal is to encapsulate the data and the operations on that data into reusable and modular components called classes.

---

## **Tuples**  
A tuple is a collection of values, similar to a list but **immutable**, meaning its elements cannot be changed after it is created. Tuples are useful when you want to store multiple values in a single variable that should not be altered.

### Example:
```python
# Defining a tuple
coordinates = (3, 4)

# Accessing tuple elements
x = coordinates[0]
y = coordinates[1]
```

You can't modify a tuple’s elements after it's created, unlike lists.

---

## **Classes and Objects**  

### **Class**  
A class is a blueprint for creating objects (instances). It defines attributes and behaviors (methods) that are common to all objects of that class. 

### **Object**  
An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.  

### **Attributes and Instance Variables**  
Attributes are properties of an object, and instance variables are the specific values assigned to those attributes for an object.

### **Methods**  
Methods are functions defined inside a class that describe the behaviors of the objects. Special methods in Python begin and end with double underscores, such as `__init__`, `__str__`, etc.

---

## **Key Concepts**

### `__init__` (Constructor)  
The `__init__` method is a special method used to initialize a new object. It's called when a new instance of a class is created.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

### `self`  
The `self` keyword refers to the current instance of the class. It's used to access the object's attributes and methods.

### `__str__`  
The `__str__` method is used to define a string representation of an object, making it more user-friendly.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} belongs to {self.house}."
```

### `__repr__`  
The `__repr__` method provides a more technical string representation of an object, mainly for debugging.

```python
class Student:
    def __repr__(self):
        return f"Student(name={self.name}, house={self.house})"
```

---

## **Decorators**  
Decorators are functions that modify the behavior of other functions or methods. The `@property` decorator allows you to define a method as a property of a class.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value
```

### Example of `@staticmethod` and `@classmethod`
- `@staticmethod`: A method that doesn't take a reference to the instance or class.
- `@classmethod`: A method that takes a reference to the class as its first argument.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return x * y
```

---

## **Inheritance**  
Inheritance allows a class to inherit properties and methods from another class. The `super()` function is used to call methods from the parent class.

### Example of Inheritance:
```python
class Parent:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Child(Parent):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

child = Child("John", "Gryffindor")
```

---

## **Exception Handling**  
In Python, exceptions are errors that disrupt the flow of a program. The `raise` keyword is used to raise exceptions, while `try`, `except`, `else`, and `finally` blocks are used to handle them.

### Example:
```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Please enter a number.")
```

---

## **Operator Overloading**  
Operator overloading allows you to define custom behaviors for operators like `+`, `-`, etc. You can override the behavior of operators for custom classes.

### Example: Overloading `+` operator for a `Point` class:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2  # Calls __add__()
```

---

## **Common Python Classes**

- **`int`**: Represents integer numbers.
- **`str`**: Represents string values.
- **`list`**: Represents a list of items.
- **`dict`**: Represents a dictionary of key-value pairs.

You can create objects of these built-in classes, and you can also define custom classes.

### Example of `list`:
```python
numbers = list([1, 2, 3])
# --SECTION 10--: Extra Cetera

## **Reading Material**
- [Official Python Documentation](https://docs.python.org/3)
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Official Python Library](https://docs.python.org/3/library/)
- [Official Python References](https://docs.python.org/3/reference)
- [Official Python How-To Guides](https://docs.python.org/3/howto/)

---

## **Set**
A set is a collection of unique elements, where duplicate values are automatically eliminated.

- **Example:**
  ```python
  my_set = {1, 2, 3, 3, 4}
  print(my_set)  # Output: {1, 2, 3, 4}
  ```

[Official Python Library - Sets](https://docs.python.org/3/library/stdtypes.html#set)

---

## **Global Variables**
Global variables are defined outside of functions, making them accessible throughout the entire program. However, modifying them from within functions can be tricky, as they can introduce side effects if not handled carefully.

---

## **Constants**
Constants are variables whose values are not meant to change after being set. Python does not enforce constant values, but it is a common practice to define constants in all uppercase letters to indicate that their values should not be changed.

- **Example:**
  ```python
  PI = 3.14159
  ```

---

## **Type Hints**
Python is dynamically typed, meaning you don't need to explicitly declare variable types. However, type hints provide a way to specify the expected types of variables and functions, helping with code clarity and bug detection.

- **Example 1:**
  ```python
  def meow(n: int):
      for _ in range(n):
          print("meow")
  ```

- **Example 2:**
  ```python
  def meow(n: int) -> str:
      return "meow\n" * n
  ```

[Official Python Library - Typing](https://docs.python.org/3/library/typing.html)

---

## **Mypy**
Mypy is a static type checker for Python. It checks whether your code adheres to the type hints provided.

- Install Mypy with: `pip install mypy`
- Run it on your Python file using the command:
  ```bash
  mypy filename.py
  ```

[Official Mypy Documentation](https://mypy.readthedocs.io)

---

## **Docstrings**
Docstrings are used to document your functions, classes, and methods. They are written between triple quotes (`"""docstring"""`) and can be used to automatically generate documentation.

- **Example:**
  ```python
  def meow(n: int) -> str:
      """
      Meow n times.
      
      :param n: Number of times to meow
      :type n: int
      :raises TypeError: If n is not an int
      :returns: A string of n meows, one per line
      :rtype: str
      """
      return "meow\n" * n
  ```

[Official Python Documentation - PEP 257](https://peps.python.org/pep0257/)

---

## **Command-Line Arguments**

### `-n`
This argument specifies the number of times the code should be executed.

- **Example in Terminal:**
  ```bash
  python meows.py -n 3
  ```

### **Argparse**
The `argparse` module allows you to parse command-line arguments in Python programs.

- **Example:**
  ```python
  import argparse
  
  parser = argparse.ArgumentParser()
  parser.add_argument("-n", help="Number of times to meow")
  args = parser.parse_args()

  for _ in range(int(args.n)):
      print("meow")
  ```

[Official Python Library - argparse](https://docs.python.org/3/library/argparse.html)

---

## **Unpacking**

### `*input`
Unpacks data from a sequence into individual variables.

- **Example:**
  ```python
  def total(galleons, sickles, knuts):
      return (galleons * 17 + sickles) * 29 + knuts

  coins = [100, 50, 25]
  print(total(*coins), "knuts")
  ```

### `**input`
Unpacks a dictionary into function arguments.

- **Example:**
  ```python
  coins = {"galleons": 100, "sickles": 50, "knuts": 25}
  print(total(**coins), "knuts")
  ```

---

## **`*args` and `**kwargs`**

- `*args`: Allows for a variable number of positional arguments.
- `**kwargs`: Allows for a variable number of keyword arguments.

---

## **Map**
The `map` function applies a given function to all items in an iterable.

- **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  squared = map(lambda x: x ** 2, numbers)
  print(list(squared))
  ```

[Official Python Library - map](https://docs.python.org/3/library/functions.html#map)

---

## **List Comprehensions**
List comprehensions allow you to create a list in a concise, one-line syntax.

- **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  squares = [x ** 2 for x in numbers]
  print(squares)
  ```

---

## **Filter**
The `filter` function is similar to `map`, but it filters elements based on a condition.

- **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  even_numbers = filter(lambda x: x % 2 == 0, numbers)
  print(list(even_numbers))
  ```

[Official Python Library - filter](https://docs.python.org/3/library/functions.html#filter)

---

## **Dictionary Comprehensions**
Dictionary comprehensions allow you to create dictionaries in a concise, one-line syntax.

- **Example:**
  ```python
  numbers = [1, 2, 3, 4]
  squared_dict = {x: x ** 2 for x in numbers}
  print(squared_dict)
  ```

---

## **Enumerate**
The `enumerate` function allows you to iterate over a sequence while keeping track of the index of each item.

- **Example:**
  ```python
  fruits = ['apple', 'banana', 'cherry']
  for index, fruit in enumerate(fruits):
      print(f"{index}: {fruit}")
  ```

[Official Python Library - enumerate](https://docs.python.org/3/library/functions.html#enumerate)

---

## **Generators**
Generators allow you to generate values lazily, one at a time, without storing them in memory.

- **Example:**
  ```python
  def count_up_to(max):
      count = 1
      while count <= max:
          yield count
          count += 1

  counter = count_up_to(5)
  for num in counter:
      print(num)
  ```

[Official Python Library - Generators](https://docs.python.org/3/library/functions.html#generators)

---
