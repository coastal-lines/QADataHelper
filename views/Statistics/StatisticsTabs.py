from tkinter import ttk
from views.Statistics.ListTab.List import ListOfTestCasesTab
from views.Statistics.StructureTab.Structure import StructureOfTestCasesTab
from views.Statistics.DetailsTab.Details import DetailsTab
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

        self.extended_details = ExtendedDetails()
        self.result_tab_control.add(self.extended_details.extended_details_frame, text='Extended details')