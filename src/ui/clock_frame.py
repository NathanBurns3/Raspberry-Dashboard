import tkinter as tk
from utils.data.fetch_clock import fetch_clock

class ClockFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Nathan: make changes to this configuration
        label = tk.Label(self, text="Clock")
        label.pack(side="top", fill="x", pady=10)
        time = fetch_clock()
        tk.Label(self, text=time).pack()