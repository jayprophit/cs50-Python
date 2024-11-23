'''
Test hello
'''

import pytest
from hello import hello

def test_default():
    assert hello() == "hello, world"

"test a loop for multiple names"
def test_argument():
    for name in ["Hermione", "Harry", "Ron"]
        assert hello("name") == f"hello, {name}"

'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



def test_argument():
    assert hello("Jonathan") == "hello, world"




def test_hello():
    assert hello("Jonathan") == "hello, Jonathan"
    assert hello() == "hello, world"
'''