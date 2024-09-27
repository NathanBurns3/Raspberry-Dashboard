import tkinter as tk
from utils.data.fetch_stock import fetch_stock

class StockFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=800, height=480)
        
        self.stock_list_frame = tk.Frame(self)
        self.stock_list_frame.pack(fill="both", expand=True)
        
        self.update_stock_list()
    
    def update_stock_list(self):
        stocks = fetch_stock()
        
        for widget in self.stock_list_frame.winfo_children():
            widget.destroy()
        
        for index, stock in enumerate(stocks):
            row = index // 3
            column = index % 3
            stock_label = tk.Label(
                self.stock_list_frame, 
                text=f"{stock['name']}: {stock['symbol']}: ${stock['price']} ({stock['percentage_change']}%)",
                font=("Helvetica", 12)
            )
            stock_label.grid(row=row, column=column, padx=10, pady=5, sticky="nsew")
        
        for i in range(3):
            self.stock_list_frame.grid_columnconfigure(i, weight=1)
        for i in range(2):
            self.stock_list_frame.grid_rowconfigure(i, weight=1)