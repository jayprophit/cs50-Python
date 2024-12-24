'''
say
'''

import cowsay
# text to speech
import pyttsx3

engine = pyttsx3.init()
this = input("what's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()


'''
# different variations to produce the same result and solve the problem
# descending from currently used practices to basic beginner code


'''