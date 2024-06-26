from tkinter import ttk
from typing import List

from service_components.service_test_case import ServiceTestCase
from utils.statistics.data_formatter import DataFormatter
from views.statistics.defects_timeline_tab.defects_timeline import DefectsTimeLine
from views.statistics.details_tab.details_tab import DetailsTab
from views.statistics.extended_details_tab.extended_details import ExtendedDetails
from views.statistics.list_tab.list_of_test_cases_tab import ListOfTestCasesTab
from views.statistics.structure_tab.structure_of_test_cases_tab import StructureOfTestCasesTab


class StatisticsTabs:
    def __init__(self, query_frame):

        self.query_frame = query_frame

        self.result_tab_control = ttk.Notebook(master = self.query_frame, name="resultTabControl")
        self.result_tab_control.place(x = 0, y = 50, width = 1200, height = 660)

        self.structure_tab = StructureOfTestCasesTab()
        self.result_tab_control.add(self.structure_tab.tree_result_frame, text='Structure of test cases')
        
        self.list_tab = ListOfTestCasesTab()
        self.result_tab_control.add(self.list_tab.list_result_frame, text='List of test cases')

        self.details_tab = DetailsTab()
        self.result_tab_control.add(self.details_tab.details_frame, text='DetailsTab')

        self.defects_time_line = DefectsTimeLine()
        self.result_tab_control.add(self.defects_time_line.defects_time_line_frame, text='Defects Timeline')

        self.extended_details = ExtendedDetails()
        self.result_tab_control.add(self.extended_details.extended_details_frame, text='Extended details')
        
    def update_structure_tab(self, test_cases: List[ServiceTestCase]):
        self.structure_tab.update_structure_of_test_cases(test_cases)

    def update_list_tab(self, test_cases: List[ServiceTestCase]):
        self.list_tab.update_list_test_cases(test_cases)
        
    def update_details(self, test_cases: List[ServiceTestCase]):
        self.details_tab.update(test_cases)

    def update_defects_timeline_tab(self, test_cases: List[ServiceTestCase]):
        self.defects_time_line.update_defects_full_timeline(test_cases)
        self.defects_time_line.update_defects_three_months_timeline(test_cases)

    def update_extended_details(self, result_for_statistics_tab: List[ServiceTestCase], number_all_test_cases: int):
        prepared_queries = DataFormatter().prepare_user_queries_for_statistics(result_for_statistics_tab, number_all_test_cases)
        self.extended_details.update_screen(prepared_queries, number_all_test_cases)