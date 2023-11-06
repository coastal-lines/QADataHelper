from tkinter import ttk
from views.Statistics.ListTab.List import ListOfTestCasesTab
from views.Statistics.StructureTab.Structure import StructureOfTestCasesTab
from views.Statistics.DetailsTab.Details import DetailsTab
from views.Statistics.ExtendedDetailsTab.ExtendedDetails import ExtendedDetails

class StatisticsTabs:
    def __init__(self, query_frame):

        self.query_frame = query_frame

