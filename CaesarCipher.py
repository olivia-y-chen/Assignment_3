"""
Created on 10/24/2021

@author: Olivia Chen
"""
import os.path

file = os.path.join("data","lowerwords.txt")

f = open(file)

if __name__ == '__main__':
    pass

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

def encrypt(w):
    """encrypts string w using an alphabetical shift by changing each
    letter to its matching letter in the shifted alphabet. non-alphabetical
    characters are left unchanged"""
    global lower_alph, upper_alph, shifted_upper, shifted_lower
    newStrng = ""
    for char in w:
        if char not in lower_alph and char not in upper_alph:
            newStrng += char
        elif char in lower_alph:
            for i in range(len(lower_alph)):
                if lower_alph[i] == char:
                    newStrng += shifted_lower[i]
        else:
            for i in range(len(upper_alph)):
                if upper_alph[i] == char:
                    newStrng += shifted_upper[i]
    return newStrng

def setShift(u):
    """reassigns shift to u, causing the shifted alphabet to be shifted from
    the original alphabet by u"""
    global shift, shifted_upper, shifted_lower, upper_alph, lower_alph
    shift = u
    shifted_upper = upper_alph[shift:] + upper_alph[:shift]
    shifted_lower = lower_alph[shift:] + lower_alph[:shift]

def findShift(t):
    """finds the most likely Caesar shift of an Caesar encrypted string
    by finding the shift with the highest number of actual words and storing
    that shift"""
    wordsClean = [w.strip() for w in f.read().split()]
    highWordNum = 0
    finalShift = 0
    for i in range(len(lower_alph)):
        setShift(i)
        new = encrypt(t).split()
        wordNum = 0
        for word in new:
            if word in wordsClean:
                wordNum += 1
        if wordNum > highWordNum:
            highWordNum = wordNum
            finalShift = 26 -i
    return finalShift

encrypt("I love to eat mac-and-cheese.")
setShift(10)
encrypt("this is my last call.")
print(findShift('Zkdw grhv wkh ira vdb?'))