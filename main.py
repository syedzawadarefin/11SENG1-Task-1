# memory puzzle
# spelling bee 
# word meanings 

import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests

def getWord():
    global randomword
    with open("words.txt", 'r') as wordlist:
        words = []
        for c in wordlist:
            words.append(c)
    randomword = words[random.randint(0, len(words))]
    print(randomword)
    


def getWordEasy():
    global randomword
    with open("wordseasier.txt", "r") as wordlist:
        words = []
        for c in wordlist:
            words.append(c)
    randomword = words[random.randint(0, len(words))]
    print(randomword)


def defineWord():
    website = BeautifulSoup(requests.get("https://dictionary.com/browse/" + randomword).text, features="lxml")
    definition = str(website.p.get_text())
    if definition == "":
        definition = (website.find_all("p")[1])
        definition = definition.get_text()
        if ":" in definition:
            print(definition[0:definition.index(":")])
    else: 
        if ":" in definition:
            print(definition[0:definition.index(":")])
        else: print(definition)
            
            