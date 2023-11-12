import tkinter as tk

class ListOfTestCasesTab:

    def __init__(self):
        self.list_result_frame = tk.Frame()
        
        self.text_for_list_result = tk.Text(self.list_result_frame, height=1, borderwidth=0, yscrollcommand = v.set, wrap = tk.NONE)
        self.text_for_list_result.place(x=0, y=0, width=1180, height=630)

        v.config(command=self.text_for_list_result.yview)
