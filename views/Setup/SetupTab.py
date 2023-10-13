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