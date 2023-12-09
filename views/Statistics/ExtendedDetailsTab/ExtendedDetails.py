import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from utils.VisualizationHelper import Visualization

class ExtendedDetails(Visualization):
    def __init__(self):
        self.extended_details_frame = tk.Frame()
        self.extended_details_frame.place()
        
        self.x = 0
        self.y = 0

    def _remove_all_already_existed_widgets(self):
        for widget in self.extended_details_frame.winfo_children():
            widget.destroy()