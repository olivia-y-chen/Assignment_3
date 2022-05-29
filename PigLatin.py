"""
Created on 10/23/2021

@author: Olivia Chen
"""
def check(strng):
    """checks if string has any vowels, if not returns 0, if so returns 1"""
    vowelLst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', "Y"]
    word2 = ""
    for char in strng:
        if char not in vowelLst:
            word2 += char
        else:
            pass
    if len(word2) == len(strng):
        return 0
    else:
        return 1

if __name__ == '__main__':
    pass

def encrypt (original):
    """encrypts string into Pig Latin, checks if starts with vowel,
    qu, or any number of vowels"""
    vowelLst = ["a", 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowelLstY = ["a", 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', "Y"]
    wordLst = original.split()
    for i in range(len(wordLst)):
        if check(wordLst[i]) == 0:
            wordLst[i] = wordLst[i] + "-way"
        elif wordLst[i][0] in vowelLst:
            wordLst[i] = wordLst[i] + "-way"
        elif wordLst[i][0] == 'q' or wordLst[i][0] == 'Q':
            if wordLst[i][2] in vowelLst:
                wordLst[i] = wordLst[i][2:] + '-' + wordLst[i][:2] + "ay"
            else:
                numLst = []
                for u in range(2, len(wordLst[i])):
                    if wordLst[i][u] in vowelLstY:
                        numLst.append(u)
                wordLst[i] = wordLst[i][numLst[0]:] + "-" + wordLst[i][0:numLst[0]] + "ay"
                numLst = []
        else:
            numLst = []
            for u in range(1,len(wordLst[i])):
                if wordLst[i][u] in vowelLstY:
                    numLst.append(u)
            wordLst[i]= wordLst[i][numLst[0]:] + "-" + wordLst[i][0:numLst[0]] + "ay"
            numLst = []
    return " ".join(wordLst)

def decrypt (original):
    """decrypts Pig Latin by readding the consonants in front of the 'ay'
    or just subtracting '-way' if it is just '-way'"""
    wordLst = original.split()
    for i in range(len(wordLst)):
        newLst = wordLst[i].split("-")
        if newLst[1] == "way":
            wordLst[i] = newLst[0]
        else:
            wordLst[i] = newLst[1][0:-2] + newLst[0]
    return " ".join(wordLst)

encrypt("I love to eat cheese yoohoo STRONG rhythm")
decrypt("I-way ove-lay o-tay eat-way eese-chay oohoo-yay ONG-STRay ythm-rhay")