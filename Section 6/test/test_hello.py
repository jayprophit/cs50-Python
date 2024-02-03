'''
Test hello 2
'''

from hello import hello

def test_default():
    assert hello() == "hello, world"
    
def test_argument():
    assert hello("Jonathan") == "hello, Jonathan"
    
'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code

'''