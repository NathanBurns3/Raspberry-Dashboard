import tkinter as tk
from ui.todo_frame import TodoFrame
from ui.weather_frame import WeatherFrame
from ui.sports_frame import SportsFrame

class RaspberryPiDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        # Nathan: make changes to this configuration
        self.title("Raspberry Pi Dashboard")
        self.geometry("800x480")
        self.configure(bg="black")

        self.frames = {}
        self.frame_order = [TodoFrame, WeatherFrame, SportsFrame]
        self.current_frame_index = 0

        # Nathan: add the new frames here
        for F in self.frame_order:
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("TodoFrame")
        self.cycle_frames()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def cycle_frames(self):
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frame_order)
        next_frame = self.frame_order[self.current_frame_index].__name__
        self.show_frame(next_frame)
        self.after(5000, self.cycle_frames)

if __name__ == "__main__":
    app = RaspberryPiDashboard()
    app.mainloop()