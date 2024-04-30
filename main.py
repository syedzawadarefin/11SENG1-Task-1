import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests
import gtts
import playsound

app = tk.CTk()
app.geometry("1000x700")
app.resizable(False, False)
app.title("English Games")
app.config(bg="#22223b")
fontlabel = ("Chilanka, 80, bold")

app.introlabel = tk.CTkLabel(app, 
                             text="English Games"
                             font=fontlabel,
                             )


app.mainloop()