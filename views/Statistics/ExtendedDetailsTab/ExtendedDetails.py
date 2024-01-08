import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from utils.visualization_helper import VisualizationHelper

class ExtendedDetails(VisualizationHelper):
    def __init__(self):
        self.extended_details_frame = tk.Frame()
        self.extended_details_frame.place()
        
        #TODO - double check this list. Remove is not necessary
        #self.queries = []
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

    def _get_duration_auto_manual(self, data):
        duration_auto = str(data.duration[1] // 60)
        duration_manual = str(data.duration[0] // 60)

        if (duration_auto == "0" and duration_manual == "0"):
            return str(data.duration[1]) + "m" + "/" + str(data.duration[0]) + "m"
        else:
            return str(duration_auto) + "h" + "/" + str(duration_manual) + "h"
        
    def _create_additional_elements_for_each_frame(self, frame, data):
        label_separator = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=("DejaVu Sans", 12), text="_______________________________________________")
        label_separator.place(x=100, y=170, width=200)

        label_number_test_cases = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Test cases: ")
        label_number_test_cases.place(x=110, y=200, width=80)
        label_number_test_cases_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=data.number_tc)
        label_number_test_cases_value.place(x=260, y=200, width=80)

        label_duration = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Duration auto/manual: ")
        label_duration.place(x=110, y=220, width=140)
        label_duration_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=str(self._get_duration_auto_manual(data)))
        label_duration_value.place(x=260, y=220, width=80)

        label_number_test_type = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Auto/Manual: ")
        label_number_test_type.place(x=110, y=240, width=80)
        label_number_test_type_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=str(data.number_auto) + "/" + str(data.number_manual))
        label_number_test_type_value.place(x=260, y=240, width=60)

        label_number_defects = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Defects: ")
        label_number_defects.place(x=110, y=260, width=80)
        label_number_defects_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=data.number_defects)
        label_number_defects_value.place(x=260, y=260, width=60)

        label_number_steps = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text="Steps average: ")
        label_number_steps.place(x=110, y=280, width=120)
        label_number_steps_value = tk.Label(master=frame, bg=self.background_color, anchor=self.anchor, font=self.font, text=data.number_steps)
        label_number_steps_value.place(x=260, y=280, width=60)
        
    def _create_frame(self):
        frame = tk.Frame(self.extended_details_frame, highlightbackground="black", highlightthickness=1)
        frame.place(x=self.x, y=self.y, width=400, height=300)

        return frame
        
    def _create_windows(self, frame):
        self.canvas.create_window(self.x, self.y, width=390, height=300, window=frame)
        self.x += 390
        if (self.x > 1130):
            self.y += 300
            self.x = 0
            
    def _pack_figure(self, figure, frame):
        figure_canvas = FigureCanvasTkAgg(figure, master=frame)
        figure_canvas.draw()
        figure_canvas.get_tk_widget().place(x=0, y=0)
        
    def update_screen(self, prepared_data, number_all_test_cases):
        self._remove_all_already_existed_widgets()
        self._create_canvas()

        for data in prepared_data:
            frame = self._create_frame()
            steps_fig = self._create_figure_and_axes(data, number_all_test_cases)
            self._pack_figure(steps_fig, frame)
            self._create_additional_elements_for_each_frame(frame, data)
            self._create_windows(frame)

        self.canvas.configure(scrollregio=self.canvas.bbox("all"))