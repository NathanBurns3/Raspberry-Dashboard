import tkinter as tk
from utils.data.fetch_photos import fetch_photo
from PIL import Image, ImageTk

class PhotosFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        photo_path = fetch_photo()
        if photo_path:
            image = Image.open(photo_path)
            image = image.resize((800, 480), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            photo_label = tk.Label(self, image=photo)
            photo_label.image = photo
            photo_label.pack(fill="both", expand=True)
        else:
            tk.Label(self, text="No photos available").pack()