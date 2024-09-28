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
            row = index // 3 * 2
            column = index % 3 * 2
            
            symbol_label = tk.Label(
                self.stock_list_frame, 
                text=f"{stock['symbol']}",
                font=("Helvetica", 12)
            )
            symbol_label.grid(row=row, column=column, padx=0, pady=0, sticky="se")
            
            price_label = tk.Label(
                self.stock_list_frame, 
                text=f"${stock['price']}",
                font=("Helvetica", 12)
            )
            price_label.grid(row=row, column=column+1, padx=0, pady=0, sticky="sw")
            
            name_label = tk.Label(
                self.stock_list_frame, 
                text=f"{stock['name']}",
                font=("Helvetica", 12)
            )
            name_label.grid(row=row+1, column=column, padx=0, pady=0, sticky="ne")
            
            percentage_change_label = tk.Label(
                self.stock_list_frame, 
                text=f"{stock['percentage_change']}%",
                font=("Helvetica", 12)
            )
            percentage_change_label.grid(row=row+1, column=column+1, padx=0, pady=0, sticky="nw")
        
        for i in range(6):
            self.stock_list_frame.grid_columnconfigure(i, weight=1)
        for i in range(len(stocks) * 2 // 3):
            self.stock_list_frame.grid_rowconfigure(i, weight=1)