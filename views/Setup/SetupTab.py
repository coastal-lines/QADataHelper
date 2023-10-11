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