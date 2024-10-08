import tkinter as tk
import customtkinter as ctk
import random
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime, timedelta
from utils.data.fetch_sports import fetch_favorites, fetch_nfl_scores, fetch_ncaaf_scores, fetch_ncaam_scores, fetch_nba_scores, fetch_mlb_scores, fetch_ufc_scores

class SportsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, data_type="FAVORITES"):
        super().__init__(parent, width=800, height=480)
        self.controller = controller
        self.data_type = data_type
        self.configure_grid()
        self.update_content()

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1, minsize=50)
        for i in range(1, 4):
            self.grid_rowconfigure(i, weight=1, minsize=140)
        for j in range(2):
            self.grid_columnconfigure(j, weight=1, minsize=400)
        self.bind("<Configure>", self.enforce_max_constraints)

    def enforce_max_constraints(self, event):
        max_row_height = min(140, self.winfo_height() // 3)
        for i in range(1, 4):
            self.grid_rowconfigure(i, minsize=max_row_height)
        max_col_width = min(400, self.winfo_width() // 2)
        for j in range(2):
            self.grid_columnconfigure(j, minsize=max_col_width)

    def update_content(self):
        for widget in self.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(self, text=f"SPORTS - {self.data_type}", font=ctk.CTkFont(family="Subway Ticker", size=40))
        label.grid(row=0, column=0, columnspan=2, pady=(15, 5))

        if self.data_type == "FAVORITES":
            data_list = fetch_favorites()
        elif self.data_type == "NFL":
            data_list = fetch_nfl_scores()
        elif self.data_type == "NCAAF":
            data_list = fetch_ncaaf_scores()
        elif self.data_type == "NCAAM":
            data_list = fetch_ncaam_scores()
        elif self.data_type == "NBA":
            data_list = fetch_nba_scores()
        elif self.data_type == "MLB":
            data_list = fetch_mlb_scores()
        elif self.data_type == "UFC":
            data_list = fetch_ufc_scores()
        else:
            data_list = []

        if len(data_list) > 6:
            data_list = random.sample(data_list, 6)

        num_games = len(data_list)
        num_rows = (num_games + 1) // 2

        for i in range(1, num_rows + 1):
            self.grid_rowconfigure(i, weight=1, minsize=140)
        for j in range(2):
            self.grid_columnconfigure(j, weight=1, minsize=400)

        for index in range(num_games):
            row = (index // 2) + 1
            col = index % 2
            print(f"Displaying game {data_list[index]}")
            print()
            self.display_game_item(data_list[index], row, col)

    def display_game_item(self, item, row, col):
        frame = ctk.CTkFrame(self)
        frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        if "home_team" in item and "away_team" in item:
            if self.data_type in ["NCAAF", "NCAAM"]:
                home_team_rank = item.get('home_team_rank', '')
                away_team_rank = item.get('away_team_rank', '')

                if home_team_rank and int(home_team_rank) <= 25:
                    home_frame = ctk.CTkFrame(frame, fg_color=frame.cget("fg_color"))
                    home_frame.pack(side="right", padx=10, pady=(17, 0))
                    home_logo = ctk.CTkLabel(home_frame, text="", image=self.load_image(item["home_team_logo"]))
                    home_logo.pack(side="top")
                    home_rank = ctk.CTkLabel(
                        home_frame, 
                        text=f"#{home_team_rank}", 
                        font=ctk.CTkFont(family="Subway Ticker", size=16, weight="bold"),
                        fg_color=frame.cget("fg_color")
                    )
                    home_rank.pack(side="bottom")
                else:
                    home_logo = ctk.CTkLabel(frame, text="", image=self.load_image(item["home_team_logo"]))
                    home_logo.pack(side="right", padx=10)

                if away_team_rank and int(away_team_rank) <= 25:
                    away_frame = ctk.CTkFrame(frame, fg_color=frame.cget("fg_color"))
                    away_frame.pack(side="left", padx=10, pady=(17, 0))
                    away_logo = ctk.CTkLabel(away_frame, text="", image=self.load_image(item["away_team_logo"]))
                    away_logo.pack(side="top")
                    away_rank = ctk.CTkLabel(
                        away_frame, 
                        text=f"#{away_team_rank}", 
                        font=ctk.CTkFont(family="Subway Ticker", size=16, weight="bold"),
                        fg_color=frame.cget("fg_color")
                    )
                    away_rank.pack(side="bottom")
                else:
                    away_logo = ctk.CTkLabel(frame, text="", image=self.load_image(item["away_team_logo"]))
                    away_logo.pack(side="left", padx=10)
            else:
                home_logo = ctk.CTkLabel(frame, text="", image=self.load_image(item["home_team_logo"]))
                home_logo.pack(side="left", padx=10)
                away_logo = ctk.CTkLabel(frame, text="", image=self.load_image(item["away_team_logo"]))
                away_logo.pack(side="right", padx=10)

            game_time = item.get('game_time', '')
            formatted_time = self.format_game_time(game_time)
            
            if item.get('is_game_still_playing', '') == True:
                info_frame = ctk.CTkFrame(frame, fg_color=frame.cget("fg_color"))
                info_frame.pack(side="top", fill="both", expand=True)
                
                game_info = ctk.CTkLabel(info_frame, text=f"{item.get('score', '')} {formatted_time}", font=ctk.CTkFont(family="Subway Ticker", size=20))
                game_info.pack(side="top", fill="both", expand=True, pady=(25, 0))
                
                period = item.get('period', '')
                
                inning_label = ctk.CTkLabel(info_frame, text=period, font=ctk.CTkFont(family="Subway Ticker", size=16))
                inning_label.pack(side="top", fill="both", expand=True, pady=(0, 25))
            else:
                info_frame = ctk.CTkFrame(frame, fg_color=frame.cget("fg_color"))
                info_frame.pack(side="top", fill="both", expand=True)
            
                game_info = ctk.CTkLabel(info_frame, text=f"{item.get('score', '')} {formatted_time}", font=ctk.CTkFont(family="Subway Ticker", size=20))
                game_info.pack(side="top", fill="both", expand=True)

    def format_game_time(self, game_time):
        try:
            dt = datetime.strptime(game_time, "%Y-%m-%dT%H:%MZ")
            dt = dt - timedelta(hours=4)
            return dt.strftime("%m/%d %I:%M %p")
        except ValueError:
            return game_time

    def load_image(self, url):
        try:
            response = requests.get(url)
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image = image.resize((75, 75), Image.ANTIALIAS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image from {url}: {e}")
            return None

if __name__ == "__main__":
    root = ctk.CTk()
    frame = SportsFrame(root, None, "NFL")
    frame.pack(fill="both", expand=True)
    root.mainloop()