import tkinter as tk

class QueryTab:
    def __init__(self, controller):
        self.query_frame = tk.Frame()
        self.query_frame.pack()

        self.controller = controller
        
        self.query_text = tk.Entry(master = self.query_frame)
        self.query_text.place(x = 0, y = 0, width=1100, height = 25)
        self.query_text.insert(0, '')
        
        self.button_find_test_cases = tk.Button(master = self.query_frame, text = "Find",
                                           command=lambda: self.controller.on_find_test_cases_click
                                           (
                                               self.query_text.get())
                                           )

        self.button_find_test_cases.place(x = 1100, y = 0, width=50)
        
        self.button_save_test_cases = tk.Button(master = self.query_frame, text = "Save",
                                                command=self.controller.on_save_found_test_cases_click)

        self.button_save_test_cases.place(x=1150, y=0, width=50)
        
        self.query_extended_text = tk.Entry(master=self.query_frame)
        self.query_extended_text.place(x=0, y=25, width=1100, height=25)
        self.query_extended_text.insert(0, '')

        self.button_find_extended_test_cases = tk.Button(master = self.query_frame, text = "Extended search",
                                           command=lambda: self.controller.on_find_extra_test_cases_click
                                           (
                                               self.query_extended_text.get())
                                           )

        self.button_find_extended_test_cases.place(x = 1100, y = 25, width=100, height=25)

    def get_query_tab_frame(self):
        return self.query_frame