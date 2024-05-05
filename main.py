import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests
import gtts
import playsound
import json


root = tk.CTk()
root.geometry("1000x700")
root.resizable(False, False)
root.title("English Games")
root.config(bg="#22223b")

fontlabel = ("Chilanka", 80, "bold")
fontbtn = ("Chilanka", 40, "bold")
prefontbtn = "Chilanka", 70, "bold"
prelabel = ("Chilanka", 100, "bold")

bg = "#22223b"
tc = "#c9ada7"
fg = "#4a4e69"
hover = "#6b729c"

def highscore():
    global sbscore
    with open("highscores.json", "r") as file:
        scores = json.load(file)
        sbscore = scores["scores"][0]["spellingbee"]
highscore()

def SpellingbeePre():
    introlabel.place_forget()
    spellingbtn.pack_forget()
    definbtn.pack_forget()
    quitbtn.pack_forget()


    spelling = tk.CTkLabel(root,
                            text="Spelling Bee",
                            font=(prelabel),
                            bg_color=(bg),
                            text_color=tc)
    spelling.pack(pady=(110,80))


    start = tk.CTkButton(root, 
                         text="Play",
                         width=350,
                         height=125,
                         font=prefontbtn,
                         fg_color=fg,
                         bg_color=bg,
                         hover_color=hover,
                         corner_radius=7,
                         border_width=5,
                         border_color="white",
                         command=SpellingBee)
    start.pack()
    
    highscore = tk.CTkLabel(root,
                            text="2",
                            font=("Chilanka", 30, "bold"),
                            bg_color=bg,
                            text_color=tc)
    highscore.pack(pady=50)

    highscore.configure(text=f"High Score: {sbscore}")

def SpellingBee():
    pass

introlabel = tk.CTkLabel(root, 
                            text="English Games",
                            font=(fontlabel),
                            bg_color=bg,
                            text_color=tc)
#introlabel.pack()
introlabel.place(relx = 0.5, rely=0.2, anchor = tk.CENTER)

spellingbtn = tk.CTkButton(root, 
                            text="Spelling Bee", 
                            width=350, 
                            height=125, 
                            font=(fontbtn),
                            fg_color=(fg),
                            hover_color=hover,
                            corner_radius=7,
                            border_width=5,
                            border_color="white",
                            bg_color=bg,
                            command=SpellingbeePre)
spellingbtn.pack(pady=(250,0))

definbtn = tk.CTkButton(root, 
                            text="Definitions", 
                            width=350, 
                            height=125, 
                            font=(fontbtn),
                            fg_color=fg,
                            hover_color=hover,
                            corner_radius=7,
                            border_width=5,
                            border_color="white",
                            bg_color=bg)
definbtn.pack(pady=(35,0))

quitbtn = tk.CTkButton(root, 
                            text="Quit", 
                            width=150, 
                            height=40, 
                            font=(fontbtn),
                            fg_color=fg,
                            hover_color=hover,
                            corner_radius=5,
                            border_width=5,
                            border_color="white",
                            bg_color=bg)
quitbtn.pack(pady=(35,0))


root.mainloop()