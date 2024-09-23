import tkinter as tk
from utils.data.fetch_quotes import fetch_quotes

class QuotesFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Quotes")
        label.pack(side="top", fill="x", pady=10)
        quote = fetch_quotes()
        tk.Label(self, text=quote).pack()