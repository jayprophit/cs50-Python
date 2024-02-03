'''
Test Calculator
'''

import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():    
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():    
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



"while using the 3rd party program pytest, main isn't defined"    
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0



def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

if __name__ == "__main__":
    main()



def test_square():
    assert square(2) == 4
    assert square(3) == 9



def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
'''