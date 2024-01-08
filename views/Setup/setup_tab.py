import tkinter as tk
from utils.converter_base64 import ConverterBase64

class SetupTab:
    def __init__(self, controller, view_mode=None):
        self.main_frame = tk.Frame()
        self.main_frame.pack()

        self.controller = controller

        self.label_server = tk.Label(master=self.main_frame, text="Server:", anchor='w')
        self.label_server.place(x=0, y=0, width=100)
        self.server_text = tk.Entry(master=self.main_frame)
        self.server_text.place(x=120, y=0, width=200)

        self.label_user = tk.Label(master=self.main_frame, text="User:", anchor='w')
        self.label_user.place(x=0, y=20, width=100)
        self.login = tk.Entry(master=self.main_frame)
        self.login.place(x=120, y=20, width=200)
        
        self.label_password = tk.Label(master=self.main_frame, text="Password:", anchor='w')
        self.label_password.place(x=0, y=40, width=100)
        self.password = tk.Entry(master=self.main_frame, show="*")
        self.password.place(x=120, y=40, width=200)
        
        self.label_workplace = tk.Label(master=self.main_frame, text="Workspace:", anchor='w')
        self.label_workplace.place(x=0, y=60, width=100)
        self.workspace_text = tk.Entry(master=self.main_frame)
        self.workspace_text.place(x=120, y=60, width=200)

        self.label_project = tk.Label(master=self.main_frame, text="Project for test cases:", anchor='w')
        self.label_project.place(x=0, y=80, width=120)
        self.project_text = tk.Entry(master=self.main_frame)
        self.project_text.place(x=120, y=80, width=200)

        self.label_project_folders = tk.Label(master=self.main_frame, text="Project for folders:", anchor='w')
        self.label_project_folders.place(x=0, y=100, width=100)
        self.project_text_folders = tk.Entry(master=self.main_frame)
        self.project_text_folders.place(x=120, y=100, width=200)
        
        self.label_root_folder = tk.Label(master=self.main_frame, text="Root folder:", anchor='w')
        self.label_root_folder.place(x=0, y=160, width=100)
        self.root_folder_text = tk.Entry(master=self.main_frame)
        self.root_folder_text.place(x=120, y=160, width=200)
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

        self.button_start_session.place(x=120, y=120, width=200)
        
        self.button_download_test_cases = tk.Button(master=self.main_frame,
                                               text="Download data from root folder",
                                               command=lambda: self.controller.on_download_all_test_cases_click
                                                   (
                                                       self.get_credits(),
                                                       self.project_text.get(),
                                                       self.project_text_folders.get())
                                                    )

        self.button_download_test_cases.place(x=120, y=180, width=200)
        
        self.label_upload_data = tk.Label(master=self.main_frame, text="Load data:", anchor='w')
        self.label_upload_data.place(x=0, y=220, width=100)
        self.button_upload_test_cases = tk.Button(master=self.main_frame,
                                             text="Upload data",
                                             command=self.controller.on_upload_all_test_cases_click)

        self.button_upload_test_cases.place(x=120, y=220, width=200)

        if view_mode == "demo":
            self.server_text.insert(0, "server_url")
            self.login.insert(0, "login")
            self.password.insert(0, "123")
            self.workspace_text.insert(0, "workspace")
            self.project_text.insert(0, "project_name")
            self.project_text_folders.insert(0, "project_main_folder")
            self.root_folder_text.insert(0, "root_folder")

            self.server_text.config(state="disabled")
            self.login.config(state="disabled")
            self.password.config(state="disabled")
            self.workspace_text.config(state="disabled")
            self.project_text.config(state="disabled")
            self.project_text_folders.config(state="disabled")
            self.root_folder_text.config(state="disabled")

            self.button_start_session.config(state="disabled")
            self.button_download_test_cases.config(state="disabled")

    def get_setup_tab_frame(self):
        return self.main_frame

    def get_project_for_test_cases(self):
        return self.project_text.get()

    def get_project_for_folders(self):
        return self.project_text_folders.get()

    def get_root_folder(self):
        return self.root_folder_text.get()

    def get_credits(self):
        user_credits = self.login.get() + ":" + self.password.get()
        return ConverterBase64().convert_into_base64(user_credits)