import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


def create_canvas(parent_frame, figure, x, y):
    figure.set_size_inches(4.0, 3.2)
    frame = tk.Frame(parent_frame,  highlightbackground="black", highlightthickness=1)
    frame.place(x=x, y=y, width=400, height=320)
    canvas = FigureCanvasTkAgg(figure, master=frame)

    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=0)