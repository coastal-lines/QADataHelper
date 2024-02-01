from tkinter import ttk

from utils.Statistics.data_formatter import DataFormatter
from views.Statistics.DefectsTimeLineTab.DefectsTimeLine import DefectsTimeLine
from views.Statistics.ListTab.list_of_test_cases_tab import ListOfTestCasesTab
from views.Statistics.StructureTab.structure_of_test_cases_tab import StructureOfTestCasesTab
from views.Statistics.DetailsTab.details_tab import DetailsTab
from views.Statistics.ExtendedDetailsTab.ExtendedDetails import ExtendedDetails


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
        
    def update_structure_tab(self, test_cases):
        self.structure_tab.update_structure_of_test_cases(test_cases)

    def update_list_tab(self, test_cases):
        self.list_tab.update_list_test_cases(test_cases)
        
    def update_details(self, test_cases):
        self.details_tab.update(test_cases)

    def update_defects_timeline_tab(self, test_cases):
        self.defects_time_line.update_defects_full_timeline(test_cases)
        self.defects_time_line.update_defects_three_months_timeline(test_cases)

    def update_extended_details(self, prepared_data, number_all_test_cases):
        prepared_queries = DataFormatter().prepare_user_queries_for_statistics(prepared_data, number_all_test_cases)
        self.extended_details.update_screen(prepared_queries, number_all_test_cases)