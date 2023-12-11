import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from utils.VisualizationHelper import Visualization

class ExtendedDetails(Visualization):
    def __init__(self):
        self.extended_details_frame = tk.Frame()
        self.extended_details_frame.place()
        
        self.queries = []
        self.canvas = None
        
        self.x = 0
        self.y = 0

    def _remove_all_already_existed_widgets(self):
        for widget in self.extended_details_frame.winfo_children():
            widget.destroy()
            
    def _create_canvas(self):
        self.canvas = tk.Canvas(self.extended_details_frame)
        self.canvas.config(scrollregion = self.canvas.bbox("all"))
        self.canvas.pack(expand = tk.YES, fill = tk.BOTH)

        scr = tk.Scrollbar(self.canvas)
        scr.pack(side = tk.RIGHT, fill = tk.Y)

        self.canvas.config(yscrollcommand = scr.set)
        scr.config(command = self.canvas.yview)
        
    def _create_figure_and_axes(self, data, number_all_test_cases):
        steps_fig, steps_ax = plt.subplots()
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        steps_fig.set_size_inches(4.0, 3.0)
        steps_fig.subplots_adjust(bottom=0.5)

        if(data.query == ""):
            steps_ax.bar(["Test cases according query"], [data.number_tc], color="cornflowerblue")
        else:
            steps_ax.bar(["\"" + data.query + "\""], [data.number_tc], color="cornflowerblue")

        steps_ax.bar(['Other test cases'], [number_all_test_cases - data.number_tc], color="lightsteelblue")

        if(len(data.query) > 80):
            steps_ax.set_title("Exteded results:")
        else:
            steps_ax.set_title(data.query)

        return steps_fig