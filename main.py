import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests
import gtts
import playsound


class app(tk.CTk):
    def __init__(self):
        self.app = tk.CTk()
        self.app.geometry("1000x700")
        app.resizable(False, False)
        app.title("English Games")
        app.config(bg="#22223b")
        fontlabel = ("Chilanka", 80, "bold")

        app.introlabel = tk.CTkLabel(app, 
                                    text="English Games",
                                    font=("Chilanka", 80, "bold"),
                                    bg_color="#22223b",
                                    text_color="#c9ada7")

        app.introlabel.place(relx = 0.5, rely=0.25, anchor = tk.CENTER)

        app.spellingbutton = tk.CTkButton(app, 
                                        text="Spelling Bee",
                                        width=350,
                                        height=125,
                                        )

        app.mainloop()