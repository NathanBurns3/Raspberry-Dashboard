import customtkinter as ctk
from utils.data.fetch_stock import fetch_stock

class StockFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=800, height=480, fg_color="black")
        
        self.stock_list_frame = ctk.CTkFrame(self, fg_color="black")
        self.stock_list_frame.pack(fill="both", expand=True)
        
        self.update_stock_list()
    
    def update_stock_list(self):
        stocks = fetch_stock()
        
        for widget in self.stock_list_frame.winfo_children():
            widget.destroy()
        
        for index, stock in enumerate(stocks):
            row = index // 2 * 2
            column = index % 2 * 3
            
            symbol_label = ctk.CTkLabel(
                self.stock_list_frame, 
                text=f"{stock['symbol']}",
                font=ctk.CTkFont(family="Subway Ticker", size=30, weight="bold"),
                text_color="white"
            )
            symbol_label.grid(row=row, column=column, padx=5, pady=5, sticky="sew")
            
            price_label = ctk.CTkLabel(
                self.stock_list_frame, 
                text=f"${stock['price']}",
                font=ctk.CTkFont(family="Subway Ticker", size=26, weight="bold"),
                text_color="white"
            )
            price_label.grid(row=row, column=column+1, padx=5, pady=5, sticky="sew")
            
            name_label = ctk.CTkLabel(
                self.stock_list_frame, 
                text=f"{stock['name']}",
                font=ctk.CTkFont(family="Roboto Slab", size=22, weight="normal"),
                text_color="white"
            )
            name_label.grid(row=row+1, column=column, padx=5, pady=5, sticky="new")
            
            percentage_change = stock['percentage_change']
            bg_color = "green" if percentage_change >= 0 else "red"
            
            percentage_change_label = ctk.CTkLabel(
                self.stock_list_frame, 
                text=f"{percentage_change}%",
                font=ctk.CTkFont(family="Subway Ticker", size=22, weight="normal"),
                fg_color=bg_color,
                text_color="white",
                corner_radius=10
            )
            percentage_change_label.grid(row=row+1, column=column+1, padx=5, pady=5, sticky="new")
        
        for i in range(6):
            self.stock_list_frame.grid_columnconfigure(i, weight=1)
        for i in range(len(stocks) * 2 // 2):
            self.stock_list_frame.grid_rowconfigure(i, weight=1)