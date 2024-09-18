import tkinter as tk
from utils.data.fetch_sports import fetch_sports

class SportsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Nathan: make changes to this configuration
        label = tk.Label(self, text="Sports")
        label.pack(side="top", fill="x", pady=10)
        todoList = fetch_sports()
        for item in todoList:
            tk.Label(self, text=item).pack()