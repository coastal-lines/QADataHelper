import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup

from views.Statistics.StatisticsTabs import StatisticsTabs
from views.Setup.SetupTab import SetupTab
from views.Query.QueryTab import QueryTab
from utils.ConverterBase64 import ConverterBase64


class View(tk.Tk):
    setup_tab = None
    
    main_frame = None
    query_frame = None
    details_frame = None
    
    login = None
    password = None

    def __init__(self, controller, view_mode=None):
        super().__init__()

        self.geometry("1200x725")
        self.title('Test Cases Statistics')

        self._private_make_tab_control()

        self.setup_tab = SetupTab(controller, view_mode)
        self.tabControl.add(self.setup_tab.get_setup_tab_frame(), text='Setup')

        self.query_tab = QueryTab(controller, view_mode)
        self.tabControl.add(self.query_tab.get_query_tab_frame(), text='Query')

        self.statistics_tabs = StatisticsTabs(self.query_tab.get_query_tab_frame())

    def main(self):
        #endles loop for wait any user interactions - will works during window is opened
        self.mainloop()
        
    #create container for tabs
    def _private_make_tab_control(self):
        self.tabControl = ttk.Notebook(self)
        self.tabControl.place(x = 0, y = 0, width = 1200, height = 730)

    def get_credits(self):
        return ConverterBase64().convert_into_base64(self.login.get() + ":" + self.password.get())
        
    def set_upload_mode(self):
        #user can works with uploaded tests only
        self.setup_tab.button_download_test_cases["state"] = "disabled"
        self.setup_tab.button_start_session["state"] = "disabled"
        self.query_tab.button_find_test_cases["state"] = "disabled"
        self.query_tab.button_save_test_cases["state"] = "disabled"
        self.query_tab.query_text["state"] = "disabled"
        
    def lock_save_test_cases_button(self):
        self.query_tab.button_save_test_cases["state"] = "disabled"

    def unlock_save_test_cases_button(self):
        self.query_tab.button_save_test_cases["state"] = "normal"
        
    def get_server_instance(self):
        return self.setup_tab.server_text.get()
        
    def update_view(self, test_cases):
        self.statistics_tabs.update_list_tab(test_cases)
        self.statistics_tabs.update_structure_tab(test_cases)
        self.statistics_tabs.update_details(test_cases)

    def update_view_extended_details(self, prepared_data, number_all_test_cases):
        self.statistics_tabs.update_extended_details(prepared_data, number_all_test_cases)
        
    def update_view_null_result(self):
        #update List of test cases
        self.statistics_tabs.list_tab.text_for_list_result.delete(0.0, tk.END)
        self.statistics_tabs.list_tab.text_for_list_result.insert(0.0, "No results")

        #update Structure of test cases
        html_base = "<html><body><h3>No results</h3><ul id='main'></ul></html>"
        html_document = BeautifulSoup(html_base, 'html.parser')
        self.statistics_tabs.structure_tab.html_frame.load_html(str(html_document.contents[0]))

    def switch_active_tab(self, tab_index: int):
        self.tabControl.select(tab_index)