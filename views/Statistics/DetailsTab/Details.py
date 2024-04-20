import tkinter as tk

from views.Statistics.DetailsTab.Tabs.Success import SuccessCanvas
from views.Statistics.DetailsTab.Tabs.Defects import DefectsCanvas
from views.Statistics.DetailsTab.Tabs.Duration import DurationCanvas
from views.Statistics.DetailsTab.Tabs.Steps import StepsCanvas
from views.Statistics.DetailsTab.Tabs.ManualAndAuto import ManualAutoTab
from views.Statistics.DetailsTab.Tabs.TestTypes import TestTypesTab

class DetailsTab:
    def __init__(self):
        self.details_frame = tk.Frame(highlightbackground="black", highlightthickness=4)
        self.details_frame.place(x=0, y=0, width=1200, height=620)
        
        self.success = SuccessCanvas()
        self.defects = DefectsCanvas()
        self.duration = DurationCanvas()
        self.steps = StepsCanvas()
        self.manual_auto = ManualAutoTab()
        self.test_types = TestTypesTab()
        
    def update(self, test_cases):
        self.success.update_success(self.details_frame, test_cases)
        self.defects.update_defects(self.details_frame, test_cases)
        self.duration.update_duration(self.details_frame, test_cases)
        self.steps.update_steps(self.details_frame, test_cases)
        self.manual_auto.update_manual_auto(self.details_frame, test_cases)
        self.test_types.update_test_types(self.details_frame, test_cases)