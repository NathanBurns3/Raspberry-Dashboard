import tkinter as tk
from utils.data.fetch_weather import fetch_weather

class WeatherFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Nathan: make changes to this configuration
        label = tk.Label(self, text="Weather")
        label.pack(side="top", fill="x", pady=10)
        todoList = fetch_weather()
        for item in todoList:
            tk.Label(self, text=item).pack()