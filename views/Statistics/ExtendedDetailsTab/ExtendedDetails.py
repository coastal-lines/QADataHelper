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
        
        self.font = ("DejaVu Sans", 8)
        self.background_color = "white"
        self.anchor = 'w'
        
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
        
    def _create_additional_elements_for_each_frame(self, frame, data):
        label_separator = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=("DejaVu Sans", 12), text="_______________________________________________")
        label_separator.place(x=100, y=170, width=200)

        label_number_test_cases = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Test cases: ")
        label_number_test_cases.place(x=145, y=200, width=80)
        label_number_test_cases_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=data.number_tc)
        label_number_test_cases_value.place(x=225, y=200, width=80)

        label_duration = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Duration auto/manual: ")
        label_duration.place(x=145, y=220, width=80)
        label_duration_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=str(data.duration[1]//60) + "h" + "/" + str(data.duration[0]//60) + "h")
        label_duration_value.place(x=225, y=220, width=80)

        label_number_test_type = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Auto/Manual: ")
        label_number_test_type.place(x=145, y=240, width=80)
        label_number_test_type_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=str(data.number_auto) + "/" + str(data.number_manual))
        label_number_test_type_value.place(x=225, y=240, width=60)

        label_number_defects = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Defects: ")
        label_number_defects.place(x=145, y=260, width=80)
        label_number_defects_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=data.number_defects)
        label_number_defects_value.place(x=225, y=260, width=60)

        label_number_steps = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Steps average: ")
        label_number_steps.place(x=145, y=280, width=80)
        label_number_steps_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=data.number_steps)
        label_number_steps_value.place(x=225, y=280, width=60)