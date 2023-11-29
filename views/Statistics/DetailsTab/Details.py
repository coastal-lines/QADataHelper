import tkinter as tk


class DetailsTab:
    def __init__(self):
        self.details_frame = tk.Frame(highlightbackground="black", highlightthickness=4)
        self.details_frame.place(x=0, y=0, width=1200, height=620)
        
        '''
        self.success = SuccessCanvas()
        self.defects = DefectsCanvas()
        self.duration = DurationCanvas()
        self.steps = StepsCanvas()
        self.manual_auto = ManualAutoTab()
        self.test_types = TestTypesTab()
        '''