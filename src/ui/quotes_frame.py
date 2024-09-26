import tkinter as tk
from tkinter import font
from utils.data.fetch_quotes import fetch_quotes

class QuotesFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(width=800, height=480, bg="sky blue")
        
        self.quote_font = font.Font(family="Georgia", size=36, slant="italic")
        self.author_font = font.Font(family="Georgia", size=24, weight="bold")
        
        self.create_widgets()
        
        self.display_quote()

    def create_widgets(self):
        self.quote_label = tk.Label(self, font=self.quote_font, wraplength=700, justify="center", bg="sky blue", fg="white")
        self.quote_label.pack(pady=(75, 10), padx=20, fill="both", expand=True)
        
        self.author_label = tk.Label(self, font=self.author_font, bg="sky blue", fg="steel blue")
        self.author_label.pack(pady=(0, 100))

    def display_quote(self):
        quote = fetch_quotes()
        self.quote_label.config(text=quote.quote)
        self.author_label.config(text=quote.author)
