# memory puzzle
# spelling bee 
# word meanings 

import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests
import gtts
import playsound
import os
#from PIL import Image, ImageTk

def getWord():
    global randomword
    with open("words.txt", 'r') as wordlist:
        words = []
        for c in wordlist:
            words.append(c)
    randomword = words[random.randint(0, len(words))]
    return str(randomword)
getWord()



def getWordEasy():
    global randomword
    with open("wordseasier.txt", "r") as wordlist:
        words = []
        for c in wordlist:
            words.append(c)
    randomword = words[random.randint(0, len(words))]
    return str(randomword)


def defineWord():
    website = BeautifulSoup(requests.get("https://dictionary.com/browse/" + randomword).text, features="lxml")
    definition = str(website.p.get_text())
    if definition == "":
        definition = (website.find_all("p")[1])
        definition = definition.get_text()
        if ":" in definition:
            definition = (definition[0:definition.index(":")])
            return definition
    else: 
        if ":" in definition:
            return (definition[0:definition.index(":")])
        else: return definition
        
def getAudio(randomword: str):
     audio = gtts.gTTS(text=randomword)
     audio.save("audio.mp3")
     playsound.playsound("audio.mp3")
     os.remove("audio.mp3")
getAudio(randomword)

class sidebarMenu(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure((4), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.homebutton = tk.CTkButton(self, text='Home')
        self.homebutton.grid(padx=10, pady=(10,5), row=0, column=0, sticky="new")
        self.memorybutton = tk.CTkButton(self, text='Memory Games')
        self.memorybutton.grid(padx=10, pady=5, row=1, column=0, sticky="new")
        self.spellingbee = tk.CTkButton(self, text='Spelling Bee')
        self.spellingbee.grid(padx=10,row=2, pady=5, column=0, sticky="new")
        self.meaningsbutton = tk.CTkButton(self, text='Meanings Game')
        self.meaningsbutton.grid(padx=10,row=3, pady=5, column=0, sticky="ew")
        self.settings = tk.CTkButton(self, text='Settings')
        self.settings.grid(padx=10, pady=10, row=4, column=0, sticky="sew")
        
class App(tk.CTk):
    def __init__(self):
        super().__init__()

        tk.set_appearance_mode("light")
        self.title("Fun Puzzles")
        self.geometry("1000x700")
        self.grid_columnconfigure((1,2,3), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.sidebarMenu = sidebarMenu(self)
        self.sidebarMenu.grid(column=0, row=0, sticky="nsew")

        self.button1 = tk.CTkButton(self, text="test")
        self.button1.grid(column=2, row=0)

app = App()
app.mainloop()