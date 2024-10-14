import tkinter as tk
from utils.data.fetch_photos import fetch_photo
from PIL import Image, ImageTk

class PhotosFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.photo_label = tk.Label(self)
        self.photo_label.pack(fill="both", expand=True)
        self.update_photo()

    def update_photo(self):
        photo_path = fetch_photo()
        if photo_path:
            image = Image.open(photo_path)
            image = image.resize((800, 480), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.photo_label.configure(image=photo)
            self.photo_label.image = photo
        else:
            self.photo_label.configure(text="No photos available")