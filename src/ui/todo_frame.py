import customtkinter as ctk
from utils.data.fetch_todo import fetch_todo
import tkinter as tk

class TodoFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.configure(fg_color="tan")
        
        label = ctk.CTkLabel(self, text="Todo List", font=("American Typewriter", 72, "bold"))
        label.pack(side="top", fill="x", pady=(10, 50))
        
        todoList = fetch_todo()
        for item in todoList:
            canvas = tk.Canvas(self, width=800, height=40, bg="tan", highlightthickness=0)
            canvas.pack(pady=5, fill="x")
            text_id = canvas.create_text(400, 20, anchor="center", text=item["name"], font=("American Typewriter", 24), fill="black")
            if item["completed"]:
                bbox = canvas.bbox(text_id)
                canvas.create_line(bbox[0], (bbox[1] + bbox[3]) / 2, bbox[2], (bbox[1] + bbox[3]) / 2, fill="red", width=2)