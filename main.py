# memory puzzle
# spelling bee 
# word meanings 

import random
from bs4 import BeautifulSoup
import requests

def getWord():
    global randomword
    wordslist = open("words.txt", 'r')
    word = []
    for c in wordslist:
        word.append(c)
    randomword = word[random.randint(0, len(word))]
    print(randomword)
    


def getWordEasy():
    global randomword
    wordslist = open("wordseasier.txt", "r")
    word = []
    for c in wordslist:
        word.append(c)
    randomword = word[random.randint(0, len(word))]
    


def defineWord():
    website = BeautifulSoup(requests.get("https://dictionary.com/browse/" + "radio").text, features="lxml")
    definition = str(website.p.get_text())
    if ":" in definition:
        definition = (definition[0:(definition.index(":"))])
        print(definition)
    else: print(definition)
    
getWord()
defineWord()

