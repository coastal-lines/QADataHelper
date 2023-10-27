import tkinter as tk
from utils.ConverterBase64 import ConverterBase64

class SetupTab:
    def __init__(self, controller):
        self.main_frame = tk.Frame()
        self.main_frame.pack()

        self.controller = controller

        self.label_server = tk.Label(master=self.main_frame, text="Server:")
        self.label_server.place(x=0, y=0, width=100)
        self.server_text = tk.Entry(master=self.main_frame)
        self.server_text.place(x=100, y=0, width=200)

        self.label_user = tk.Label(master=self.main_frame, text="User:")
        self.label_user.place(x=0, y=20, width=100)
        self.login = tk.Entry(master=self.main_frame)
        self.login.place(x=100, y=20, width=200)
        
        self.label_password = tk.Label(master=self.main_frame, text="Password:")
        self.label_password.place(x=0, y=40, width=100)
        self.password = tk.Entry(master=self.main_frame, show="*")
        self.password.place(x=100, y=40, width=200)
        
        self.label_workplace = tk.Label(master=self.main_frame, text="Workspace:")
        self.label_workplace.place(x=0, y=60, width=100)
        self.workspace_text = tk.Entry(master=self.main_frame)
        self.workspace_text.place(x=100, y=60, width=200)

        self.label_project = tk.Label(master=self.main_frame, text="Project for test cases:")
        self.label_project.place(x=0, y=80, width=100)
        self.project_text = tk.Entry(master=self.main_frame)
        self.project_text.place(x=100, y=80, width=200)

        self.label_project_folders = tk.Label(master=self.main_frame, text="Project for folders:")
        self.label_project_folders.place(x=0, y=100, width=100)
        self.project_text_folders = tk.Entry(master=self.main_frame)
        self.project_text_folders.place(x=100, y=100, width=200)
        
        self.label_root_folder = tk.Label(master=self.main_frame, text="Root folder:")
        self.label_root_folder.place(x=0, y=160, width=100)
        self.root_folder_text = tk.Entry(master=self.main_frame)
        self.root_folder_text.place(x=100, y=160, width=200)
        self.button_start_session = tk.Button(master=self.main_frame, text="Start session",
                                             command=lambda: self.controller.on_start_session_click
                                                 (
                                                     self.server_text.get(),
                                                     self.login.get(),
                                                     self.password.get(),
                                                     self.workspace_text.get(),
                                                     self.project_text.get(),
                                                     self.root_folder_text.get())
                                                )

        self.button_start_session.place(x=100, y=120, width=200)
        
        self.button_download_test_cases = tk.Button(master=self.main_frame,
                                               text="Download data from root folder",
                                               command=lambda: self.controller.on_download_all_test_cases_click
                                                   (
                                                       self.get_credits(),
                                                       self.project_text.get(),
                                                       self.project_text_folders.get())
                                                    )

        self.button_download_test_cases.place(x=100, y=180, width=200)
        
        self.label_upload_data = tk.Label(master=self.main_frame, text="Load data:")
        self.label_upload_data.place(x=0, y=220, width=100)
        self.button_upload_test_cases = tk.Button(master=self.main_frame,
                                             text="Upload data",
                                             command=self.controller.on_upload_all_test_cases_click)

        self.button_upload_test_cases.place(x=100, y=220, width=200)
        
        #self.DEBUG_()
        
        def get_setup_tab_frame(self):
            return self.main_frame

        def get_project_for_test_cases(self):
            return self.project_text.get()