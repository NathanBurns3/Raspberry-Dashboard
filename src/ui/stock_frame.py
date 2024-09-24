import tkinter as tk
from utils.data.fetch_stock import fetch_stock

class StockFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Stock")
        label.pack(side="top", fill="x", pady=10)
        stock = fetch_stock()
        tk.Label(self, text=stock).pack()