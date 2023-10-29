import tkinter as tk

class QueryTab:
    def __init__(self, controller):
        self.query_frame = tk.Frame()
        self.query_frame.pack()

        self.controller = controller

    def get_query_tab_frame(self):
        return self.query_frame