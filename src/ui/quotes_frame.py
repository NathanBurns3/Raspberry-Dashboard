import customtkinter as ctk
from utils.data.fetch_quotes import fetch_quotes

class QuotesFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=800, height=480, fg_color="sky blue")
        
        self.quote_font = ctk.CTkFont(family="Georgia", size=36, slant="italic")
        self.author_font = ctk.CTkFont(family="Georgia", size=24, weight="bold")
        
        self.create_widgets()
        
        self.display_quote()

    def create_widgets(self):
        self.quote_label = ctk.CTkLabel(self, font=self.quote_font, wraplength=700, justify="center", fg_color="sky blue", text_color="white")
        self.quote_label.pack(pady=(75, 10), padx=20, fill="both", expand=True)
        
        self.author_label = ctk.CTkLabel(self, font=self.author_font, fg_color="sky blue", text_color="steel blue")
        self.author_label.pack(pady=(0, 100))

    def display_quote(self):
        quote = fetch_quotes()
        self.quote_label.configure(text=quote["quote"])
        self.author_label.configure(text=quote["author"])