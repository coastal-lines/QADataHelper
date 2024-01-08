import tkinter as tk
from tkinterweb import HtmlFrame

from utils.TestCaseUtils.html_helper import HtmlHelper


class StructureOfTestCasesTab:

    def __init__(self):
        self.tree_result_frame = tk.Frame(name="treeResultFrame")
        
        self.html_frame = HtmlFrame(self.tree_result_frame)
        self.html_frame.place(x=0, y=0, width=1200, height=620)
        
    def update_structure_of_test_cases(self, test_cases):
        html_code = HtmlHelper().create_html(test_cases)
        self.html_frame.load_html(str(html_code.contents[0]))