import tkinter as tk

class ListOfTestCasesTab:

    def __init__(self):
        self.list_result_frame = tk.Frame()
        
        self.text_for_list_result = tk.Text(self.list_result_frame, height=1, borderwidth=0, yscrollcommand = v.set, wrap = tk.NONE)
        self.text_for_list_result.place(x=0, y=0, width=1180, height=630)

        v.config(command=self.text_for_list_result.yview)
        
    def update_list_test_cases(self, test_cases):
        str_list_of_formatted_ids_test_cases = ""
        self.text_for_list_result.delete(0.0, tk.END)

        for tc in test_cases:
            str_list_of_formatted_ids_test_cases += str(tc.FormattedID) + "\n"

        self.text_for_list_result.insert(0.0, str_list_of_formatted_ids_test_cases)
