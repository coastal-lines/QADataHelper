import tkinter as tk
from tkinter import ttk
from typing import List

from bs4 import BeautifulSoup

from resources.resources_dataclass import Resources
from service_components.service_test_case import ServiceTestCase
from utils import file_helper
from utils.converter_base64 import convert_into_base64
from views.statistics.statistics_tabs import StatisticsTabs
from views.setup.setup_tab import SetupTab
from views.query.query_tab import QueryTab


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
        self.tab_control.add(self.setup_tab.get_setup_tab_frame(), text='Setup')

        self.query_tab = QueryTab(controller, view_mode)
        self.tab_control.add(self.query_tab.get_query_tab_frame(), text='Query')

        self.statistics_tabs = StatisticsTabs(self.query_tab.get_query_tab_frame())

    def main(self):
        """
            Endles loop for wait any user interactions - will works during window is opened
        """
        self.mainloop()

    def _private_make_tab_control(self):
        """
            Create container for tabs
        """
        self.tab_control = ttk.Notebook(self)
        self.tab_control.place(x = 0, y = 0, width = 1200, height = 730)

    def get_credits(self):
        return convert_into_base64(self.login.get() + ":" + self.password.get())
        
    def set_upload_mode(self):
        """
            User can works with uploaded tests only
        """
        self.setup_tab.button_download_test_cases["state"] = "disabled"
        self.setup_tab.button_start_session["state"] = "disabled"
        self.query_tab.button_find_test_cases["state"] = "disabled"
        self.query_tab.button_save_test_cases["state"] = "disabled"
        self.query_tab.query_text["state"] = "disabled"
        
    def lock_save_test_cases_button(self):
        self.query_tab.button_save_test_cases["state"] = "disabled"

    def unlock_save_test_cases_button(self):
        self.query_tab.button_save_test_cases["state"] = "normal"
        
    def get_server_instance(self) -> str:
        return self.setup_tab.server_text.get()
        
    def update_view(self, test_cases: List[ServiceTestCase]):
        self.statistics_tabs.update_list_tab(test_cases)
        self.statistics_tabs.update_structure_tab(test_cases)
        self.statistics_tabs.update_details(test_cases)
        self.statistics_tabs.update_defects_timeline_tab(test_cases)

    def update_view_extended_details(self, result_for_statistics_tab: List[ServiceTestCase], number_all_test_cases: int):
        self.statistics_tabs.update_extended_details(result_for_statistics_tab, number_all_test_cases)
        
    def update_view_null_result(self):
        """
            Update List of test cases
        """
        #
        self.statistics_tabs.list_tab.text_for_list_result.delete(0.0, tk.END)
        self.statistics_tabs.list_tab.text_for_list_result.insert(0.0, "No results")

        """
            Update Structure of test cases
        """
        html_base = file_helper.load_file(Resources.no_results_testcases_html_file)
        html_document = BeautifulSoup(html_base, 'html.parser')
        self.statistics_tabs.structure_tab.html_frame.load_html(str(html_document.contents[0]))

    def switch_active_tab(self, tab_index: int):
        self.tab_control.select(tab_index)