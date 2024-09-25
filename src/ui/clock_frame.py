from datetime import datetime
import tkinter as tk
import math
import calendar
from utils.data.fetch_clock import fetch_clock

class ClockFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=800, height=480, bg='black')
        
        self.canvas = tk.Canvas(self, width=400, height=480, bg='black', highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.center_x = 200
        self.center_y = 240
        self.clock_radius = 150
        
        self.right_frame = tk.Frame(self, width=400, height=480, bg='black')
        self.right_frame.pack(side="right", fill="both", expand=True)
        
        self.calendar_frame = tk.Frame(self.right_frame, bg='black')
        self.calendar_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.create_calendar()
        
        self.update_clock()
    
    def create_calendar(self):
        now = datetime.now()
        cal = calendar.monthcalendar(now.year, now.month)
        
        month_label = tk.Label(self.calendar_frame, text=now.strftime("%B"), fg="red", bg="black", font=("Arial Black", 26))
        month_label.pack(pady=20)
        
        days_frame = tk.Frame(self.calendar_frame, bg='black')
        days_frame.pack(pady=15)
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            day_label = tk.Label(days_frame, text=day, fg="white", bg="black", font=("Arial", 18, "bold"), width=3)
            day_label.grid(row=0, column=i, padx=4)
        
        for week in cal:
            week_frame = tk.Frame(self.calendar_frame, bg='black')
            week_frame.pack(pady=5)
            for i, day in enumerate(week):
                day_str = str(day) if day != 0 else ""
                day_label = tk.Label(week_frame, text=day_str, fg="white", bg="black", font=("Arial", 18), width=3)
                day_label.grid(row=1, column=i, padx=4)
                
                if day == now.day:
                    day_label.config(fg="red")
                    day_label.bind("<Configure>", lambda e, lbl=day_label: lbl.config(highlightbackground="red", highlightcolor="red", highlightthickness=2))

    
    def update_clock(self):
        self.canvas.delete("all")
        self.draw_clock_face()
        self.draw_clock_hands()
        self.after(1000, self.update_clock)
    
    def draw_clock_face(self):
        self.canvas.create_oval(self.center_x - self.clock_radius, self.center_y - self.clock_radius,
                                self.center_x + self.clock_radius, self.center_y + self.clock_radius,
                                outline="white", width=4)
        
        for i in range(60):
            angle = math.radians(i * 6)
            x1 = self.center_x + self.clock_radius * 0.9 * math.sin(angle)
            y1 = self.center_y - self.clock_radius * 0.9 * math.cos(angle)
            x2 = self.center_x + self.clock_radius * 0.95 * math.sin(angle)
            y2 = self.center_y - self.clock_radius * 0.95 * math.cos(angle)
            width = 2 if i % 5 == 0 else 1
            self.canvas.create_line(x1, y1, x2, y2, fill="white", width=width)
        
        for i in range(12):
            angle = math.radians(i * 30)
            x = self.center_x + self.clock_radius * 0.75 * math.sin(angle)
            y = self.center_y - self.clock_radius * 0.75 * math.cos(angle)
            self.canvas.create_text(x, y, text=str(i if i != 0 else 12), fill="white", font=("Helvetica", 18))
    
    def draw_clock_hands(self):
        current_time_str = fetch_clock()
        if current_time_str:
            current_time = datetime.strptime(current_time_str, "%Y-%m-%dT%H:%M:%S")
            hours = current_time.hour % 12
            minutes = current_time.minute
            seconds = current_time.second
            
            self.draw_hand(hours * 30 + minutes * 0.5, self.clock_radius * 0.5, 6, color="white")
            self.draw_hand(minutes * 6, self.clock_radius * 0.75, 4, color="white")
            self.draw_hand(seconds * 6, self.clock_radius * 0.9, 2, color="red")
        
        self.canvas.create_oval(self.center_x - 5, self.center_y - 5, self.center_x + 5, self.center_y + 5, fill="white")
    
    def draw_hand(self, angle, length, width, color="white"):
        angle = math.radians(angle)
        x = self.center_x + length * math.sin(angle)
        y = self.center_y - length * math.cos(angle)
        self.canvas.create_line(self.center_x, self.center_y, x, y, fill=color, width=width)