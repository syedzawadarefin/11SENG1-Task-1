# memory puzzle
# spelling bee 
# word meanings 

import customtkinter as tk
import random
from bs4 import BeautifulSoup
import requests

class Words():
    def getWord():
        global randomword
        with open("words.txt", 'r') as wordlist:
            words = []
            for c in wordlist:
                words.append(c)
        randomword = words[random.randint(0, len(words))]
        


    def getWordEasy():
        global randomword
        with open("wordseasier.txt", "r") as wordlist:
            words = []
            for c in wordlist:
                words.append(c)
        randomword = words[random.randint(0, len(words))]


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

class answerSpace(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.CTkLabel(self, text="Equation")
        self.label.grid(row=0, column=0, pady=10, padx=10,)


class buttonSpace(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        self.seven = tk.CTkButton(self, text="7")
        self.seven.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.eight = tk.CTkButton(self, text="8")
        self.eight.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.nine = tk.CTkButton(self, text="9")
        self.nine.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
        self.divide = tk.CTkButton(self, text="DIVIDE")
        self.divide.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)
        self.four = tk.CTkButton(self, text="4")
        self.four.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.five = tk.CTkButton(self, text="5")
        self.five.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.six = tk.CTkButton(self, text="6")
        self.six.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
        self.multiply = tk.CTkButton(self, text="MULTIPLY")
        self.multiply.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)
        self.one = tk.CTkButton(self, text="1")
        self.one.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.two = tk.CTkButton(self, text="2")
        self.two.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
        self.three = tk.CTkButton(self, text="3")
        self.three.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)
        self.add = tk.CTkButton(self, text="ADD")
        self.add.grid(row=2, column=3, sticky="nsew", padx=10, pady=10)
        self.zero = tk.CTkButton(self, text="0")
        self.zero.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
        self.answer = tk.CTkButton(self, text="=")
        self.answer.grid(row=3, column=2, sticky="nsew", padx=10, pady=10)
        self.subtract = tk.CTkButton(self, text="SUBTRACT")
        self.subtract.grid(row=3, column=3, sticky="nsew", padx=10, pady=10)
        
class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fun Puzzles")
        self.geometry("700x900")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        self.answerSpace = answerSpace(self)
        self.answerSpace.grid(row=0, column=0, pady=20,padx=20, sticky="nsew", rowspan=1)

        self.buttonSpace = buttonSpace(self)
        self.buttonSpace.grid(row=1, column=0, padx=20, pady=(0,20), sticky="nsew", rowspan=3)


app = App()
app.mainloop()