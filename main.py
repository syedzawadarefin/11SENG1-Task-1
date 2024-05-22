import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests
import gtts
import playsound
import json
from PIL import Image, ImageTk
from time import sleep


root = tk.CTk()
root.geometry("1000x700")
root.resiable(False, False)
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

# gets all word from wordslist
with open("words.txt", "r") as file:
    wordslist = []
    for c in file:
        wordslist.append(c[0:len(c)-1])
#

# gets 1 random word spelling bee game
def getRandom1():
    global randomword
    randomword = str(wordslist[random.randint(0, len(wordslist))]).lower()
    print(randomword)
    return randomword

#

# gets 4 random words for definitions game
def getRandom2():
    global x1
    global x2
    global x3
    global x4
    x1 = wordslist.pop(random.randint(0, len(wordslist)))
    x2 = wordslist.pop(random.randint(0, len(wordslist)))
    x3 = wordslist.pop(random.randint(0, len(wordslist)))
    x4 = wordslist.pop(random.randint(0, len(wordslist)))
#

# reads highs score from file
def highscorefunc():
    global sbscore
    with open("highscores.json", "r") as file:
        scores = json.load(file)
        sbscore = scores["scores"][0]["spellingbee"]
        defscore = scores["scores"][0]["definitions"]
highscorefunc()

# plays audio file of random word
def playAudio():
    audio = gtts.gTTS(text=randomword, slow=False)
    audio.save("audio.mp3")
    playsound.playsound("audio.mp3")

def checkans():
    global answer
    global score
    global correctlabel
    global incorrectlabel
    global questions
    answer = textbox.get().lower()


    print(f"the answer is {answer} and word is {randomword}")
    if answer == randomword:
        print("Correct")
        score=+1
        questions=+1
        correctlabel = tk.CTkLabel(root,
                                   text="Correct!",
                                   font=("Chilanka", 40, "bold"),
                                   bg_color=bg,
                                   text_color=tc)
        correctlabel.pack(pady=5)
        playsound.playsound("correct.wav")
        sleep(0.5)
        correctlabel.destroy()
        textbox.destroy()
        scorelabel.destroy()
        audiobutton.destroy()
        answerget.destroy()
        SpellingBee()


    else:

        print("wrong")
        questions =+ 1
        incorrectlabel = tk.CTkLabel(root,
                            text="Incorrect",
                            font=("Chilanka", 40, "bold"),
                            bg_color=bg,
                            fg_color=fg,
                            text_color=tc)
        incorrectlabel.pack(pady=10)
        playsound.playsound("incorrect.mp3")
        sleep(0.5)
        incorrectlabel.destroy()
        correctlabel.destroy()
        textbox.destroy()
        scorelabel.destroy()
        audiobutton.destroy()
        answerget.destroy()
        SpellingBee()
        

def SpellingBeeCorClear():
    correctlabel.pack_forget()
    SpellingBee()

def HomePageClear():
    spelling.pack_forget()
    start.pack_forget()
    highscore.pack_forget()

score = 0
questions = 0
# Spelling bee Ingame
def SpellingBee():
    global textbox
    global scorelabel
    global audiobutton
    global answerget
    HomePageClear()
    if questions != 10:
        getRandom1()
        

        scorelabel = tk.CTkLabel(root,
                                    text="Score: 0",
                                    bg_color = bg,
                                    text_color=tc,
                                    font=("Chilanka", 30, "bold"))
        scorelabel.place(relx= 0.865, rely=0.01)
        scorelabel.configure(text=f"Score: {score}")

        audioimage = ImageTk.PhotoImage(Image.open("audiobutton.png"))
        audiobutton = tk.CTkButton(root,
                                    image=audioimage,
                                    text="",
                                    width = 300,
                                    height = 300,
                                    bg_color=bg,
                                    fg_color=fg,
                                    hover_color=hover,
                                    command = playAudio)
        audiobutton.pack(pady=(100,80))

        textbox = tk.CTkEntry(root,
                                placeholder_text="Spell the word here..",
                                font=fontbtn,
                                width = 700,
                                height = 50,
                                corner_radius=10,
                                bg_color=bg)
        textbox.pack()

        answerget = tk.CTkButton(root,
                                text='Check',
                                font=fontbtn,
                                bg_color=bg,
                                fg_color=fg,
                                hover_color=hover,
                                width = 200,
                                height=50,
                                command=checkans)
        answerget.pack(pady=30)
    else:
        print("finished")
        
#

def SpellingbeePre():
# Spelling bee pregame
    global spelling
    global start
    global highscore

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


    start = tk.CTkButton(root, ]
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
#


# Home Page
introlabel = tk.CTkLabel(root, 
                            text="English Games",
                            font=(fontlabel),
                            bg_color=bg,
                            text_color=tc)
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