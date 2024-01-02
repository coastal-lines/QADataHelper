import pickle
from tkinter import filedialog as fd

class FileHelper:
    def save_test_cases_into_file(self, test_cases):
        file_path = self.call_file_save_dialog()

        with open(file_path, 'w+b') as file:
            pickle.dump(test_cases, file)

        print("Test cases were saved")

    def load_files(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                files = pickle.load(file)
                return files
        except AttributeError as ex:
            print("Deserialization file is not supported.")
            raise ex

        except Exception as ex:
            print("Please use correct serialized file.")
            raise ex
        
    def call_file_save_dialog(self):
        file_path = fd.asksaveasfilename(filetypes=[("Test Cases", ".data")], defaultextension=".data")
        return file_path

    def call_file_open_dialog(self):
        file_path = fd.askopenfilename()
        return file_path