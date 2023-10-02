import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    setup_tab = None
    
    login = None
    password = None

    def __init__(self, controller):
        super().__init__()

        self.geometry("1200x725")
        self.title('Test Cases Statistics')

        self._private_make_tab_control()

        self.setup_tab = SetupTab(controller)
        self.tabControl.add(self.setup_tab.get_setup_tab_frame(), text='Setup')

        self.query_tab = QueryTab(controller)
        self.tabControl.add(self.query_tab.get_query_tab_frame(), text='Query')

        self.statistics_tabs = StatisticsTabs(self.query_tab.get_query_tab_frame())

    def main(self):
        # endles loop for wait any user interactions - will works during window is opened
        self.mainloop()
        
	#create container for tabs
    def _private_make_tab_control(self):
        self.tabControl = ttk.Notebook(self)
        self.tabControl.place(x = 0, y = 0, width = 1200, height = 730)