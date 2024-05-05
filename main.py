import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests
import gtts
import playsound


root = tk.CTk()
root.geometry("1000x700")
root.resizable(False, False)
root.title("English Games")
root.config(bg="#22223b")

fontlabel = ("Chilanka", 80, "bold")

introlabel = tk.CTkLabel(root, 
                            text="English Games",
                            font=("Chilanka", 80, "bold"),
                            bg_color="#22223b",
                            text_color="#c9ada7")
#introlabel.pack()
introlabel.place(relx = 0.5, rely=0.25, anchor = tk.CENTER)

spellingbtn = tk.CTkButton(root, 
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
spellingbtn.pack(pady=(250,0))

definbtn = tk.CTkButton(root, 
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
definbtn.pack(pady=(35,0))

quitbtn = tk.CTkButton(root, 
                            text="Quit", 
                            width=150, 
                            height=40, 
                            font=("Chilanka", 25, "bold"),
                            fg_color="#4a4e69",
                            hover_color="#d60000",
                            corner_radius=5,
                            border_width=5,
                            border_color="white",
                            bg_color="#22223b")
quitbtn.pack(pady=(35,0))


root.mainloop()