import pickle
from tkinter import filedialog as fd

class FileHelper:
    def load_files(self, file_path):

        files = None
        with open(file_path, 'rb') as file:
            files = pickle.load(file)

        return files