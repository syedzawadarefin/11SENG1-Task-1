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

def defineWord():
    website = BeautifulSoup(requests.get("https://dictionary.com/browse/" + randomword).text, features="lxml")
    definition = str(website.p.get_text())
    index = definition.index(":")
    print(definition[0:(index)])

getWord()
defineWord()


