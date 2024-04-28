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
import os

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
     os.remove("audio.mp3")

# class sidebarMenu(tk.CTkFrame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.grid_rowconfigure((4), weight=1)
#         self.grid_columnconfigure(0, weight=1)
#         self.homebutton = tk.CTkButton(self, text='Home')
#         self.homebutton.grid(padx=10, pady=(10,5), row=0, column=0, sticky="new")
#         self.memorybutton = tk.CTkButton(self, text='Memory Games')
#         self.memorybutton.grid(padx=10, pady=5, row=1, column=0, sticky="new")
#         self.spellingbee = tk.CTkButton(self, text='Spelling Bee')
#         self.spellingbee.grid(padx=10,row=2, pady=5, column=0, sticky="new")
#         self.meaningsbutton = tk.CTkButton(self, text='Meanings Game')
#         self.meaningsbutton.grid(padx=10,row=3, pady=5, column=0, sticky="ew")
#         self.settings = tk.CTkButton(self, text='Settings')
#         self.settings.grid(padx=10, pady=10, row=4, column=0, sticky="sew")
        




class App(tk.CTk):
    def __init__(self):
        super().__init__()
        

        # def quit():
        #     msg = CTkMessagebox(title="Quit?", 
        #                         message="Are you sure you want to quit the app?", 
        #                         option_1="Cancel", 
        #                         option_2="No", 
        #                         option_3="Yes")
        #     response = msg.get()
        #     if response=="Yes":
        #         self.destroy()

        self.bgcolor='#22223b'
        self.title("English Games")
        self.geometry("1000x700")
        self.resizable(False,False)
        self.config(bg="#22223b")
        self.grid_columnconfigure((1,2,3), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)
        

        # self.sidebarMenu = sidebarMenu(self)
        # self.sidebarMenu.grid(column=0, row=0, sticky="nsew")

        self.introlabel = tk.CTkLabel(self, 
                                      text="English Games", font=("Chilanka", 80,'bold'), text_color="#c9ada7", bg_color=(self.bgcolor))
        self.introlabel.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.spellingbtn = tk.CTkButton(self, 
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
        self.spellingbtn.pack(pady=(250,0))

        self.definbtn = tk.CTkButton(self, 
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
        self.definbtn.pack(pady=(35,0))

        self.quitbtn = tk.CTkButton(self, 
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
                                    command=self.quit)
        self.quitbtn.pack(pady=(35,0))


app = App()
app.mainloop()