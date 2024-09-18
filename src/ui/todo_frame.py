import tkinter as tk
from utils.data.fetch_todo import fetch_todo

class TodoFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Nathan: make changes to this configuration
        label = tk.Label(self, text="Todo List")
        label.pack(side="top", fill="x", pady=10)
        todoList = fetch_todo()
        for item in todoList:
            tk.Label(self, text=item).pack()