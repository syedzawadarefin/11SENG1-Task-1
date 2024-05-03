import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests
import gtts
import playsound


class app(tk.CTk):
    def __init__(self):
        super().__init__(self, master)
        self.self.app = tk.CTk()
        self.self.app.geometry("1000x700")
        self.self.app.resizable(False, False)
        self.app.title("English Games")
        self.app.config(bg="#22223b")
        self.fontlabel = ("Chilanka", 80, "bold")

        self.app.introlabel = tk.CTkLabel(self.app, 
                                    text="English Games",
                                    font=("Chilanka", 80, "bold"),
                                    bg_color="#22223b",
                                    text_color="#c9ada7")

        self.app.introlabel.place(relx = 0.5, rely=0.25, anchor = tk.CENTER)

        self.app.spellingbtn = tk.CTkButton(self.app, 
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
        self.app.spellingbtn.pack(pady=(250,0))

        self.app.definbtn = tk.CTkButton(self.app, 
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
        self.app.definbtn.pack(pady=(35,0))

        self.app.quitbtn = tk.CTkButton(self.app, 
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
        self.app.quitbtn.pack(pady=(35,0))


app = App()
app.mainloop()