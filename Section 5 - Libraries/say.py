'''
Cowsay
'''


import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])



'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code



import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])



import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])



import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
'''