import tkinter as tk


class StructureOfTestCasesTab:

    def __init__(self):
        self.tree_result_frame = tk.Frame(name="treeResultFrame")
        
        self.html_frame = HtmlFrame(self.tree_result_frame)
        self.html_frame.place(x=0, y=0, width=1200, height=620)