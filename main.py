# memory puzzle
# spelling bee 
# word meanings 

import customtkinter as tk
import CTkMessagebox
import random
from bs4 import BeautifulSoup
import requests
import gtts
import playsound

def getWord():
    global randomword
    with open("words.txt", 'r') as wordlist:
        words = []
        for c in wordlist:
            words.append(c)
    randomword = words[random.randint(0, len(words))]
    return str(randomword)

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
     audio = gtts.gTTS(text=randomword, slow=False)
     audio.save("audio.mp3")
     playsound.playsound("audio.mp3")

getWord()
defineWord()
getAudio()


app = tk.CTk()
app.bgcolor='#22223b'
app.title("English Games")
app.geometry("1000x700")
app.resizable(False,False)
app.config(bg="#22223b")
app.grid_columnconfigure((1,2,3), weight=1)
app.grid_rowconfigure((0,1,2), weight=1)

def quitapp():
    box = CTkMessagebox(title="Quit?",
                        message="Are you sure you want to quit?",
                        option_1="Cancel",
                        option_2="No",
                        option_3="Yes")
    response = box.get()
    if response == "Yes":
        app.destroy()




app.introlabel = tk.CTkLabel(app, 
                                text="English Games", font=("Chilanka", 80,'bold'), text_color="#c9ada7", bg_color=(app.bgcolor))
app.introlabel.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

app.spellingbtn = tk.CTkButton(app, 
                            text="Spelling Bee", 
                            width=350, 
                            height=125, 
                            font=("Chilanka", 40, "bold"),
                            fg_color=("#4a4e69"),
                            hover_color="#6b729c",
                            corner_radius=7,
                            border_width=5,
                            border_color="white",
                            bg_color="#22223b")
app.spellingbtn.pack(pady=(250,0))

app.definbtn = tk.CTkButton(app, 
                            text="Definitions", 
                            width=350, 
                            height=125, 
                            font=("Chilanka", 40, "bold"),
                            fg_color="#4a4e69",
                            hover_color="#6b729c",
                            corner_radius=7,
                            border_width=5,
                            border_color="white",
                            bg_color="#22223b")
app.definbtn.pack(pady=(35,0))

app.quitbtn = tk.CTkButton(app, 
                            text="Quit", 
                            width=150, 
                            height=40, 
                            font=("Chilanka", 25, "bold"),
                            fg_color="#4a4e69",
                            hover_color="#d60000",
                            corner_radius=5,
                            border_width=5,
                            border_color="white",
                            bg_color="#22223b",
                            command=quitapp)
app.quitbtn.pack(pady=(35,0))



app.mainloop()