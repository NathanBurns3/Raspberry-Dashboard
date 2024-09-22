import tkinter as tk
from utils.data.fetch_photos import fetch_photos

class PhotosFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Photos")
        label.pack(side="top", fill="x", pady=10)
        photo = fetch_photos()
        tk.Label(self, text=photo).pack()