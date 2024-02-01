import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


def create_canvas(parent_frame, figure, x, y):
    figure.set_size_inches(4.0, 3.2)
    frame = tk.Frame(parent_frame,  highlightbackground="black", highlightthickness=1)
    frame.place(x=x, y=y, width=400, height=320)
    canvas = FigureCanvasTkAgg(figure, master=frame)

    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=0)

def create_full_tab_canvas(parent_frame, figure, x_inches, y_inches, frame_x=0, frame_y=0):
    #figure.set_size_inches(12.0, 6.3)
    figure.set_size_inches(x_inches, y_inches)
    frame = tk.Frame(parent_frame,  highlightbackground="black", highlightthickness=1)
    #frame.place(x=x, y=y, width=1200, height=630)
    frame.place(x=frame_x, y=frame_y, width=1200, height=350)
    canvas = FigureCanvasTkAgg(figure, master=frame)

    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=0)